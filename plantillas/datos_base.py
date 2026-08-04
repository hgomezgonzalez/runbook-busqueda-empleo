# -*- coding: utf-8 -*-
"""
Fuente única de verdad del CV.

Reemplaza los [MARCADORES]. No escribas contenido en ningún otro archivo:
todos los generadores leen de aquí.

Convención: los campos con texto visible son dicts {"es": ..., "en": ...}.
Los nombres técnicos (Docker, PostgreSQL) van como cadena simple, no se traducen.
"""


def t(data, lang="es"):
    """Extrae el idioma de un dict bilingüe; si no lo es, devuelve el valor tal cual."""
    if isinstance(data, dict) and ("es" in data or "en" in data):
        return data.get(lang, data.get("es", ""))
    return data


# --------------------------------------------------------------------------
# Datos de contacto
# --------------------------------------------------------------------------
PERSONAL = {
    "name": "[NOMBRE COMPLETO]",
    "title": {
        "es": "[CARGO AL QUE ASPIRAS] | [CARGO ALTERNO] | [ESPECIALIDAD]",
        "en": "[TARGET ROLE] | [ALTERNATE ROLE] | [SPECIALTY]",
    },
    "location": "[CIUDAD, PAÍS]",
    "phone": "[+00 000 000 0000]",
    "email": "[correo@ejemplo.com]",
    "linkedin": "[linkedin.com/in/tu-perfil]",
}

PHOTO_PATH = "datos/foto_perfil.jpg"   # ruta relativa; deja "" si no usas foto


# --------------------------------------------------------------------------
# Perfil profesional — 4 a 6 líneas. Admite **negrita**.
# Estructura: qué eres + años + dominio → mayor logro con cifra → stack → aporte
# --------------------------------------------------------------------------
PROFILE = {
    "es": (
        "[PROFESIÓN] con [N] años de experiencia en [DOMINIO/SECTOR], especializado en "
        "[ÁREA DE ESPECIALIDAD]. Lideré [PROYECTO MÁS IMPORTANTE] logrando **[MÉTRICA]**. "
        "Manejo [TECNOLOGÍA 1], [TECNOLOGÍA 2] y [TECNOLOGÍA 3]. "
        "Combino [FORTALEZA A] con [FORTALEZA B] para [RESULTADO QUE APORTAS]."
    ),
    "en": (
        "[PROFESSION] with [N] years of experience in [DOMAIN], specialized in [AREA]. "
        "Led [MAIN PROJECT] achieving **[METRIC]**. Skilled in [TECH 1], [TECH 2] and [TECH 3]. "
        "I combine [STRENGTH A] with [STRENGTH B] to [VALUE YOU BRING]."
    ),
}


# --------------------------------------------------------------------------
# Barra de impacto — 4 cifras memorables y defendibles
# Recomendado: trayectoria · escala · mejora · alcance
# --------------------------------------------------------------------------
KEY_METRICS = {
    "es": [
        {"value": "[N]+",  "label": "[años de experiencia]"},
        {"value": "[N]",   "label": "[personas lideradas]"},
        {"value": "[N]%",  "label": "[mejora lograda]"},
        {"value": "[N]",   "label": "[escala: usuarios/transacciones]"},
    ],
    "en": [
        {"value": "[N]+",  "label": "[years of experience]"},
        {"value": "[N]",   "label": "[people led]"},
        {"value": "[N]%",  "label": "[improvement achieved]"},
        {"value": "[N]",   "label": "[scale]"},
    ],
}


# --------------------------------------------------------------------------
# Experiencia — de más reciente a más antigua.
# Logro = verbo + qué hiciste + con qué + resultado medible.
# 3 a 5 logros por puesto; el primero, el más fuerte.
# --------------------------------------------------------------------------
EXPERIENCE = [
    {
        "company": "[EMPRESA ACTUAL]",
        "period": {"es": "[AÑO] – Presente", "en": "[YEAR] – Present"},
        "role": {"es": "[CARGO]", "en": "[ROLE]"},
        "achievements": {
            "es": [
                "[Verbo] [qué hiciste] con [tecnología/método], logrando [MÉTRICA].",
                "[Verbo] [alcance: equipo/sistemas] entregando [RESULTADO CONCRETO].",
                "[Verbo] [mejora] reduciendo [MÉTRICA] de [X] a [Y].",
            ],
            "en": [
                "[Verb] [what you did] using [tech], achieving [METRIC].",
                "[Verb] [scope] delivering [CONCRETE RESULT].",
                "[Verb] [improvement] reducing [METRIC] from [X] to [Y].",
            ],
        },
    },
    {
        "company": "[EMPRESA ANTERIOR]",
        "period": {"es": "[AÑO] – [AÑO]", "en": "[YEAR] – [YEAR]"},
        "role": {"es": "[CARGO]", "en": "[ROLE]"},
        "achievements": {
            "es": ["[LOGRO 1]", "[LOGRO 2]"],
            "en": ["[ACHIEVEMENT 1]", "[ACHIEVEMENT 2]"],
        },
    },
    # Lo de hace más de 10 años: agrúpalo en una sola entrada de "Experiencia previa".
]


# --------------------------------------------------------------------------
# Proyectos propios / destacados (opcional pero diferencia mucho)
# --------------------------------------------------------------------------
PROJECTS = {
    "es": [
        {"name": "[NOMBRE]", "desc": "[Qué resuelve] construido con [stack]. [Resultado o estado]."},
    ],
    "en": [
        {"name": "[NAME]", "desc": "[What it solves] built with [stack]. [Result or status]."},
    ],
}


# --------------------------------------------------------------------------
# Habilidades técnicas — (nombre, nivel 1-5). No bilingüe.
# 5 = lo defiendes a fondo · 4 = producción · 3 = proyectos. 1-2 no van.
# --------------------------------------------------------------------------
TECHNICAL_SKILLS = [
    ("[TECNOLOGÍA PRINCIPAL]", 5),
    ("[TECNOLOGÍA PRINCIPAL 2]", 5),
    ("[TECNOLOGÍA]", 4),
    ("[TECNOLOGÍA]", 4),
    ("[TECNOLOGÍA]", 3),
]

SOFT_SKILLS = {
    "es": ["[HABILIDAD 1]", "[HABILIDAD 2]", "[HABILIDAD 3]"],
    "en": ["[SKILL 1]", "[SKILL 2]", "[SKILL 3]"],
}


# --------------------------------------------------------------------------
# Formación
# --------------------------------------------------------------------------
EDUCATION = {
    "es": [
        {"degree": "[TÍTULO]", "institution": "[INSTITUCIÓN]", "year": "[AÑO]"},
        # En trámite: {"degree": "[TÍTULO] (en trámite de grado)", ...}
    ],
    "en": [
        {"degree": "[DEGREE]", "institution": "[INSTITUTION]", "year": "[YEAR]"},
    ],
}

CERTIFICATIONS = {
    "es": [{"name": "[CERTIFICACIÓN]", "issuer": "[EMISOR]"}],
    "en": [{"name": "[CERTIFICATION]", "issuer": "[ISSUER]"}],
}

LANGUAGES = {
    "es": [("[IDIOMA]", "[Nativo / C1 / B2]")],
    "en": [("[LANGUAGE]", "[Native / C1 / B2]")],
}


# --------------------------------------------------------------------------
# Keywords para filtros automáticos (ATS)
# Sácalas de 8-10 ofertas reales del puesto que buscas.
# Incluye variantes y siglas: la coincidencia es literal.
# Solo términos que puedas defender. 30-50 en total.
# --------------------------------------------------------------------------
CORE_KEYWORDS = {
    "es": [
        "[CARGO OBJETIVO]", "[CARGO ALTERNO]",
        "[TECNOLOGÍA]", "[SIGLA DE ESA TECNOLOGÍA]",
        "[METODOLOGÍA]", "[ÁREA DE CONOCIMIENTO]",
    ],
    "en": [
        "[TARGET ROLE]", "[ALTERNATE ROLE]",
        "[TECHNOLOGY]", "[ACRONYM]",
        "[METHODOLOGY]", "[KNOWLEDGE AREA]",
    ],
}


# --------------------------------------------------------------------------
# Rótulos de sección — aquí para que los generadores no tengan texto
# --------------------------------------------------------------------------
SECTION_TITLES = {
    "profile":        {"es": "Perfil Profesional",   "en": "Professional Profile"},
    "metrics":        {"es": "Logros Clave",         "en": "Key Achievements"},
    "keywords":       {"es": "Competencias Clave",   "en": "Core Competencies"},
    "experience":     {"es": "Experiencia Profesional", "en": "Professional Experience"},
    "projects":       {"es": "Proyectos",            "en": "Projects"},
    "skills":         {"es": "Competencias Técnicas", "en": "Technical Skills"},
    "soft_skills":    {"es": "Habilidades Blandas",  "en": "Soft Skills"},
    "education":      {"es": "Formación Académica",  "en": "Education"},
    "certifications": {"es": "Certificaciones",      "en": "Certifications"},
    "languages":      {"es": "Idiomas",              "en": "Languages"},
}
