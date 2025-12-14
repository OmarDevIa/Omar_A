// ====================================
// 1. Initialisation de AOS (Animate On Scroll)
// ====================================
document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        // Une fois que l'animation s'est produite, elle ne se répète pas au défilement
        once: true, 
        // Durée de l'animation en millisecondes
        duration: 1000, 
        // Écart (offset) par rapport au bas de la fenêtre pour déclencher l'animation
        offset: 50, 
    });

    // Optionnel: Défilement fluide pour les liens internes
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});

// ====================================
// 2. Script Typewriter (Animation de texte)
// ====================================

// Note: Le titre principal est maintenant géré par le H1 statique pour le SEO.
// Nous ciblons ici l'élément H1 si vous souhaitez conserver l'effet.
const titles = [
    "Omar Atta Y M",
    "Développeur IA & Logiciel Freelance",
    "4 ans d'expérience"
];

let i = 0, j = 0;
let isDeleting = false;
const speed = 70; // Vitesse de frappe (plus petit = plus rapide)
const delay = 1500; // Délai avant de commencer à effacer

function typeWriter() {
    const h1 = document.getElementById("typewriter");
    if (!h1) return;

    let currentTitle = titles[i];
    
    if (isDeleting) {
        // Suppression
        currentTitle = currentTitle.substring(0, j - 1);
        j--;
    } else {
        // Écriture
        currentTitle = currentTitle.substring(0, j + 1);
        j++;
    }

    h1.textContent = currentTitle;

    let timeout = speed;

    if (!isDeleting && j === titles[i].length) {
        // Texte entièrement écrit
        timeout = delay;
        isDeleting = true;
    } else if (isDeleting && j === 0) {
        // Texte entièrement effacé
        isDeleting = false;
        i = (i + 1) % titles.length; // Passe au titre suivant (boucle)
        timeout = 500; // Petite pause avant de commencer à écrire le nouveau titre
    }

    // Ajustement de la vitesse pendant la suppression
    if (isDeleting) {
        timeout = speed / 2; 
    }

    setTimeout(typeWriter, timeout);
}

// Démarre l'animation de frappe
document.addEventListener("DOMContentLoaded", typeWriter);