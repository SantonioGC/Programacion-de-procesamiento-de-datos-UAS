import pandas as pd

#api de simulacion que me acabo de aventar -_-
api = {
    "NVIDIA RTX 4080":             {"fabricante": "NVIDIA",   "categoria": "GPU"},
    "Samsung 990 Pro 1TB":         {"fabricante": "Samsung",  "categoria": "SSD"},
    "Corsair Vengeance DDR5 32GB": {"fabricante": "Corsair",  "categoria": "RAM"},
    "Intel Core i7-13700K":        {"fabricante": "Intel",    "categoria": "CPU"},
    "AMD Ryzen 9 7950X":           {"fabricante": "AMD",      "categoria": "CPU"},
    "Logitech G502":               {"fabricante": "Logitech", "categoria": "Mouse"},
}

df = pd.read_csv("csv/inventario_hardware.csv")

resultados = []
for producto in df["producto"]:
    datos = api.get(producto, {}).copy()
    resultados.append(datos)

df_api = pd.DataFrame(resultados)

df_final = pd.concat([df, df_api], axis=1)

df_final.fillna("Desconocido", inplace=True)
df_final.to_csv("csv/inventario_enriquecido.csv", index=False)

print(df_final.head(3))