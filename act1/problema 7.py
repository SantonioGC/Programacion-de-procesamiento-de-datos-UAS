arboles = ["manzano", "pino", "madroño", "eucalipto", "nogal", "olivo", "almendro"]
encontrar_tabachin = False

for arbol in arboles:
    if arbol == "ficus":
        break
    print(arbol)
    
    if arbol == "tabachin":
        encontrar_tabachin = True

if not encontrar_tabachin:
    print("el arbol Tabachin no esta en la lista.")
