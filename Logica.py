from Bd import tipos

def calcular_daño(carta_ataque, carta_defensa):
    Ataque = carta_ataque[2] #tomamos el atque y defensa del atacante
    Defensa = carta_ataque[3]

    elemento_ataque = carta_ataque[4]
    elemento_defensa = carta_defensa[4]

    if elemento_ataque in tipos and elemento_defensa in tipos[elemento_ataque]: #comparamos en el diccionario de tipos si hay ventaja
        ventaja = tipos[elemento_ataque][elemento_defensa]
        Ataque += ventaja
        Defensa += ventaja
    
    daño = Ataque #calculamos el daño realizado a la carta defensora
    return daño

def batalla(carta_ataque, carta_defensa):
    daño = calcular_daño(carta_ataque, carta_defensa) #hacemos el calculo del daño

    if daño > 0: #tomamos los elementos de batalla, donde el que gana destruye al otro
        if daño > carta_defensa[3]:
            "Monstruo defensor destruido"
        elif daño == carta_defensa[3]:
            "Ambos montruos son destruidos"
        else:
            diferencia = daño - carta_defensa[3]
            "Atacante pierde puntos de vida igual a la diferencia"
