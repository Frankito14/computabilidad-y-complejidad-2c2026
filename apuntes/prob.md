### Clase Prob

Los problemas tienen 2 clasificaciones
- Problemas de desicion (SI/NO)
- Problemas de resolucion general
    - Necesita dar una respuesta que no es si/no

Lenguajes:
- alfabeto: Conjunto de simbolos
- alfabeto E = {a, b}
- Sin restricciones -> Lenguaje universal E* = {lamda, a, b, ab, ba}
- Sigma = alfabeto
- Sigma* = Lenguaje universal

L1 = {empiezan con a} -> 1 restriccion (Coloquial)
L1 = {aw / w pertenece a E*} (Simbolica)
L1 = {a, ab, abaa, ...} (Extension)

L2 = {a*b} -> 2 restricciones
L2 = { ab, aab, ababab}

Problemas de desicion:
- ¿ab pertenece a L2?
- ¿L1 incluido en L2?

Siempre se asocia a un lenguaje.

PROBLEMAS SOLUBLES
Descidible -> La maquina va a dar una respuesta y va a frenar
- SIEMPRE TERMINA, HAYA ACEPTADO O RECHAZADO

PROBELMAS INSOLUBLES
- No existe algoritmo, y si existe no termina
- Puede terminar para ciertas entradas pero no para otras

Gramatica ambigua: Misma palabra por 2 caminos. 2 caminos para una misma palabra:

S -> ab | aA
A -> b

-> : Derivo

S => ab
S => aA => ab


Problema de correspondencia de POST:

TESTING DE SOFTWARE -> Problema sin solucion
- Puedo REDUCIR la cantidad de bugs pero no puedo asegurar al 100% que está libre de errores porque mi programa puede recibir infinitas entradas, lo que es imposible de testear.

- 