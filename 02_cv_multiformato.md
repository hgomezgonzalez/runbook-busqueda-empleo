# Fase 1 — CV en varios formatos

← [Volver al runbook](00_RUNBOOK.md) · Requiere [Fase 0](01_datos_base.md)

**Qué produce:** cuatro artefactos desde los mismos datos — CV ATS, CV diseñado, CV web y foto de perfil.

---

## Por qué tres CV y no uno

No es vanidad. Cada versión la lee algo distinto y las tres son incompatibles entre sí.

| Versión | Quién la lee | Regla de oro |
|---|---|---|
| **ATS** | Un filtro automático | Una columna, sin tablas, sin iconos, sin cajas de texto |
| **Diseñada** | Una persona, en pantalla o impreso | Que se entienda en 20 segundos |
| **Web** | Reclutador que llega por el enlace | Que cargue rápido y se vea bien en móvil |

**El error más caro de esta fase** es mandar la versión diseñada a un portal con filtro automático. Los
parsers no entienden columnas: leen la página de izquierda a derecha y te mezclan la columna de
habilidades con la de experiencia. Tu CV bonito llega como un revoltijo y quedas fuera sin que un humano
te haya visto.

Regla práctica: **portal o formulario → ATS. Correo a una persona → diseñada. Firma y perfiles → web.**

---

## 1. Versión ATS (empieza por esta)

La que te permite postular desde el primer día.

### Restricciones duras

- **Una sola columna.** Nada de layout en paralelo.
- **Sin tablas.** Ni siquiera invisibles para maquetar.
- **Sin iconos, emojis ni glifos** decorativos. Un teléfono se marca con la palabra "Teléfono".
- **Fuente estándar**: Arial, Calibri o Times New Roman.
- **Sin encabezado ni pie de página**: muchos parsers los ignoran, y ahí suele ir el contacto.
- **Sin imágenes**, foto incluida.
- **Fechas en formato consistente**: `MM/AAAA – MM/AAAA` o `AAAA – AAAA`, siempre igual.
- Los títulos de sección, con los nombres que espera el parser: *Experiencia Profesional*, *Formación
  Académica*, *Competencias Técnicas*.

### Generación

Un script `generar_cv_ats.py` que lee `datos_base.py` y produce dos salidas por idioma:

- **`.docx`** con `python-docx`: párrafos planos, sin tablas.
- **`.txt`** plano UTF-8: encabezados en mayúsculas subrayados con `===`, viñetas con `- `. Sirve para
  pegar en formularios que piden el CV en texto.

Funciones auxiliares que vas a necesitar:

```python
def strip_md(texto):
    """Quita el **negrita** de los datos: el ATS no lo necesita."""
    return texto.replace("**", "")

def nivel_a_texto(n):
    """El nivel numérico no le dice nada a un parser; la palabra sí."""
    return {5: "Experto", 4: "Avanzado", 3: "Intermedio"}.get(n, "Básico")

def normalizar_periodo(periodo, lang):
    """Evita que quede 'Presente / Present' en la misma línea."""
    return t(periodo, lang)
```

El PDF **no se genera con Python**: se convierte el `.docx`, así el PDF conserva la estructura de texto
que el parser necesita.

```bash
soffice --headless --convert-to pdf --outdir salidas salidas/CV_ATS_ES.docx
```

### Verificación

La prueba real, que además es gratis: **copia el texto del PDF y pégalo en un editor plano**.

```bash
# si tienes pdftotext (poppler)
pdftotext -layout salidas/CV_ATS_ES.pdf - | head -50
```

Si lo que sale está en orden y completo, el parser lo va a leer bien. Si aparece desordenado o faltan
trozos, tu CV está roto para un ATS aunque se vea perfecto en pantalla.

- [ ] El texto extraído mantiene el orden lógico
- [ ] Nombre, teléfono y correo aparecen en las primeras líneas
- [ ] No hay caracteres raros donde iban viñetas
- [ ] Las fechas se leen completas
- [ ] Cabe en 2 páginas (3 si tienes más de 15 años de trayectoria)

---

## 2. Versión diseñada

Para cuando hay una persona del otro lado: un correo directo, una recomendación, una entrevista impresa.

Estructura que funciona:

```
┌──────────────────────────────────────────┐
│  NOMBRE          Título profesional      │  ← cabecera, opcionalmente con foto
│  contacto · correo · ciudad · linkedin   │
├──────────────────────────────────────────┤
│  PERFIL  (párrafo con fondo suave)       │
├──────────────────────────────────────────┤
│  [N]+ años  │ [N] equipo │ [N]% mejora   │  ← barra de métricas
├──────────────────────────────────────────┤
│  COMPETENCIAS CLAVE (chips de keywords)  │
├──────────────────────────────────────────┤
│  EXPERIENCIA  (una columna, completa)    │
├─────────────────────┬────────────────────┤
│  Proyectos          │  Habilidades       │  ← dos columnas solo abajo
│  Educación          │  Idiomas           │
└─────────────────────┴────────────────────┘
```

Las dos columnas van **solo en el bloque inferior**, con la experiencia a ancho completo. Se implementan
con una tabla sin bordes.

### Separar estilo de contenido

Un módulo `estilos.py` con tokens y componentes, **sin una sola palabra de contenido**:

```python
# tokens
COLOR_PRIMARIO = "1F3355"
COLOR_ACENTO   = "0A7FBD"
FUENTE_TITULO  = "Calibri"
FUENTE_CUERPO  = "Calibri"

# componentes
def add_section_header(doc, texto): ...
def add_experience_entry(doc, empresa, periodo, cargo, logros): ...
def add_metrics_bar(doc, metricas): ...
def add_skill_bar(doc, nombre, nivel): ...
```

Con `python-docx` hay cosas que solo se pueden hacer tocando el XML (sombreado de celda, quitar bordes de
tabla, márgenes internos). Se resuelven con `docx.oxml`:

```python
from docx.oxml.ns import qn
from docx.oxml import parse_xml

def sombrear_celda(celda, hex_color):
    celda._tc.get_or_add_tcPr().append(
        parse_xml(f'<w:shd {{}} w:fill="{hex_color}"/>'.format(
            'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'))
    )
```

### Verificación

- [ ] Se lee bien **en PDF**, no solo en Word (las fuentes cambian al convertir)
- [ ] Impreso en blanco y negro sigue siendo legible
- [ ] Máximo 2 páginas
- [ ] Ningún texto cortado ni columna desbordada

---

## 3. Versión web

Un `index.html` autocontenido: CSS y JS embebidos, sin dependencias externas. Se publica en GitHub Pages
y el enlace va en la firma del correo, en LinkedIn y en el propio CV.

Características que valen la pena:

- **Los dos idiomas en el mismo archivo**, con un botón que alterna. Dos `<article>`, uno oculto, y el
  estado guardado en `localStorage`.
- **Botón de descarga** que apunta al PDF del idioma activo.
- **Responsive de verdad**: la mitad de los reclutadores lo abren en el móvil.
- **`@media print`** para que imprimirlo desde el navegador dé un documento decente.
- **`prefers-color-scheme`** para modo oscuro.

Un generador `generar_cv_html.py` con solo la librería estándar:

```python
import html

def esc(s):
    return html.escape(str(s))

def rich(s):
    """Escapa y convierte **negrita** en <strong>."""
    import re
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html.escape(str(s)))
```

Publicación:

```bash
cd cv-web
git add index.html && git commit -m "docs: actualiza CV" && git push
# Settings → Pages → rama main → queda en https://<usuario>.github.io/<repo>/
```

Verificación en vivo (Pages tarda 1–3 minutos y el navegador cachea):

```bash
curl -s -H 'Cache-Control: no-cache' "https://<usuario>.github.io/<repo>/?v=$RANDOM" | grep -o "<title>.*</title>"
```

### Verificación

- [ ] Abre bien en móvil (prueba con el móvil real, no solo redimensionando)
- [ ] El botón de idioma alterna y persiste al recargar
- [ ] El botón de descarga apunta al PDF correcto en cada idioma
- [ ] Sin scroll horizontal en pantalla estrecha
- [ ] Funciona sin conexión (no debe cargar nada externo)

---

## 4. Foto de perfil

No siempre hace falta, pero cuando la piden conviene tenerla resuelta. La receta técnica completa está en
[`ANEXO_A`, receta 3](ANEXO_A_recetas_tecnicas.md#3-foto-de-perfil-cambiar-el-fondo).

Lo esencial:
- Fondo neutro y uniforme (azul o gris claro son las apuestas seguras).
- Encuadre de pecho hacia arriba, mirando a cámara.
- Ten a mano una versión **3×4 tipo carné**: varios formatos oficiales la piden.
- Si le cambias el fondo, revisa el borde del pelo. Es donde se nota el recorte.

---

## Errores frecuentes

**Mandar la versión diseñada a un portal.** Ya explicado arriba: es el error que más entrevistas cuesta.

**Regenerar solo un idioma.** Cuando cambies los datos, regenera las seis salidas de un tirón. Si no,
tarde o temprano mandas la versión vieja.

**Confiar en que el PDF se ve igual que el Word.** Al convertir cambian fuentes y saltos de página. Revisa
siempre el PDF, que es lo que envías.

**Foto informal o antigua.** Una foto recortada de una foto social se nota, y juega en contra.

**Enlazar un CV web con enlaces rotos.** Si el PDF que enlaza la web no existe o quedó desactualizado, es
peor que no tener web.

---

**Siguiente:** [Fase 2 — Cartas y LinkedIn](03_cartas_y_linkedin.md)
