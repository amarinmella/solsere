const header = document.getElementById('site-header');
const navToggle = document.getElementById('nav-toggle');
const navLinks = document.querySelectorAll('.nav-link');
const sections = document.querySelectorAll('section[id]');

/* Clase .scrolled cuando scrollY > 50px */
function updateScrolled() {
  header.classList.toggle('scrolled', window.scrollY > 50);
}

window.addEventListener('scroll', updateScrolled, { passive: true });
updateScrolled();

/* Cerrar menú mobile al hacer clic en cualquier nav-link */
navLinks.forEach(link => {
  link.addEventListener('click', () => {
    if (navToggle) navToggle.checked = false;
  });
});

/* Marcar ítem activo con IntersectionObserver */
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = entry.target.id;
      navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
      });
    }
  });
}, {
  rootMargin: '-40% 0px -55% 0px',
  threshold: 0
});

sections.forEach(section => observer.observe(section));
