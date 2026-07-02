# Configuración de Formspree para Solsere

**Formulario de contacto en:** www.solsere.com → Sección "Conversemos"

---

## ¿Qué es Formspree?

Formspree es un servicio que procesa formularios web de forma segura. Cuando alguien envía el formulario de contacto en tu sitio, Formspree automáticamente te envía un email con los datos.

**Ventajas:**
- ✅ Gratis (hasta 50 envíos/mes)
- ✅ No requiere backend
- ✅ Seguro y confiable
- ✅ Recibe emails con los datos del cliente

---

## Pasos de Configuración

### Paso 1: Crear cuenta en Formspree

1. Ve a **https://formspree.io**
2. Haz clic en **"Sign Up"** (esquina superior derecha)
3. Completa con:
   - Email: Tu correo (puede ser contacto@solsere.com)
   - Contraseña: Una segura
   - Haz clic en **"Create Account"**

### Paso 2: Crear nuevo formulario

1. Una vez en tu dashboard, haz clic en **"New Form"**
2. Completa:
   - **Form Name**: "Contacto Solsere"
   - **Email Address**: Tu email para recibir mensajes (amarinmella@gmail.com o el que prefieras)
3. Haz clic en **"Create Form"**

### Paso 3: Obtener tu ID

1. Te mostrarán una página con tu **"Form ID"** (algo como `f1a2b3c4d5e6`)
2. **Copia este ID** — lo necesitarás ahora

### Paso 4: Actualizar el sitio web

Necesitas reemplazar el placeholder en el formulario:

**Archivo a editar:** `index.html`  
**Busca esta línea (aprox. línea 245):**
```html
<form class="contact-form" action="https://formspree.io/f/REEMPLAZAR_CON_TU_ID" method="POST" novalidate>
```

**Reemplaza `REEMPLAZAR_CON_TU_ID` con tu ID real.**

**Ejemplo (con ID ficticio):**
```html
<form class="contact-form" action="https://formspree.io/f/xyzabc123" method="POST" novalidate>
```

### Paso 5: Listo

Una vez guardado, el formulario está activo. Prueba enviando un mensaje desde www.solsere.com y verifica que llegue a tu email.

---

## ¿Qué pasa cuando alguien envía el formulario?

1. **Usuario** rellena el formulario y hace clic en "Enviar mensaje"
2. **Formspree** procesa los datos de forma segura
3. **Tú** recibes un email automático con:
   - Nombre completo
   - Email del cliente
   - Teléfono (si lo incluye)
   - Asunto (Clases Online / Terapias / etc.)
   - Mensaje completo

4. **Usuario** ve un mensaje de "¡Gracias! Tu mensaje fue enviado"

---

## Límites Gratuitos

- **50 envíos/mes** → Suficiente para la mayoría de casos
- Si necesitas más, upgrade a plan pagado (~$25 USD/mes)

---

## Soporte

- **Dudas de Formspree:** https://formspree.io/help
- **Tu panel de Formspree:** https://formspree.io/forms

---

## Checklist Pre-Deploy

- [ ] Cuenta creada en Formspree
- [ ] Formulario creado y ID obtenido
- [ ] Reemplazaste `REEMPLAZAR_CON_TU_ID` en `index.html`
- [ ] Probaste enviar un mensaje de prueba
- [ ] Recibiste el email de prueba
- [ ] ¡Listo para publicar!

---

**Documento preparado por:** Innova IA Studio
