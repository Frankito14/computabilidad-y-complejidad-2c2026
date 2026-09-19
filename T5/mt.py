
#Simulador paso a paso de una Maquina de Turing codificada
BLANCO = '10' 

COD_MOVIMIENTO = {
    "L": '10',
    "R": '01',
    "S": '00',
}

def obtener_entrada(mt):
    """
    Retrona el contenido de la cinta y la posicion del cabezal
    """
    return mt.split('$', 1)[0]


def obtener_estado(mt, ancho_transicion, ancho_valor):
    """
    Retorna una tupla (estado, valor_leido) 
    """
    resto = mt.split('$', 1)[1]            
    segmento_estado = resto.split('#', 1)[0] 

    estado = segmento_estado[:ancho_transicion]
    valor_leido = segmento_estado[ancho_transicion: ancho_transicion + ancho_valor]

    return estado, valor_leido


def obtener_transiciones(mt, ancho_transicion, ancho_valor):
    """
    Devuelve la lista completa de transiciones codificadas
    cada una como un diccionario con sus 5 campos.
    """
    ancho_movimiento = 2
    bloques = mt.split('#')[1:]  
    largo_bloque = 2 * ancho_transicion + 2 * ancho_valor + ancho_movimiento

    transiciones = []
    for bloque in bloques:
        bloque = bloque[:largo_bloque]  

        i = 0
        estado_actual = bloque[i:i + ancho_transicion]; i += ancho_transicion
        leyendo       = bloque[i:i + ancho_valor];       i += ancho_valor
        estado_nuevo  = bloque[i:i + ancho_transicion];  i += ancho_transicion
        escribir      = bloque[i:i + ancho_valor];       i += ancho_valor
        mover         = bloque[i:i + ancho_movimiento]

        transiciones.append({
            "estado_actual": estado_actual,
            "leyendo": leyendo,
            "estado_nuevo": estado_nuevo,
            "escribir": escribir,
            "mover": mover,
        })
    return transiciones


def buscar_transicion_del_estado(transiciones, estado, valor):
    """
    Retorna la transicion que conindice con el estado y valor pasados como parametro 
    """
    for transicion in transiciones:
        if transicion["estado_actual"] == estado and transicion["leyendo"] == valor:
            return transicion
    return None


# Funciones sobre la cinta

def separar_cinta_y_cabezal(entrada, ancho_valor):
    """
    A partir de la cinta codificada con '*' (ej: '101*01')
    Devuelve (lista_de_simbolos, indice_cabezal).
    """
    pos_cabezal = entrada.index('*')
    valor_cinta = entrada[:pos_cabezal] + entrada[pos_cabezal + 1:]

    indice_cabezal = pos_cabezal // ancho_valor
    simbolos = [valor_cinta[i:i + ancho_valor] for i in range(0, len(valor_cinta), ancho_valor)]
    return simbolos, indice_cabezal


def simular_transicion(simbolos, indice_cabezal, transicion, ancho_valor):
    """
    Aplica UNA transicion sobre la cinta:
    Si el cabezal se sale de la cinta actual, se agrega una celda en blanco
    (simulando una cinta infinita).
    Devuelve (nuevos_simbolos, nuevo_indice_cabezal).
    """
    simbolos = list(simbolos)  # copiamos para no pisar la cinta anterior
    simbolos[indice_cabezal] = transicion["escribir"]

    if transicion["mover"] == COD_MOVIMIENTO["L"]:      
        nuevo_indice = indice_cabezal - 1
        if nuevo_indice < 0:
            simbolos.insert(0, BLANCO)
            nuevo_indice = 0
    elif transicion["mover"] == COD_MOVIMIENTO["R"]:                                 
        nuevo_indice = indice_cabezal + 1 
        if nuevo_indice >= len(simbolos):
            simbolos.append(BLANCO)
    else:
        nuevo_indice = indice_cabezal #S

    return simbolos, nuevo_indice


def obtener_codificacion(simbolos, indice_cabezal, estado_nuevo, transiciones):
    """
    Arma de nuevo el string completo 'mt' a partir de:
      - la cinta actual (como lista de simbolos) + posicion del cabezal
      - el nuevo estado
      - las transiciones (que son siempre las mismas, no cambian nunca)
    """
    ancho_valor = len(simbolos[0])
    cinta_bits = "".join(simbolos)
    pos_cabezal = indice_cabezal * ancho_valor
    cinta_con_cabezal = cinta_bits[:pos_cabezal] + "*" + cinta_bits[pos_cabezal:]

    valor_bajo_cabezal = simbolos[indice_cabezal]  # lo que "se lee" ahora, ya movido el cabezal
    segmento_estado = "$" + estado_nuevo + valor_bajo_cabezal

    segmento_transiciones = "".join(
        "#" + t["estado_actual"] + t["leyendo"] + t["estado_nuevo"] + t["escribir"] + t["mover"]
        for t in transiciones
    )

    return cinta_con_cabezal + segmento_estado + segmento_transiciones


# printeo

def mostrar_step(numero_step, mt, estado, valor, transicion):
    """Imprime UNA ejecucion de la MT simulada"""
    cinta = obtener_entrada(mt)

    print(f"#T{numero_step}: {mt}")
    print(f"- Cinta: {cinta}")
    print(f"- Estado actual: {estado}(*{valor})")

    if transicion is None:
        print("- No hay transicion aplicable: la maquina se DETIENE ")
    else:
        if transicion["mover"] == COD_MOVIMIENTO["L"]:
            direccion = "L"
        elif transicion["mover"] == COD_MOVIMIENTO["R"]:
            direccion = "R"
        else:
            direccion = "S"
        print(
            f"- Transicion: δ ({estado}, {valor}) -> "
            f"({transicion['estado_nuevo']}, {transicion['escribir']}, {direccion})"
        )
    print()


# main

def simular_ejecucion(mt, config, steps=5, numero_step=1):
    """
    Simula 'steps' pasos de la maquina de Turing codificada en 'mt',
    imprimiendo cada configuracion (C1, C2, C3, ...) por consola.

    config debe tener las claves:
        "ANCHO_VALOR"      -> cuantos bits ocupa cada simbolo
        "ANCHO_TRANSICION" -> cuantos bits ocupa cada estado
    """
    ancho_valor = config["ANCHO_VALOR"]
    ancho_transicion = config["ANCHO_TRANSICION"]

    entrada = obtener_entrada(mt)
    estado, valor = obtener_estado(mt, ancho_transicion, ancho_valor)
    lista_transiciones = obtener_transiciones(mt, ancho_transicion, ancho_valor)


    transicion = buscar_transicion_del_estado(lista_transiciones, estado, valor)

    mostrar_step(numero_step, mt, estado, valor, transicion)

    if transicion is None or steps <= 1:
        return

    simbolos, indice_cabezal = separar_cinta_y_cabezal(entrada, ancho_valor)
    nuevos_simbolos, nuevo_indice = simular_transicion(simbolos, indice_cabezal, transicion, ancho_valor)

    nueva_codificacion = obtener_codificacion(
        nuevos_simbolos, nuevo_indice, transicion["estado_nuevo"], lista_transiciones
    )

    simular_ejecucion(nueva_codificacion, config, steps - 1, numero_step + 1)


#Programa principal
if __name__ == "__main__":

    print(" Simulador de Maquina de Turing codificada ")

    # Pedir datos de configuracion.
    mt_ingresada = input("Codificacion de la maquina M (con w ya incluido en la cinta): ").strip()
    ancho_valor = int(input("ANCHO_VALOR (bits por simbolo): ").strip())
    ancho_transicion = int(input("ANCHO_TRANSICION (bits por estado): ").strip())
    cantidad_pasos = int(input("Cantidad de pasos a simular: ").strip())
    configuracion = {
        "ANCHO_VALOR": ancho_valor,
        "ANCHO_TRANSICION": ancho_transicion,
    }
    print()
    simular_ejecucion(mt_ingresada, configuracion, steps=cantidad_pasos)

    """
    DATOS DE PRUEBA:
    MT = Sumar 1 bit al numero binario que esta en la cinta (ej: 001 -> 010)
    ### Codificación
    - Simbolos: 0 = 00; 1 = 01; □ = 10
    - Movimientos: 00 = S; 10 = L; 01 = R
    - Estados: q0 = 00; q1 = 01; qf = 10
    - Transiciones: 
    - 00_00_00_00_01: (q0, 0) -> (q0, 0 , R) -> #0000000001
    - 00_01_00_01_01: (q0, 1) -> (q0, 1 , R) -> #0001000101
    - 00_10_01_10_10: (q0, □) -> (q1, □ , L) -> #0010011010
    - 01_00_10_01_00: (q1, 0) -> (qf, 1 , S) -> #0100100100
    - 01_01_01_00_10: (q1, 1) -> (q1, 0 , L) -> #0101010010
    - 01_10_10_01_00: (q1, □) -> (qf, 1 , S) -> #0110100100
    - Ejemplo: *0001$0000#0000000001#0001000101#0010011010#0100100100#0101010010#0110100100
    w = 01
    ANCHO_VALOR = 2
    ANCHO_ESTADO = 2
    ANCHO_MOVIMIENTO = 2
    MT_COD = *0001$0000#0000000001#0001000101#0010011010#0100100100#0101010010#0110100100
    """