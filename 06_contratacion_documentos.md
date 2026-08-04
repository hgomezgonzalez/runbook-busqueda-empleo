# Fase 5 — Proceso de contratación

← [Volver al runbook](00_RUNBOOK.md)

**Qué produce:** un paquete documental completo, organizado y dentro del límite de tamaño, listo para
enviar.

Esta fase arranca cuando te seleccionan. **Suele llegar con plazo de días**, así que conviene haber leído
esto antes de necesitarlo.

---

## Qué va a pasar

Cuando pasas las entrevistas, casi siempre hay una etapa de verificación: un **estudio de seguridad**
(propio o de una consultora externa) que confirma que eres quien dices y que tu trayectoria es real.

Te van a pedir, en una sola tanda y con poco tiempo:

- Formatos propios de la empresa, diligenciados y firmados
- Documento de identidad, y a veces libreta militar o pasaporte
- Diplomas y actas de grado
- **Certificaciones laborales de cada empleo**, con fechas y cargo
- Historial de aportes a pensión
- Afiliaciones vigentes de salud, pensión y cesantías
- Referencias personales y laborales con teléfono
- Comprobante de domicilio
- A veces documentos familiares

---

## Anticípate: la carpeta permanente

Lo más rentable de esta fase es hacer **hoy** lo que te van a pedir después. Ten una carpeta con lo que ya
puedas reunir, aunque no estés en ningún proceso:

```
documentos-personales/
  identidad/          # documento, pasaporte, libreta militar
  educacion/          # diplomas y actas de cada nivel
  laboral/            # una certificación por empleo
  certificaciones/    # cursos y certificaciones técnicas
  seguridad-social/   # salud, pensión, cesantías, historial de aportes
  domicilio/          # comprobante reciente
```

**Pide las certificaciones laborales cuando sales de una empresa, no años después.** Es la que más
problemas da: las áreas de RR.HH. tardan, la gente que te conocía se fue, y algunas empresas
sencillamente ya no existen.

---

## El índice: la pieza clave del método

El entregable no es una carpeta con archivos sueltos: es una **carpeta con su índice**. Ese documento
mapea cada requisito con el archivo que lo satisface, y es lo que hace que quien revisa no tenga que
adivinar.

Usa [`plantillas/LISTA_DOCUMENTOS.md`](plantillas/LISTA_DOCUMENTOS.md).

### Convención de nombres

Numeración por familias, de modo que el orden alfabético sea el orden lógico:

```
1. Hoja de vida.pdf
2. Documento de identidad.pdf
3.1 Certificacion laboral - [EMPLEO 1].pdf
3.2 Certificacion laboral - [EMPLEO 2].pdf
5. Acta de grado.pdf
9.1 Certificacion [TEMA].pdf
10.1 Afiliacion salud.pdf
10.2 Afiliacion pension.pdf
```

Sin tildes ni caracteres especiales en los nombres: algunos portales de carga los rompen.

### El semáforo

En el índice, cada documento con su estado y **cómo conseguirlo**:

| # | Documento | Estado | Cómo obtenerlo |
|---|---|---|---|
| 1 | [Documento] | 🟢 Tengo | — |
| 2 | [Documento] | 🟡 Diligenciar | Formato de la empresa, firmar |
| 3 | [Documento] | 🔴 Solicitar | Escribir a [entidad], tarda [N] días |

Sirve para dos cosas: saber por dónde empezar, y poder decirle a la empresa con precisión qué falta y
cuándo llega.

---

## Cuando un documento no se puede conseguir

Pasa más de lo que parece, y **la solución nunca es callarse**. Se aporta el sustituto con una nota que
explique por qué.

| Situación | Qué aportar |
|---|---|
| La empresa ya no existe | Certificado de liquidación o registro mercantil que lo pruebe, más lo que sí tengas: contrato, liquidación, comprobantes de pago |
| RR.HH. no responde | Contrato + comprobantes de aportes a pensión de ese periodo (el historial de aportes es una fuente oficial e independiente) |
| Título en trámite | Certificación de terminación de estudios + carta de compromiso con la fecha en que entregarás el acta |
| Documento en otra ciudad | Dilo y da fecha de entrega |

La nota va en el índice, no en un correo aparte que se pierde.

> *Ej.: "El empleador de [PERIODO] se encuentra liquidado, por lo que no puede expedir certificación
> laboral. Se aporta el auto de liquidación y el historial de aportes correspondiente."*

---

## Diligenciar formatos de la empresa

Suelen mandar un `.docx` o un PDF con tablas. Dos caminos:

**Si es `.docx`:** se puede diligenciar por código conservando el formato original. La receta completa
está en [`ANEXO_A`, receta 4](ANEXO_A_recetas_tecnicas.md#4-diligenciar-un-docx-conservando-el-formato).
Ventaja real: cuando el formato tiene 8 bloques iguales (uno por empleo) y necesitas 12, se replican los
bloques respetando bordes y tipografía.

**Si es PDF:** rellenar a mano, imprimir, firmar y escanear.

**Regla:** nunca dejes un campo en blanco sin explicación. Si algo no aplica, escribe "No aplica". Si
falta un dato, escribe "Pendiente" y avisa. Un campo vacío parece un descuido; uno marcado, una decisión.

---

## Comprimir para enviar

El límite de correo suele ser 25 MB y los portales piden a veces menos de 5 MB por archivo. Un paquete de
escaneos llega fácil a 30 MB.

Receta completa en [`ANEXO_A`, receta 1](ANEXO_A_recetas_tecnicas.md#1-comprimir-pdfs-sin-arruinarlos).
Lo esencial:

- **No re-comprimas los PDF que ya tienen texto** (los generados digitalmente). Rasterizarlos los empeora
  y a veces los agranda.
- **Los escaneos sí**: bajarlos a ~1800 px de lado mayor con calidad JPEG media reduce un 70–80% sin
  perder legibilidad.
- **Si un documento tiene firma o huella, trátalo aparte** con calidad alta. Son detalle fino y se
  destruyen con compresión agresiva.
- **Verifica abriendo el resultado**, no mirando el tamaño. Si no puedes leer un número de documento, no
  sirve.
- Si el resultado pesa más que el original, quédate con el original.

---

## Envío

- [ ] Índice incluido como primer archivo
- [ ] Nombres de archivo sin tildes ni caracteres especiales
- [ ] Todo abre correctamente (ábrelos uno por uno)
- [ ] Peso dentro del límite
- [ ] Asunto del correo con tu nombre y el proceso
- [ ] Copia a ti mismo, para tener acuse con fecha
- [ ] Lo que quede pendiente, dicho explícitamente con fecha de entrega

---

## Coherencia: lo que de verdad revisan

El estudio de seguridad **cruza fuentes**. Antes de enviar, comprueba que estas cuatro cuentan lo mismo:

1. Tu CV
2. El formato que diligenciaste
3. LinkedIn
4. El historial de aportes a pensión

Los puntos donde aparecen diferencias:

- **Fechas de entrada y salida.** Tu CV dice años; el historial de aportes dice meses exactos. Si hay
  diferencia, ten la explicación lista.
- **Periodos solapados.** Dos contratos a la vez es perfectamente normal (consultoría, prestación de
  servicios), pero **te lo van a preguntar**. Ten la respuesta preparada.
- **Vacíos entre empleos.** También te los preguntan. La respuesta honesta —estudiando, proyecto propio,
  búsqueda— sirve; la evasiva, no.
- **Títulos en trámite.** Si el CV dice "Ingeniero" y el acta no existe todavía, se nota. Escribe "en
  trámite de grado" desde el principio.

Ninguno de estos es un problema en sí mismo. **El problema es que te tomen por sorpresa.**

---

## Errores frecuentes

**Empezar a pedir certificaciones cuando ya te las pidieron.** Algunas tardan semanas.

**Enviar sin índice.** Multiplica las idas y vueltas.

**Comprimir sin verificar.** Un documento ilegible es un documento no entregado.

**Ocultar un vacío o un solapamiento.** Se detecta en el cruce y se convierte en un problema de confianza,
que es mucho peor que el hecho en sí.

**Dejar campos en blanco** sin decir por qué.

---

## Anexos relacionados

- [Recetas técnicas](ANEXO_A_recetas_tecnicas.md) — comprimir, diligenciar, firmas y huellas
- [Checklists](ANEXO_B_checklists.md) — la lista de verificación antes de enviar
