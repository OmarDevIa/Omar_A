"""Pages ciblées (SEO longue traîne). Contenu unique par page — pas de pages copiées.

Chaque entrée : slug (nom du fichier .html), title (balise title ≤ 60 car.), h1, desc (meta ≤ 158 car.),
eyebrow, lead, body (HTML), points (liste « Ce que vous obtenez »), faqs, projects (fichiers liés),
service (slug du service parent), area (zone géographique ou None).
"""

LANDINGS = [
    {
        'slug': 'creation-site-web-niamey',
        'title': 'Création de site web à Niamey (Niger) | Omar A. Wankoye',
        'h1': 'Création de site web à Niamey',
        'desc': 'Développeur web freelance pour les entreprises de Niamey et du Niger : site vitrine, e-commerce avec Mobile Money, SEO local. Devis gratuit sous 48 h.',
        'eyebrow': 'Niger · Niamey',
        'lead': 'Un site professionnel, rapide même avec une connexion lente, pensé pour WhatsApp et le paiement mobile, pour que vos clients de Niamey et de tout le Niger vous trouvent et vous contactent.',
        'area': {'name': 'Niamey', 'country': 'Niger'},
        'service': 'creation-site-web',
        'body': '''
<h2>Un site web adapté aux réalités du Niger</h2>
<p>À Niamey, la plupart de vos clients découvrent une entreprise sur leur téléphone, souvent avec une connexion 3G/4G variable, et préfèrent écrire sur <strong>WhatsApp</strong> plutôt que remplir un formulaire. Un site qui fonctionne au Niger doit donc être <strong>léger, rapide et pensé mobile d’abord</strong>, avec un contact direct en un clic.</p>
<p>Je conçois des sites vitrines, des boutiques en ligne et des applications web pour les commerces, cabinets, écoles, ONG, restaurants et PME de Niamey, Maradi, Zinder, Tahoua ou Agadez — entièrement à distance, en français, avec des échanges simples par WhatsApp et visio.</p>
<h3>Ce qui fait la différence</h3>
<ul>
<li><strong>Performance :</strong> pages optimisées (images WebP, code léger) pour s’afficher vite même sur un réseau mobile lent.</li>
<li><strong>Contact immédiat :</strong> bouton WhatsApp, appel en un clic, formulaire de devis.</li>
<li><strong>Paiement en ligne :</strong> intégration possible des solutions de paiement mobile disponibles au Niger ou d’un paiement à la livraison pour une boutique.</li>
<li><strong>Visibilité locale :</strong> fiche Google Business Profile, pages optimisées pour « [votre activité] Niamey », données structurées.</li>
<li><strong>Autonomie :</strong> un espace d’administration simple pour modifier textes, prix et photos sans dépendre d’un prestataire.</li>
</ul>
<h3>Exemples de projets possibles</h3>
<p>Site vitrine pour un cabinet médical ou juridique avec prise de rendez-vous, catalogue en ligne pour une boutique avec commande WhatsApp, site d’école avec inscriptions, plateforme de réservation pour un hôtel ou un restaurant, site d’ONG avec présentation des projets et dons.</p>
<h3>Comment on travaille ensemble</h3>
<ol>
<li>Un appel gratuit (WhatsApp ou visio) pour comprendre votre activité et vos clients.</li>
<li>Un devis clair sous 48 h, avec le contenu, les délais et le prix.</li>
<li>Une maquette à valider, puis le développement avec des démos régulières.</li>
<li>La mise en ligne (nom de domaine, hébergement, HTTPS) et une formation à la gestion du site.</li>
</ol>
''',
        'points': [
            'Site responsive optimisé pour les connexions mobiles',
            'Bouton WhatsApp et appel en un clic',
            'Paiement mobile ou commande WhatsApp (boutique)',
            'Google Business Profile et SEO local Niamey',
            'Nom de domaine, hébergement et HTTPS',
            'Formation pour gérer votre site',
        ],
        'faqs': [
            ('Travaillez-vous avec des entreprises de Niamey à distance ?',
             'Oui. Tout se fait à distance : appel découverte sur WhatsApp ou en visio, validation des maquettes en ligne, démos régulières et formation en visio. Vous n’avez pas besoin de vous déplacer.'),
            ('Mon site sera-t-il rapide avec les connexions mobiles au Niger ?',
             'C’est une priorité : images compressées en WebP, code léger et pages optimisées pour mobile, afin que le site s’affiche vite même sur une connexion 3G ou 4G variable.'),
            ('Peut-on vendre en ligne au Niger avec un site web ?',
             'Oui : selon votre activité, la boutique peut proposer un paiement mobile, un paiement à la livraison ou une commande directe par WhatsApp, avec un catalogue que vous gérez vous-même.'),
            ('Comment être trouvé sur Google à Niamey ?',
             'En combinant un site bien structuré, des pages qui mentionnent votre activité et votre ville, une fiche Google Business Profile complète et des avis clients. Je mets en place ces éléments lors de la création du site.'),
        ],
        'projects': ['cabinet.html', 'myshop.html', 'convinium.html'],
    },
    {
        'slug': 'creation-site-web-abidjan',
        'title': 'Création de site web à Abidjan | Omar A. Wankoye',
        'h1': 'Création de site web à Abidjan',
        'desc': 'Développeur web freelance pour les PME d’Abidjan et de Côte d’Ivoire : site vitrine, e-commerce, paiement mobile, SEO local. Devis gratuit sous 48 h.',
        'eyebrow': 'Côte d’Ivoire · Abidjan',
        'lead': 'Un site moderne et rapide qui inspire confiance, attire des clients sur Google et transforme vos visiteurs en demandes de devis ou en ventes, pour les entreprises d’Abidjan et de toute la Côte d’Ivoire.',
        'area': {'name': 'Abidjan', 'country': 'Côte d’Ivoire'},
        'service': 'creation-site-web',
        'body': '''
<h2>Se démarquer sur un marché digital dynamique</h2>
<p>À Abidjan, la concurrence en ligne est forte : vos clients comparent plusieurs entreprises sur leur smartphone avant de vous contacter. Un site professionnel, rapide et clair est souvent ce qui fait la différence entre un prospect qui vous écrit et un prospect qui part chez un concurrent.</p>
<p>J’accompagne les PME, startups, commerces, cabinets, restaurants et indépendants d’Abidjan (Cocody, Plateau, Marcory, Yopougon…) et de Côte d’Ivoire, à distance, de la stratégie à la mise en ligne.</p>
<h3>Des sites pensés pour convertir</h3>
<ul>
<li><strong>Message clair dès la première seconde :</strong> qui vous êtes, ce que vous proposez, pourquoi vous choisir.</li>
<li><strong>Appels à l’action visibles :</strong> WhatsApp, appel, devis, prise de rendez-vous.</li>
<li><strong>E-commerce :</strong> catalogue, panier et paiement en ligne avec les solutions de paiement mobile ou carte adaptées à votre activité.</li>
<li><strong>SEO local :</strong> pages optimisées pour vos services et votre quartier/ville, fiche Google Business Profile, données structurées.</li>
<li><strong>GEO :</strong> un contenu structuré pour que les assistants IA (ChatGPT, Gemini, Perplexity) comprennent votre activité et puissent vous recommander.</li>
</ul>
<h3>Et après la mise en ligne ?</h3>
<p>Je peux aussi automatiser vos relances clients, connecter votre site à un CRM ou à Google Sheets, ajouter un chatbot IA qui répond aux questions fréquentes 24 h/24, et animer vos réseaux sociaux pour générer du trafic vers le site.</p>
''',
        'points': [
            'Design moderne et responsive',
            'Pages services pensées pour convertir',
            'Boutique en ligne et paiement mobile',
            'SEO local Abidjan + Google Business Profile',
            'Données structurées pour Google et les IA',
            'Formation et accompagnement après la mise en ligne',
        ],
        'faqs': [
            ('Pouvez-vous créer un site pour mon entreprise à Abidjan sans être sur place ?',
             'Oui. Le projet se déroule entièrement à distance : appels WhatsApp ou visio, maquettes partagées en ligne, démos à chaque étape. De nombreux projets web sont aujourd’hui menés ainsi, sans perte de qualité.'),
            ('Le site peut-il accepter les paiements mobiles ?',
             'Oui, une boutique en ligne peut intégrer une solution de paiement compatible avec le paiement mobile et la carte bancaire, ou proposer la commande par WhatsApp et le paiement à la livraison selon votre organisation.'),
            ('En combien de temps mon site sera-t-il en ligne ?',
             'Comptez en général 1 à 3 semaines pour un site vitrine et 3 à 6 semaines pour une boutique en ligne, selon le nombre de pages, de produits et la rapidité de transmission des contenus.'),
            ('Comment apparaître sur Google à Abidjan ?',
             'Grâce à un site rapide et bien structuré, des pages qui ciblent vos services et votre ville, une fiche Google Business Profile complète et une stratégie d’avis clients. Ces bases sont incluses dans chaque projet.'),
        ],
        'projects': ['cabinet.html', 'ocart.html', 'veppo.html'],
    },
    {
        'slug': 'automatisation-n8n-pme',
        'title': 'Automatisation n8n pour PME | Freelance Omar A. Wankoye',
        'h1': 'Automatisation n8n pour PME',
        'desc': 'Freelance n8n : automatisez devis, relances, CRM, e-mails et Google Sheets pour votre PME. Workflows sur mesure, IA intégrée, hébergement maîtrisé.',
        'eyebrow': 'Automatisation · n8n',
        'lead': 'Connectez vos outils et supprimez les tâches répétitives : avec n8n, vos devis, relances, factures et suivis clients s’exécutent tout seuls, pendant que votre équipe se concentre sur les clients.',
        'area': None,
        'service': 'automatisation-ia-workflows',
        'body': '''
<h2>Pourquoi n8n pour une PME ?</h2>
<p><strong>n8n</strong> est un outil d’automatisation de workflows qui relie vos applications entre elles (formulaires, e-mail, CRM, Google Sheets, WhatsApp, boutique en ligne, comptabilité…). Contrairement à des outils facturés à chaque tâche exécutée, n8n peut être <strong>auto-hébergé</strong> : vos données restent sous votre contrôle et le coût reste maîtrisé, même avec beaucoup d’automatisations.</p>
<p>Je conçois aussi des workflows sur <strong>Make</strong> et <strong>Zapier</strong> lorsque c’est plus adapté à votre contexte.</p>
<h3>Exemples d’automatisations</h3>
<ul>
<li><strong>Prospects :</strong> un formulaire du site crée automatiquement le contact dans votre CRM, vous notifie sur WhatsApp ou Slack et envoie un e-mail de confirmation au prospect.</li>
<li><strong>Devis et relances :</strong> génération d’un devis PDF, envoi, puis relance automatique après quelques jours sans réponse.</li>
<li><strong>Commandes :</strong> chaque commande de la boutique met à jour un Google Sheet de suivi, prévient la logistique et envoie la facture.</li>
<li><strong>Reporting :</strong> un rapport hebdomadaire des ventes et des leads envoyé par e-mail chaque lundi.</li>
<li><strong>IA intégrée :</strong> tri et résumé des e-mails entrants, réponses suggérées, extraction de données de documents avec un modèle de langage.</li>
</ul>
<h3>Ma méthode</h3>
<ol>
<li>Audit gratuit : on liste vos tâches répétitives et le temps qu’elles prennent.</li>
<li>On priorise les automatisations au meilleur retour sur investissement.</li>
<li>Je construis, teste et documente chaque workflow, avec gestion des erreurs.</li>
<li>Je forme votre équipe et assure le suivi.</li>
</ol>
''',
        'points': [
            'Audit des tâches répétitives',
            'Workflows n8n sur mesure (ou Make / Zapier)',
            'Connexion CRM, e-mail, Google Sheets, WhatsApp',
            'IA intégrée : tri, résumé, extraction',
            'Gestion des erreurs et alertes',
            'Documentation et formation',
        ],
        'faqs': [
            ('Qu’est-ce que n8n et pourquoi le choisir ?',
             'n8n est un outil d’automatisation qui connecte vos applications entre elles avec des workflows visuels. Il peut être auto-hébergé, ce qui garde vos données sous contrôle et limite les coûts quand le volume d’automatisations augmente.'),
            ('Quelles tâches une PME peut-elle automatiser ?',
             'La saisie et la synchronisation de données, les relances de devis et de factures, la création de contacts dans un CRM, les notifications d’équipe, les rapports périodiques, ainsi que le tri d’e-mails ou de documents avec l’aide de l’IA.'),
            ('Faut-il des compétences techniques pour utiliser les automatisations ?',
             'Non. Une fois en place, les workflows tournent seuls. Je documente chaque automatisation et forme la personne qui pourra les surveiller ou les ajuster simplement.'),
            ('n8n, Make ou Zapier : lequel choisir ?',
             'Zapier est très simple pour des besoins légers, Make offre plus de flexibilité visuelle, et n8n est idéal pour des workflows complexes, de gros volumes ou l’auto-hébergement. Je vous recommande l’outil adapté après l’audit.'),
        ],
        'projects': ['chatbotpdf.html', 'suptechchatbot.html', 'myshop.html'],
    },
    {
        'slug': 'chatbot-ia-entreprise',
        'title': 'Chatbot IA pour entreprise | Freelance Omar A. Wankoye',
        'h1': 'Chatbot IA pour votre entreprise',
        'desc': 'Création de chatbots IA sur mesure : support client 24/7, assistant interne sur vos documents (RAG), site web et WhatsApp. Freelance certifié IBM AI Developer.',
        'eyebrow': 'IA · Chatbots',
        'lead': 'Un assistant IA qui répond à vos clients 24 h/24 avec vos propres informations, ou qui aide vos équipes à retrouver instantanément la bonne réponse dans vos documents.',
        'area': None,
        'service': 'automatisation-ia-workflows',
        'body': '''
<h2>Un chatbot qui connaît vraiment votre entreprise</h2>
<p>Un chatbot générique invente parfois des réponses. Les chatbots que je développe s’appuient sur <strong>vos propres contenus</strong> — catalogue, FAQ, procédures, tarifs, documents PDF — grâce à la technique <strong>RAG</strong> (Retrieval-Augmented Generation). Le modèle de langage cherche d’abord l’information dans vos documents, puis formule une réponse claire et vérifiable.</p>
<p>Je suis certifié <strong>IBM AI Developer</strong> et j’ai déjà livré des chatbots en production, comme un assistant de support pour une université et un chatbot documentaire pour une entreprise.</p>
<h3>Cas d’usage</h3>
<ul>
<li><strong>Support client 24/7</strong> sur votre site ou WhatsApp : horaires, tarifs, suivi de commande, questions fréquentes.</li>
<li><strong>Assistant interne :</strong> vos équipes interrogent les procédures, contrats ou fiches techniques en langage naturel.</li>
<li><strong>Qualification de prospects :</strong> le chatbot pose les bonnes questions et transmet un résumé à votre équipe commerciale.</li>
<li><strong>Éducation et formation :</strong> réponses aux étudiants, aide à l’orientation, FAQ administrative.</li>
</ul>
<h3>Fiabilité et confidentialité</h3>
<ul>
<li>Réponses limitées à vos sources, avec transfert vers un humain si la question sort du périmètre.</li>
<li>Choix du modèle (OpenAI, Gemini, modèles open source) selon vos contraintes de coût et de confidentialité.</li>
<li>Hébergement maîtrisé et accès sécurisés.</li>
<li>Tableau de suivi des conversations pour améliorer les réponses.</li>
</ul>
''',
        'points': [
            'Chatbot entraîné sur vos documents (RAG)',
            'Intégration site web et WhatsApp',
            'Transfert vers un humain si besoin',
            'Choix du modèle IA selon vos contraintes',
            'Suivi des conversations',
            'Déploiement cloud sécurisé',
        ],
        'faqs': [
            ('Un chatbot IA peut-il répondre avec les informations de mon entreprise ?',
             'Oui. Avec la technique RAG, le chatbot recherche d’abord la réponse dans vos documents (FAQ, catalogue, procédures) puis la formule clairement. Il reste ainsi fidèle à vos informations.'),
            ('Le chatbot peut-il fonctionner sur WhatsApp ?',
             'Oui, le même assistant peut être intégré à votre site web et à WhatsApp Business, pour répondre là où vos clients vous écrivent déjà.'),
            ('Que se passe-t-il si le chatbot ne connaît pas la réponse ?',
             'Il l’indique honnêtement et propose de transmettre la demande à un membre de votre équipe, avec un résumé de la conversation.'),
            ('Mes données restent-elles confidentielles ?',
             'Oui. Je choisis avec vous le modèle et l’hébergement adaptés, avec des accès limités, et des modèles open source hébergés de façon maîtrisée si la confidentialité est critique.'),
        ],
        'projects': ['suptechchatbot.html', 'chatbotpdf.html', 'siteimage.html'],
    },
    {
        'slug': 'developpeur-django-freelance',
        'title': 'Développeur Django freelance | Omar A. Wankoye',
        'h1': 'Développeur Django & Python freelance',
        'desc': 'Développeur Django freelance certifié IBM Full Stack : applications web, back-offices, API REST, e-commerce et intégration IA. Remote France, Italie, Afrique.',
        'eyebrow': 'Python · Django',
        'lead': 'Applications web robustes, back-offices sur mesure et API REST en Python/Django — avec une interface moderne et, si besoin, de l’intelligence artificielle intégrée.',
        'area': None,
        'service': 'developpement-application-web-mobile',
        'body': '''
<h2>Pourquoi Django pour votre projet ?</h2>
<p><strong>Django</strong> est un framework Python reconnu pour sa sécurité, sa rapidité de développement et son <strong>interface d’administration</strong> prête à l’emploi. C’est un excellent choix pour un back-office métier, une plateforme de gestion, un e-commerce sur mesure ou une API qui alimente une application mobile.</p>
<p>Je développe en Django depuis plusieurs années et je suis certifié <strong>IBM Full Stack Software Developer</strong>. Côté interface, je combine Django avec React, Tailwind ou des templates HTML optimisés selon le projet.</p>
<h3>Ce que je développe avec Django</h3>
<ul>
<li><strong>Back-offices et outils métier :</strong> gestion de produits, stocks, fournisseurs, commandes, rendez-vous.</li>
<li><strong>API REST</strong> avec Django REST Framework pour une application mobile ou un front-end React.</li>
<li><strong>E-commerce sur mesure</strong> avec commande en ligne et génération de documents PDF.</li>
<li><strong>Intégration IA :</strong> chatbots, analyse de documents, recommandations, via LangChain et des modèles de langage.</li>
<li><strong>Reprise et maintenance</strong> d’applications Django existantes : mises à jour, sécurité, performances.</li>
</ul>
<h3>Exemples réalisés</h3>
<p>Un site de cabinet médical avec prise de rendez-vous (React + Django REST Framework + PostgreSQL), une boutique avec back-office produits/fournisseurs et bons de commande PDF (Django), et un site de pizzeria avec menu administrable.</p>
<h3>Qualité et déploiement</h3>
<ul>
<li>Code structuré, testé et documenté.</li>
<li>Sécurité : authentification, permissions, protections CSRF/XSS, variables d’environnement.</li>
<li>Déploiement sur Render, PythonAnywhere, AWS ou IBM Cloud, avec Docker si nécessaire.</li>
</ul>
''',
        'points': [
            'Applications et back-offices Django sur mesure',
            'API REST (Django REST Framework)',
            'Front-end React / Tailwind',
            'Intégration IA (LangChain, LLM)',
            'Reprise, maintenance et sécurité',
            'Déploiement cloud et Docker',
        ],
        'faqs': [
            ('Pourquoi choisir Django pour une application web ?',
             'Django est sécurisé, rapide à développer et fournit une interface d’administration complète. Il convient parfaitement aux outils métier, aux plateformes de gestion, aux e-commerces sur mesure et aux API pour applications mobiles.'),
            ('Pouvez-vous reprendre une application Django existante ?',
             'Oui. Je commence par un audit du code, des dépendances et de l’hébergement, puis je propose un plan de mise à jour, de correction et d’amélioration des performances et de la sécurité.'),
            ('Travaillez-vous avec React en front-end ?',
             'Oui, je combine régulièrement Django REST Framework côté serveur et React (ou Next.js) côté interface, comme pour le site de cabinet médical présenté dans mes réalisations.'),
            ('Où hébergez-vous les applications Django ?',
             'Selon le budget et les besoins : Render, PythonAnywhere, AWS ou IBM Cloud, avec Docker et une base PostgreSQL pour les projets qui doivent évoluer.'),
        ],
        'projects': ['cabinet.html', 'myshop.html', 'portfolio-site-restaurant.html'],
    },
]
