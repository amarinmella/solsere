# Cómo crear tu evento en Calendly

**Para:** Marta Gadal
**Proyecto:** Rediseño Web Solsere

---

## Antes de empezar

Ya tienes tu cuenta de Calendly activa en plan **Standard**. El pago se coordina aparte por Mercado Pago o WhatsApp — este evento es solo para **agendar una llamada breve de coordinación**.

Necesitas crear **un solo evento**, usado tanto para Clases Online como para Equilibrio Emocional. Durante la llamada, tú defines los horarios específicos con cada clienta.

---

## Paso 1: Crear el evento

1. Entra a **calendly.com** e inicia sesión
2. En el panel principal, clic en **"+ Nuevo tipo de evento"**
3. Selecciona **"En privado"** (1 organizador → 1 invitado)
4. Completa:
   - **Nombre del evento:** `Coordinación de horarios` (o "Agenda tu hora")
   - **Duración:** `30 minutos`
   - **Ubicación:** llamada telefónica, WhatsApp, Google Meet o la que prefieras
5. En **"Description"**, agrega:
   > "Agenda una llamada breve para coordinar horarios. Clases Online ($90.000, paquete 7 clases) o Equilibrio Emocional ($45.000, 2 atenciones). El pago se coordina por Mercado Pago o WhatsApp."

---

## Paso 2: Agregar la pregunta de qué servicio le interesa

Esto es clave para que sepas de qué hablar antes de la llamada:

1. Dentro de la configuración del evento, busca la sección **"Preguntas de invitados"** (Invitee Questions)
2. Agrega una nueva pregunta:
   - **Tipo:** Selección única (radio buttons) o menú desplegable
   - **Pregunta:** `¿Qué servicio te interesa?`
   - **Opciones:**
     - `Clases Online`
     - `Equilibrio Emocional`
   - Marca la pregunta como **obligatoria**
3. Guarda con **"Save & Close"** o **"Save & Publish"**

---

## Paso 3: Configurar tu disponibilidad

1. Ve a **Availability** (menú lateral)
2. Define los días y horarios en que puedes atender llamadas de coordinación (ejemplo: Lunes a Viernes, 15:00–19:00)

---

## Paso 4: Copiar el link y enviarlo

1. Desde la lista de **Event Types**, busca el botón **"Copy Link"** (o "Share")
2. Copia el link y envíaselo a Juan

---

## Paso 5: Integración final

Con ese único link, Juan actualiza el archivo del sitio (`js/modules/calendly.js`) y los 3 botones de "Agenda tu hora" del sitio (hero, Clases Online, Equilibrio Emocional) quedan apuntando al mismo evento.

---

## Recomendación extra: recordatorios automáticos

Dentro del Event Type, ve a **"Notifications"** y activa el recordatorio automático por email 24 horas antes de la llamada. Esto reduce las inasistencias.

---

## ¿Cómo funciona el flujo completo?

```
Cliente entra a solsere.com
        ↓
Clic en "Agenda tu hora" (en cualquier tarjeta de servicio)
        ↓
Se abre Calendly (popup)
        ↓
Cliente elige fecha y hora + responde
"¿Qué servicio te interesa?"
        ↓
Reserva confirmada
        ↓
Tú recibes la notificación con la respuesta —
ya sabes de qué hablar en la llamada
        ↓
En la llamada, coordinas los horarios específicos
y el cliente paga por Mercado Pago o WhatsApp
```

---

## Checklist rápido

- [ ] Evento "Coordinación de horarios" creado (En privado, 30 min)
- [ ] Pregunta "¿Qué servicio te interesa?" agregada y marcada obligatoria
- [ ] Disponibilidad configurada (días y horarios)
- [ ] Link copiado y enviado a Juan
- [ ] Recordatorios automáticos activados (opcional pero recomendado)

---

**Documento preparado por:** Innova IA Studio
