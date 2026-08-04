# Fase 4 — Postulación

← [Volver al runbook](00_RUNBOOK.md) · Requiere [Fase 1](02_cv_multiformato.md) y [Fase 2](03_cartas_y_linkedin.md)

**Qué produce:** postulaciones enviadas y una tabla de seguimiento que te dice qué hacer cada día.

---

## Los canales, por tasa de respuesta

De mayor a menor efectividad real:

| Canal | Comentario |
|---|---|
| **Referido interno** | Con diferencia el mejor. Vale más un mensaje a un conocido que 20 postulaciones a ciegas |
| **Reclutador que te contacta** | Ya te quiere; solo hay que no arruinarlo |
| **Portal de la propia empresa** | Mejor que los agregadores: menos competencia y llega directo |
| **LinkedIn / agregadores** | Volumen alto, respuesta baja. Sirve para descubrir vacantes, no tanto para aplicar |
| **Convocatorias públicas** | Procesos largos y formales, pero muy predecibles y con reglas claras |

**Consecuencia práctica:** antes de aplicar en frío, revisa si conoces a alguien en la empresa. Diez
minutos en LinkedIn cambian tus probabilidades más que veinte formularios.

---

## Formularios largos: el método asistido

Los portales corporativos piden entre 40 y 80 campos, casi todos datos que ya tienes. Llenarlos a mano es
lento y propenso a errores.

Con cualquier herramienta de automatización de navegador —las hay integradas en asistentes de IA, y están
Playwright o Selenium si prefieres escribirlo tú— **el ciclo es siempre el mismo**, y es lo que importa
recordar. Los ejemplos usan una CLI genérica; traduce los verbos a tu herramienta:

```bash
# 1. Ver qué hay en la página (árbol de accesibilidad con referencias)
agent-browser snapshot -i

# 2. Ubicar el campo que buscas
agent-browser snapshot -i | grep -iE "textbox|combobox|Dirección|Teléfono"

# 3. Actuar por referencia
agent-browser fill @e44 "[VALOR]"
agent-browser click @e55
agent-browser check @e51

# 4. Verificar
agent-browser is checked @e51
agent-browser screenshot /tmp/paso1.png
```

### Trampas reales

Estas cuestan tiempo la primera vez:

- **Los desplegables hay que abrirlos antes de poder leer sus opciones.** El snapshot no muestra las
  opciones de un `select` cerrado: primero `click`, luego `snapshot | grep`, y ahí sí eliges.
- **Deja pausas entre acciones.** Un `sleep 1` tras cada clic. Las SPA re-renderizan y las referencias
  `@eNN` cambian.
- **Verifica los checkboxes**, no asumas. `is checked` existe por algo, sobre todo en los de aceptación de
  términos.
- **Las referencias caducan.** Si la página cambió, vuelve a hacer `snapshot`.
- **Captura de pantalla en cada paso importante.** Cuando algo falle, sabrás dónde.
- **Los campos de dirección con autocompletado** exigen escribir y luego seleccionar de la lista: `type`
  seguido de `snapshot` y `click` sobre la opción.

### Cuándo NO automatizar

Hay portales —típicamente los públicos— cuyas SPA exigen **gestos de usuario reales** y rechazan la
interacción automatizada. Ahí el enfoque correcto es distinto y funciona igual de bien:

> **Preparar el guion y llenarlo a mano.**

Se escribe un documento con el **valor exacto para cada campo, en el orden de las pantallas**, y se llena
mirándolo. Se tarda 20 minutos en vez de 5, pero no falla. Y ese guion sirve para siempre: la próxima
convocatoria es copiar y pegar.

El guion debe terminar con una sección explícita:

```
## Solo tú puedes hacer esto
- Iniciar sesión
- Adjuntar los PDF
- Confirmar y enviar
```

---

## Postulación por correo

Cuando el canal es un correo (bancos de hojas de vida, contactos directos):

**Verifica el canal antes de enviar.** Los correos institucionales publicados en las webs oficiales se
caen y nadie actualiza la página. Si te rebota, llama, pregunta la dirección vigente y déjala anotada.

Estructura del correo:

```
Asunto: [Cargo al que aplicas] — [Tu nombre] — [Referencia si la hay]

[Saludo]

[1 párrafo: quién eres y a qué aplicas]
[1 párrafo: por qué encajas, con 2 logros y sus cifras]
[Cierre: disponibilidad + enlace a tu CV web]

[Firma con teléfono, correo, LinkedIn]

Adjunto: CV en PDF (versión ATS)
```

Reglas: el PDF adjunto, no un enlace de Drive (muchos filtros corporativos lo bloquean). Nombre de archivo
claro: `CV_[Nombre]_[Cargo].pdf`. Y una sola página de correo.

---

## Seguimiento

Sin registro, a las tres semanas no sabes dónde aplicaste. Usa
[`plantillas/seguimiento_postulaciones.md`](plantillas/seguimiento_postulaciones.md).

| Campo | Para qué |
|---|---|
| Fecha | Calcular cuándo hacer seguimiento |
| Empresa / Cargo | Identificación |
| Canal | Saber qué canal te funciona |
| Versión de CV y carta enviadas | Poder repetir lo que funcionó |
| Contacto | A quién escribirle |
| Estado | Enviado · Confirmado · Entrevista · Prueba · Oferta · Descartado |
| Próxima acción + fecha | **La columna más importante** |
| Notas | Lo que aprendiste |

**Ritmo de seguimiento:** si a los 7–10 días hábiles no hay respuesta, un correo breve. Uno solo. Si no
responden, sigue tu camino.

**Revisa la tabla al final de cada semana**: cuántas enviaste, cuántas respondieron, por qué canal. Si de
30 postulaciones no hay respuestas, el problema no es el volumen: es el CV, el canal o el encaje.

---

## Verificación antes de cada envío

- [ ] Versión correcta del CV (ATS para portal, diseñada para persona)
- [ ] Nombre de archivo profesional
- [ ] La carta menciona algo concreto de esa empresa
- [ ] Los datos del formulario coinciden con el CV — **se cruzan después**
- [ ] Captura o acuse guardado
- [ ] Registrado en la tabla con su próxima acción

---

## Errores frecuentes

**Aplicar sin leer la oferta.** Se nota, y quema la empresa para futuras vacantes.

**El mismo CV genérico a todo.** Ajustar el título y reordenar keywords según la oferta toma dos minutos y
cambia el resultado.

**No registrar.** Te llaman de una empresa y no recuerdas a qué aplicaste ni con qué versión.

**Volumen sin análisis.** 50 postulaciones sin respuesta no piden más postulaciones, piden revisar el CV.

**Descuidar los datos "de trámite".** La dirección, el estado civil o el nivel educativo que pones en un
formulario se cruzan luego en la verificación de antecedentes. Ten una única fuente para esos datos.

---

**Siguiente:** [Fase 5 — Proceso de contratación](06_contratacion_documentos.md)
