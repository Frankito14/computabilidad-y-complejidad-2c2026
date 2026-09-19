<div align="center">

# 💻 Computabilidad y Complejidad

**Universidad Nacional de Hurlingham**  
*2° Cuatrimestre 2026*

---

</div>

<br/>

<div align="center">
  <img src="./banner.jpg" alt="Banner Computabilidad y Complejidad" width="100%">
</div>

---

## 📂 Índice de tareas

| Tarea | Descripción | Enlace |
| :---: | :--- | :---: |
| **T1** | Trabajo práctico 1: Científicos | [Ver carpeta](./T1/) |
| **T2** | Trabajo práctico 2: Máquinas de Turing | [Ver carpeta](./T2/) |
| **T3** | Trabajo práctico 3: Máquinas de Turing con distitos lenguajes| [Ver carpeta](./T3/) |
| **T4** | Trabajo práctico 4: Máquinas de Turing Calculables| [Ver carpeta](./T4/) |
| **T5** | Trabajo práctico 4: Máquinas de Turing Universal| [Ver carpeta](./T5/) |


---

## Tarea 1: Científicos

 **Recursos adicionales:** 
 - [Carpeta T1](./T1/) 
 - [Hoja de Cálculo en Google Drive](https://docs.google.com/spreadsheets/d/19Bz7HpqyY465uTSSMZl_xUvJH9eviDKqdAx2mwPVTQA/edit?usp=sharing)

<br/>

<table>
  <tr>
    <td width="240" align="center" valign="top">
      <img src="./T1/retrato.webp" alt="Kurt Friedrich Gödel" width="200" style="border-radius: 6px;">
    </td>
    <td valign="top">
      <h3>Kurt Friedrich Gödel</h3>
      <p><b>Profesión:</b> Lógico, matemático y filósofo</p>
      <ul>
        <li><b>Fechas:</b> 28/04/1906 – 14/01/1978</li>
        <li><b>Nacionalidad:</b> Checoslovaca, Austriaca, Estadounidense</li>
        <li><b>Educación:</b> Universidad de Viena (Tesis: <i>Über die Vollständigkeit des Logikkalküls</i>)</li>
        <li><b>Aporte principal:</b> Teoremas de incompletitud (1931)</li>
      </ul>
    </td>
  </tr>
</table>

### Aportes y conceptos asociados
- Teoremas de completitud e incompletitud
- Numeración de Gödel
- Teoría de conjuntos de Von Neumann-Bernays-Gödel
- Métrica de Gödel y Universo constructible

### Reconocimientos
- **Premio Albert Einstein (1951):** Por grandes contribuciones en ciencias naturales.
- **Medalla Nacional de Ciencia (1974):** Galardón en ciencias físicas.

### Aplicación en Ciencias de la Computación
Su trabajo establece un límite fundamental sobre los sistemas formales:
- **Problema de la detención:** Alan Turing se basó en los teoremas de Gödel para demostrar las limitaciones de los algoritmos.
- **Inteligencia Artificial:** Define el alcance y los límites deductivos de los sistemas basados en reglas y axiomas (p. ej., Prolog).

-  **Curiosidad:** Padecía una paranoia obsesiva a ser envenenado y solo consumía alimentos preparados por su esposa Adele. Durante una hospitalización prolongada de ella en 1977, Gödel se rehusó a comer, lo que provocó su fallecimiento por desnutrición.

---

# Tarea 2: Maquina de Turing

 **Recursos adicionales:** 
 - [Carpeta T2](./T2/) 

## Maquina
<img src="./T2/MT.png" alt="Maquina de Turing que duplica cantidad de unos"  />

### Ejemplos
<img src="./T2/inputs.png" alt="Distintos inputs"  />

#### Input "1"
<img src="./T2/11.png" alt="Input 11" />

#### Input "11"
<img src="./T2/21.png" alt="Input 11" />

#### Input "111"
<img src="./T2/31.png" alt="Input 111"/>

#### Input "1111"
<img src="./T2/41.png" alt="Input 1111" />

#### Input "11111"
<img src="./T2/51.png" alt="Input 11111" />

---

# Tarea 3: Maquinas de Turing con distintos lenguajes

 **Recursos adicionales:** 
 - [Carpeta T3](./T3/) 

## MTAccept vs MTCalc
| Característica | MTAccept (Reconocedora) | MTCalc (Calculadora) |
| :--- | :--- | :--- |
| **Objetivo** | Decidir si una palabra es válida o no. | Calcular un resultado o función matemática. |
| **Resultado** | Un estado de aceptación o rechazo. | Una cadena nueva escrita en la cinta. |
| **Parada de éxito** | Estado final.| Al terminar la computación. |
| **Contenido final** | Lo que queda en la cinta no importa. | Lo que queda en la cinta es la respuesta. |
| **Ejemplo** | Validar si la palabra tiene igual número de O y A. | Duplicar la cantidad de unos de la cinta |

## 1. MT Lenguaje Regular 
- _L = { B O O* C A }_
- Objetivo: Reconocer la palabra escrita en la cinta

### Definición Formal
*M = ⟨ Γ, Σ, □, Q, q0, F, δ ⟩*
- _Γ  = { B, O, C, A, □}_
- _Σ = { B, O, C, A }_
- □ ∈ Γ
- _Q = { q0, q1, q2, q3, q4 }_
- _q0 ∈ Q (Estado inicial)_
- _F = { q4 }_ 
- _δ = Q x Γ → Q x Γ { L, R, S }_


<img src="https://github.com/Frankito14/computabilidad-y-complejidad-2c2026/blob/main/T3/MT_AC_LF_BOCA.png?raw=true" alt="Maquina de Turing Lenguaje regular"  />

### Tabla de transiciones
| **Estado** | **B** | **O** | **C** | **A** | **□** |
| :---   | :---       | :---       | :---      | :---       | :--- |
| > q0   | (q1, B, R) | -          | -         | -          | - |
| q1     | -          | (q2, O, R) | -         | -          | - |
| q2     | -          | (q2, O, R) | (q3, C, R)| -          | - |
| q3     | -          | -          | -         | (q4, A, S) | - |
| *q4    | -          | -          | -         | -          | - |


### Ejemplos
<img src="https://github.com/Frankito14/computabilidad-y-complejidad-2c2026/blob/main/T3/MT_AC_FAIL.png?raw=true" />

> "BCA" No es una palabra valida en mi lenguaje. *Rechazado*

<img src="https://github.com/Frankito14/computabilidad-y-complejidad-2c2026/blob/main/T3/MT_AC_SUCCESS.png?raw=true" />

> "BOOOCA" es una palabra valida en mi lenguaje. *Aceptado*

## 2. MT Lenguaje Regular (CALC)
- _L = { B O O* C A }_
- Objetivo: Escribir la palabra "BOCA" con tantas O segun "1" ingresados

> Ejemplos: 111 -> BOOOCA; 1 -> BOCA; 
   
### Definición Formal
*M = ⟨ Γ, Σ, □, Q, q0, F, δ ⟩*
- _Γ  = { B, O, C, A, □}_
- _Σ = { B, O, C, A }_
- □ ∈ Γ
- _Q = { q0, q1, q2, q3, q4 }_
- _q0 ∈ Q (Estado inicial)_
- _F = { q4 }_ 
- _δ = Q x Γ → Q x Γ { L, R, S }_


<img src="https://github.com/Frankito14/computabilidad-y-complejidad-2c2026/blob/main/T3/MT_CALC_LF_BOCA.png?raw=true" alt="Maquina de Turing Lenguaje regular"  />

### Tabla de transiciones
| **Estado** | **1** | **□** |
| :---   | :---       | :---       |  
| > q0   | (q1, B, R) | -          |
| q1     | (q1, O, R) | (q2, O, R) | 
| q2     | -          | (q3, C, R) |
| q3     | -          | (q4, A, R) |
| *q4    | -          | -          |


### Ejemplos
<img src="https://github.com/Frankito14/computabilidad-y-complejidad-2c2026/blob/main/T3/MT_CALC_INPUT.png?raw=true" />

> Se ingresa "1111", se espera que el resultado sea "BOOOOCA" 

<img src="https://github.com/Frankito14/computabilidad-y-complejidad-2c2026/blob/main/T3/MT_CALC_SUCCESS.png?raw=true" />

> El resultado fue "BOOOOCA"

## 3. MT Lenguaje Incontextual (ACCEPT)
- _L = { B Oⁿ C Aⁿ | n >= 1 }_
- Objetivo: Reconocer si palabra "BOCA" tiene la misma cantidad de "O" que de "A"
- "BOOOCAAA" ✅
- "BOOOCA" ❌
 
   
### Definición Formal
*M = ⟨ Γ, Σ, □, Q, q0, F, δ ⟩*
- _Γ  = { B, O, C, A, □, x, y }_
- _Σ = { B, O, C, A }_
- □ ∈ Γ
- _Q = { q0, q1, q2, q3, q4, q5 }_
- _q0 ∈ Q (Estado inicial)_
- _F = { q5 }_ 
- _δ = Q x Γ → Q x Γ { L, R, S }_


<img src="https://github.com/Frankito14/computabilidad-y-complejidad-2c2026/blob/main/T3/MT_AC_LIC.png?raw=true" alt="Maquina de Turing Lenguaje regular"  />

### Tabla de transiciones
| **Estado** | **B** | **O** | **C** | **A** | **□** | **x** | **y** |
| :---   | :---       | :---       | :---      | :---       | :--- | :--- | :--- |
| > q0   | (q1, B, R) | -          | -         | -          | - | - | - |
| q1     | -          | (q2, x, R) | (q4, C, R)         | -          | - | - | - |
| q2     | -          | (q2, O, R) | (q2, C, R)| (q3, y, L)         | - | - | (q2, y, R) |
| q3     | -          | (q3, O, L) | (q3, C, L)|  | - | (q1, x, R) | (q3, y, L) |
| q4    | -          | -          | -         | -          | (q5, □, S) | - | (q4, y, R)|
| *q5    | -          | -          | -         | -          | - | - | - |



### Ejemplos
<img src="https://github.com/Frankito14/computabilidad-y-complejidad-2c2026/blob/main/T3/MT_AC_LIC_1_INITIAL.png?raw=true" />
<img src="https://github.com/Frankito14/computabilidad-y-complejidad-2c2026/blob/main/T3/MT_AC_LIC_1_FINAL.png?raw=true" />

> La palabra "BOOCAA" es valida porque tiene la cantidad de caracteres "A" = cantidad de caracteres "O"

<img src="https://github.com/Frankito14/computabilidad-y-complejidad-2c2026/blob/main/T3/MT_AC_LIC_2_INITIAL.png?raw=true" />
<img src="https://github.com/Frankito14/computabilidad-y-complejidad-2c2026/blob/main/T3/MT_AC_LIC_2_FINAL.png?raw=true" />

> La palabra "BOOCA" NO es valida porque la cantidad de caracteres "A" es distinta a la cantidad de caracteres "O"

## MTAccept vs MTCalc
| Característica | MTAccept (Reconocedora) | MTCalc (Calculadora) |
| :--- | :--- | :--- |
| **Objetivo** | Decidir si una palabra es válida o no. | Calcular un resultado o función matemática. |
| **Resultado** | Un estado de aceptación o rechazo. | Una cadena nueva escrita en la cinta. |
| **Parada de éxito** | Estado final.| Al terminar la computación. |
| **Contenido final** | Lo que queda en la cinta no importa. | Lo que queda en la cinta es la respuesta. |
| **Ejemplo** | Validar si la palabra tiene igual número de O y A. | Duplicar la cantidad de unos de la cinta |

---

## 🛠️ Recursos

- [JFLAP - Formal Languages and Automata Package](https://www.jflap.org/)