# Runbook de búsqueda de empleo para perfiles técnicos

Procedimiento estándar, de punta a punta, para montar el material y las herramientas de una búsqueda de
trabajo seria: CV en varios formatos, presencia web, preparación de entrevistas, postulación y respuesta
al proceso de contratación.

No es una guía de consejos. Es un **runbook**: cada fase dice qué produce, cómo verificar que quedó bien y
qué sale mal.

> **Empieza por [`00_RUNBOOK.md`](00_RUNBOOK.md).**

---

## La idea

La búsqueda de empleo produce más material del que parece: el CV tiene al menos tres versiones que deben
decir lo mismo, cada vacante pide una carta con otro énfasis, LinkedIn quiere el mismo contenido en otro
formato, y si te seleccionan te piden treinta documentos en una semana.

Hacerlo a mano se desincroniza y se vuelve lento justo cuando necesitas ser rápido. De ahí el principio
que sostiene todo:

> **Una fuente de datos. Muchos renderizados.**

Escribes tu experiencia una vez, en un solo archivo. De ahí salen el CV diseñado, el CV para filtros
automáticos, el CV web, las cartas y el guion de LinkedIn.

---

## Contenido

| Archivo | Qué cubre |
|---|---|
| [`00_RUNBOOK.md`](00_RUNBOOK.md) | Mapa de fases, cronograma y las 10 reglas del sistema |
| [`01_datos_base.md`](01_datos_base.md) | La fuente única de verdad y cómo redactar un logro |
| [`02_cv_multiformato.md`](02_cv_multiformato.md) | CV para filtros automáticos, diseñado, web y foto |
| [`03_cartas_y_linkedin.md`](03_cartas_y_linkedin.md) | Cartas por cargo e idioma, perfil de LinkedIn |
| [`04_preparacion_entrevista.md`](04_preparacion_entrevista.md) | Guía de estudio, banco STAR, simulador |
| [`05_postulacion.md`](05_postulacion.md) | Canales, formularios largos, seguimiento |
| [`06_contratacion_documentos.md`](06_contratacion_documentos.md) | Paquete documental y verificación de antecedentes |
| [`ANEXO_A_recetas_tecnicas.md`](ANEXO_A_recetas_tecnicas.md) | 7 recetas con código: comprimir PDFs, foto sin fondo, diligenciar `.docx`, firmas |
| [`ANEXO_B_checklists.md`](ANEXO_B_checklists.md) | Listas de verificación para el día de |
| [`plantillas/`](plantillas/) | Esquema de datos, índice de documentos, seguimiento, banco de preguntas |

---

## Para quién es

Alguien que usa terminal, Python y git. El runbook no explica qué es una terminal; sí explica por qué no
hay que rasterizar un PDF que ya tiene capa de texto.

Si no programas, el método sigue sirviendo — la parte de estrategia, entrevistas y documentación es
independiente de las herramientas.

## Requisitos

```bash
python3 -m pip install python-docx pymupdf pillow numpy
```

Más LibreOffice para convertir `docx → pdf` sin abrir Word, y una cuenta de GitHub si quieres publicar el
CV web con Pages. Todo está detallado en el runbook.

---

## Tres reglas que ahorran disgustos

**Nunca declares experiencia que el CV no respalde.** Inventar se detecta en dos preguntas. *"No lo he
operado en producción, pero conozco el modelo y estas son las equivalencias con lo que sí manejo"* es una
respuesta fuerte, no una debilidad.

**La versión ATS del CV es un artefacto de primera clase.** No es "el CV feo": es el que leen los filtros
automáticos, y por tanto el que decide si un humano llega a verte. Mandar el CV diseñado a dos columnas a
un portal es el error más caro de todos.

**Empieza a postular antes de tenerlo perfecto.** El sistema se mejora con las respuestas del mercado.

---

## Aviso

Este repositorio contiene **el método, no datos de nadie**. Todos los campos personales están como
marcadores `[ASÍ]`.

Cuando lo apliques, tu carpeta de trabajo sí tendrá documento de identidad, dirección y datos familiares:
**mantenla fuera de cualquier repositorio público.** El runbook lo advierte en cada fase donde aplica.

## Licencia

[MIT](LICENSE) — úsalo, adáptalo y compártelo.
