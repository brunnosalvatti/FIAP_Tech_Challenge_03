import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import joblib

os.makedirs('models', exist_ok=True)

voos = pd.read_csv('raw_processed/processed_flights.csv', low_memory=False)

# Seleção de colunas
cols = ['Atraso na Partida', 'Atraso por Aeronave Anterior', 'Atraso da Companhia',
        'Atraso por Controle de Espaço Aéreo', 'Atraso por Condições Meteorológicas',
        'Horário Programado para Partida (HHMM)', 'Atraso de Chegada']

# Evita erro se o dataset tiver < 3 milhões de linhas
ml = voos[cols].sample(n=min(3000000, len(voos)), random_state=42)

from sklearn.preprocessing import StandardScaler
from factor_analyzer.factor_analyzer import calculate_kmo

scaler = StandardScaler()
ml_scaled = scaler.fit_transform(ml)

kmo_variaveis, kmo = calculate_kmo(ml_scaled)

df_var_kmo = pd.DataFrame({
    "Variável": ml.columns,
    "KMO": kmo_variaveis
})

print("Avaliação do KMO por variável:")
print(df_var_kmo)
print('\n')

# Separa-se apenas as variáveis com KMO maior que 0.5 (no seu caso 3 colunas)
data = ml[['Atraso na Partida', 'Horário Programado para Partida (HHMM)', 'Atraso de Chegada']].sample(300000)

# Construção de modelo de PCA
from sklearn.decomposition import PCA

scaled = StandardScaler()
data_scaled = scaled.fit_transform(data)

n = 2
pca = PCA(n_components=n)


x_pca = pca.fit_transform(data_scaled)

df_loadings = pd.DataFrame(
    pca.components_.T,
    columns=[f"PC{i+1}" for i in range(n)],
    index=data.columns
)

print(df_loadings)

# Plot PCA
plt.figure(figsize=(8, 6))
plt.scatter(
    x_pca[:, 0],
    x_pca[:, 1],
    s=5,
    alpha=0.3
)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA — Projeção dos dados")
plt.show()
plt.savefig('processed_analysis/PCA.png')