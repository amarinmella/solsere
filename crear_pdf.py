#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

# Crear PDF
pdf_path = "CONFIGURACION_CALENDLY_STRIPE.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter, topMargin=0.75*inch, bottomMargin=0.75*inch)
styles = getSampleStyleSheet()

# Estilos personalizados
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor('#2D5A27'),
    spaceAfter=12,
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=13,
    textColor=colors.HexColor('#4A7C40'),
    spaceAfter=8,
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontSize=10,
    spaceAfter=6,
)

# Contenido del documento
story = []

# Título
story.append(Paragraph("Configuración de Calendly y Stripe para Solsere", title_style))
story.append(Paragraph("Documento preparado para: Marta Gadal", body_style))
story.append(Spacer(1, 12))

# Resumen
story.append(Paragraph("Resumen Ejecutivo", heading_style))
story.append(Paragraph(
    "Para que tu sitio web de Solsere funcione correctamente y puedas recibir pagos online, necesitamos configurar dos herramientas: Calendly (agenda) y Stripe (pagos). Ambas son profesionales, seguras y ampliamente usadas.",
    body_style
))
story.append(Spacer(1, 12))

# Calendly
story.append(Paragraph("Calendly — Sistema de Agendamiento", heading_style))
story.append(Paragraph("Qué es: Calendly permite que tus clientes vean tu disponibilidad y reserven hora directamente desde el sitio web, sin mensajería ni llamadas.", body_style))
story.append(Paragraph("<b>Costo:</b> ~$12 USD/mes (plan Professional, necesario para cobros)", body_style))
story.append(Spacer(1, 8))

# Stripe
story.append(Paragraph("Stripe — Procesamiento de Pagos", heading_style))
story.append(Paragraph("Qué es: Stripe procesa pagos de forma segura. Recibe dinero de tus clientes automáticamente.", body_style))
story.append(Paragraph("<b>Costo:</b> Gratis crear cuenta. Pagas ~3% por cada transacción (solo cuando vendes).", body_style))
story.append(Spacer(1, 12))

# Pasos para Marta
story.append(Paragraph("Pasos que debes hacer (Marta)", heading_style))
story.append(Paragraph("1. Crear cuenta en Calendly (calendly.com) ✓", body_style))
story.append(Paragraph("2. Suscribirse a plan Professional (~$12 USD/mes) ✓", body_style))
story.append(Paragraph("3. Crear cuenta en Stripe (stripe.com) ✓", body_style))
story.append(Paragraph("4. Conectar tu cuenta bancaria chilena en Stripe ✓", body_style))
story.append(Paragraph("5. Conectar Stripe a Calendly desde tu panel ✓", body_style))
story.append(Paragraph("6. Crear 2 eventos en Calendly: Clases Online ($80k) y Terapias Florales ($35k) ✓", body_style))
story.append(Paragraph("7. Enviarme los 2 links públicos de los eventos ✓", body_style))
story.append(Spacer(1, 12))

# Pasos para ti
story.append(Paragraph("Pasos que haré (Juan)", heading_style))
story.append(Paragraph("1. Recibir los 2 links de Calendly", body_style))
story.append(Paragraph("2. Integrarlos en el sitio web (2 minutos)", body_style))
story.append(Paragraph("3. Testear que funcione", body_style))
story.append(Paragraph("4. Deploy", body_style))
story.append(Spacer(1, 12))

# Ejemplos de ingresos
story.append(Paragraph("Ejemplos de ingresos netos", heading_style))
story.append(Paragraph("<b>1 clase online ($80.000):</b><br/>Stripe cobra ~3% = $2.400<br/>Marta recibe: $77.600", body_style))
story.append(Paragraph("<b>1 terapia floral ($35.000):</b><br/>Stripe cobra ~3% = $1.050<br/>Marta recibe: $33.950", body_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Con 2-3 ventas/mes, el costo de Calendly Professional se justifica fácilmente.", body_style))

# Build
doc.build(story)
print(f"PDF creado exitosamente: {pdf_path}")
