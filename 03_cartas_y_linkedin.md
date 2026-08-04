# Fase 2 — Cartas de motivación y LinkedIn

← [Volver al runbook](00_RUNBOOK.md) · Requiere [Fase 0](01_datos_base.md)

**Qué produce:** cartas de motivación en variantes por cargo e idioma, y el contenido de tu perfil de
LinkedIn listo para pegar campo por campo.

---

## Parte 1 — La carta como datos, no como documento

Si escribes cada carta desde cero, pasa una de dos cosas: dejas de mandarlas, o mandas siempre la misma
carta genérica que no dice nada.

La solución es tratarla igual que el CV: **contenido estructurado + renderizado**.

### Variantes por cargo

La misma trayectoria se cuenta distinto según a qué apuntes. **Los hechos y las cifras no cambian nunca;
cambia qué se pone primero.**

> Ejemplo con un perfil que ha liderado equipos y también construido software:
>
> - Para una vacante de **liderazgo**: abre con el tamaño del equipo y los resultados de entrega.
> - Para una vacante de **arquitectura**: abre con las decisiones de diseño y sus efectos medibles.
> - Para una vacante **generalista**: abre con la combinación de ambas.
>
> En los tres casos el proyecto es el mismo y la métrica es la misma. Solo cambia el orden y el énfasis.

Estructura de datos:

```javascript
const CARTAS = {
  liderazgo: {
    es: { cargo: "[CARGO]", parrafos: ["[P1]", "[P2]", "[P3]"] },
    en: { cargo: "[ROLE]",  parrafos: ["[P1]", "[P2]", "[P3]"] },
  },
  arquitectura: { es: {...}, en: {...} },
  general:      { es: {...}, en: {...} },
};
```

### Anatomía de la carta

Cuatro párrafos, nunca más de una página:

1. **Por qué esta empresa** — algo concreto de ellos. Si no puedes decir nada específico, la carta no
   aporta y es mejor no mandarla.
2. **Qué te hace encajar** — 2 o 3 logros de tu CV, con la cifra, elegidos por relevancia para *esa*
   vacante.
3. **Qué aportas** — traduce tu experiencia al problema que ellos tienen.
4. **Cierre** — disponibilidad y una llamada a la acción breve.

### Renderizado

Lo más práctico es una página HTML con dos grupos de botones (variante e idioma) que re-renderiza al
vuelo, guarda la elección en `localStorage` y trae `@media print` con márgenes para imprimir a PDF.

```css
@page { margin: 16mm; }
@media print { .controles { display: none; } }
```

Genera también una versión `.txt` plana de cada combinación, con encabezado simple (nombre / cargo /
contacto), para los formularios que piden pegar la carta como texto.

### Verificación

- [ ] Cada variante menciona algo específico de la empresa (o queda claro dónde personalizarlo)
- [ ] Las cifras coinciden **exactamente** con las del CV
- [ ] Cabe en una página al imprimir
- [ ] La versión `.txt` no tiene caracteres raros

---

## Parte 2 — LinkedIn como manual de copiar y pegar

LinkedIn no es un documento que se lee: es un formulario que se llena. Así que el entregable de esta parte
no es un texto bonito, sino **un bloque listo para pegar en cada campo**, con la instrucción de dónde va.

Por qué importa: es donde te encuentran. Un CV excelente sin LinkedIn optimizado solo sirve cuando tú
postulas; con LinkedIn optimizado, te buscan.

### Campos, en orden de impacto

**1. Titular (headline) — 220 caracteres.**
Lo que más pesa en las búsquedas de reclutadores. No pongas solo tu cargo actual: pon los cargos que
buscas, separados por barras, más una especialidad.

> *Ej.: "[Cargo objetivo] | [Cargo alterno] | [Especialidad] | [Tecnología clave]"*

**2. Acerca de (about).**
Mismo contenido que el perfil del CV, pero en primera persona y con saltos de línea (LinkedIn corta a las
3 primeras líneas, así que lo importante va arriba). Cierra con una línea de contacto.

**3. Experiencia.**
Los mismos logros del CV. Aquí sí puedes extenderte un poco más que en el papel.

**4. Aptitudes (skills) — hasta 50.**
Ordénalas por relevancia: las 3 primeras son las que se muestran. Deben coincidir con tus
`CORE_KEYWORDS`, porque los reclutadores filtran por ellas.

**5. Configuración que la gente olvida:**
- [ ] URL personalizada (`linkedin.com/in/tu-nombre`, no el número por defecto)
- [ ] "Open to work" configurado — visible solo para reclutadores si sigues empleado
- [ ] Perfil en el idioma secundario (LinkedIn permite versiones por idioma)
- [ ] Foto y banner
- [ ] Sección "Destacado" con el enlace a tu CV web

### Formato del entregable

Un documento donde cada sección es:

```
━━━ TITULAR ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[texto exacto listo para pegar]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dónde: Perfil → Editar introducción → Titular
Límite: 220 caracteres (el tuyo usa [N])
```

La clave es que quien lo use no tenga que decidir nada: abrir, copiar, pegar, siguiente.

### Verificación

- [ ] El titular está por debajo de 220 caracteres
- [ ] Las 3 primeras líneas del "Acerca de" funcionan solas (es lo que se ve sin desplegar)
- [ ] Las aptitudes coinciden con las keywords del CV
- [ ] La URL está personalizada
- [ ] Las fechas de experiencia coinciden con el CV — **esto se verifica en el estudio de seguridad**

---

## Errores frecuentes

**Cartas genéricas.** Una carta que sirve para cualquier empresa no aporta nada. O la personalizas o no la
mandas.

**Inflar en LinkedIn lo que el CV dice distinto.** Las fechas y los cargos se cruzan en la verificación de
antecedentes (Fase 5). Cualquier diferencia hay que poder explicarla.

**Dejar el perfil solo en un idioma** cuando buscas en dos mercados.

**Poner "Open to work" en público estando empleado.** Tu empleador actual lo ve.

**Que el CV web enlazado desde LinkedIn esté desactualizado.** Si lo enlazas, mantenlo.

---

**Siguiente:** [Fase 3 — Preparación de entrevista](04_preparacion_entrevista.md)
