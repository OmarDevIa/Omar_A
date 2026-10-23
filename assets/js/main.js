/* Omar.tech — motion & interactions v2 (JS natif, sans dépendance, ~6 Ko)
   Règles perf : lectures DOM groupées dans requestAnimationFrame, écritures
   uniquement en transform/opacity, effets souris désactivés sur tactile. */
(function () {
    "use strict";

    var doc = document.documentElement;
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
    var supportsScrollTimeline = window.CSS && CSS.supports && CSS.supports("animation-timeline: scroll()");
    var raf = window.requestAnimationFrame.bind(window);

    /* ---------- Boucle de scroll unique (header, progression, timeline, marquee) ---------- */
    function initScrollLoop() {
        var header = document.querySelector(".site-header");
        var bar = supportsScrollTimeline ? null : document.querySelector(".progress");
        var process = document.querySelector(".process");
        var marquees = [];
        if (!reduce && "getAnimations" in Element.prototype) {
            document.querySelectorAll(".marquee-track").forEach(function (t) { marquees.push(t); });
        }
        var lastY = window.scrollY, velocity = 0, ticking = false, docH = 0, vh = 0;

        function measure() { docH = doc.scrollHeight - window.innerHeight; vh = window.innerHeight; }
        function frame() {
            var y = window.scrollY;
            var delta = y - lastY;
            velocity = velocity * 0.8 + delta * 0.2;
            if (header) {
                header.classList.toggle("is-scrolled", y > 20);
                header.classList.toggle("is-hidden", delta > 0 && y > 400 && !doc.classList.contains("menu-open"));
            }
            if (bar) bar.style.transform = "scaleX(" + (docH > 0 ? y / docH : 0) + ")";
            if (process) {
                var top = process.getBoundingClientRect().top;
                var p = Math.min(Math.max((vh * 0.85 - top) / (vh * 0.6), 0), 1);
                process.style.setProperty("--p", reduce ? 1 : p.toFixed(3));
            }
            marquees.forEach(function (t) {
                var anim = t.getAnimations()[0];
                if (anim) anim.playbackRate = 1 + Math.min(Math.abs(velocity) / 12, 5) * (velocity < 0 ? -1 : 1);
            });
            lastY = y;
            ticking = false;
        }
        function onScroll() { if (!ticking) { ticking = true; raf(frame); } }
        window.addEventListener("scroll", onScroll, { passive: true });
        window.addEventListener("resize", function () { raf(measure); }, { passive: true });
        raf(function () { measure(); frame(); });
        // Ramène doucement le marquee à sa vitesse normale après le scroll
        if (marquees.length) setInterval(function () { if (Math.abs(velocity) > 0.05) { velocity *= 0.6; onScroll(); } }, 120);
    }

    /* ---------- Menu mobile ---------- */
    function initMenu() {
        var btn = document.querySelector(".menu-btn");
        var menu = document.getElementById("mobile-menu");
        if (!btn || !menu) return;
        function set(open) {
            doc.classList.toggle("menu-open", open);
            btn.setAttribute("aria-expanded", open ? "true" : "false");
            btn.setAttribute("aria-label", open ? "Fermer le menu" : "Ouvrir le menu");
            menu.setAttribute("aria-hidden", open ? "false" : "true");
            if (open) { menu.removeAttribute("inert"); } else { menu.setAttribute("inert", ""); }
            document.body.style.overflow = open ? "hidden" : "";
            if (open) { var first = menu.querySelector("a"); if (first) first.focus(); }
        }
        set(false);
        btn.addEventListener("click", function () { set(!doc.classList.contains("menu-open")); });
        menu.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { set(false); }); });
        document.addEventListener("keydown", function (e) {
            if (e.key === "Escape" && doc.classList.contains("menu-open")) { set(false); btn.focus(); }
        });
    }

    /* ---------- Révélations au scroll ---------- */
    function initReveal() {
        document.querySelectorAll("[data-stagger]").forEach(function (group) {
            var step = parseInt(group.getAttribute("data-stagger"), 10) || 80;
            Array.prototype.forEach.call(group.querySelectorAll("[data-reveal]"), function (el, i) {
                el.style.setProperty("--d", Math.min(i * step, 600) + "ms");
            });
        });
        var els = document.querySelectorAll(".section [data-reveal], .section .split, .step, .site-footer [data-reveal]");
        if (reduce || !("IntersectionObserver" in window)) {
            els.forEach(function (el) { el.classList.add("is-in"); });
            return;
        }
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) { entry.target.classList.add("is-in"); io.unobserve(entry.target); }
            });
        }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
        els.forEach(function (el) { io.observe(el); });
        window.addEventListener("beforeprint", function () { els.forEach(function (el) { el.classList.add("is-in"); }); });
    }

    /* ---------- Mot rotatif ---------- */
    function initRotator() {
        var rot = document.querySelector(".rotator");
        if (!rot) return;
        var items = rot.querySelectorAll("span");
        if (items.length < 2) return;
        var i = 0;
        items[0].classList.add("is-current");
        if (reduce) return;
        setInterval(function () {
            if (document.hidden) return;
            var cur = items[i];
            i = (i + 1) % items.length;
            var next = items[i];
            cur.classList.remove("is-current");
            cur.classList.add("is-leaving");
            next.classList.remove("is-leaving");
            next.classList.add("is-current");
            setTimeout(function () { cur.classList.remove("is-leaving"); }, 750);
        }, 2600);
    }

    /* ---------- Compteurs ---------- */
    function initCounters() {
        var els = document.querySelectorAll("[data-count]");
        if (!els.length) return;
        function run(el) {
            var target = parseFloat(el.getAttribute("data-count"));
            var suffix = el.getAttribute("data-suffix") || "";
            if (reduce) { el.textContent = target + suffix; return; }
            var start = null, dur = 1600;
            function step(t) {
                if (!start) start = t;
                var p = Math.min((t - start) / dur, 1);
                el.textContent = Math.round(target * (1 - Math.pow(1 - p, 4))) + suffix;
                if (p < 1) raf(step);
            }
            raf(step);
        }
        if (!("IntersectionObserver" in window)) { els.forEach(run); return; }
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) { if (e.isIntersecting) { run(e.target); io.unobserve(e.target); } });
        }, { threshold: 0.6 });
        els.forEach(function (el) { io.observe(el); });
    }

    /* ---------- Texte qui roule dans les boutons ---------- */
    function initRollText() {
        if (reduce) return;
        document.querySelectorAll(".btn, .link-arrow").forEach(function (btn) {
            Array.prototype.slice.call(btn.childNodes).forEach(function (node) {
                if (node.nodeType !== 3 || !node.textContent.trim()) return;
                var text = node.textContent.trim();
                var wrap = document.createElement("span");
                wrap.className = "roll";
                var a = document.createElement("span"); a.textContent = text;
                var b = document.createElement("span"); b.textContent = text; b.setAttribute("aria-hidden", "true");
                wrap.appendChild(a); wrap.appendChild(b);
                var lead = /^\s/.test(node.textContent) ? " " : "";
                var trail = /\s$/.test(node.textContent) ? " " : "";
                var frag = document.createDocumentFragment();
                if (lead) frag.appendChild(document.createTextNode(lead));
                frag.appendChild(wrap);
                if (trail) frag.appendChild(document.createTextNode(trail));
                btn.replaceChild(frag, node);
            });
        });
    }

    /* ---------- Effets souris : magnétisme, spotlight, inclinaison, curseur ---------- */
    function initPointerFx() {
        if (!finePointer || reduce) return;

        document.querySelectorAll("[data-magnetic]").forEach(function (el) {
            var rect = null;
            el.addEventListener("pointerenter", function () { rect = el.getBoundingClientRect(); });
            el.addEventListener("pointermove", function (e) {
                if (!rect) rect = el.getBoundingClientRect();
                el.style.setProperty("--bx", ((e.clientX - rect.left - rect.width / 2) * 0.25).toFixed(1) + "px");
                el.style.setProperty("--by", ((e.clientY - rect.top - rect.height / 2) * 0.35).toFixed(1) + "px");
            });
            el.addEventListener("pointerleave", function () { rect = null; el.style.setProperty("--bx", "0px"); el.style.setProperty("--by", "0px"); });
        });

        document.querySelectorAll(".card").forEach(function (card) {
            var rect = null;
            var tilt = card.matches(".service, .project, .cert-pro, .badge");
            if (tilt) card.classList.add("tilt");
            card.addEventListener("pointerenter", function () { rect = card.getBoundingClientRect(); if (tilt) card.classList.add("is-tilting"); });
            card.addEventListener("pointermove", function (e) {
                if (!rect) rect = card.getBoundingClientRect();
                var x = e.clientX - rect.left, y = e.clientY - rect.top;
                card.style.setProperty("--mx", x + "px");
                card.style.setProperty("--my", y + "px");
                if (tilt) {
                    card.style.setProperty("--ry", ((x / rect.width - 0.5) * 6).toFixed(2) + "deg");
                    card.style.setProperty("--rx", ((0.5 - y / rect.height) * 6).toFixed(2) + "deg");
                }
            });
            card.addEventListener("pointerleave", function () {
                rect = null;
                if (tilt) { card.classList.remove("is-tilting"); card.style.setProperty("--rx", "0deg"); card.style.setProperty("--ry", "0deg"); }
            });
        });

        var hero = document.querySelector(".hero");
        var blobs = document.querySelectorAll(".hero .blob");
        if (hero && blobs.length) {
            hero.addEventListener("pointermove", function (e) {
                var cx = e.clientX / window.innerWidth - 0.5, cy = e.clientY / window.innerHeight - 0.5;
                raf(function () {
                    blobs.forEach(function (b, k) { var f = (k + 1) * 18; b.style.translate = (cx * f).toFixed(1) + "px " + (cy * f).toFixed(1) + "px"; });
                });
            });
        }

        // Curseur sur-mesure : point + anneau avec inertie, libellé « Voir » sur les projets
        var dot = document.createElement("div"); dot.className = "cursor"; dot.setAttribute("aria-hidden", "true");
        var ring = document.createElement("div"); ring.className = "cursor-ring"; ring.setAttribute("aria-hidden", "true");
        ring.innerHTML = "<span>Voir</span>";
        document.body.appendChild(dot); document.body.appendChild(ring);
        var mx = -100, my = -100, rx = -100, ry = -100, running = false;
        function loop() {
            rx += (mx - rx) * 0.18; ry += (my - ry) * 0.18;
            dot.style.transform = "translate3d(" + mx + "px," + my + "px,0)";
            ring.style.transform = "translate3d(" + rx.toFixed(1) + "px," + ry.toFixed(1) + "px,0)" + (ring.classList.contains("is-down") ? " scale(.85)" : "");
            if (Math.abs(mx - rx) > 0.1 || Math.abs(my - ry) > 0.1) { raf(loop); } else { running = false; }
        }
        window.addEventListener("pointermove", function (e) {
            if (e.pointerType !== "mouse") return;
            mx = e.clientX; my = e.clientY;
            doc.classList.add("has-cursor");
            if (!running) { running = true; raf(loop); }
        }, { passive: true });
        document.addEventListener("pointerleave", function () { doc.classList.remove("has-cursor"); });
        window.addEventListener("pointerdown", function () { ring.classList.add("is-down"); if (!running) { running = true; raf(loop); } });
        window.addEventListener("pointerup", function () { ring.classList.remove("is-down"); if (!running) { running = true; raf(loop); } });
        document.addEventListener("pointerover", function (e) {
            var t = e.target;
            var view = t.closest && t.closest(".project, .next-case");
            var link = t.closest && t.closest("a, button, summary, .filter");
            ring.classList.toggle("is-view", !!view);
            ring.classList.toggle("is-link", !view && !!link);
        });
    }

    /* ---------- Filtres des projets ---------- */
    function initFilters() {
        var buttons = document.querySelectorAll(".filter");
        var items = document.querySelectorAll(".project[data-cat]");
        if (!buttons.length) return;
        buttons.forEach(function (btn) {
            btn.addEventListener("click", function () {
                var cat = btn.getAttribute("data-filter");
                buttons.forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
                var apply = function () {
                    var n = 0;
                    items.forEach(function (it) {
                        var show = cat === "all" || it.getAttribute("data-cat") === cat;
                        it.hidden = !show;
                        if (show) { it.style.setProperty("--d", (n++ * 60) + "ms"); it.classList.remove("is-in"); }
                    });
                    raf(function () { raf(function () { items.forEach(function (it) { if (!it.hidden) it.classList.add("is-in"); }); }); });
                };
                if (document.startViewTransition && !reduce) { document.startViewTransition(apply); } else { apply(); }
            });
        });
    }

    /* ---------- Copier l'e-mail ---------- */
    function initCopy() {
        document.querySelectorAll("[data-copy]").forEach(function (btn) {
            btn.addEventListener("click", function (e) {
                e.preventDefault(); e.stopPropagation();
                var label = btn.querySelector("span");
                if (navigator.clipboard && navigator.clipboard.writeText) {
                    navigator.clipboard.writeText(btn.getAttribute("data-copy")).then(function () {
                        if (!label) return;
                        var old = label.textContent;
                        label.textContent = "Copié !";
                        setTimeout(function () { label.textContent = old; }, 1800);
                    }, function () {});
                }
            });
        });
    }

    /* ---------- Lien de navigation actif ---------- */
    function initActiveNav() {
        var links = document.querySelectorAll('.nav a[href*="#"]');
        if (!links.length || !("IntersectionObserver" in window)) return;
        var map = {};
        links.forEach(function (a) {
            var id = a.getAttribute("href").split("#")[1];
            if (id && document.getElementById(id)) map[id] = a;
        });
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                if (!map[e.target.id]) return;
                if (e.isIntersecting) {
                    links.forEach(function (l) { l.classList.remove("is-active"); });
                    map[e.target.id].classList.add("is-active");
                }
            });
        }, { rootMargin: "-45% 0px -50% 0px" });
        Object.keys(map).forEach(function (id) { io.observe(document.getElementById(id)); });
    }

    function initYear() {
        document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
    }

    function boot() {
        initMenu();
        initReveal();
        initRotator();
        initCounters();
        initRollText();
        initFilters();
        initCopy();
        initActiveNav();
        initYear();
        // Effets non essentiels : après le premier rendu, quand le navigateur est libre
        var idle = window.requestIdleCallback || function (cb) { return setTimeout(cb, 200); };
        idle(function () { initScrollLoop(); initPointerFx(); });
    }
    if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", boot); } else { boot(); }
})();
