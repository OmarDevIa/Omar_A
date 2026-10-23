"""Omar.tech — générateur du site statique (refonte premium sombre 2026).

Usage : python _build/build.py   (depuis la racine du dépôt)
Contenu : _build/content_data.py (profil, services, FAQ, compétences, badges) et _build/projects_v2.py (études de cas).
Génère : index.html, 5 pages services, 12 études de cas, robots.txt, sitemap.xml, llms.txt
"""
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import content_data as C  # noqa: E402
from projects_v2 import CATS, CATS_SHORT, PROJECTS
from landing_data import LANDINGS  # noqa: E402

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent
SCRATCH = HERE.parent
SITE = 'https://www.omar-tech.com'
TODAY = '2026-10-23'
TODAY_FR = '23 octobre 2026'
EMAIL = 'attaomar66@gmail.com'
WA_NUM = '+39 328 721 09 29'
WHATSAPP = ('https://wa.me/393287210929?text=Bonjour%20Omar%2C%20j%27ai%20vu%20votre%20portfolio%20'
            'et%20je%20souhaiterais%20discuter%20d%27un%20projet.')
LINKEDIN = 'https://www.linkedin.com/in/omaratta-805a36344'
GITHUB = 'https://github.com/OmarDevIa'
CREDLY = 'https://www.credly.com/users/omar-atta-yakouba-maikassa'
SAME_AS = [LINKEDIN, GITHUB, CREDLY]
AREAS = [a.strip() for a in C.PROFILE['areas_served'].split(',')]
OG_IMAGE = f'{SITE}/img/og-omar-atta.jpg'
PRO_CERTS = [
    ('IBM Full Stack Software Developer', 'Professional Certificate · IBM',
     'https://www.credly.com/badges/84bc6f03-87d3-4fc6-b3dd-c67a48f70d2a/public_url', 'img/badge-ibm-full-stack-developer.webp'),
    ('IBM AI Developer', 'Professional Certificate · IBM',
     'https://www.credly.com/badges/b5b05f89-e8e7-48a4-b96d-f73b05b33f1f/public_url', 'img/badge-ibm-ai-developer.webp'),
]
SERVICE_ICONS = {
    'creation-site-web': 'layout-template', 'developpement-application-web-mobile': 'smartphone',
    'automatisation-ia-workflows': 'workflow', 'seo-geo-referencement': 'chart-line', 'gestion-reseaux-sociaux': 'share-2',
}
SERVICE_TAGS = {
    'creation-site-web': ['Sites vitrines', 'E-commerce', 'WordPress', 'Shopify', 'Sur mesure'],
    'developpement-application-web-mobile': ['SaaS', 'ERP / CRM', 'Flutter', 'React', 'Django'],
    'automatisation-ia-workflows': ['n8n', 'Make', 'Zapier', 'Chatbots', 'RAG'],
    'seo-geo-referencement': ['Audit', 'Schema.org', 'SEO local', 'ChatGPT', 'Perplexity'],
    'gestion-reseaux-sociaux': ['Instagram', 'LinkedIn', 'TikTok', 'Facebook', 'Contenu IA'],
}
SKILL_ICONS = ['code-xml', 'layers', 'shopping-cart', 'smartphone', 'brain', 'zap', 'cloud-upload', 'search', 'sparkles', 'share-2']
STACK = ['Python', 'Django', 'FastAPI', 'React', 'Next.js', 'TypeScript', 'Angular', 'Node.js', 'Laravel', 'Flutter',
         'WordPress', 'Shopify', 'n8n', 'Make', 'Zapier', 'LangChain', 'OpenAI', 'Gemini', 'Hugging Face',
         'PostgreSQL', 'MySQL', 'Docker', 'AWS', 'IBM Cloud', 'Google Search Console']

e = html.escape
SERVICES = C.SERVICES
SVC = {s['slug']: s for s in SERVICES}
PRJ = {p['file']: p for p in PROJECTS}


# ------------------------------------------------------------------ icônes
def build_sprite():
    cached = HERE / 'icons.svg'
    if cached.exists():
        return cached.read_text(encoding='utf-8')
    lucide = SCRATCH / 'lucide' / 'icons'
    names = ['arrow-right', 'arrow-up-right', 'check', 'mail', 'award', 'globe', 'map-pin', 'chevron-down', 'sparkles',
             'layers', 'zap', 'cloud-upload', 'brain', 'file-down', 'message-circle', 'chart-line', 'badge-check',
             'languages', 'clock', 'code-xml', 'smartphone', 'search', 'shopping-cart', 'share-2', 'layout-template',
             'workflow', 'copy', 'briefcase', 'external-link', 'calendar']
    symbols = []
    for n in names:
        svg = (lucide / f'{n}.svg').read_text()
        inner = re.search(r'<svg[^>]*>(.*)</svg>', svg, re.S).group(1)
        inner = re.sub(r'\s+', ' ', inner).strip()
        symbols.append(f'<symbol id="i-{n}" viewBox="0 0 24 24">{inner}</symbol>')
    symbols.append('<symbol id="i-linkedin" viewBox="0 0 24 24"><rect x="2.5" y="2.5" width="19" height="19" rx="4"/>'
                   '<path d="M7.5 10.5v6M7.5 7.5v.01M11.5 16.5v-6M11.5 13a2.5 2.5 0 0 1 5 0v3.5"/></symbol>')
    for n in ['whatsapp', 'github']:
        svg = (SCRATCH / 'si' / 'icons' / f'{n}.svg').read_text()
        path = re.search(r'<path d="([^"]+)"', svg).group(1)
        symbols.append(f'<symbol id="i-{n}" viewBox="0 0 24 24"><path class="fill" d="{path}"/></symbol>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">'
            '<style>.fill{fill:currentColor;stroke:none}</style>' + ''.join(symbols) + '</svg>')


SPRITE = None


def load_css():
    css = (ROOT / 'assets' / 'css' / 'main.css').read_text(encoding='utf-8')
    css = css.replace('url("../fonts/', 'url("assets/fonts/')
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{};:,>])\s*', r'\1', css)
    css = css.replace(';}', '}')
    # rétablir les espaces significatifs dans les sélecteurs descendants « :hover .x » etc. déjà conservés
    return css.strip()


INLINE_CSS = ''


def icon(name, cls='icon'):
    return f'<svg class="{cls}" aria-hidden="true" focusable="false"><use href="#i-{name}"/></svg>'


# ------------------------------------------------------------------ JSON-LD
def ld(data):
    return json.dumps(prune(data), ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')


def prune(v):
    if isinstance(v, dict):
        return {k: prune(x) for k, x in v.items() if x not in (None, [], '', {})}
    if isinstance(v, list):
        return [prune(x) for x in v if x not in (None, '', {})]
    return v


def strip(s):
    return ' '.join(re.sub(r'<[^>]+>', ' ', s).split())


def service_url(s):
    return f'{SITE}/{s["slug"]}.html'


def site_graph():
    creds = [{'@type': 'EducationalOccupationalCredential', 'name': n, 'credentialCategory': 'Professional Certificate',
              'url': u, 'recognizedBy': {'@type': 'Organization', 'name': 'IBM'}} for n, _, u, _ in PRO_CERTS]
    for label, issuer, bid, img, issued, order in C.CREDLY_BADGES:
        creds.append({'@type': 'EducationalOccupationalCredential', 'name': label, 'credentialCategory': 'Certificate',
                      'url': C.credly_badge_url(bid), 'recognizedBy': {'@type': 'Organization', 'name': issuer.split(' · ')[0]}})
    offers = [{'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': s['title'], 'description': s['description'],
                                                 'url': service_url(s), 'provider': {'@id': f'{SITE}/#business'}}} for s in SERVICES]
    return {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebSite', '@id': f'{SITE}/#website', 'url': f'{SITE}/', 'name': 'Omar.tech', 'inLanguage': 'fr-FR',
         'publisher': {'@id': f'{SITE}/#business'}},
        {'@type': 'Person', '@id': f'{SITE}/#person', 'name': 'Omar Amadou Wankoye', 'alternateName': ['Omar A. Wankoye', 'Omar Wankoye', 'Omar Atta', 'Omar Atta Yakouba Maikassa'],
         'jobTitle': 'Développeur web freelance', 'url': f'{SITE}/', 'image': f'{SITE}/img/omar-atta-portrait.webp',
         'email': f'mailto:{EMAIL}', 'sameAs': SAME_AS, 'description': strip(C.PROFILE['about_intro']),
         'knowsAbout': [s[2] for s in C.SKILLS], 'knowsLanguage': ['fr', 'en'], 'hasCredential': creds,
         'worksFor': {'@id': f'{SITE}/#business'}},
        {'@type': 'ProfessionalService', '@id': f'{SITE}/#business', 'name': 'Omar.tech',
         'alternateName': 'Omar A. Wankoye – Développeur web freelance', 'description': C.PROFILE['seo_description'],
         'url': f'{SITE}/', 'logo': f'{SITE}/img/og-omar-atta.jpg', 'image': OG_IMAGE, 'email': EMAIL,
         'founder': {'@id': f'{SITE}/#person'}, 'areaServed': [{'@type': 'Place', 'name': a} for a in AREAS],
         'availableLanguage': ['French', 'English'], 'sameAs': SAME_AS, 'knowsAbout': [s['title'] for s in SERVICES],
         'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Développement web, IA et marketing digital', 'itemListElement': offers},
         'contactPoint': {'@type': 'ContactPoint', 'contactType': 'sales', 'email': EMAIL, 'url': f'{SITE}/#contact',
                          'availableLanguage': ['French', 'English']}},
    ]}


def faq_ld(faqs):
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faqs]}


def crumbs_ld(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i, 'name': n, 'item': u} for i, (n, u) in enumerate(items, 1)]}


# ------------------------------------------------------------------ gabarits
def head(title, desc, canonical, *, og_type='website', image=OG_IMAGE, image_alt='Omar A. Wankoye, développeur web freelance',
         extra_ld=(), preload=''):
    blocks = ''.join(f'\n<script type="application/ld+json">{ld(b)}</script>' for b in extra_ld)
    return f'''<!DOCTYPE html>
<html lang="fr" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="author" content="Omar A. Wankoye">
<meta name="theme-color" content="#07080c">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="fr" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<link rel="alternate" type="text/plain" title="llms.txt" href="{SITE}/llms.txt">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Omar.tech">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{image}">
<meta property="og:image:alt" content="{e(image_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{image}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="img/omar-atta-contact.webp">
<link rel="preload" href="assets/fonts/bricolage-grotesque.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/instrument-serif-italic.woff2" as="font" type="font/woff2" crossorigin>
{preload}<style>{INLINE_CSS}</style>
<script>document.documentElement.classList.replace('no-js','js')</script>
<script src="assets/js/main.js" defer></script>
<script type="application/ld+json">{ld(site_graph())}</script>{blocks}
</head>
'''


NAV = [('Services', 'services'), ('À propos', 'about'), ('Méthode', 'process'), ('Projets', 'projects'),
       ('Certifications', 'certifications'), ('FAQ', 'faq')]


def header(home):
    p = '' if home else 'index.html'
    links = '\n'.join(f'      <a href="{p}#{anchor}">{label}</a>' for label, anchor in NAV)
    mlinks = '\n'.join(f'      <a href="{p}#{anchor}" style="--i:{i}">{label}</a>' for i, (label, anchor) in enumerate(NAV + [('Contact', 'contact')]))
    return f'''<body>
<a class="skip-link" href="#main">Aller au contenu</a>
<div class="progress" aria-hidden="true"></div>
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="Omar.tech — accueil">Omar<b>.</b>tech</a>
    <nav class="nav" aria-label="Navigation principale">
{links}
    </nav>
    <div class="header-cta">
      <a class="btn btn--primary btn--sm" href="{p}#contact" data-magnetic>Devis gratuit {icon('arrow-up-right', 'icon icon--diag')}</a>
      <button class="menu-btn" type="button" aria-controls="mobile-menu" aria-expanded="false" aria-label="Ouvrir le menu"><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu" aria-hidden="true">
  <nav aria-label="Navigation mobile">
{mlinks}
  </nav>
  <div class="mobile-menu-foot">
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    <a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp · {WA_NUM}</a>
  </div>
</div>
'''


def footer():
    svc = '\n'.join(f'          <li><a href="{s["slug"]}.html">{e(s["title"])}</a></li>' for s in SERVICES)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="index.html">Omar<b>.</b>tech</a>
        <p style="margin-top:14px">Omar A. Wankoye, développeur web freelance certifié IBM &amp; Google. Sites web, applications, automatisation IA, SEO &amp; GEO et réseaux sociaux.</p>
        <div class="socials">
          <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{icon('linkedin')}</a>
          <a href="{GITHUB}" target="_blank" rel="noopener" aria-label="GitHub">{icon('github')}</a>
          <a href="{WHATSAPP}" target="_blank" rel="noopener" aria-label="WhatsApp">{icon('whatsapp')}</a>
          <a href="mailto:{EMAIL}" aria-label="E-mail">{icon('mail')}</a>
        </div>
      </div>
      <nav aria-label="Services">
        <p class="footer-title">Services</p>
        <ul>
{svc}
        </ul>
      </nav>
      <div>
        <p class="footer-title">Expertises</p>
        <ul>
{''.join(f'          <li><a href="{l["slug"]}.html">{e(l["h1"])}</a></li>' + chr(10) for l in LANDINGS)}          <li><a href="index.html#projects">Projets</a></li>
          <li><a href="cv.pdf" target="_blank">CV (PDF)</a></li>
        </ul>
      </div>
      <div>
        <p class="footer-title">Zones</p>
        <p>{' · '.join(e(a) for a in AREAS)}</p>
        <p>Français · English</p>
      </div>
    </div>
    <p class="footer-giant" aria-hidden="true">Omar.tech</p>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Omar A. Wankoye — Omar.tech. Tous droits réservés.</span>
      <span>Conçu &amp; développé par Omar A. Wankoye</span>
    </div>
  </div>
</footer>
{SPRITE}
</body>
</html>
'''


def contact_block(heading_tag='h2'):
    return f'''<section class="section" id="contact" aria-labelledby="contact-title">
  <div class="marquee mega-marquee" aria-hidden="true" style="border:0;background:none"><div class="marquee-track"><span>Votre projet mérite le meilleur</span><span>Devis gratuit sous 48 h</span><span>Votre projet mérite le meilleur</span><span>Devis gratuit sous 48 h</span></div></div>
  <div class="container">
    <div class="cta noise" data-reveal="scale">
      <p class="eyebrow">Contact</p>
      <{heading_tag} id="contact-title">Parlons de votre <span class="serif grad-text">projet</span>.</{heading_tag}>
      <p>Site, application, automatisation, visibilité Google &amp; IA ou réseaux sociaux : décrivez votre besoin, je vous réponds avec un devis gratuit et détaillé sous 48 h.</p>
      <div class="cta-actions">
        <a class="btn btn--primary" href="mailto:{EMAIL}?subject=Demande%20de%20devis%20-%20omar-tech.com" data-magnetic>{icon('mail')} Demander un devis</a>
        <a class="btn btn--whatsapp" href="{WHATSAPP}" target="_blank" rel="noopener" data-magnetic>{icon('whatsapp')} WhatsApp</a>
      </div>
      <div class="contact-grid">
        <div class="card contact-item">
          <span class="ci">{icon('mail')}</span>
          <div><strong><a href="mailto:{EMAIL}">E-mail</a></strong><span>{EMAIL}</span>
            <button class="copy-btn" type="button" data-copy="{EMAIL}">{icon('copy')}<span>Copier l’adresse</span></button></div>
        </div>
        <a class="card contact-item" href="{WHATSAPP}" target="_blank" rel="noopener">
          <span class="ci">{icon('whatsapp')}</span>
          <div><strong>WhatsApp</strong><span>{WA_NUM} · réponse rapide</span></div>
        </a>
        <a class="card contact-item" href="{LINKEDIN}" target="_blank" rel="noopener">
          <span class="ci">{icon('linkedin')}</span>
          <div><strong>LinkedIn</strong><span>Voir mon parcours</span></div>
        </a>
      </div>
    </div>
  </div>
</section>
'''


def faq_block(faqs):
    items = '\n'.join(f'''      <details{' open' if i == 0 else ''}>
        <summary><h3>{e(q)}</h3><span class="plus" aria-hidden="true"></span></summary>
        <div class="answer"><p>{e(a)}</p></div>
      </details>''' for i, (q, a) in enumerate(faqs))
    return f'''<div class="faq">
{items}
    </div>'''


def split_words(text_html_parts):
    """text_html_parts : liste de (texte, classe_css|None). Retourne le HTML mot par mot."""
    out, i = [], 0
    for text, cls in text_html_parts:
        for word in text.split(' '):
            if not word:
                continue
            inner = e(word)
            if cls:
                inner = f'<span class="{cls}">{inner}</span>'
            out.append(f'<span class="w"><span style="--i:{i}">{inner}</span></span>')
            i += 1
    return ' '.join(out)


def split_titles(html_out):
    """Découpe les titres de section (h2.section-title, .cta h2) en mots animés."""
    def conv(m):
        open_tag, inner = m.group(1), m.group(2)
        parts, i = [], 0
        for seg in re.split(r'(<span class="[^"]+">.*?</span>)', inner):
            if not seg:
                continue
            sm = re.match(r'<span class="([^"]+)">(.*?)</span>', seg)
            cls, text = (sm.group(1), sm.group(2)) if sm else (None, seg)
            for word in re.split(r'(\s+)', text):
                if not word or word.isspace():
                    if word:
                        parts.append(' ')
                    continue
                inner_w = f'<span class="{cls}">{word}</span>' if cls else word
                parts.append(f'<span class="w"><span style="--i:{i}">{inner_w}</span></span>')
                i += 1
        tag = open_tag.replace('class="', 'class="split ', 1) if 'class="' in open_tag else open_tag[:-1] + ' class="split">'
        return tag + ''.join(parts).strip() + '</h2>'
    return re.sub(r'(<h2[^>]*class="section-title"[^>]*>|<h2 id="contact-title">)(.*?)</h2>', conv, html_out, flags=re.S)


def project_card(p, i=0, reveal=True):
    tags = ''.join(f'<li>{e(t)}</li>' for t in p['tech'][:4])
    return f'''      <article class="card project" data-cat="{p['cat']}"{' data-reveal' if reveal else ''}>
        <div class="project-media">
          <img src="img/projects/{p['slug']}.webp" width="960" height="600" alt="Aperçu du projet {e(p['title'])}" loading="lazy" decoding="async">
          <span class="open" aria-hidden="true">{icon('arrow-up-right')}</span>
        </div>
        <div class="project-body">
          <p class="project-cat">{e(CATS_SHORT[p['cat']])} · {e(p['sector'])}</p>
          <h3><a href="{p['file']}">{e(p['title'])}</a></h3>
          <p>{e(p['card'])}</p>
          <ul class="tags" aria-label="Technologies">{tags}</ul>
        </div>
      </article>'''


# ------------------------------------------------------------------ accueil
def build_index():
    h1 = split_words([('Développeur web freelance :', None), ('des sites, des apps et de l’IA', 'serif grad-text'),
                      ('qui vous apportent des clients.', None)])
    rot = ''.join(f'<span>{e(t)}</span>' for t in [
        'Création de sites web', 'Applications web & mobiles', 'Automatisation & IA', 'SEO & GEO', 'Réseaux sociaux'])

    cards = []
    for i, s in enumerate(SERVICES):
        wide = ' service--wide' if i < 2 else ''
        tags = ''.join(f'<li>{e(t)}</li>' for t in SERVICE_TAGS[s['slug']])
        cards.append(f'''      <article class="card service{wide}" data-reveal>
        <div class="service-top"><span class="service-icon">{icon(SERVICE_ICONS[s['slug']])}</span><span class="service-num">0{i + 1}</span></div>
        <h3>{e(s['title'])}</h3>
        <p>{e(s['description'])}</p>
        <ul aria-label="Exemples">{tags}</ul>
        <a class="link-arrow stretched" href="{s['slug']}.html">Découvrir le service<span class="sr-only"> : {e(s['title'])}</span> {icon('arrow-up-right')}</a>
      </article>''')
    cards = '\n'.join(cards)

    stats = [('4', '+', "Années d’expérience"), ('12', '+', 'Projets livrés'), ('43', '', 'Badges IBM & Google'), ('48', ' h', 'Pour recevoir un devis')]
    stats_html = '\n'.join(f'''        <div class="stat" data-reveal><strong data-count="{n}" data-suffix="{e(suf)}">{n}{e(suf)}</strong><span>{e(l)}</span></div>''' for n, suf, l in stats)

    steps = [('Appel découverte', 'Gratuit, 30 min : vos objectifs, votre cible, votre budget et vos délais.'),
             ('Devis & plan d’action', 'Une proposition claire sous 48 h : périmètre, planning et prix fixes.'),
             ('Conception & réalisation', 'Livraisons par étapes avec démo : vous validez au fur et à mesure.'),
             ('Mise en ligne & croissance', 'Formation, suivi des résultats, SEO et améliorations continues.')]
    steps_html = '\n'.join(f'''      <li class="step"><span class="step-dot">0{i + 1}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>''' for i, (t, d) in enumerate(steps))

    skills_html = '\n'.join(f'''        <li data-reveal><span class="ci">{icon(SKILL_ICONS[k])}</span><div><strong>{e(t)}</strong><span>{e(d)}</span></div></li>'''
                            for k, (cat, _ic, t, d, o) in enumerate(C.SKILLS))

    filters = '<button class="filter" type="button" data-filter="all" aria-pressed="true">Tous</button>' + ''.join(
        f'<button class="filter" type="button" data-filter="{k}" aria-pressed="false">{e(v)}</button>' for k, v in CATS.items())
    projects_html = '\n'.join(project_card(p, i) for i, p in enumerate(PROJECTS))

    pro_html = '\n'.join(f'''      <a class="card cert-pro" href="{u}" target="_blank" rel="noopener" data-reveal>
        <img src="{img}" width="104" height="104" alt="Badge {e(n)}" loading="lazy" decoding="async">
        <div><strong>{e(n)}</strong><span>{icon('badge-check')} {e(sub)} — vérifier sur Credly</span></div>
      </a>''' for n, sub, u, img in PRO_CERTS)
    badges_html = '\n'.join(f'''      <a class="card badge" href="{C.credly_badge_url(bid)}" target="_blank" rel="noopener" data-reveal>
        <img src="{img}" width="88" height="88" alt="Badge {e(label)}" loading="lazy" decoding="async">
        <strong>{e(label)}</strong><span>{e(issuer)} · {issued[:4]}</span>
      </a>''' for label, issuer, bid, img, issued, order in C.CREDLY_BADGES)

    zone_links = {'Niger': 'creation-site-web-niamey.html', 'Côte d’Ivoire': 'creation-site-web-abidjan.html'}
    zones_html = ''.join(
        (f'<li><a href="{zone_links[a]}">{icon("map-pin")}{e(a)}</a></li>' if a in zone_links else f'<li>{icon("map-pin")}{e(a)}</li>')
        for a in AREAS)
    marquee = ''.join(f'<span>{e(t)}</span>' for t in STACK)

    out = head(C.PROFILE['seo_title'], C.PROFILE['seo_description'], f'{SITE}/', extra_ld=[faq_ld(C.GENERAL_FAQS)],
               preload='<link rel="preload" as="image" href="img/omar-atta-portrait.webp" imagesrcset="img/omar-atta-portrait-480.webp 360w, img/omar-atta-portrait-600.webp 600w, img/omar-atta-portrait.webp 720w" imagesizes="(max-width: 860px) 54vw, 440px" type="image/webp" fetchpriority="high">\n')
    out += header(True)
    out += f'''<main id="main">

<section class="hero noise" id="top" aria-labelledby="hero-title">
  <div class="hero-bg" aria-hidden="true"><div class="grid-lines"></div><div class="blob blob--gold"></div><div class="blob blob--terra"></div><div class="blob blob--teal"></div></div>
  <div class="container hero-grid">
    <div class="portrait" data-reveal="scale" style="--d:300ms">
      <div class="portrait-ring" aria-hidden="true"></div>
      <div class="portrait-frame">
        <img src="img/omar-atta-portrait.webp" srcset="img/omar-atta-portrait-480.webp 360w, img/omar-atta-portrait-600.webp 600w, img/omar-atta-portrait.webp 720w" sizes="(max-width: 860px) 54vw, 440px" width="720" height="900" fetchpriority="high" decoding="async" alt="Portrait d’Omar Amadou Wankoye, développeur web freelance">
      </div>
      <span class="chip-float chip-float--1">{icon('chart-line')} SEO &amp; GEO</span>
      <span class="chip-float chip-float--2">{icon('workflow')} n8n · Make · IA</span>
      <span class="chip-float chip-float--3">{icon('smartphone')} Web &amp; mobile</span>
    </div>
    <div class="hero-copy">
      <p class="status-pill" data-reveal="fade"><span class="dot"></span>Disponible pour de nouveaux projets · réponse sous 48 h</p>
      <h1 class="split" id="hero-title">{h1}</h1>
      <p class="hero-rotator" data-reveal style="--d:500ms">Spécialiste <span class="rotator" aria-hidden="true">{rot}</span><span class="sr-only">création de sites web, applications, automatisation IA, SEO &amp; GEO et réseaux sociaux</span></p>
      <p class="hero-lead" data-reveal style="--d:620ms">Je m’appelle <strong>Omar Amadou Wankoye</strong>. J’aide les PME, startups et indépendants à <strong>gagner des clients en ligne</strong> : un site qui convertit, des outils sur mesure, des tâches automatisées par l’IA et une visibilité sur Google comme dans ChatGPT.</p>
      <div class="hero-actions" data-reveal style="--d:740ms">
        <a class="btn btn--primary" href="#contact" data-magnetic>Démarrer mon projet {icon('arrow-right', 'icon icon--move')}</a>
        <a class="btn btn--ghost" href="#projects" data-magnetic>Voir les réalisations</a>
      </div>
      <ul class="hero-trust" data-reveal style="--d:860ms">
        <li>{icon('badge-check')} Certifié IBM &amp; Google</li>
        <li>{icon('briefcase')} 12+ projets livrés</li>
        <li>{icon('globe')} France · Italie · Afrique · Remote</li>
      </ul>
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true">Défiler<i></i></div>
</section>

<div class="marquee" aria-label="Technologies maîtrisées"><div class="marquee-track"><span>{marquee}</span><span aria-hidden="true">{marquee}</span></div></div>

<section class="section" id="services" aria-labelledby="services-title">
  <div class="container">
    <div class="section-head" data-reveal>
      <p class="eyebrow">Services</p>
      <h2 class="section-title" id="services-title">Tout ce qu’il faut pour <span class="serif grad-text">grandir en ligne</span>.</h2>
      <p class="section-lead">Cinq expertises complémentaires, un seul interlocuteur : du site qui inspire confiance à l’automatisation qui vous fait gagner des heures, jusqu’à la visibilité sur Google et dans les IA.</p>
    </div>
    <div class="bento" data-stagger="90">
{cards}
    </div>
  </div>
</section>

<section class="section section--alt" id="about" aria-labelledby="about-title">
  <div class="container about-grid">
    <div class="about-media" data-reveal="clip">
      <img src="img/omar-atta-a-propos.webp" width="900" height="600" alt="Omar Amadou Wankoye au travail sur un projet de développement web" loading="lazy" decoding="async">
      <div class="badge-float">{icon('award')}<span>Certifié <strong>IBM Full Stack</strong>, <strong>IBM AI Developer</strong> &amp; <strong>Google AI</strong></span></div>
    </div>
    <div class="about-text">
      <div data-reveal>
        <p class="eyebrow">À propos</p>
        <h2 class="section-title" id="about-title">Un développeur full-stack <span class="serif grad-text">orienté résultats</span>.</h2>
      </div>
      <div data-reveal>
        {C.PROFILE['about_intro']}
        {C.PROFILE['about_body']}
      </div>
      <div class="hero-actions" data-reveal style="margin:10px 0 0">
        <a class="btn btn--ghost btn--sm" href="cv.pdf" target="_blank">{icon('file-down')} Télécharger mon CV</a>
        <a class="btn btn--ghost btn--sm" href="{LINKEDIN}" target="_blank" rel="noopener">{icon('linkedin')} LinkedIn</a>
      </div>
      <div class="stats" data-stagger="100">
{stats_html}
      </div>
    </div>
  </div>
</section>

<section class="section" id="process" aria-labelledby="process-title">
  <div class="container">
    <div class="section-head" data-reveal>
      <p class="eyebrow">Méthode</p>
      <h2 class="section-title" id="process-title">Un processus clair, <span class="serif grad-text">sans surprise</span>.</h2>
      <p class="section-lead">Vous savez à chaque étape ce qui est fait, ce qui reste à faire et combien cela coûte.</p>
    </div>
    <ol class="process">
{steps_html}
    </ol>
  </div>
</section>

<section class="section section--alt" id="skills" aria-labelledby="skills-title">
  <div class="container">
    <div class="section-head section-head--center" data-reveal>
      <p class="eyebrow">Compétences</p>
      <h2 class="section-title" id="skills-title">Une stack moderne, <span class="serif grad-text">maîtrisée</span>.</h2>
    </div>
    <ul class="skills-grid" data-stagger="60">
{skills_html}
    </ul>
  </div>
</section>

<section class="section" id="projects" aria-labelledby="projects-title">
  <div class="container">
    <div class="section-head" data-reveal>
      <p class="eyebrow">Réalisations</p>
      <h2 class="section-title" id="projects-title">Des projets <span class="serif grad-text">concrets</span>, en ligne.</h2>
      <p class="section-lead">Sites, e-commerce, applications et chatbots IA livrés pour des restaurants, la santé, l’éducation, l’édition et le commerce.</p>
    </div>
    <div class="filters" role="group" aria-label="Filtrer les projets">{filters}</div>
    <div class="projects" data-stagger="70">
{projects_html}
    </div>
  </div>
</section>

<section class="section section--alt" id="certifications" aria-labelledby="cert-title">
  <div class="container">
    <div class="section-head section-head--center" data-reveal>
      <p class="eyebrow">Certifications</p>
      <h2 class="section-title" id="cert-title">Des compétences <span class="serif grad-text">vérifiables</span>.</h2>
      <p class="section-lead">Certifié par IBM et Google (via Coursera). Chaque badge est vérifiable publiquement sur Credly.</p>
    </div>
    <div class="cert-hero" data-stagger="120">
{pro_html}
    </div>
    <div class="badges" data-stagger="50">
{badges_html}
    </div>
    <div class="center-cta"><a class="btn btn--ghost" href="{CREDLY}" target="_blank" rel="noopener" data-magnetic>Voir les 43 badges sur Credly {icon('arrow-up-right', 'icon icon--diag')}</a></div>
  </div>
</section>

<section class="section section--tight" id="zones" aria-labelledby="zones-title">
  <div class="container">
    <div class="card zones-band" data-reveal>
      <div>
        <p class="eyebrow">Zones d’intervention</p>
        <h2 id="zones-title">100 % remote, <span class="serif grad-text">partout</span>.</h2>
        <p>En français ou en anglais, avec des clients en Europe et en Afrique francophone. Fuseau horaire Europe (UTC+1/+2).</p>
      </div>
      <ul class="zone-list">{zones_html}</ul>
    </div>
  </div>
</section>

<section class="section" id="faq" aria-labelledby="faq-title">
  <div class="container">
    <div class="section-head section-head--center" data-reveal>
      <p class="eyebrow">FAQ</p>
      <h2 class="section-title" id="faq-title">Questions <span class="serif grad-text">fréquentes</span>.</h2>
    </div>
    {faq_block(C.GENERAL_FAQS)}
  </div>
</section>

{contact_block()}
</main>
'''
    out += footer()
    (ROOT / 'index.html').write_text(split_titles(out), encoding='utf-8')


# ------------------------------------------------------------------ services
SERVICE_PROJECTS = {
    'creation-site-web': ['cabinet.html', 'myshop.html', 'convinium.html'],
    'developpement-application-web-mobile': ['myshop.html', 'suptechchatbot.html', 'portfolio-application-mobile-ai.html'],
    'automatisation-ia-workflows': ['suptechchatbot.html', 'chatbotpdf.html', 'siteimage.html'],
    'seo-geo-referencement': ['cabinet.html', 'convinium.html', 'portfolio-site-restaurant.html'],
    'gestion-reseaux-sociaux': [],
}


def build_services():
    for s in SERVICES:
        url = service_url(s)
        title = f'{s["title"]} | Omar A. Wankoye, freelance'
        if len(title) > 60:
            title = f'{s["title"]} | Omar A. Wankoye'
        desc = s['summary'] + ' ' + s['description']
        desc = desc if len(desc) <= 158 else desc[:155].rsplit(' ', 1)[0] + '…'
        service_ld = {'@context': 'https://schema.org', '@type': 'Service', 'name': s['title'], 'serviceType': s['title'],
                      'description': s['summary'], 'url': url, 'provider': {'@id': f'{SITE}/#business'},
                      'areaServed': [{'@type': 'Place', 'name': a} for a in AREAS],
                      'availableChannel': {'@type': 'ServiceChannel', 'serviceUrl': f'{SITE}/#contact'}}
        crumbs = crumbs_ld([('Accueil', f'{SITE}/'), ('Services', f'{SITE}/#services'), (s['title'], url)])
        points = '\n'.join(f'        <li>{icon("check")}<span>{e(p)}</span></li>' for p in s['detail_points'].splitlines())
        others = '\n'.join(f'        <li><a href="{o["slug"]}.html">{icon(SERVICE_ICONS[o["slug"]])}{e(o["title"])}</a></li>' for o in SERVICES if o is not s)
        spec = [l for l in LANDINGS if l['service'] == s['slug']]
        if spec:
            others = '\n'.join(f'        <li><a href="{l["slug"]}.html">{icon("sparkles")}{e(l["h1"])}</a></li>' for l in spec) + '\n' + others
        rel = SERVICE_PROJECTS[s['slug']]
        related = ''
        if rel:
            related = f'''
      <div class="related">
        <h2>Réalisations liées</h2>
        <div class="projects" data-stagger="80" style="grid-template-columns:repeat(auto-fill,minmax(260px,1fr))">
{chr(10).join(project_card(PRJ[f]) for f in rel)}
        </div>
      </div>'''
        h1 = split_words([(s['title'], None)])
        out = head(title, desc, url, extra_ld=[service_ld, faq_ld(s['faqs']), crumbs])
        out += header(False)
        out += f'''<main id="main">
<section class="page-hero noise">
  <div class="hero-bg" aria-hidden="true"><div class="grid-lines"></div><div class="blob blob--gold"></div></div>
  <div class="container">
    <nav aria-label="Fil d’Ariane"><ol class="breadcrumb"><li><a href="index.html">Accueil</a></li><li><a href="index.html#services">Services</a></li><li aria-current="page">{e(s['title'])}</li></ol></nav>
    <p class="eyebrow" data-reveal="fade">Service · Omar A. Wankoye, freelance</p>
    <h1 class="split">{h1}</h1>
    <p class="lead" data-reveal style="--d:300ms">{e(s['summary'])} {e(s['description'])}</p>
    <div class="hero-actions" data-reveal style="--d:420ms;margin:0">
      <a class="btn btn--primary" href="#contact" data-magnetic>Obtenir un devis gratuit {icon('arrow-right', 'icon icon--move')}</a>
      <a class="btn btn--ghost" href="{WHATSAPP}" target="_blank" rel="noopener" data-magnetic>{icon('whatsapp')} WhatsApp</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container page-layout">
    <article>
      <div class="prose" data-reveal>
        {s['full_description']}
      </div>{related}
      <div class="related" data-reveal>
        <h2 id="faq-service">Questions fréquentes</h2>
        {faq_block(s['faqs'])}
      </div>
      <p class="updated">Mis à jour le {TODAY_FR} · Omar A. Wankoye, développeur web freelance certifié IBM &amp; Google.</p>
    </article>
    <aside class="card aside-card" data-reveal>
      <h2>Ce que vous obtenez</h2>
      <ul class="checks">
{points}
      </ul>
      <a class="btn btn--primary btn--block" href="#contact">Obtenir un devis gratuit</a>
      <a class="btn btn--whatsapp btn--block" href="{WHATSAPP}" target="_blank" rel="noopener">{icon('whatsapp')} Discuter sur WhatsApp</a>
      <h2 style="margin-top:14px">Autres services</h2>
      <ul class="aside-links">
{others}
      </ul>
    </aside>
  </div>
</section>

{contact_block()}
</main>
'''
        out += footer()
        (ROOT / f'{s["slug"]}.html').write_text(split_titles(out), encoding='utf-8')



# ------------------------------------------------------------------ pages ciblées (longue traîne)
def build_landings():
    for l in LANDINGS:
        url = f'{SITE}/{l["slug"]}.html'
        parent = SVC[l['service']]
        if l['area']:
            area_ld = [{'@type': 'City', 'name': l['area']['name'],
                        'containedInPlace': {'@type': 'Country', 'name': l['area']['country']}}]
        else:
            area_ld = [{'@type': 'Place', 'name': a} for a in AREAS]
        service_ld = {'@context': 'https://schema.org', '@type': 'Service', 'name': l['h1'], 'serviceType': parent['title'],
                      'description': l['desc'], 'url': url, 'provider': {'@id': f'{SITE}/#business'},
                      'areaServed': area_ld, 'availableChannel': {'@type': 'ServiceChannel', 'serviceUrl': f'{SITE}/#contact'}}
        crumbs = crumbs_ld([('Accueil', f'{SITE}/'), (parent['title'], service_url(parent)), (l['h1'], url)])
        points = '\n'.join(f'        <li>{icon("check")}<span>{e(p)}</span></li>' for p in l['points'])
        siblings = '\n'.join(f'        <li><a href="{o["slug"]}.html">{icon("sparkles")}{e(o["h1"])}</a></li>' for o in LANDINGS if o is not l)
        cards = chr(10).join(project_card(PRJ[f]) for f in l['projects'])
        h1 = split_words([(l['h1'], None)])
        out = head(l['title'], l['desc'], url, extra_ld=[service_ld, faq_ld(l['faqs']), crumbs])
        out += header(False)
        out += f'''<main id="main">
<section class="page-hero noise">
  <div class="hero-bg" aria-hidden="true"><div class="grid-lines"></div><div class="blob blob--gold"></div></div>
  <div class="container">
    <nav aria-label="Fil d’Ariane"><ol class="breadcrumb"><li><a href="index.html">Accueil</a></li><li><a href="{parent['slug']}.html">{e(parent['title'])}</a></li><li aria-current="page">{e(l['h1'])}</li></ol></nav>
    <p class="eyebrow" data-reveal="fade">{e(l['eyebrow'])}</p>
    <h1 class="split">{h1}</h1>
    <p class="lead" data-reveal style="--d:300ms">{e(l['lead'])}</p>
    <div class="hero-actions" data-reveal style="--d:420ms;margin:0">
      <a class="btn btn--primary" href="#contact" data-magnetic>Obtenir un devis gratuit {icon('arrow-right', 'icon icon--move')}</a>
      <a class="btn btn--ghost" href="{WHATSAPP}" target="_blank" rel="noopener" data-magnetic>{icon('whatsapp')} WhatsApp</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container page-layout">
    <article>
      <div class="prose" data-reveal>
        {l['body']}
      </div>
      <div class="related">
        <h2>Réalisations</h2>
        <div class="projects" data-stagger="80" style="grid-template-columns:repeat(auto-fill,minmax(260px,1fr))">
{cards}
        </div>
      </div>
      <div class="related" data-reveal>
        <h2>Questions fréquentes</h2>
        {faq_block(l['faqs'])}
      </div>
      <p class="updated">Mis à jour le {TODAY_FR} · Omar A. Wankoye, développeur web freelance certifié IBM &amp; Google.</p>
    </article>
    <aside class="card aside-card" data-reveal>
      <h2>Ce que vous obtenez</h2>
      <ul class="checks">
{points}
      </ul>
      <a class="btn btn--primary btn--block" href="#contact">Obtenir un devis gratuit</a>
      <a class="btn btn--whatsapp btn--block" href="{WHATSAPP}" target="_blank" rel="noopener">{icon('whatsapp')} Discuter sur WhatsApp</a>
      <h2 style="margin-top:14px">Le service complet</h2>
      <ul class="aside-links">
        <li><a href="{parent['slug']}.html">{icon(SERVICE_ICONS[parent['slug']])}{e(parent['title'])}</a></li>
      </ul>
      <h2 style="margin-top:14px">Autres expertises</h2>
      <ul class="aside-links">
{siblings}
      </ul>
    </aside>
  </div>
</section>

{contact_block()}
</main>
'''
        out += footer()
        (ROOT / f'{l["slug"]}.html').write_text(split_titles(out), encoding='utf-8')


# ------------------------------------------------------------------ études de cas
def build_projects():
    for idx, p in enumerate(PROJECTS):
        url = f'{SITE}/{p["file"]}'
        title = f'{p["title"]} | Omar A. Wankoye'
        if len(title) > 62:
            title = f'{p["title"].split(" — ")[0]} – Étude de cas | Omar A. Wankoye'
        desc = f'{p["card"]} Étude de cas réalisée par Omar A. Wankoye, développeur web freelance.'
        desc = desc if len(desc) <= 158 else desc[:155].rsplit(' ', 1)[0] + '…'
        img = f'{SITE}/img/projects/{p["slug"]}-full.webp'
        work = {'@context': 'https://schema.org', '@type': 'CreativeWork', 'name': p['title'], 'description': p['card'],
                'url': url, 'image': img, 'keywords': ', '.join(p['tech']), 'genre': CATS[p['cat']],
                'about': p['sector'], 'creator': {'@id': f'{SITE}/#person'}, 'inLanguage': 'fr-FR',
                'sameAs': p['url'] or None}
        crumbs = crumbs_ld([('Accueil', f'{SITE}/'), ('Projets', f'{SITE}/#projects'), (p['title'], url)])
        sol = '\n'.join(f'          <li>{e(x)}</li>' for x in p['solution'])
        tech = ''.join(f'<li>{e(t)}</li>' for t in p['tech'])
        svc_links = '\n'.join(f'        <li><a href="{sl}.html">{icon(SERVICE_ICONS[sl])}{e(SVC[sl]["title"])}</a></li>' for sl in p['services'])
        live = (f'<a class="btn btn--primary" href="{p["url"]}" target="_blank" rel="noopener" data-magnetic>Voir le projet en ligne {icon("arrow-up-right", "icon icon--diag")}</a>'
                if p['url'] else '')
        nxt = PROJECTS[(idx + 1) % len(PROJECTS)]
        h1 = split_words([(p['title'], None)])
        out = head(title, desc, url, og_type='article', image=img, image_alt=f'Aperçu du projet {p["title"]}', extra_ld=[work, crumbs])
        out += header(False)
        out += f'''<main id="main">
<section class="page-hero noise">
  <div class="hero-bg" aria-hidden="true"><div class="grid-lines"></div><div class="blob blob--gold"></div></div>
  <div class="container">
    <nav aria-label="Fil d’Ariane"><ol class="breadcrumb"><li><a href="index.html">Accueil</a></li><li><a href="index.html#projects">Projets</a></li><li aria-current="page">{e(p['title'])}</li></ol></nav>
    <p class="eyebrow" data-reveal="fade">Étude de cas · {e(CATS[p['cat']])}</p>
    <h1 class="split">{h1}</h1>
    <p class="lead" data-reveal style="--d:300ms">{e(p['card'])}</p>
    <div class="hero-actions" data-reveal style="--d:420ms;margin:0">
      {live}
      <a class="btn btn--ghost" href="#contact" data-magnetic>Un projet similaire ? Parlons-en</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="meta-grid" data-stagger="90">
      <div class="stat" data-reveal><strong>{e(p['sector'])}</strong><span>Secteur</span></div>
      <div class="stat" data-reveal><strong>{e(p['type'])}</strong><span>Type de projet</span></div>
      <div class="stat" data-reveal><strong>{e(', '.join(p['tech'][:3]))}</strong><span>Technologies principales</span></div>
    </div>
    <figure class="case-media" data-reveal="clip">
      <img src="img/projects/{p['slug']}-full.webp" alt="Capture d’écran du projet {e(p['title'])}" loading="lazy" decoding="async">
    </figure>
    <div class="page-layout">
      <article class="prose" data-reveal>
        <h2>Le contexte</h2>
        <p>{e(p['context'])}</p>
        <h3>La solution</h3>
        <ul>
{sol}
        </ul>
        <h3>Le résultat</h3>
        <p>{e(p['outcome'])}</p>
        <p class="updated">Projet réalisé par Omar A. Wankoye, développeur web freelance.</p>
      </article>
      <aside class="card aside-card" data-reveal>
        <h2>Technologies</h2>
        <ul class="tags">{tech}</ul>
        <h2 style="margin-top:14px">Services associés</h2>
        <ul class="aside-links">
{svc_links}
        </ul>
        <a class="btn btn--primary btn--block" href="#contact">Demander un devis</a>
      </aside>
    </div>
    <a class="card next-case" href="{nxt['file']}" data-reveal>
      <div><span>Projet suivant</span><strong>{e(nxt['title'])}</strong></div>
      <span class="link-arrow" aria-hidden="true">{icon('arrow-right')}</span>
    </a>
  </div>
</section>

{contact_block()}
</main>
'''
        out += footer()
        (ROOT / p['file']).write_text(split_titles(out), encoding='utf-8')


# ------------------------------------------------------------------ robots / sitemap / llms
AI_BOTS = ['Googlebot', 'Bingbot', 'Google-Extended', 'GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot',
           'ClaudeBot', 'Claude-SearchBot', 'Applebot-Extended', 'CCBot']


def build_seo_files():
    rules = ['Disallow: /_build/', 'Disallow: /boot.html', 'Disallow: /contact-frame.html', 'Disallow: /portfolio-site-restaurant2.html']
    lines = ['User-agent: *', 'Allow: /'] + rules + ['']
    for b in AI_BOTS:
        lines += [f'User-agent: {b}', 'Allow: /'] + rules + ['']
    lines += [f'Sitemap: {SITE}/sitemap.xml', '', f'# Résumé du site pour les IA : {SITE}/llms.txt', '']
    (ROOT / 'robots.txt').write_text('\n'.join(lines), encoding='utf-8')

    urls = [(f'{SITE}/', '1.0', 'weekly', f'{SITE}/img/omar-atta-portrait.webp')]
    urls += [(service_url(s), '0.9', 'monthly', None) for s in SERVICES]
    urls += [(f'{SITE}/{l["slug"]}.html', '0.8', 'monthly', None) for l in LANDINGS]
    urls += [(f'{SITE}/{p["file"]}', '0.7', 'yearly', f'{SITE}/img/projects/{p["slug"]}-full.webp') for p in PROJECTS]
    body = []
    for u, pr, cf, im in urls:
        img = f'\n    <image:image><image:loc>{im}</image:loc></image:image>' if im else ''
        body.append(f'  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>{img}\n  </url>')
    (ROOT / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + '\n'.join(body) + '\n</urlset>\n', encoding='utf-8')

    L = ['# Omar Amadou Wankoye — Omar.tech', '', f'> {C.PROFILE["seo_description"]}', '',
         'Omar Amadou Wankoye (Omar A. Wankoye, également connu sous le nom d’Omar Atta sur Credly et LinkedIn) est développeur web freelance full-stack, 4 ans d’expérience, '
         'certifié IBM (Full Stack Software Developer, AI Developer, Front-End Developer) et Google (AI Professional Certificate). '
         f'Il travaille à distance, en français et en anglais, pour des clients en : {", ".join(AREAS)}.', '', '## Services']
    L += [f'- [{s["title"]}]({service_url(s)}): {s["description"]}' for s in SERVICES]
    L += ['', '## Expertises et zones']
    L += [f'- [{l["h1"]}]({SITE}/{l["slug"]}.html): {l["desc"]}' for l in LANDINGS]
    L += ['', '## Certifications (vérifiables sur Credly)']
    L += [f'- [{n}]({u})' for n, _, u, _ in PRO_CERTS]
    L += [f'- [{label}]({C.credly_badge_url(bid)}) — {issuer}' for label, issuer, bid, *_ in C.CREDLY_BADGES]
    L += [f'- [Profil Credly complet (43 badges)]({CREDLY})', '', '## Études de cas']
    L += [f'- [{p["title"]}]({SITE}/{p["file"]}): {p["card"]} Secteur : {p["sector"]}. Technologies : {", ".join(p["tech"])}.' for p in PROJECTS]
    L += ['', '## Méthode', '1. Appel découverte gratuit', '2. Devis et plan d’action sous 48 h', '3. Réalisation par étapes avec démos',
          '4. Mise en ligne, formation et suivi', '', '## Questions fréquentes']
    for q, a in C.GENERAL_FAQS:
        L += [f'### {q}', a, '']
    L += ['## Contact', f'- Devis gratuit : {SITE}/#contact', f'- E-mail : {EMAIL}', f'- WhatsApp : {WA_NUM}',
          f'- LinkedIn : {LINKEDIN}', f'- GitHub : {GITHUB}', '']
    (ROOT / 'llms.txt').write_text('\n'.join(L), encoding='utf-8')

    (ROOT / 'favicon.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ffd98a"/><stop offset="1" stop-color="#e8794a"/></linearGradient></defs>'
        '<rect width="64" height="64" rx="16" fill="#07080c"/><text x="32" y="44" text-anchor="middle" '
        'font-family="Arial Black, Arial, sans-serif" font-size="34" font-weight="900" fill="url(#g)">O.</text></svg>\n',
        encoding='utf-8')


if __name__ == '__main__':
    SPRITE = build_sprite()
    INLINE_CSS = load_css()
    build_index()
    build_services()
    build_landings()
    build_projects()
    build_seo_files()
    print('ok')
