#Colocaremos cada carta en esta bd, representando sus atributos principales a la par que su ID.
base_datos = {
    0: (0, "Contrato", 1500, 2200, "Tierra"),
    1: (1, "A la deriva mokey mokey", 3000, 100, "Luz"),
    2: (2, "A bao a qu", 2800, 0, "Oscuridad"),
    3: (3, "Abedul ojo de serpiente", 0, 2100, "Fuego"),
    4: (4, "Abeja blindada", 1600, 1200, "Viento")
} #debe llegar maximo hasta 80 cartas

tipos = {
    "Luz": {"Oscuridad": 500},
    "Fuego": {"Bosque": 500},
    "Bosque": {"Viento": 500},
    "Viento": {"Tierra": 500},
    "Tierra": {"Trueno": 500},
    "Agua": {"Fuego": 500} 
} #Elementos contra los que son fuertes (aumenta 500 de ataque/defensa)