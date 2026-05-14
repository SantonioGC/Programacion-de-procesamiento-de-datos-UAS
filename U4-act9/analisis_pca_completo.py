import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#1 configurar una semilla para que los datos sean reproducibles
np.random.seed(42)
num_registros = 100000

#2 Generar variables numéricas con correlaciones simuladas
edad = np.random.normal(loc=40, scale=12, size=num_registros).astype(int)
ingreso = (edad * 1500) + np.random.normal(loc=20000, scale=8000, size=num_registros)
puntuacion_gasto = np.random.randint(1, 101, size=num_registros)
ahorro = (ingreso * 0.2) - (puntuacion_gasto * 50) + np.random.normal(loc=5000, scale=2000, size=num_registros)
historial_credito = np.clip(np.random.normal(loc=0.7, scale=0.15, size=num_registros), 0.0, 1.0)

#3 Crear categorías de clasificación (Target)
condiciones = [
    (ingreso > 85000) & (historial_credito > 0.75),
    (ingreso < 45000) | (historial_credito < 0.5)
]
opciones = ['Premium', 'Bajo Perfil']
target = np.select(condiciones, opciones, default='Estándar')

#4 Estructurar los datos en un DataFrame
datos = {
    'Edad': edad,
    'Ingreso_Anual': ingreso.astype(int),
    'Puntuacion_Gasto': puntuacion_gasto,
    'Indice_Ahorro': ahorro.astype(int),
    'Historial_Credito': np.round(historial_credito, 2),
    'target_column': target
}
df = pd.DataFrame(datos)

#5 Guardar el archivo CSV
nombre_archivo = 'tu_archivo.csv'
df.to_csv(nombre_archivo, index=False)
print(f"¡Archivo '{nombre_archivo}' generado con éxito! ({num_registros:,} registros)")
print(df.head())

#1 Cargar el conjunto de datos generado previamente
df = pd.read_csv('tu_archivo.csv')

#2 Separar características (X) eliminando la columna objetivo
X = df.drop(columns=['target_column'])

#3 Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#4 Inicializar PCA con TODOS los componentes posibles
pca_completo = PCA()
pca_completo.fit(X_scaled)

#5 Calcular la varianza explicada acumulada
varianza_individual = pca_completo.explained_variance_ratio_
varianza_acumulada = np.cumsum(varianza_individual)

#6 Determinar automáticamente el número óptimo de componentes para el 80% y 95%
componentes_80 = np.argmax(varianza_acumulada >= 0.80) + 1
componentes_95 = np.argmax(varianza_acumulada >= 0.95) + 1

print("\n--- ANÁLISIS DE VARIANZA ---")
for i, var in enumerate(varianza_individual):
    print(f"Componente {i+1}: {var:.2%} (Acumulada: {varianza_acumulada[i]:.2%})")

print(f"\nNúmero óptimo de componentes para retener el 80% de información: {componentes_80}")
print(f"Número óptimo de componentes para retener el 95% de información: {componentes_95}")

#7 Graficar la Varianza Explicada Acumulada (Scree Plot)
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

ax1 = axes[0]
ax1.plot(range(1, len(varianza_acumulada) + 1), varianza_acumulada,
         marker='o', linestyle='--', color='b', label='Varianza Acumulada')
ax1.bar(range(1, len(varianza_individual) + 1), varianza_individual,
        alpha=0.5, color='g', label='Varianza Individual')
ax1.axhline(y=0.90, color='r', linestyle=':', label='Umbral del 90% de Información')
ax1.set_title('Gráfico de Codo (Scree Plot) - Selección de Componentes PCA')
ax1.set_xlabel('Número de Componentes Principales')
ax1.set_ylabel('Fracción de Varianza Explicada')
ax1.set_xticks(range(1, len(varianza_acumulada) + 1))
ax1.set_ylim(0, 1.05)
ax1.legend(loc='best')
ax1.grid(True, linestyle='--', alpha=0.6)

#1 Cargar el conjunto de datos desde el archivo CSV
df = pd.read_csv('tu_archivo.csv')

#2 Separar las variables predictoras (X) y la variable objetivo (y)
X = df.drop(columns=['target_column'])
y = df['target_column']

#3 Escalar los datos (Paso obligatorio antes de aplicar PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#4 Configurar y aplicar PCA
#'n_components=2' reduce los datos a las 2 dimensiones principales
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

#5 Crear un nuevo DataFrame con los resultados del PCA
df_pca = pd.DataFrame(data=X_pca, columns=['Componente Principal 1', 'Componente Principal 2'])
df_pca['Target'] = y.values

#6 Mostrar la varianza explicada por cada componente
print(f"Varianza explicada por cada componente: {pca.explained_variance_ratio_}")
print(f"Varianza total retenida: {sum(pca.explained_variance_ratio_):.2%}")

#7 Graficar los componentes principales en un espacio 2D
ax2 = axes[1]
targets = df_pca['Target'].unique()
colors = {'Premium': '#2ecc71', 'Estándar': '#3498db', 'Bajo Perfil': '#e74c3c'}

for tgt in targets:
    indices_to_keep = df_pca['Target'] == tgt
    ax2.scatter(
        df_pca.loc[indices_to_keep, 'Componente Principal 1'],
        df_pca.loc[indices_to_keep, 'Componente Principal 2'],
        label=tgt,
        s=10,
        alpha=0.4,
        color=colors.get(tgt, None)
    )

ax2.set_xlabel('Componente Principal 1')
ax2.set_ylabel('Componente Principal 2')
ax2.set_title('Visualización de PCA (2 Componentes)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('resultado_pca.png', dpi=150, bbox_inches='tight')
plt.close()

print("Imagen guardada como 'resultado_pca.png'")
