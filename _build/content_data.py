"""
Contenu éditorial de référence du portfolio (positionnement 2026).

Utilisé par :
- la migration de données 0023 (mise à jour unique de la base en production) ;
- la commande `seed_portfolio` (installation locale / nouvelle base).

Tout reste modifiable ensuite depuis l'admin Django.
"""

PROFILE = {
    'full_name': 'Omar Amadou Wankoye',
    'brand_name': 'Omar.tech',
    'hero_badge_text': 'Disponible pour nouveaux projets — devis gratuit sous 48 h',
    'hero_role': 'Développeur web freelance',
    'hero_highlight': 'sites web, applications, automatisation IA, SEO/GEO & réseaux sociaux',
    'hero_description': (
        '<p>J’aide les PME, startups, indépendants et associations à <strong>gagner des clients en ligne</strong> : '
        'création de sites web et e-commerce, développement d’applications web et mobiles, '
        'automatisation de tâches avec l’IA, référencement <strong>SEO</strong> sur Google et '
        '<strong>GEO</strong> dans les moteurs d’IA (ChatGPT, Gemini, Perplexity), et gestion de vos réseaux sociaux. '
        'Je travaille en remote pour la France, l’Italie, l’Afrique francophone et l’international.</p>'
    ),
    'years_experience': 4,
    'experience_label': "Ans d'expérience",
    'impact_value': '43',
    'impact_label': 'Badges certifiés IBM & Google (Credly)',
    'about_title': 'Développeur full-stack certifié IBM & Google, orienté résultats business.',
    'about_intro': (
        '<p>Je m’appelle <strong>Omar Amadou Wankoye</strong>, développeur freelance full-stack. Depuis 4 ans, je conçois des '
        'sites web, des boutiques en ligne, des applications web et mobiles, des chatbots IA et des automatisations '
        'pour des entreprises qui veulent être visibles en ligne et gagner du temps.</p>'
    ),
    'about_body': (
        '<p>Mes compétences sont vérifiables : <strong>IBM Full Stack Software Developer</strong>, '
        '<strong>IBM AI Developer</strong>, <strong>IBM Front-End Developer</strong>, '
        '<strong>Google AI Professional Certificate</strong> et plus de 40 badges publiés sur Credly. '
        'Ma méthode est simple : comprendre votre objectif (plus de demandes, plus de ventes, moins de tâches manuelles), '
        'livrer une solution rapide et propre, puis mesurer les résultats avec vous.</p>'
        '<p>Langues de travail : français et anglais. Projets réalisés à distance pour la France, l’Italie, '
        'la Belgique, la Suisse et l’Afrique francophone (Côte d’Ivoire, Sénégal, Niger, Cameroun, Maroc…).</p>'
    ),
    'footer_tagline': 'Développeur web freelance · Apps · Automatisation IA · SEO & GEO · Réseaux sociaux',
    'availability_text': 'Disponible — France, Italie, Afrique francophone & remote',
    'hero_signals': 'Web,Mobile,Automation,IA,SEO,GEO',
    'tech_stack_marquee': (
        'Python,Django,React,Next.js,Laravel,Node.js,Flutter,WordPress,Shopify,'
        'n8n,Make,Zapier,LangChain,OpenAI,Gemini,Docker,AWS,IBM Cloud,PostgreSQL,Google Search Console'
    ),
    'primary_badge_text': 'Certifié IBM & Google',
    'secondary_badge_text': 'Devis gratuit sous 48 h',
    'primary_certificate_label': 'IBM Full Stack Software Developer',
    'primary_certificate_url': 'https://www.credly.com/badges/84bc6f03-87d3-4fc6-b3dd-c67a48f70d2a/public_url',
    'secondary_certificate_label': 'IBM AI Developer',
    'secondary_certificate_url': 'https://www.credly.com/badges/b5b05f89-e8e7-48a4-b96d-f73b05b33f1f/public_url',
    'cert_section_title': 'Certifications vérifiables IBM & Google',
    'cert_section_desc': (
        '<p>Mes compétences en développement logiciel, cloud et intelligence artificielle sont certifiées par '
        'IBM et Google (via Coursera) et vérifiables publiquement sur Credly.</p>'
    ),
    'cert_section_note': 'Cliquez sur un badge pour le vérifier sur Credly.',
    'services_section_subtitle': 'Services',
    'services_section_title': 'Ce que je peux faire pour votre entreprise',
    'skills_section_subtitle': 'Compétences',
    'skills_section_title': 'Compétences & expertises',
    'portfolio_section_title': 'Projets & réalisations',
    'contact_section_subtitle': 'Contact',
    'contact_section_title': 'Parlons de votre projet — devis gratuit',
    'seo_title': 'Omar A. Wankoye – Développeur Web Freelance, Apps, IA & SEO/GEO',
    'seo_description': 'Développeur freelance : sites web, applications, automatisation IA, SEO & GEO, réseaux sociaux. France, Italie, Afrique francophone. Devis gratuit.',
    'areas_served': (
        'France,Italie,Belgique,Suisse,Côte d’Ivoire,Sénégal,Niger,Cameroun,Maroc,Remote international'
    ),
    'credly_profile_url': 'https://www.credly.com/users/omar-atta-yakouba-maikassa',
}


SERVICES = [
    {
        'slug': 'creation-site-web',
        'icon': 'fas fa-laptop-code',
        'title': 'Création de sites web & e-commerce',
        'description': 'Sites vitrines, landing pages et boutiques en ligne rapides, responsive et pensés pour transformer vos visiteurs en clients.',
        'summary': 'Un site professionnel, rapide et bien référencé qui présente vos services et génère des demandes de devis.',
        'full_description': (
            '<h2>Un site web qui travaille pour vous</h2>'
            '<p>Je crée des <strong>sites vitrines</strong>, <strong>landing pages</strong> et <strong>boutiques e-commerce</strong> '
            'sur mesure (Django, React, Next.js, Laravel) ou sur CMS (WordPress, Shopify) selon votre budget et votre autonomie souhaitée.</p>'
            '<h3>Pour qui ?</h3>'
            '<p>Artisans, restaurants, cabinets, commerces, startups et PME en France, en Italie et en Afrique francophone '
            'qui veulent une présence en ligne crédible et des contacts entrants.</p>'
            '<h3>Ma méthode</h3>'
            '<ol><li>Appel découverte et objectifs (gratuit)</li><li>Maquette et contenu</li>'
            '<li>Développement, optimisation SEO et performance</li><li>Mise en ligne, formation et suivi</li></ol>'
            '<p>Exemples réalisés : site de cabinet médical avec prise de rendez-vous (React + Django), boutique Django avec gestion des commandes, sites de restaurants et intégrations e-commerce responsive (Mocart, ShopGrids, Veppo).</p>'
        ),
        'detail_points': (
            'Design responsive (mobile, tablette, ordinateur)\n'
            'SEO technique inclus : balises, sitemap, données structurées\n'
            'Paiement en ligne (Stripe, PayPal, Mobile Money sur demande)\n'
            'Formulaire de contact, WhatsApp et Google Analytics\n'
            'Hébergement, nom de domaine et HTTPS configurés\n'
            'Formation pour modifier vos contenus'
        ),
        'order': 1,
        'faqs': [
            ('Combien de temps faut-il pour créer un site web ?',
             'Un site vitrine est généralement livré en 1 à 3 semaines, une boutique e-commerce en 3 à 6 semaines, selon le nombre de pages, de produits et la disponibilité des contenus.'),
            ('Pourrai-je modifier mon site moi-même ?',
             'Oui. Chaque site est livré avec un espace d’administration (WordPress, Shopify ou back-office Django sur mesure) et une courte formation pour mettre à jour textes, images et produits.'),
            ('Le référencement Google est-il inclus ?',
             'Oui, le SEO technique de base est inclus : structure des pages, balises title et meta description, sitemap, données structurées Schema.org, vitesse et compatibilité mobile.'),
        ],
    },
    {
        'slug': 'developpement-application-web-mobile',
        'icon': 'fas fa-mobile-screen-button',
        'title': 'Développement d’applications web & mobiles',
        'description': 'Applications métier, SaaS, plateformes de réservation et apps Android/iOS (Flutter) sur mesure, de la maquette à la mise en production.',
        'summary': 'Des applications fiables et évolutives pour digitaliser votre activité : web, Android et iOS.',
        'full_description': (
            '<h2>Des applications sur mesure pour votre activité</h2>'
            '<p>Je développe des <strong>applications web</strong> (tableaux de bord, ERP/CRM légers, plateformes de réservation, SaaS) '
            'et des <strong>applications mobiles Android et iOS</strong> avec Flutter, connectées à vos données et à vos outils.</p>'
            '<h3>Stack technique</h3>'
            '<p>Python (Django, FastAPI, Flask), JavaScript/TypeScript (React, Next.js, Angular, Node.js), PHP (Laravel, Symfony), '
            'Flutter/Dart, Firebase, PostgreSQL/MySQL, Docker, AWS, IBM Cloud et Render.</p>'
            '<h3>Exemples</h3>'
            '<p>Boutique Myshop (Django : produits, fournisseurs, commandes et bons PDF), application mobile IA d’estimation de l’âge (Python/Kivy), '
            'chatbots IA (LangChain, OpenAI) et générateur de légendes d’images (Hugging Face).</p>'
        ),
        'detail_points': (
            'Cadrage fonctionnel et maquettes cliquables\n'
            'Applications web, Android et iOS (Flutter)\n'
            'API REST sécurisées et intégrations tierces\n'
            'Espace administrateur et gestion des rôles\n'
            'Déploiement cloud (Docker, AWS, Render) et CI/CD\n'
            'Maintenance et évolutions après livraison'
        ),
        'order': 2,
        'faqs': [
            ('Développez-vous des applications pour Android et iOS ?',
             'Oui, avec Flutter je développe une seule base de code publiée sur Android et iOS, ce qui réduit les coûts et les délais par rapport à deux applications natives.'),
            ('Pouvez-vous reprendre une application existante ?',
             'Oui. Je commence par un audit du code et de l’hébergement, puis je propose un plan de corrections, de sécurisation et d’évolutions.'),
            ('Comment se passe le suivi du projet ?',
             'Le projet est découpé en étapes courtes avec une démo à chaque étape. Vous suivez l’avancement en direct et validez chaque fonctionnalité avant la mise en production.'),
        ],
    },
    {
        'slug': 'automatisation-ia-workflows',
        'icon': 'fas fa-robot',
        'title': 'Automatisation & intelligence artificielle',
        'description': 'Chatbots IA, assistants virtuels et workflows automatisés (n8n, Make, Zapier, API) pour gagner des heures chaque semaine.',
        'summary': 'Automatisez les tâches répétitives et répondez à vos clients 24/7 grâce à l’IA.',
        'full_description': (
            '<h2>Gagnez du temps avec l’automatisation et l’IA</h2>'
            '<p>Je connecte vos outils (formulaires, CRM, e-mails, Google Sheets, WhatsApp, boutique en ligne) pour supprimer les tâches '
            'manuelles, et je crée des <strong>chatbots et assistants IA</strong> entraînés sur vos propres documents (RAG).</p>'
            '<h3>Exemples d’automatisations</h3>'
            '<ul><li>Réponse automatique aux demandes de devis et prise de rendez-vous</li>'
            '<li>Synchronisation commandes / factures / CRM</li>'
            '<li>Chatbot support client ou étudiant (projet SupTech Chatbot)</li>'
            '<li>Assistant interne qui répond à partir de vos PDF et procédures</li>'
            '<li>Génération de contenus et de rapports avec l’IA</li></ul>'
            '<p>Outils : n8n, Make, Zapier, Python, LangChain, OpenAI, Google Gemini, Hugging Face.</p>'
        ),
        'detail_points': (
            'Audit des tâches répétitives à automatiser\n'
            'Workflows n8n, Make, Zapier ou scripts Python\n'
            'Chatbots IA sur site web et WhatsApp\n'
            'Assistants IA connectés à vos documents (RAG)\n'
            'Intégration CRM, e-mail, Google Workspace\n'
            'Documentation et transfert de compétences'
        ),
        'order': 3,
        'faqs': [
            ('Quelles tâches peut-on automatiser ?',
             'Toute tâche répétitive basée sur des règles : relances, saisie de données, envoi de devis, synchronisation entre outils, tri des e-mails, réponses aux questions fréquentes, création de rapports.'),
            ('Un chatbot IA peut-il répondre avec les informations de mon entreprise ?',
             'Oui. Avec la technique RAG, le chatbot s’appuie sur vos propres documents (catalogue, FAQ, procédures) pour donner des réponses précises, et peut transférer à un humain si nécessaire.'),
            ('Mes données restent-elles confidentielles ?',
             'Oui. Je privilégie des hébergements maîtrisés, des accès limités et, si besoin, des modèles IA hébergés en Europe ou en local.'),
        ],
    },
    {
        'slug': 'seo-geo-referencement',
        'icon': 'fas fa-magnifying-glass-chart',
        'title': 'Référencement SEO & GEO',
        'description': 'Être trouvé sur Google et cité par les IA (ChatGPT, Gemini, Perplexity) : audit, SEO technique, contenus et SEO local.',
        'summary': 'Plus de visibilité sur Google et dans les réponses des intelligences artificielles.',
        'full_description': (
            '<h2>SEO + GEO : être visible partout où vos clients cherchent</h2>'
            '<p>Le <strong>SEO</strong> (Search Engine Optimization) positionne votre site sur Google et Bing. '
            'Le <strong>GEO</strong> (Generative Engine Optimization) rend votre entreprise compréhensible et citable par les moteurs '
            'de réponse IA : ChatGPT, Google AI Overviews, Gemini, Perplexity, Copilot.</p>'
            '<h3>Ce que je mets en place</h3>'
            '<ul><li>Audit SEO technique (vitesse, Core Web Vitals, indexation, erreurs)</li>'
            '<li>Données structurées Schema.org (entreprise, services, FAQ, avis)</li>'
            '<li>Recherche de mots-clés et pages services optimisées</li>'
            '<li>SEO local : fiche Google Business Profile, citations, avis clients</li>'
            '<li>GEO : contenus question-réponse, fichier llms.txt, cohérence de votre marque sur le web</li>'
            '<li>Suivi Google Search Console, Bing Webmaster Tools et rapports mensuels</li></ul>'
        ),
        'detail_points': (
            'Audit SEO complet et plan d’action priorisé\n'
            'Optimisation technique et vitesse du site\n'
            'Données structurées Schema.org & llms.txt\n'
            'SEO local et Google Business Profile\n'
            'Contenus optimisés pour Google et les IA\n'
            'Rapport mensuel de positions et de trafic'
        ),
        'order': 4,
        'faqs': [
            ('Quelle est la différence entre SEO et GEO ?',
             'Le SEO vise à classer vos pages dans les résultats de Google et Bing. Le GEO vise à ce que les moteurs d’IA générative comme ChatGPT, Gemini ou Perplexity comprennent votre activité et vous citent dans leurs réponses. Les deux se complètent.'),
            ('En combien de temps voit-on des résultats en SEO ?',
             'Les corrections techniques ont un effet en quelques semaines ; les gains de positions durables sur des mots-clés concurrentiels demandent généralement 3 à 6 mois de travail régulier.'),
            ('Travaillez-vous le référencement local ?',
             'Oui : optimisation de la fiche Google Business Profile, pages par ville ou pays, citations dans les annuaires et stratégie d’avis clients, pour la France, l’Italie et l’Afrique francophone.'),
        ],
    },
    {
        'slug': 'gestion-reseaux-sociaux',
        'icon': 'fas fa-share-nodes',
        'title': 'Gestion des réseaux sociaux',
        'description': 'Stratégie, création de contenus assistée par IA et publication sur Facebook, Instagram, LinkedIn et TikTok pour développer votre audience.',
        'summary': 'Une présence régulière et professionnelle sur les réseaux sociaux qui attire de nouveaux clients.',
        'full_description': (
            '<h2>Des réseaux sociaux qui amènent des clients</h2>'
            '<p>Je gère vos pages <strong>Facebook, Instagram, LinkedIn et TikTok</strong> : ligne éditoriale, calendrier de publication, '
            'création de visuels et de textes (avec l’appui d’outils IA, certification Google AI for Content Creation), '
            'programmation et analyse des statistiques.</p>'
            '<h3>Objectifs</h3>'
            '<ul><li>Renforcer la notoriété et la confiance</li><li>Rediriger le trafic vers votre site ou WhatsApp</li>'
            '<li>Générer des demandes de contact et des ventes</li></ul>'
            '<p>Une marque cohérente sur les réseaux sociaux renforce aussi votre référencement Google et votre visibilité dans les moteurs d’IA.</p>'
        ),
        'detail_points': (
            'Audit de vos comptes et de la concurrence\n'
            'Stratégie et calendrier éditorial mensuel\n'
            'Création de visuels, carrousels et vidéos courtes\n'
            'Rédaction optimisée et hashtags pertinents\n'
            'Programmation et animation de la communauté\n'
            'Rapport mensuel de performances'
        ),
        'order': 5,
        'faqs': [
            ('Sur quels réseaux sociaux intervenez-vous ?',
             'Facebook, Instagram, LinkedIn et TikTok principalement. Le choix dépend de votre cible : LinkedIn pour le B2B, Instagram et TikTok pour le grand public, Facebook pour le local.'),
            ('Combien de publications par mois ?',
             'Les formules vont généralement de 8 à 20 publications par mois, plus les stories, selon vos objectifs et votre budget. Tout est validé avec vous avant publication.'),
            ('Utilisez-vous l’IA pour créer les contenus ?',
             'Oui, l’IA aide à produire plus vite des idées, textes et visuels, mais chaque contenu est relu, adapté à votre ton et vérifié avant publication.'),
        ],
    },
]


GENERAL_FAQS = [
    ('Quels services propose Omar Amadou Wankoye ?',
     'Omar Amadou Wankoye est développeur web freelance. Il propose la création de sites web et e-commerce, le développement d’applications web et mobiles, l’automatisation et les chatbots IA, le référencement SEO et GEO, et la gestion des réseaux sociaux.'),
    ('Travaillez-vous avec des clients à l’étranger ?',
     'Oui, tout se fait à distance : clients en France, en Italie, en Belgique, en Suisse et en Afrique francophone (Côte d’Ivoire, Sénégal, Niger, Cameroun, Maroc…), en français ou en anglais.'),
    ('Combien coûte un projet ?',
     'Chaque projet fait l’objet d’un devis gratuit et détaillé, envoyé sous 48 h après un premier échange. Le prix dépend du périmètre, des fonctionnalités et des délais souhaités.'),
    ('Vos compétences sont-elles certifiées ?',
     'Oui : IBM Full Stack Software Developer, IBM AI Developer, IBM Front-End Developer, Google AI Professional Certificate et plus de 40 badges vérifiables publiquement sur Credly.'),
    ('Comment démarrer un projet ?',
     'Envoyez un message via le formulaire de contact ou WhatsApp en décrivant votre besoin. Un appel découverte gratuit permet ensuite de définir les objectifs, le planning et le budget.'),
]


SKILLS = [
    ('web', 'fas fa-code', 'Développement web full-stack', 'Django, FastAPI, Laravel, Symfony, Node.js/Express, API REST.', 1),
    ('web', 'fab fa-react', 'Front-end React, Next.js & Angular', 'Interfaces rapides en TypeScript/JavaScript, responsive et accessibles.', 2),
    ('web', 'fas fa-cart-shopping', 'E-commerce WordPress & Shopify', 'Boutiques en ligne, paiement Stripe, CMS WordPress, Shopify, Webflow, Strapi.', 3),
    ('mobile', 'fas fa-mobile-screen-button', 'Applications mobiles Flutter', 'Apps Android & iOS avec Flutter/Dart, Firebase et IA embarquée (TensorFlow Lite).', 4),
    ('ia', 'fas fa-brain', 'IA générative, RAG & chatbots', 'LLM, LangChain, OpenAI, Gemini, Hugging Face, assistants sur documents.', 5),
    ('automation', 'fas fa-bolt', 'Automatisation n8n, Make & Zapier', 'Workflows no-code/low-code, intégrations CRM, e-mail et Google Workspace.', 6),
    ('automation', 'fas fa-cloud-arrow-up', 'Cloud & DevOps', 'Docker, CI/CD, AWS, IBM Cloud, Render, Nginx, PostgreSQL/MySQL.', 7),
    ('marketing', 'fas fa-magnifying-glass-chart', 'SEO technique & local', 'Audit, Core Web Vitals, Schema.org, Search Console, Google Business Profile.', 8),
    ('marketing', 'fas fa-wand-magic-sparkles', 'GEO – visibilité dans les IA', 'Optimisation pour ChatGPT, Gemini, Perplexity et Google AI Overviews, llms.txt.', 9),
    ('marketing', 'fas fa-share-nodes', 'Réseaux sociaux & contenu IA', 'Stratégie éditoriale, création de contenus, Facebook, Instagram, LinkedIn, TikTok.', 10),
]


# Badges Credly vérifiés (profil public : 43 badges au total).
CREDLY_BADGES = [
    # (label, issuer, badge_id, image_url, issued_on, order)
    ('Google AI Professional Certificate', 'Google · Coursera', '0d189f38-17e2-4161-90cc-b1ea2e641291',
     'https://images.credly.com/images/782f33e7-c4b5-4d1d-a7ce-02f25b7b9a1e/blob', '2026-07-19', 1),
    ('IBM Front-End Developer Professional Certificate', 'IBM · Coursera', '92a42052-d2ae-4959-82fd-6e01c23fcbed',
     'https://images.credly.com/images/e646f624-ca3d-4917-9e90-16a051497bdb/image.png', '2025-03-25', 2),
    ('Google AI for App Building', 'Google · Coursera', '8a7d78ea-1f9d-475b-8ad0-bc9dfc0aaf1c',
     'https://images.credly.com/images/2cf18bea-6b75-401a-bf9d-ac0a23f582fd/blob', '2026-07-19', 3),
    ('Google AI for Content Creation', 'Google · Coursera', '77dd9add-320b-4fa8-afda-0c356536d9b2',
     'https://images.credly.com/images/f0c5c16d-1480-4968-9259-50851d03f79a/blob', '2026-06-11', 4),
    ('Building Generative AI-Powered Applications with Python', 'IBM · Coursera', 'fc916346-e1f5-4927-8cbb-76a73aafd4d8',
     'https://images.credly.com/images/e462102c-b2ee-4208-aca0-b58f53331266/image.png', '2025-04-02', 5),
    ('Cloud Application Development Foundations', 'IBM · Coursera', '1ba3b351-f8a3-4e0f-af55-5c7ea98c5fe5',
     'https://images.credly.com/images/98751a94-e69c-425f-a8a0-0fd0a54d7c7a/Coursera_20Cloud_20Appl_20Devel_20Foundations_20Specialization.png', '2025-06-20', 6),
    ('JavaScript Programming Essentials', 'IBM · Coursera', 'a667cf56-4771-4535-a3e1-214ee532ca4c',
     'https://images.credly.com/images/899a5963-d3c7-45ee-a16c-4827cf24e836/image.png', '2026-04-16', 7),
    ('Web Development with HTML, CSS, JavaScript Essentials', 'IBM · Coursera', '1fe0f625-a96f-4341-a155-510954a3008b',
     'https://images.credly.com/images/2d1797d5-1de7-4778-8975-9e5c6ec73a1a/image.png', '2025-04-02', 8),
    ('Google AI for Writing and Communicating', 'Google · Coursera', 'bc6539db-bf86-4ef9-b491-8fcd0a85f103',
     'https://images.credly.com/images/791a77e5-1590-40bc-92a9-c69126fa4e4b/blob', '2026-06-10', 9),
    ('Google AI for Brainstorming and Planning', 'Google · Coursera', '00ff7da6-e4c1-4065-8d8b-5ba3e735eaf8',
     'https://images.credly.com/images/fb6dc8be-1471-4aab-b2ab-da1f76080ecf/blob', '2026-05-09', 10),
    ('Google AI Fundamentals', 'Google · Coursera', '66f44ae5-d1b9-4639-8ddd-4b95deb8b0d1',
     'https://images.credly.com/images/36ecc7ff-8ccf-4bd8-83a7-6f35797e0b64/blob', '2026-05-09', 11),
]


def credly_badge_url(badge_id):
    return f'https://www.credly.com/badges/{badge_id}/public_url'
