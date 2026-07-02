# Configuración de Calendly y Stripe para Solsere

**Documento preparado para:** Marta Gadal  
**Fecha:** Julio 2026  
**Proyecto:** Rediseño Web Solsere

---

## 📋 Resumen Ejecutivo

Para que tu sitio web de Solsere funcione correctamente y puedas recibir pagos online, necesitamos configurar dos herramientas:

1. **Calendly** — Agenda tus clases y consultas directamente en el sitio
2. **Stripe** — Procesa los pagos automáticamente cuando alguien reserva

Ambas son profesionales, seguras y ampliamente usadas por educadores y emprendedores en Chile y el mundo.

---

## 🔵 Calendly — Sistema de Agendamiento

### ¿Qué es?
Calendly es una plataforma que permite que tus clientes vean tu disponibilidad y reserven hora sin necesidad de mensajería o llamadas. Todo es automático.

### ¿Por qué lo necesitas?
- **Reduce fricciones:** El cliente agenda en 30 segundos desde tu sitio web
- **Automático:** Confirmaciones y recordatorios se envían solos
- **Profesional:** Tu calendario se sincroniza con Google Calendar o Outlook
- **Integración con Stripe:** Los pagos se cobran al momento de la reserva

### Costo
- **Versión Gratuita:** Existe, pero **NO permite cobros**
- **Calendly Professional:** ~$12 USD/mes (~$10.000 CLP/mes)
  - Incluye integración con Stripe
  - Eventos ilimitados
  - Recordatorios automáticos
  - Branding personalizado

### ¿Qué configuraremos?

Crearemos **2 tipos de eventos** en tu cuenta:

| Evento | Precio | Detalles |
|--------|--------|----------|
| **Clases Online** | $80.000 CLP | 6 horas · Hasta 2 alumnos |
| **Terapias Florales** | $35.000 CLP | Mensual · 2 atenciones + material |

Cada uno tendrá su propio link que aparecerá en el sitio web.

### Pasos para ti

1. Crea una cuenta en **calendly.com** con tu email
2. Nos compartes tus links de evento (public booking URLs)
3. Nosotros los integramos en el sitio web
4. ¡Listo! Tus clientes pueden agendar directamente

---

## 🔴 Stripe — Procesamiento de Pagos

### ¿Qué es?
Stripe es la plataforma de pagos más confiable para recibir dinero online. Procesa tarjetas de crédito, débito y otros métodos de pago de forma segura.

### ¿Por qué lo necesitas?
- **Seguro:** Tus datos bancarios nunca quedan en el sitio web
- **Confiable:** Usado por empresas como Uber, Airbnb, Shopify
- **Flexible:** Acepta múltiples métodos de pago
- **Chile compatible:** Funciona perfectamente en Chile (comisión local aplicable)

### Costo
- **Cuota de membresía:** $0 (GRATIS)
- **Comisión por transacción:** ~2.9% + $30 CLP por pago
  - Solo pagas cuando alguien te paga
  - Sin transacciones = $0

### Ejemplo de ingresos

**Venta de 1 clase online ($80.000):**
```
Precio que cobra Marta:         $80.000
Comisión Stripe (~3%):          -$2.400
Dinero que recibe Marta:        $77.600
```

**Venta de 1 terapia floral ($35.000):**
```
Precio que cobra Marta:         $35.000
Comisión Stripe (~3%):          -$1.050
Dinero que recibe Marta:        $33.950
```

### Pasos para ti

1. Crea una cuenta en **stripe.com** con tu email
2. Completa verificación básica (nombre, empresa, documento)
3. Conecta tu cuenta bancaria chilena
4. Activa la integración con Calendly desde tu panel
5. ¡Listo! Los pagos llegan automáticamente a tu banco

---

## 🔗 ¿Cómo funcionan juntas?

```
Cliente accede a solsere.com
         ↓
    Ve "Agendar hora"
         ↓
    Abre Calendly (popup)
         ↓
    Selecciona fecha/hora
         ↓
    Ingresa email y paga con tarjeta
         ↓
    Stripe procesa el pago (seguro)
         ↓
    Tú recibes confirmación + dinero en el banco
         ↓
    Cliente recibe recordatorio automático
```

---

## ✅ Checklist de Configuración

### Antes del deploy:

- [ ] Crearás cuenta en Calendly con tu email
- [ ] Crearás cuenta en Stripe con tus datos
- [ ] Conectarás Stripe a Calendly desde tu panel
- [ ] Compartirás los links de evento con nosotros
- [ ] Nosotros integraremos los links en el sitio web
- [ ] Haremos prueba de pago (transacción de $100 CLP de prueba)
- [ ] Publicamos el sitio en www.solsere.com

### Después del deploy (mantenimiento):

- [ ] Revisar pagos en Stripe regularmente
- [ ] Actualizar disponibilidad en Calendly
- [ ] Mantener contacto bancario vigente

---

## 💰 Inversión Mensual

| Concepto | Costo | Notas |
|----------|-------|-------|
| Calendly Professional | $12 USD (~$10.000 CLP) | Obligatorio para pagos |
| Stripe | $0 base | Pagas solo comisión por venta (~3%) |
| **Total sin ventas** | **~$10.000 CLP** | |
| **Con 2 ventas/mes** | **~$10.000 + comisiones** | Ej: 2 clases = $80k × 2 × 3% ≈ $4.800 adicional |

**Rentabilidad:** Con vender solo 1 clase o 2-3 terapias al mes, cubres el costo de Calendly y ganas.

---

## 🔒 Seguridad

### Tus datos están seguros porque:
1. **Calendly y Stripe son certificadas internacionalmente** (SOC 2, PCI DSS)
2. **No guardamos tarjetas de crédito** — Stripe lo hace encriptado
3. **Tú tienes control total** — Puedes pausar/cancelar en cualquier momento
4. **Tu cuenta bancaria es segura** — Solo nosotros podemos conectar servicios

---

## ❓ Preguntas Frecuentes

### ¿Puedo cambiar los precios después?
Sí. Calendly permite actualizar precios en cualquier momento desde tu panel.

### ¿Qué pasa si un cliente cancela?
Calendly tiene opciones de reembolso. Tú controlas la política.

### ¿Necesito pagar impuestos por esto?
Sí, los ingresos por pagos online deben declararse como corresponde. Consulta con tu contador.

### ¿Funciona si el cliente no tiene tarjeta de crédito?
Stripe en Chile también acepta:
- Tarjetas de débito
- Transferencia bancaria (en algunos casos)
- Billeteras digitales

### ¿Qué pasa si Calendly o Stripe falla?
Ambos tienen 99.9% de disponibilidad. Si algo falla, el dinero queda en tránsito (no se pierde) y se resuelve en horas.

---

## 📞 Próximos Pasos

1. **Tú:** Creas cuentas en Calendly y Stripe
2. **Tú:** Nos compartes los links públicos de los eventos
3. **Nosotros:** Integramos los links en tu sitio web
4. **Ambos:** Hacemos una prueba de pago
5. **Listo:** Publicamos en producción

**Tiempo estimado:** 2-3 horas de trabajo de tu parte (incluyendo verificaciones)

---

## 📧 Contacto y Soporte

Si tienes dudas:
- **Sobre Calendly:** support@calendly.com o sus videos tutoriales
- **Sobre Stripe:** support@stripe.com (en español disponible)
- **Sobre integración en tu sitio:** Escríbeme directamente

---

**Documento preparado por:** Innova IA Studio  
**Para más info:** www.innovaiastudio.com
