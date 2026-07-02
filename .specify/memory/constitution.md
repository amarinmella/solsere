<!-- SYNC IMPACT REPORT
Version change: (none) → 1.0.0 (initial ratification)
Added principles: I. Mobile-First, II. Stack Vanilla, III. Conversión Intencional, IV. Identidad Visual Consistente, V. Contenido Sobre Forma
Added sections: Restricciones Técnicas, Flujo de Desarrollo
Templates updated: ✅ constitution.md (this file)
Templates pending manual review: ⚠ plan-template.md (Constitution Check gates should reference these principles)
Deferred: none
-->

# Solsere Constitution

## Core Principles

### I. Mobile-First (NO NEGOCIABLE)

Todo diseño y desarrollo DEBE comenzar desde el viewport móvil (375px mínimo) y escalar hacia arriba.
- El layout base se define en móvil; desktop es una expansión, no el punto de partida.
- Imágenes DEBEN tener tamaños responsivos (`srcset` o CSS clamp).
- Ningún elemento visible en desktop puede ser inaccesible en móvil.
- Tocar/hacer clic DEBE tener áreas mínimas de 44×44px.

### II. Stack Vanilla (NO NEGOCIABLE)

El proyecto usa exclusivamente HTML5, CSS3 y JavaScript ES6+ sin frameworks ni librerías externas.
- Prohibido: React, Vue, Angular, jQuery, Bootstrap, Tailwind, o cualquier npm package.
- Permitido: fuentes de Google Fonts, íconos SVG inlineados, y variables CSS nativas.
- Todo archivo JS DEBE ser un módulo ES6 (`type="module"`).
- El sitio DEBE funcionar sin JavaScript habilitado en su estructura base (contenido y navegación accesibles via HTML/CSS).

### III. Conversión Intencional

Cada sección de cada página DEBE tener una ruta clara hacia una acción concreta.
- Acciones válidas: Reservar Clase, Suscribirse a Plan, Contactar por WhatsApp, Ver Servicios.
- Ninguna sección puede quedar "de lectura pura" sin un CTA visible.
- Los CTAs DEBEN ser consistentes en texto, color y jerarquía visual en todo el sitio.
- El formulario/botón de WhatsApp DEBE estar accesible en ≤2 clics desde cualquier punto del sitio.

### IV. Identidad Visual Consistente

La paleta, tipografía y tono de Solsere DEBEN mantenerse sin excepciones en todo el sitio.
- Paleta: verdes naturales, tonos pasteles botánicos, dorado cálido de acento.
- Tagline canónico: "Bienestar que florece desde adentro" — no parafrasear.
- Claim canónico: "Tu bienestar es único, tu camino también" — no parafrasear.
- Ilustraciones y fotograf­ías DEBEN alinearse con estética botánica/natural (flores, hojas, luz suave).
- Tono de copy: cálido, humanista, directo — evitar lenguaje clínico o corporativo.

### V. Contenido Sobre Forma

La jerarquía de contenido de Solsere dirige el layout, nunca al revés.
- Los tres pilares (Clases Online, Terapias Florales, Enfoque Integrativo) DEBEN tener
  igual jerarquía visual en la home.
- Información de precios DEBE ser visible sin necesidad de interacción (no ocultar en modales).
- Testimonios y prueba social DEBEN aparecer en contexto de servicio, no solo en sección separada.
- El contenido de la imagen de aniversario (21 años) es la fuente de verdad para los servicios actuales.

## Restricciones Técnicas

- **Hosting**: Hostinger — sin soporte para Node.js ni backends dinámicos en producción.
- **Formularios**: El contacto DEBE operar via WhatsApp y/o mailto (no backend propio).
- **Performance**: Lighthouse Performance Score DEBE ser ≥ 85 en mobile antes de deploy.
- **Accesibilidad**: Lighthouse Accessibility Score DEBE ser ≥ 80 (contraste, alt text, roles semánticos).
- **Estructura de archivos**:
  ```
  solsere/
  ├── index.html
  ├── css/
  │   ├── main.css
  │   └── components/
  ├── js/
  │   └── modules/
  ├── assets/
  │   ├── images/
  │   └── icons/
  └── pages/         (secciones como archivos separados si se requiere)
  ```
- **Git**: Commits frecuentes por sección completada. Rama `main` = producción.

## Flujo de Desarrollo

1. **Spec primero** (`/speckit-specify`): definir alcance, user stories y requisitos antes de escribir código.
2. **Plan técnico** (`/speckit-plan`): estructura de archivos, decisiones de layout y componentes.
3. **Tareas** (`/speckit-tasks`): desglose ejecutable en orden de dependencias.
4. **Implementación** (`/speckit-implement`): una tarea a la vez, validando en browser real.
5. **Convergencia** (`/speckit-converge`): verificar qué quedó pendiente antes de dar por terminado.

Cada sección/página completada DEBE probarse en Chrome mobile emulation (375px) antes de avanzar a la siguiente.

## Governance

- Esta constitución es la referencia suprema del proyecto Solsere.
- Cualquier decisión técnica o de contenido que contradiga estos principios DEBE justificarse
  explícitamente antes de proceder.
- Enmiendas requieren: descripción del cambio, razón, impacto en artefactos dependientes.
- Versioning: MAJOR para cambios de principios incompatibles; MINOR para nuevos principios o secciones;
  PATCH para clarificaciones y correcciones menores.
- Todos los sprints de implementación DEBEN verificar compliance con esta constitución en la revisión final.

**Version**: 1.0.0 | **Ratified**: 2026-07-02 | **Last Amended**: 2026-07-02
