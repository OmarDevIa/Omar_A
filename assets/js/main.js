/* Omar.tech — motion & interactions (JS natif, sans dépendance) */
(function () {
    "use strict";

    var doc = document.documentElement;
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

    /* ---------- Header : état scroll, masquage, progression ---------- */
    function initHeader() {
        var header = document.querySelector(".site-header");
        var bar = document.querySelector(".progress");
        var lastY = window.scrollY;
        var ticking = false;

        function update() {
            var y = window.scrollY;
            if (header) {
                header.classList.toggle("is-scrolled", y > 20);
                var goingDown = y > lastY && y > 400;
                header.classList.toggle("is-hidden", goingDown && !doc.classList.contains("menu-open"));
            }
            if (bar) {
                var h = doc.scrollHeight - window.innerHeight;
                bar.style.transform = "scaleX(" + (h > 0 ? y / h : 0) + ")";
            }
            lastY = y;
            ticking = false;
        }
        window.addEventListener("scroll", function () {
            if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
        }, { passive: true });
        update();
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

    /* ---------- Révélations au scroll (+ décalage en cascade) ---------- */
    function initReveal() {
        document.querySelectorAll("[data-stagger]").forEach(function (group) {
            var step = parseInt(group.getAttribute("data-stagger"), 10) || 80;
            Array.prototype.forEach.call(group.querySelectorAll("[data-reveal]"), function (el, i) {
                el.style.setProperty("--d", (i * step) + "ms");
            });
        });
        var els = document.querySelectorAll("[data-reveal], .split, .step");
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
        // Sécurité : tout afficher si l'observer ne s'est pas déclenché (ex. impression, capture)
        window.addEventListener("beforeprint", function () { els.forEach(function (el) { el.classList.add("is-in"); }); });
    }

    /* ---------- Mot rotatif du hero ---------- */
    function initRotator() {
        var rot = document.querySelector(".rotator");
        if (!rot) return;
        var items = rot.querySelectorAll("span");
        if (items.length < 2) return;
        var i = 0;
        items[0].classList.add("is-current");
        if (reduce) return;
        setInterval(function () {
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
            function frame(t) {
                if (!start) start = t;
                var p = Math.min((t - start) / dur, 1);
                var eased = 1 - Math.pow(1 - p, 4);
                el.textContent = Math.round(target * eased) + suffix;
                if (p < 1) requestAnimationFrame(frame);
            }
            requestAnimationFrame(frame);
        }
        if (!("IntersectionObserver" in window)) { els.forEach(run); return; }
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) { if (e.isIntersecting) { run(e.target); io.unobserve(e.target); } });
        }, { threshold: 0.6 });
        els.forEach(function (el) { io.observe(el); });
    }

    /* ---------- Boutons magnétiques & spotlight des cartes ---------- */
    function initPointerFx() {
        if (!finePointer || reduce) return;
        document.querySelectorAll("[data-magnetic]").forEach(function (el) {
            el.addEventListener("pointermove", function (e) {
                var r = el.getBoundingClientRect();
                var x = (e.clientX - r.left - r.width / 2) * 0.25;
                var y = (e.clientY - r.top - r.height / 2) * 0.35;
                el.style.setProperty("--bx", x.toFixed(1) + "px");
                el.style.setProperty("--by", y.toFixed(1) + "px");
            });
            el.addEventListener("pointerleave", function () {
                el.style.setProperty("--bx", "0px");
                el.style.setProperty("--by", "0px");
            });
        });
        document.querySelectorAll(".card").forEach(function (card) {
            card.addEventListener("pointermove", function (e) {
                var r = card.getBoundingClientRect();
                card.style.setProperty("--mx", (e.clientX - r.left) + "px");
                card.style.setProperty("--my", (e.clientY - r.top) + "px");
            });
        });
        var hero = document.querySelector(".hero");
        var blobs = document.querySelectorAll(".hero .blob");
        if (hero && blobs.length) {
            hero.addEventListener("pointermove", function (e) {
                var cx = e.clientX / window.innerWidth - 0.5;
                var cy = e.clientY / window.innerHeight - 0.5;
                blobs.forEach(function (b, k) {
                    var f = (k + 1) * 14;
                    b.style.translate = (cx * f).toFixed(1) + "px " + (cy * f).toFixed(1) + "px";
                });
            });
        }
    }

    /* ---------- Ligne de progression du processus ---------- */
    function initProcess() {
        var list = document.querySelector(".process");
        if (!list) return;
        function update() {
            var r = list.getBoundingClientRect();
            var vh = window.innerHeight;
            var p = Math.min(Math.max((vh * 0.85 - r.top) / (vh * 0.6), 0), 1);
            list.style.setProperty("--p", reduce ? 1 : p.toFixed(3));
        }
        window.addEventListener("scroll", update, { passive: true });
        update();
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
                items.forEach(function (it) {
                    var show = cat === "all" || it.getAttribute("data-cat") === cat;
                    it.hidden = !show;
                    if (show && !reduce) {
                        it.classList.remove("is-in");
                        void it.offsetWidth;
                        it.classList.add("is-in");
                    }
                });
            });
        });
    }

    /* ---------- Copier l'e-mail ---------- */
    function initCopy() {
        document.querySelectorAll("[data-copy]").forEach(function (btn) {
            btn.addEventListener("click", function (e) {
                e.preventDefault();
                e.stopPropagation();
                var value = btn.getAttribute("data-copy");
                var label = btn.querySelector("span");
                var done = function () {
                    if (!label) return;
                    var old = label.textContent;
                    label.textContent = "Copié !";
                    setTimeout(function () { label.textContent = old; }, 1800);
                };
                if (navigator.clipboard && navigator.clipboard.writeText) {
                    navigator.clipboard.writeText(value).then(done, function () {});
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
            var sec = id && document.getElementById(id);
            if (sec) map[id] = a;
        });
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                if (e.isIntersecting && map[e.target.id]) {
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
        initHeader();
        initMenu();
        initReveal();
        initRotator();
        initCounters();
        initPointerFx();
        initProcess();
        initFilters();
        initCopy();
        initActiveNav();
        initYear();
    }
    if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", boot); } else { boot(); }
})();
