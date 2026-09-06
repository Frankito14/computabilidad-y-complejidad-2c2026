# Tarea 3: MT de Aceptación y de Transducción

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





