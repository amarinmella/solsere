/*
  Calendly integration — Popup Widget

  Antes de publicar, reemplaza estos placeholders con las URLs reales
  de los Event Types de la cuenta de Marta Gadal en Calendly.

  Checklist pre-deploy:
  - [ ] CALENDLY_LINK_CLASES → URL real del Event Type "Clases Online"
  - [ ] CALENDLY_LINK_FLORALES → URL real del Event Type "Terapias Florales"
*/
const CALENDLY_LINK_CLASES = 'https://calendly.com/solsere/clases-online';
const CALENDLY_LINK_FLORALES = 'https://calendly.com/solsere/terapias-florales';

window.CALENDLY_LINK_CLASES = CALENDLY_LINK_CLASES;
window.CALENDLY_LINK_FLORALES = CALENDLY_LINK_FLORALES;

window.openCalendly = function(url) {
  if (typeof Calendly !== 'undefined' && Calendly.initPopupWidget) {
    Calendly.initPopupWidget({ url });
  } else {
    window.open(url, '_blank', 'noopener,noreferrer');
  }
};
