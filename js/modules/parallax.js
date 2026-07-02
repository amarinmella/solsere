const isMobile = () => window.matchMedia('(max-width: 768px)').matches;

let ticking = false;

function updateParallax() {
  const scrollY = window.scrollY;
  document.querySelectorAll('[data-parallax]').forEach(el => {
    const speed = parseFloat(el.dataset.parallax) || 0.3;
    el.style.transform = `translateY(${scrollY * speed}px)`;
  });
  ticking = false;
}

function onScroll() {
  if (isMobile()) return;
  if (!ticking) {
    requestAnimationFrame(updateParallax);
    ticking = true;
  }
}

function resetParallax() {
  document.querySelectorAll('[data-parallax]').forEach(el => {
    el.style.transform = '';
  });
}

window.addEventListener('scroll', onScroll, { passive: true });

window.addEventListener('resize', () => {
  if (isMobile()) resetParallax();
});
