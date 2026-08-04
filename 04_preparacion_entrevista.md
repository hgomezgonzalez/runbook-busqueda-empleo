# Fase 3 — Preparación de entrevista

← [Volver al runbook](00_RUNBOOK.md) · Requiere [Fase 0](01_datos_base.md)

**Qué produce:** una guía de estudio propia, un glosario de tu CV, un banco de preguntas con respuestas
trabajadas y un simulador cronometrado.

Esta fase se construye **por temas y en paralelo con las postulaciones**, no de un tirón. Un tema por
sesión, empezando por lo que más aparece en las ofertas a las que aplicas.

---

## El diagnóstico que ahorra tiempo

La mayoría de las entrevistas técnicas no se pierden por no saber, sino por **no saber contarlo**. Se
sabe hacer el trabajo, pero al explicarlo en voz alta bajo presión sale desordenado, sin cifras y sin la
palabra que el entrevistador espera oír.

Por eso el objetivo de esta fase no es aprender tecnología nueva: es **convertir lo que ya sabes en
frases que puedes decir**.

---

## 1. El formato: un solo archivo HTML

Un `guia.html` autocontenido, sin dependencias, que abres en el móvil. Suena rudimentario y es
justamente la ventaja: funciona sin conexión, en la sala de espera, cinco minutos antes.

Componentes que valen la pena, en orden de utilidad:

| Componente | Para qué |
|---|---|
| **Chuleta** | Lo que repasas en el ascensor: pitch de 20 s y tus 4 métricas |
| **Cursos por tema** | El material de estudio |
| **Glosario de tu CV** | Que ninguna palabra que escribiste te sorprenda |
| **Banco de preguntas** | Respuestas ya trabajadas |
| **Simulador** | Practicar con cronómetro |

---

## 2. El patrón de un tema

Cada tema sigue **siempre la misma estructura**. La repetición es deliberada: cuando todos los temas se
leen igual, estudiar es más rápido y se nota enseguida lo que falta.

```
1. Una frase de para qué sirve esta pieza
2. Analogía cotidiana        ← lo que te salva cuando te piden explicárselo a alguien de negocio
3. Los conceptos que debes distinguir   (tarjetas: nombre + rol en una frase + definición)
4. Cómo funciona / cómo se despliega    (bloque de código o diagrama)
5. El dato que demuestra profundidad    ← el detalle que separa a quien lo usó de quien lo leyó
6. "Cómo lo cuentas tú"                 ← frase en primera persona, CON MÉTRICA
7. Preguntas típicas del tema           (pregunta plegable + respuesta modelo)
```

**El punto 6 es el que importa.** Todo tema termina en una frase que puedes decir tal cual:

> *"Diseñé [QUÉ] con [TECNOLOGÍA]: [DECISIÓN TÉCNICA] y [OTRA DECISIÓN], logrando [MÉTRICA]."*

Si no puedes escribir esa frase para un tema, es que no lo dominas todavía — o que no tienes experiencia
real en él, que es información igual de útil.

---

## 3. El glosario de tu propio CV

Sencillo y muy rentable: **toma cada término técnico que escribiste en tu CV y escribe una frase que lo
explique**.

```
[TÉRMINO DEL CV]  →  [una frase clara de qué es y por qué lo usaste]
```

Objetivo declarado: que no exista ni una palabra en tu CV que, si te la preguntan, te haga dudar. Es
donde más se cae la gente: mencionan una tecnología en el CV porque la tocaron una vez, y no pueden
sostener dos preguntas sobre ella.

Si al escribir el glosario descubres que no puedes explicar algo → **quítalo del CV o baja su nivel**.

---

## 4. Banco de preguntas

Preguntas plegables con respuesta modelo, agrupadas por bloque:

- Encaje y motivación (cuéntame de ti, por qué esta empresa, por qué cambias)
- Liderazgo y equipo, con método STAR
- Técnicas por tecnología
- Arquitectura y diseño de sistemas
- Clásicas de RR.HH. (debilidad, dónde te ves, expectativa salarial)
- **Preguntas que TÚ haces al final** — se olvidan y pesan

### El método STAR y las 3 historias

Para las preguntas de comportamiento: **S**ituación → **T**area → **A**cción (lo que hiciste tú) →
**R**esultado (medible).

El truco que ahorra trabajo: **prepara 3 historias fuertes** y comprueba que con ellas puedes responder
casi cualquier pregunta de comportamiento. Un proyecto difícil que sacaste adelante, una situación de
conflicto o presión, y un caso donde aprendiste de un error. Con esas tres cubres el 80%.

### El guion honesto para lo que no dominas

Esto merece su propia sección porque es donde más gente se estrella.

Cuando pregunten por una tecnología que no has usado en producción, la respuesta que funciona es:

> *"En producción trabajo con [LO QUE SÍ USAS]. [LO QUE PREGUNTAN] no lo he operado en un proyecto real,
> pero conozco su modelo: [2 o 3 conceptos con sus equivalencias]. Como el grueso del trabajo es
> [FUNDAMENTOS COMPARTIDOS], la curva es corta."*

Funciona porque demuestra tres cosas a la vez: honestidad, que entiendes el fondo y no solo la marca, y
capacidad de aprender. **Inventar experiencia se detecta en dos preguntas** — basta con que te pregunten
por un detalle operativo, un error típico o el precio.

### La técnica de homologación

Cuando una vacante pide un stack que no manejas pero es análogo a uno que sí:

1. Haz una **tabla de equivalencias** entre lo que sabes y lo que piden.
2. Identifica las **3 o 4 diferencias reales** (no de nombre, sino de concepto). Esas son las que
   demuestran que entendiste.
3. Prepara un **ejemplo lado a lado**: el mismo procedimiento en ambos, para mostrar qué es portable.

En una semana pasas de "no lo conozco" a poder sostener una conversación técnica con honestidad. No te
convierte en experto y no debes presentarlo como tal, pero evita que te descarten por vocabulario.

---

## 5. Simulador

Una mini-app en JS, sin backend, dentro del mismo HTML. Practicar con cronómetro cambia el resultado:
responder en frío es muy distinto a leer la respuesta.

Esquema de cada pregunta:

```javascript
{
  cat:   "[categoría]",
  q:     "[la pregunta]",
  hint:  "[pista de por dónde arrancar]",
  good:  "[qué suma en la respuesta]",
  watch: "[qué te van a cuestionar]",
  level: "[cómo subir el nivel]",
  model: "[respuesta modelo]",
  sets:  ["all", "tech"],     // para filtrar por tipo de práctica
  time:  120                   // segundos sugeridos
}
```

Flujo: eliges el set → aparece la pregunta con el **cronómetro corriendo** y un campo para esbozar la
respuesta → "Ver evaluación" revela la rúbrica de 3 criterios (suma / te cuestionan / cómo subir) y la
respuesta modelo → siguiente.

Conjuntos útiles: `completo`, `rápido` (5 preguntas), `técnico`, `diseño de sistemas`, `liderazgo`.

Arranca con [`plantillas/banco_preguntas.md`](plantillas/banco_preguntas.md), que trae las categorías y
las preguntas más frecuentes con la respuesta en blanco.

---

## 6. Assessments

Muchos procesos incluyen pruebas más allá de la entrevista. Conviene tener una sección por tipo:

- **Diseño de sistemas** — con un método repetible: aclarar requisitos → estimar → diseño de alto nivel →
  profundizar en 1 o 2 componentes → cuellos de botella y trade-offs. No buscan la respuesta correcta,
  buscan cómo piensas.
- **Prueba de código** (en vivo o para casa) — practica hablando mientras programas.
- **Psicométricos** — no se estudian, pero saber qué miden baja la ansiedad.
- **Assessment center** — dinámicas de grupo, role-play.

---

## Verificación

- [ ] Puedes decir tu pitch de 30 segundos sin leerlo, terminando con una cifra
- [ ] Cada término de tu CV está en el glosario
- [ ] Tienes 3 historias STAR que cubren la mayoría de preguntas de comportamiento
- [ ] Cada tema termina en una frase en primera persona con métrica
- [ ] Tienes preparado el guion honesto para las tecnologías que no dominas
- [ ] Tienes 3 preguntas para hacerle tú al entrevistador
- [ ] La guía abre y se lee bien **en el móvil**

---

## Errores frecuentes

**Estudiar tecnología en vez de practicar la respuesta.** Sabes más de lo que crees; lo que falla es
contarlo.

**No practicar en voz alta.** Leer la respuesta y decirla son habilidades distintas. La primera vez que
digas algo no debería ser en la entrevista.

**Respuestas sin cifras.** Vale para la entrevista igual que para el CV.

**No preparar preguntas para el final.** "No, ninguna" es una mala respuesta: parece desinterés.

**Preparar solo lo técnico.** Muchos procesos se caen en la conversación de RR.HH. o en la expectativa
salarial, no en la parte técnica.

---

**Siguiente:** [Fase 4 — Postulación](05_postulacion.md)
