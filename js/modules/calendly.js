/*
  Calendly integration — Popup Widget

  Antes de publicar, reemplaza este placeholder con la URL real
  del Event Type único de la cuenta de Marta Gadal en Calendly
  (usado para coordinar tanto Clases Online como Equilibrio Emocional).

  Checklist pre-deploy:
  - [ ] CALENDLY_LINK → URL real del Event Type "Coordinación de horarios"
*/
const CALENDLY_LINK = 'https://calendly.com/solsere/coordinacion-de-horarios';

window.CALENDLY_LINK = CALENDLY_LINK;

window.openCalendly = function(url) {
  if (typeof Calendly !== 'undefined' && Calendly.initPopupWidget) {
    Calendly.initPopupWidget({ url });
  } else {
    window.open(url, '_blank', 'noopener,noreferrer');
  }
};
