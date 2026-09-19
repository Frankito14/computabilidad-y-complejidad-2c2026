### Clase MTU

#### Codificacion:
Ej:
- M = < { 1 }, { 1, 0 }, 0, { p, q, r }, p, δ, { } >
  - { 1 } = Alfabeto de entrada
  - { 1, 0} = Alfabeto de la cinta
  - 0 = Simbolo blnco
  - { p, q, r} = Cojunto de estados
  - p = Estado inicial de M
  - δ = Conjunto de transiciones
  - { } = Conjunto de estados finales.

La idea es codificar esa M en binario

Símbolos:
- 0 = 0; 1 = 1 -> {1, 0} (Alfabeto de la cinta)
Estados:
- p = 00, q = 01, r = 10 (Estados de M)
Movimientos:
- L = 1, R = 0

#### Notacion simbolos:
- "*" = Donde esta el cabezal
- "$" = Estado donde estoy + Lo que esta leyendo / donde esta parado (001) -> p1
- "#" = Transiciones
    - #0111000
    - 011 -> Estado actual (Estado 01 leyendo un 1)
    - 10 -> Estado al que voy a pasar
    - 0 -> Lo que voy a escribir
    - 0 -> Muevo a derecha
- 001 -> Busca las transiciones que empeizan con 001

#### Ejemplo completo:

Codificacion completa de una Maquina de Turing M para ser procesada por una MTU:

101*01$001#0000100#0010011#0100011#0111000#1000110#10100001

101*01 = Cinta y posicion del cabezal
 - 101 = Lo que esta detras del cabezal
 - *01 = * representa el cabezal, el primer simbolo a la derecha representa sobre donde esta parado el cabezal (0) y 1 lo que sigue a la derechx

 $001 = Indica el estado y valor actual.
 - 00 = Esta en el estado 00
 - 1 = Esta leyendo el bit 1

 #0111000 = Representacion de las transiciones
    - 01 -> Estado actual
    - 1 -> Lo que estoy leyendo
    - 10 -> Estado al que voy a pasar
    - 0 -> Lo que voy a escribir
    - 0 -> A donde me voy a mover (Izquierda)

#### Paso a paso:

101*11$001#0000100#0010011#0100011#0111000#1000110#10100001

C1: 101*01$001#0000100#0010011#0100011#0111000#1000110#10100001
- Cinta: 101*01
- Estado: 00(1)
- Proximo: 00(1) -> 00(1) (Izquierda)
- Nota: *0 deberia ser *1 porque $001 dice que estoy sobre un 1

C2: 10*111$001#0000100#0010011#0100011#0111000#1000110#10100001
- Cinta: 10*111
- Estado: 00(1)
- Proximo: 00(1) -> 00(1) (Izquierda)

C3: 1*0111$000#0000100#0010011#0100011#0111000#1000110#10100001
- Cinta: 1*0111
- Estado: 00(0)
- Proximo: 00(0) -> 01(0) (Derecha)

C4: 10*111$011#0000100#0010011#0100011#0111000#1000110#10100001
- Cinta: 10*111
- Estado: 01(1)
- Proximo: 01(1) -> 10(0) (Derecha)

C5: 100*11$011#0000100#0010011#0100011#0111000#1000110#10100001


