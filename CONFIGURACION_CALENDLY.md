# Cómo crear tus sesiones en Calendly (con pago integrado por PayPal)

**Para:** Marta Gadal
**Proyecto:** Rediseño Web Solsere

---

## Antes de empezar

Ya tienes:
- Cuenta de Calendly en plan **Standard** ✅
- Cuenta **PayPal Business** ✅

Con ambas, Calendly puede cobrar automáticamente en el mismo paso en que el cliente agenda su hora — no necesitas coordinar el pago por separado.

Necesitas crear **2 eventos**, uno por cada servicio, y conectar PayPal a cada uno.

---

## Paso 1: Conectar PayPal a Calendly

1. Entra a **calendly.com** e inicia sesión
2. Ve a **Settings (⚙️) → Payments**
3. Clic en **"Connect PayPal"**
4. Inicia sesión con las credenciales de tu cuenta **PayPal Business**
5. Autoriza el acceso cuando PayPal lo solicite
6. Confirma que en Calendly aparece el estado **"Connected"** ✅

---

## Paso 2: Crear el evento "Clases Online"

1. En el panel principal, clic en **"+ Create"** → **"Event type"** → **"One-on-One"**
2. Completa:
   - **Nombre del evento:** `Clases Online`
   - **Duración:** define según cómo dictas las 7 clases (si es una sesión por vez, define la duración de una sesión individual — por ejemplo, 60 o 90 minutos)
   - **Ubicación:** Google Meet, Zoom, o la plataforma que uses (Calendly te permite conectar tu cuenta automáticamente)
3. En **"Description"**, agrega:
   > "Paquete de 7 clases online — $90.000. Hasta 2 alumnos."
4. Activa **"Collect payment"** (dentro de la configuración del evento) e ingresa:
   - **Monto:** $90.000 CLP
5. Guarda con **"Save & Close"** o **"Save & Publish"**

---

## Paso 3: Crear el evento "Equilibrio Emocional"

1. Mismo proceso → **"+ Create"** → **"Event type"** → **"One-on-One"**
2. Completa:
   - **Nombre del evento:** `Equilibrio Emocional`
   - **Duración:** define cuánto dura una atención (por ejemplo, 45-60 min)
   - **Ubicación:** presencial, videollamada, o la que corresponda
3. En **"Description"**, agrega:
   > "Terapia Floral + EFT Tapping — $45.000, 2 atenciones + material incluido."
4. Activa **"Collect payment"** e ingresa:
   - **Monto:** $45.000 CLP
5. Guarda

---

## Paso 4: Configurar tu disponibilidad

1. Ve a **Availability** (menú lateral)
2. Define los días y horarios en que puedes atender (ejemplo: Lunes a Viernes, 15:00–19:00)
3. Esto aplica a ambos eventos por defecto. Si quieres horarios distintos para cada servicio, puedes personalizar la disponibilidad dentro de cada Event Type, en su propia sección "Availability"

---

## Paso 5: Copiar los links y enviarlos

1. Desde la lista de **Event Types**, cada uno tiene un botón **"Copy Link"** (o "Share")
2. Copia ambos links y envíalos a Juan:
   - Link de **Clases Online**
   - Link de **Equilibrio Emocional**

---

## Paso 6: Integración final

Con los 2 links, Juan actualiza el archivo del sitio (`js/modules/calendly.js`) y el flujo completo de "agenda y paga" queda 100% funcional en el sitio web.

---

## Recomendación extra: recordatorios automáticos

Dentro de cada Event Type, ve a **"Notifications"** y activa el recordatorio automático por email 24 horas antes de la cita. Esto reduce las inasistencias sin que tengas que acordarte manualmente.

---

## ¿Cómo funciona el flujo completo?

```
Cliente entra a solsere.com
        ↓
Clic en "Agenda tu hora"
        ↓
Se abre Calendly (popup)
        ↓
Cliente elige fecha y hora
        ↓
Cliente paga con PayPal (dentro del mismo flujo)
        ↓
Reserva confirmada automáticamente
        ↓
Tú recibes notificación de Calendly + el pago en tu cuenta PayPal
```

Ya no necesitas cruzar manualmente reservas con pagos — Calendly solo confirma la hora cuando el pago fue exitoso.

---

## Checklist rápido

- [ ] PayPal Business conectado a Calendly (Settings → Payments)
- [ ] Evento "Clases Online" creado con duración, descripción y cobro de $90.000 activado
- [ ] Evento "Equilibrio Emocional" creado con duración, descripción y cobro de $45.000 activado
- [ ] Disponibilidad configurada (días y horarios)
- [ ] Links copiados y enviados a Juan
- [ ] Recordatorios automáticos activados (opcional pero recomendado)
- [ ] Prueba de agendamiento + pago realizada antes de publicar

---

**Documento preparado por:** Innova IA Studio
