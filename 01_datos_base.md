# Fase 0 — La fuente única de verdad

← [Volver al runbook](00_RUNBOOK.md)

**Qué produce:** un archivo `datos_base.py` con toda tu información profesional, bilingüe, del que salen
todos los demás artefactos.

Es la fase que menos código tiene y más determina el resultado. Si los logros están mal redactados aquí,
van a estar mal en el CV, en la carta, en LinkedIn y en la entrevista.

---

## El principio

Un módulo Python con diccionarios y listas. Sin dependencias, sin lógica. Cada campo con texto visible
lleva las dos versiones de idioma:

```python
{"es": "Líder Técnico", "en": "Technical Lead"}
```

Y un helper que resuelve el idioma:

```python
def t(data, lang="es"):
    """Extrae el idioma de un dict bilingüe. Si no es dict, lo devuelve tal cual."""
    if isinstance(data, dict) and ("es" in data or "en" in data):
        return data.get(lang, data.get("es", ""))
    return data
```

Los nombres técnicos (Docker, PostgreSQL) **no se traducen**: van como cadena simple.

Arranca copiando [`plantillas/datos_base.py`](plantillas/datos_base.py), que ya trae el esquema completo
con marcadores.

---

## El esquema, campo por campo

### `PERSONAL`
```python
PERSONAL = {
    "name": "[TU NOMBRE COMPLETO]",
    "title": {"es": "[TU TÍTULO PROFESIONAL]", "en": "[YOUR TITLE]"},
    "location": "[CIUDAD, PAÍS]",
    "phone": "[+XX XXX XXX XXXX]",
    "email": "[tu@correo.com]",
    "linkedin": "[linkedin.com/in/tu-perfil]",
}
```

El **título** es lo primero que lee un reclutador. Que sea el cargo al que aspiras, no necesariamente el
que tienes. Si apuntas a varios roles, usa el patrón de barras: *"Líder Técnico | Arquitecto de
Soluciones | Backend"* — cubre tres búsquedas distintas.

### `PROFILE`
Un párrafo de 4 a 6 líneas por idioma. Se admite `**negrita**` estilo Markdown; los generadores lo
convierten al formato de cada salida.

Estructura que funciona: **qué eres + años + dominio** → **el logro más grande, con cifra** → **stack
principal** → **qué aportas**.

> *Ej.: "Ingeniero con [N] años en [DOMINIO], especializado en [ÁREA]. Lideré [PROYECTO GRANDE] logrando
> [MÉTRICA]. Manejo [3-4 TECNOLOGÍAS PRINCIPALES]. Combino [FORTALEZA A] con [FORTALEZA B]."*

### `KEY_METRICS`
Cuatro métricas para la barra de impacto de la cabecera. Son las cifras que quieres que se queden en la
cabeza del que lee.

```python
KEY_METRICS = {"es": [
    {"value": "[N]+",   "label": "[años de experiencia]"},
    {"value": "[N]",    "label": "[personas lideradas]"},
    {"value": "[N%]",   "label": "[mejora que lograste]"},
    {"value": "[N]",    "label": "[escala: usuarios, transacciones…]"},
], "en": [ ... ]}
```

Cómo elegirlas: una de **trayectoria** (años), una de **escala** (equipo, usuarios, volumen), una de
**mejora** (%, tiempo, costo) y una de **alcance** (proyectos, sistemas, países). Deben poder defenderse
si te preguntan de dónde salen.

### `EXPERIENCE`
```python
EXPERIENCE = [
    {
        "company": "[EMPRESA]",
        "period": {"es": "[AÑO] – Presente", "en": "[YEAR] – Present"},
        "role": {"es": "[CARGO]", "en": "[ROLE]"},
        "achievements": {
            "es": ["[LOGRO 1]", "[LOGRO 2]", "[LOGRO 3]"],
            "en": ["[ACHIEVEMENT 1]", ...],
        },
    },
    # de más reciente a más antiguo
]
```

**Cómo redactar un logro.** Esta es la parte que decide entrevistas. La fórmula:

> **verbo de acción** + **qué hiciste** + **cómo o con qué** + **resultado medible**

| ❌ Débil | ✅ Fuerte |
|---|---|
| "Responsable del equipo de desarrollo" | "Lideré un equipo de [N] personas entregando [N] plataformas críticas" |
| "Trabajé con Kubernetes" | "Migré [N] servicios a [PLATAFORMA], logrando despliegues sin downtime" |
| "Mejoré el rendimiento" | "Reduje el tiempo de respuesta de [X] a [Y] bajo alta carga" |
| "Encargado de la calidad" | "Implanté [PRÁCTICA], bajando los defectos en producción un [N%]" |

Reglas prácticas:
- Entre 3 y 5 logros por puesto. Más, nadie los lee.
- El primero es el más fuerte.
- Los puestos de hace más de 10 años se resumen o se agrupan en una entrada de "experiencia previa".
- Si no tienes la cifra exacta, estima con honestidad: *"cerca de un 40%"* es defendible; inventar un
  número preciso que no puedes sustentar, no.

### `TECHNICAL_SKILLS`
Lista de tuplas `(nombre, nivel)` con nivel de 1 a 5. **No bilingüe.**

```python
TECHNICAL_SKILLS = [
    ("[TECNOLOGÍA 1]", 5),
    ("[TECNOLOGÍA 2]", 4),
]
```

Escala: **5** = lo defiendes en una entrevista técnica profunda · **4** = lo has usado en producción ·
**3** = lo has usado en proyectos · 1–2 **no van en el CV**.

Sé honesto con el 5: es una invitación a que te pregunten a fondo.

### `EDUCATION`, `CERTIFICATIONS`, `LANGUAGES`
```python
EDUCATION = {"es": [{"degree": "[TÍTULO]", "institution": "[INSTITUCIÓN]", "year": "[AÑO]"}], "en": [...]}
CERTIFICATIONS = {"es": [{"name": "[CERTIFICACIÓN]", "issuer": "[EMISOR]"}], "en": [...]}
LANGUAGES = {"es": [("[IDIOMA]", "[NIVEL]")], "en": [...]}
```

Para idiomas usa el marco europeo (A1–C2) o etiquetas claras (Nativo, Avanzado). Si un título está en
trámite, dilo: *"[TÍTULO] (en trámite de grado)"*. Se verifica, y que aparezca como terminado cuando no lo
está es un problema en el estudio de seguridad (Fase 5).

### `CORE_KEYWORDS`
Lista plana de términos para los filtros automáticos.

```python
CORE_KEYWORDS = {"es": ["[CARGO]", "[TECNOLOGÍA]", "[METODOLOGÍA]", ...], "en": [...]}
```

Cómo construirla: toma **8 o 10 ofertas reales** del puesto que buscas, extrae los términos que se repiten
y quédate con los que puedas sustentar. Incluye variantes y siglas (`Kubernetes` y `K8s`, `CI/CD` e
`Integración Continua`) porque los filtros hacen coincidencia literal.

Entre 30 y 50 términos. No inventes: si el filtro te pasa por una palabra que no puedes defender, el
problema aparece en la entrevista.

### `SECTION_TITLES`
Los rótulos de las secciones, bilingües. Van en los datos y no en los generadores, para que los
generadores queden sin una sola palabra de contenido.

---

## Verificación

Antes de pasar a la Fase 1:

```bash
python3 -c "import datos_base; print('sintaxis OK')"

# comprobar que no falta ningún idioma
python3 - <<'PY'
import datos_base as d
faltan = []
for nombre in dir(d):
    if nombre.startswith('_'): continue
    v = getattr(d, nombre)
    if isinstance(v, dict) and ('es' in v or 'en' in v):
        if not v.get('es') or not v.get('en'):
            faltan.append(nombre)
print("Campos incompletos:", faltan or "ninguno")
PY
```

Lista de control:

- [ ] Todo campo bilingüe tiene sus dos idiomas
- [ ] Ningún `[MARCADOR]` sin reemplazar
- [ ] Cada logro tiene una cifra o un resultado concreto
- [ ] Las 4 métricas de cabecera se pueden sustentar si te preguntan
- [ ] Las keywords salen de ofertas reales, no de tu imaginación
- [ ] Ningún nivel 5 que no puedas defender en profundidad

---

## Errores frecuentes

**Escribir el contenido en el generador.** En cuanto un texto visible aparece dentro de un script, empieza
la desincronización. Todo va en los datos.

**Traducir literalmente.** Los cargos y las certificaciones tienen nombre propio en cada mercado. No es
traducción, es adaptación.

**Logros sin métrica.** Es el problema más común y el más costoso. Si no puedes medir un logro, replantéalo
hasta encontrar el ángulo medible.

**Listar todo lo que has tocado.** Un CV con 40 tecnologías no dice "sé mucho", dice "no sé qué es
importante". Deja las que quieres que te pregunten.

---

**Siguiente:** [Fase 1 — CV multiformato](02_cv_multiformato.md)
