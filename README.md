# Omar.tech — portfolio d'Omar Atta

Site statique (HTML/CSS/JS natif, sans framework) : https://www.omar-tech.com

## Structure
- `index.html` — accueil (services, à propos, méthode, compétences, projets, certifications, FAQ, contact)
- `creation-site-web.html`, `developpement-application-web-mobile.html`, `automatisation-ia-workflows.html`,
  `seo-geo-referencement.html`, `gestion-reseaux-sociaux.html` — pages services
- `cabinet.html`, `suptechchatbot.html`, … — études de cas (12 projets)
- `assets/css/main.css` — design system (sombre premium), `assets/js/main.js` — motion & interactions
- `img/` — images optimisées WebP ; `robots.txt`, `sitemap.xml`, `llms.txt` — SEO & GEO

## Modifier le contenu
Les pages sont générées par `_build/build.py` à partir de :
- `_build/content_data.py` — profil, services, FAQ, compétences, badges Credly
- `_build/projects_v2.py` — études de cas

```bash
python _build/build.py
```

Puis vérifier et publier (`git add -A && git commit && git push`).
