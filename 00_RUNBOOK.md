# Runbook: sistema de búsqueda de empleo para perfiles técnicos

Procedimiento estándar para montar, de punta a punta, el material y las herramientas de una búsqueda de
trabajo seria: CV en varios formatos, presencia web, preparación de entrevistas, postulación y respuesta
al proceso de contratación.

Está escrito para alguien que **usa terminal, Python y git**. No explica qué es una terminal.

---

## Por qué un sistema y no un archivo de Word

La búsqueda de empleo produce mucho más material del que parece: el CV tiene al menos tres versiones
distintas que deben decir lo mismo, cada vacante pide una carta con otro énfasis, LinkedIn quiere el mismo
contenido en otro formato, la entrevista exige tener respuestas listas, y si te seleccionan te piden
veinte o treinta documentos en una semana.

Hacerlo a mano tiene dos costos: **se desincroniza** (corriges una cifra en el CV en español y se te
olvida en el inglés) y **se vuelve lento justo cuando necesitas ser rápido**.

La idea central del sistema es una sola:

> **Una fuente de datos. Muchos renderizados.**

Escribes tu experiencia una vez, en un solo archivo, y de ahí salen el CV diseñado, el CV para robots, el
CV web, las cartas y el guion de LinkedIn. Corriges en un sitio y se propaga a todo.

---

## Mapa de fases

| Fase | Archivo | Qué produce | Depende de |
|---|---|---|---|
| 0 | [`01_datos_base.md`](01_datos_base.md) | Tu fuente única de verdad | — |
| 1 | [`02_cv_multiformato.md`](02_cv_multiformato.md) | CV diseñado, CV ATS, CV web, foto | Fase 0 |
| 2 | [`03_cartas_y_linkedin.md`](03_cartas_y_linkedin.md) | Cartas por cargo/idioma, perfil LinkedIn | Fase 0 |
| 3 | [`04_preparacion_entrevista.md`](04_preparacion_entrevista.md) | Guía de estudio, banco de preguntas, simulador | Fase 0 |
| 4 | [`05_postulacion.md`](05_postulacion.md) | Postulaciones enviadas + tabla de seguimiento | Fases 1 y 2 |
| 5 | [`06_contratacion_documentos.md`](06_contratacion_documentos.md) | Paquete documental listo para enviar | — (arranca cuando te seleccionan) |

Anexos:
- [`ANEXO_A_recetas_tecnicas.md`](ANEXO_A_recetas_tecnicas.md) — las recetas que cuestan trabajo descubrir:
  comprimir PDFs sin arruinarlos, foto sin fondo, diligenciar formatos `.docx`, componer una firma.
- [`ANEXO_B_checklists.md`](ANEXO_B_checklists.md) — listas de verificación para usar el día de.

---

## Cronograma sugerido

No hagas todo a la vez. Este orden entrega valor desde el primer día:

**Semana 1 — poder postular**
1. Fase 0 completa. Es la que más piensa y menos teclea. Sal de aquí con logros redactados con métrica.
2. Fase 1, solo la **versión ATS**. Es la que aceptan todos los portales.
3. Empieza a postular ya (Fase 4). No esperes a tenerlo todo bonito.

**Semana 2 — subir la tasa de respuesta**
4. Fase 1 completa: versión diseñada, CV web y foto.
5. Fase 2: cartas y LinkedIn. LinkedIn es donde te encuentran los reclutadores.

**Semana 3 en adelante — convertir entrevistas**
6. Fase 3, en paralelo con las postulaciones. Se construye por temas, no de un tirón.

**Cuando te seleccionen**
7. Fase 5. Suele venir con plazo de días, así que conviene haber leído el archivo antes de necesitarlo.

---

## Requisitos previos

```bash
python3 --version          # 3.9 o superior
python3 -m pip install python-docx pillow numpy
```

| Herramienta | Para qué | Alternativa |
|---|---|---|
| `python-docx` | Generar y diligenciar `.docx` | — |
| LibreOffice | Convertir `docx → pdf` sin abrir Word | Exportar a PDF desde Word/Pages a mano |
| Pillow + numpy | Procesar la foto de perfil | Herramienta web de quitar fondo |
| git + cuenta GitHub | Publicar el CV web con Pages | Netlify, Vercel, o no publicar |
| Navegador con automatización | Llenar formularios largos | Llenarlos a mano con el guion delante |

Conversión a PDF por línea de comandos:

```bash
soffice --headless --convert-to pdf --outdir . CV_ATS_ES.docx
```

Si LibreOffice no está en el `PATH`, en macOS suele estar en
`/Applications/LibreOffice.app/Contents/MacOS/soffice`.

---

## Las 10 reglas del sistema

Estas reglas salieron de errores concretos. Cada una evita un problema real.

**1. Nunca declares experiencia que el CV no respalde.**
Es la regla dura. Si una vacante pide una tecnología que no has operado, no la insinúes: prepara el guion
honesto (está en la Fase 3). Inventar experiencia en una entrevista técnica se detecta en dos preguntas, y
ahí pierdes la vacante y la credibilidad. Decir *"no lo he usado en producción, pero conozco el modelo y
estas son las equivalencias con lo que sí manejo"* es una respuesta fuerte, no una debilidad.

**2. Una fuente de verdad.**
Ningún dato de contenido se escribe dentro de un generador. Si tienes que corregir la misma cifra en dos
archivos, el sistema está mal montado.

**3. La versión ATS es un artefacto de primera clase.**
No es "el CV feo". Es el que leen los filtros automáticos, y por lo tanto el que decide si un humano te
ve. Se diseña aparte, con sus propias reglas.

**4. Verifica el canal antes de enviar.**
Los correos institucionales publicados en las páginas oficiales se caen y nadie actualiza la web. Antes de
mandar algo importante, confirma que la dirección existe. Si te rebota, llama y documenta la dirección
vigente.

**5. Separa lo que preparas de lo que solo tú puedes hacer.**
Las plataformas con sesión iniciada, los datos de identidad y el envío final son tuyos. Todo lo demás se
puede preparar por adelantado. Cada guion de postulación debe terminar con una sección explícita de "esto
lo haces tú".

**6. Conserva acuse de todo.**
Captura de pantalla del formulario enviado, copia del correo, número de radicado. Cuando un proceso se
alarga tres meses, tu memoria no sirve como prueba.

**7. Cada logro lleva una métrica.**
"Mejoré el rendimiento" no dice nada. "Reduje el tiempo de respuesta un 40%" sí. Si no tienes el número
exacto, estima con honestidad y usa un orden de magnitud.

**8. Verifica en el medio real.**
El CV se revisa en PDF, no en el editor. La web se revisa en el móvil, no solo en el escritorio. El
documento comprimido se revisa abriéndolo, no mirando su tamaño.

**9. Documenta lo que NO funcionó.**
Cuando un enfoque falla, escribe por qué. Ese es el conocimiento que no vuelves a construir. Los anexos de
este runbook son, en su mayoría, callejones sin salida ya recorridos.

**10. Empieza a postular antes de tenerlo perfecto.**
El sistema se mejora con las respuestas del mercado. Un CV ATS decente enviado hoy vale más que un sistema
completo la semana entrante.

---

## Estructura de trabajo recomendada

```
busqueda-empleo/
  datos/
    datos_base.py              # fuente única (Fase 0)
    foto_original.jpg
  generadores/                 # los scripts que escribes en las Fases 1 y 2
  salidas/
    CV_ATS_ES.{docx,pdf,txt}
    CV_ATS_EN.{docx,pdf,txt}
    CV_DISENADO_ES.{docx,pdf}
    cartas/
  entrevista/
    guia.html                  # Fase 3
  postulaciones/
    seguimiento.md             # tabla de control (Fase 4)
  procesos/                    # una carpeta por proceso de contratación (Fase 5)
    <proceso-1>/
      LISTA_DOCUMENTOS.md
      documentos/
      comprimido/
```

Dos advertencias sobre esta carpeta:

- **No la subas a un repo público.** Contiene tu documento de identidad, dirección y datos familiares. Si
  usas git, que sea un repo privado, y publica solo la carpeta del CV web.
- **Separa el código de los documentos personales.** Si algún día quieres compartir tus generadores, no
  querrás estar filtrando tu cédula del historial de git.

---

## Cómo usar este runbook

Cada archivo de fase tiene la misma estructura:

- **Qué produce** — el artefacto concreto al terminar.
- **Procedimiento** — los pasos.
- **Verificación** — cómo saber que quedó bien.
- **Errores frecuentes** — lo que sale mal y por qué.

Los marcadores `[ASÍ]` son tuyos para rellenar. Donde hacía falta un ejemplo, va uno neutro en cursiva.
