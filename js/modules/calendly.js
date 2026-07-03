/*
  Calendly integration — Popup Widget

  Event Type único de la cuenta de Marta Gadal en Calendly
  ("Solsere Servicios"), usado para coordinar tanto Clases Online
  como Equilibrio Emocional.
*/
const CALENDLY_LINK = 'https://calendly.com/martagadal/solsere-servicios';

window.CALENDLY_LINK = CALENDLY_LINK;

window.openCalendly = function(url) {
  if (typeof Calendly !== 'undefined' && Calendly.initPopupWidget) {
    Calendly.initPopupWidget({ url });
  } else {
    window.open(url, '_blank', 'noopener,noreferrer');
  }
};
