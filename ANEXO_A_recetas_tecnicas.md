# Anexo A — Recetas técnicas

← [Volver al runbook](00_RUNBOOK.md)

Procedimientos concretos que cuestan tiempo descubrir. Cada uno incluye **qué no funciona y por qué**, que
suele ser lo más útil.

Dependencias comunes:

```bash
python3 -m pip install pymupdf pillow numpy python-docx
```

---

## 1. Comprimir PDFs sin arruinarlos

**Problema:** un paquete de documentos escaneados pesa 30 MB y el límite de correo son 25 MB.

### La regla que casi nadie aplica

**Antes de comprimir, mira si el PDF tiene capa de texto.** Los PDF generados digitalmente (facturas,
certificados electrónicos, tu propio CV) ya están comprimidos de forma óptima. Rasterizarlos:

- destruye el texto seleccionable,
- empeora la calidad visual,
- y **muchas veces los agranda**.

```python
import fitz  # pymupdf

def tiene_texto(ruta, umbral=200):
    doc = fitz.open(ruta)
    chars = sum(len(p.get_text().strip()) for p in doc)
    doc.close()
    return chars > umbral
```

Si devuelve `True`: **déjalo como está**.

### Comprimir los escaneos

```python
import fitz

def comprimir_escaneo(entrada, salida, lado_max=1800, calidad=60):
    """Re-renderiza cada página como JPEG. Solo para PDF SIN capa de texto."""
    src = fitz.open(entrada)
    dst = fitz.open()
    for page in src:
        rect = page.rect
        escala = min(lado_max / max(rect.width, rect.height), 4.0)
        pix = page.get_pixmap(matrix=fitz.Matrix(escala, escala), colorspace=fitz.csRGB)
        nueva = dst.new_page(width=rect.width, height=rect.height)
        nueva.insert_image(rect, stream=pix.tobytes("jpeg", jpg_quality=calidad))
    dst.save(salida, deflate=True, garbage=4)
    dst.close(); src.close()
```

Valores de referencia: **1800 px** de lado mayor y **calidad 60** dan documentos perfectamente legibles con
un 70–80% menos de peso. Para texto muy pequeño, sube a 2000 px.

### Calidad diferenciada por página

Si el documento tiene una página de puro texto y otra con firma o huella, no las trates igual:

```python
CALIDADES = {0: 60, 1: 95}   # pág 1 texto · pág 2 firma y huella
calidad = CALIDADES.get(numero_pagina, 70)
```

Sale **más pequeño y con mejor calidad donde importa** que aplicar una calidad media a todo.

### La regla anti-crecimiento

Comprobación obligatoria al final:

```python
import os
if os.path.getsize(salida) >= os.path.getsize(entrada):
    os.remove(salida)          # el original era mejor
```

Pasa más de lo que parece, sobre todo con archivos ya optimizados.

### Verificación

**Abre el resultado y léelo.** No mires solo el tamaño. Comprueba específicamente:

- [ ] Los números de documento se leen sin dudar
- [ ] La letra pequeña (pies de página, notas legales) es legible
- [ ] Firmas y sellos conservan sus trazos
- [ ] Ninguna página salió en blanco o rotada

### Alternativas

```bash
# Ghostscript (multiplataforma)
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -sOutputFile=salida.pdf entrada.pdf
```

`/ebook` es el ajuste equilibrado; `/screen` comprime más y a veces de más.

---

## 2. Medir si la compresión arruinó lo importante

Una media de calidad sobre el documento entero no dice nada: lo que importa es **la zona crítica**. Mide
el PSNR solo ahí.

```python
import fitz, numpy as np

def psnr_zona(orig, comp, pagina, rect, dpi=150):
    """PSNR de una región concreta. rect = fitz.Rect(x0, y0, x1, y1) en puntos."""
    def region(ruta):
        d = fitz.open(ruta)
        pix = d[pagina].get_pixmap(clip=rect, dpi=dpi, colorspace=fitz.csRGB)
        a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
        d.close()
        return a.astype(np.float64)
    a, b = region(orig), region(comp)
    if a.shape != b.shape:
        return None
    mse = np.mean((a - b) ** 2)
    return 99.0 if mse == 0 else 10 * np.log10(255 ** 2 / mse)
```

Interpretación:

| PSNR | Veredicto |
|---|---|
| ≥ 45 dB | Sin pérdida perceptible |
| 40–45 dB | Muy buena, sirve para firmas y huellas |
| 35–40 dB | Aceptable para texto |
| < 35 dB | Degradada: sube la calidad |

Es una guía, no un juez. **La comprobación final siempre es mirar el resultado ampliado.**

---

## 3. Foto de perfil: cambiar el fondo

**El paso que casi todos omiten** no es recortar: es limpiar el borde.

Al recortar un sujeto, los píxeles del contorno son una **mezcla** del sujeto con el fondo original. Si
solo cambias el fondo, esos píxeles conservan el color viejo y aparece un **halo** — un contorno claro
alrededor del pelo que delata el recorte. Sobre fondo blanco no se nota; sobre cualquier color, sí.

### Procedimiento

1. **Segmentar** el sujeto (herramienta web, `rembg`, o la función de "quitar fondo" del sistema).
2. **Descontaminar el borde**: para cada píxel semitransparente, estimar el color del fondo *local* y
   despejar el color real del sujeto:

   ```
   color_real = (color_observado − fondo × (1 − alfa)) / alfa
   ```

   El fondo local se estima difuminando la imagen ponderada por `(1 − alfa)`. Un color global no basta si
   el fondo original no era uniforme, que es lo normal en una foto casera.
3. **Componer** sobre el fondo nuevo.

Con `rembg`, que ya hace parte de esto:

```bash
python3 -m pip install rembg pillow
python3 -c "
from rembg import remove
from PIL import Image
img = Image.open('foto_original.jpg')
Image.alpha_composite(
    Image.new('RGBA', img.size, (30, 80, 140, 255)),   # fondo azul
    remove(img).convert('RGBA')
).convert('RGB').save('foto_perfil.jpg', quality=95)
"
```

### Versión 3×4 para formatos oficiales

```python
from PIL import Image
img = Image.open("foto_perfil.jpg")
w, h = img.size
lado = min(w, int(h * 3 / 4))
img.crop(((w - lado) // 2, 0, (w + lado) // 2, int(lado * 4 / 3))) \
   .resize((600, 800), Image.LANCZOS).save("foto_3x4.jpg", quality=95)
```

### Verificación

- [ ] **Amplía el borde del pelo al 300%**: no debe haber contorno claro
- [ ] Componla sobre un color fuerte (magenta) para ver los defectos
- [ ] No se comieron mechones ni partes de los hombros

---

## 4. Diligenciar un `.docx` conservando el formato

**Problema:** la empresa manda un formato Word con tablas y hay que rellenarlo sin romper el diseño.

### Inspeccionar antes de escribir

Nunca asumas la estructura. Las tablas de formularios están llenas de celdas combinadas:

```python
import docx
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
doc = docx.Document("formato.docx")

for ti, tabla in enumerate(doc.tables):
    print(f"--- Tabla {ti}: {len(tabla.rows)} filas ---")
    for ri, fila in enumerate(tabla.rows):
        celdas = fila._tr.tc_lst
        info = []
        for ci, tc in enumerate(celdas):
            txt = ''.join(n.text or '' for n in tc.iter() if n.tag == W + 't')
            span = tc.find('.//' + W + 'gridSpan')
            merge = tc.find('.//' + W + 'vMerge')
            marca = ''
            if span is not None:  marca += ' [combinada-h]'
            if merge is not None: marca += ' [combinada-v]'
            info.append(f"[{ci}]{marca} {txt[:40]!r}")
        print(f"  fila {ri}: {len(celdas)} celdas :: " + " | ".join(info))
```

Una fila puede tener 2 o 3 celdas según las combinaciones. **Escribir en el índice equivocado destroza el
formato.**

### Escribir conservando el estilo

La clave: **escribir sobre el `run` que ya existe**, no crear uno nuevo. El run existente lleva la fuente,
el tamaño y el color del formato original.

```python
def escribir(celda, texto):
    for p in celda.paragraphs[1:]:              # limpia párrafos sobrantes
        p._element.getparent().remove(p._element)
    p = celda.paragraphs[0]
    if p.runs:
        p.runs[0].text = texto                  # reutiliza el formato
        for r in list(p.runs[1:]):
            r._element.getparent().remove(r._element)
    else:
        p.add_run(texto)
```

### Replicar bloques

Cuando el formato trae 4 bloques de "empleo" y necesitas 7:

```python
import copy

def clonar_filas(tabla, desde, hasta, veces=1):
    """Clona un rango de filas y lo añade al final, con bordes y estilo."""
    plantilla = [copy.deepcopy(tabla.rows[i]._tr) for i in range(desde, hasta)]
    for _ in range(veces):
        for tr in plantilla:
            tabla._tbl.append(copy.deepcopy(tr))
```

Al clonar el XML se heredan bordes, sombreado y tipografía. Reconstruir la fila a mano nunca queda igual.

### Verificación

Vuelve a abrir el archivo generado y **vuelca las tablas completas**, comprobando que cada valor quedó en
su celda y que ninguna etiqueta se sobrescribió. Después ábrelo en Word: python-docx puede producir
archivos que se abren mal si se manipuló mal el XML.

---

## 5. Extraer texto de PDFs escaneados

```python
import fitz
doc = fitz.open("documento.pdf")
for i, page in enumerate(doc):
    texto = page.get_text().strip()
    print(f"pág {i+1}: {len(texto)} caracteres")
```

**Si devuelve 0 caracteres, es una imagen.** Opciones:

1. **Leerlo tú** (o pedirle a un asistente con visión que lo lea) tras renderizarlo:

   ```python
   page.get_pixmap(dpi=200).save(f"pagina_{i}.png")
   ```

2. **OCR**, si necesitas el texto en máquina:

   ```bash
   python3 -m pip install pytesseract   # requiere tesseract instalado
   ```

Para un puñado de documentos, renderizar y leer es más rápido y fiable que montar OCR.

---

## 6. Componer una firma o una huella sobre un documento

**Caso:** tienes el formulario en digital (nítido, ligero) y la firma o la huella solo existen en un
escaneo del papel.

Vale la pena decirlo: esto es legítimo cuando es **tu propia firma sobre tu propio documento** — es lo
mismo que hace cualquier herramienta de firma electrónica. Si el destinatario espera ver el escaneo del
original firmado a mano, manda el escaneo.

### Las tres reglas

**1. No remuestrees la huella.** Las crestas están al límite de resolución; ampliarlas genera moiré y las
destruye. Extrae los píxeles originales:

```python
import fitz
doc = fitz.open("escaneo.pdf")
for img in doc[1].get_images(full=True):
    pix = fitz.Pixmap(doc, img[0])       # píxeles reales, sin reescalar
    pix.save("huella_cruda.png")
```

**2. Calcula el alfa en vez de recortar a mano.** Para que se integre sin parche visible, el fondo del
papel debe volverse transparente y la tinta opaca:

```python
import numpy as np
from PIL import Image

a = np.array(Image.open("huella_cruda.png").convert("L")).astype(float)
papel = np.percentile(a, 93)      # nivel del papel
piso  = np.percentile(a, 0.4)     # tinta más densa
v = np.clip((a - piso) / max(papel - piso, 1) * 255, 0, 255)
rgba = np.zeros((*a.shape, 4), dtype=np.uint8)
rgba[..., 3] = (255 - v).astype(np.uint8)   # negro con alfa = densidad
Image.fromarray(rgba).save("huella.png")
```

Sobre fondo blanco reproduce exactamente los grises originales.

**3. No rasterices el documento base.** Superpón la imagen sin convertir la página a mapa de bits, para
que el texto siga siendo texto:

```python
import fitz
doc = fitz.open("formulario.pdf")
doc[1].insert_image(fitz.Rect(x0, y0, x1, y1), filename="huella.png")
doc.save("formulario_firmado.pdf")
```

### Ubicar el recuadro con precisión

En vez de estimar a ojo, extrae los rectángulos dibujados en el PDF:

```python
for d in doc[1].get_drawings():
    r = d["rect"]
    if 60 < r.width < 200 and 60 < r.height < 200:
        print(f"candidato: x={r.x0:.1f} y={r.y0:.1f} w={r.width:.1f} h={r.height:.1f}")
```

Respeta la **proporción** de la huella al colocarla, o quedará deformada y se nota.

### Verificación

- [ ] La huella cae dentro del recuadro, sin tocar los bordes
- [ ] No arrastra fondo gris ni el borde del recuadro del escaneo
- [ ] El texto del documento sigue siendo seleccionable
- [ ] Ampliada al 300%, las crestas siguen separadas

---

## 7. Publicar en GitHub Pages y verificar

```bash
git add index.html
git commit -m "docs: actualiza CV"
git push origin main
```

Activar: **Settings → Pages → Source: rama `main`**. Queda en
`https://<usuario>.github.io/<repo>/`.

**Verificación en vivo.** Pages tarda 1–3 minutos y el navegador cachea con ganas — comprobar sin
cache-busting es la causa número uno de "no se actualizó":

```bash
for i in $(seq 1 20); do
  if curl -s -H 'Cache-Control: no-cache' "https://<usuario>.github.io/<repo>/?v=$i" | grep -q "[MARCA_NUEVA]"; then
    echo "publicado"; break
  fi
  sleep 10
done
```

Donde `[MARCA_NUEVA]` es algo que solo exista en la versión nueva (una fecha de despliegue visible, un
`id` nuevo). Poner un sello de fecha en la página facilita mucho esta comprobación.

---

← [Volver al runbook](00_RUNBOOK.md) · [Checklists](ANEXO_B_checklists.md)
