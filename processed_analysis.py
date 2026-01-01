import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns

os.makedirs('processed_analysis', exist_ok=True)
voos = pd.read_csv('raw_processed/processed_flights.csv')

x = voos[['Mês','Dia','Dia da Semana','Companhia Aérea','Aeroporto de Origem','Aeroporto de Destino','Horário Programado para Partida (HHMM)','Atraso na Partida','Tempo de Voo Planejado','Distância','Atraso por Controle de Espaço Aéreo','Atraso por Segurança','Atraso da Companhia','Atraso por Aeronave Anterior','Atraso por Condições Meteorológicas']]
y = voos['Atraso de Chegada']



# Criando Visualizações Básicas de Correlação
x = x.select_dtypes(include='number')

for c in x.columns:
    corr = x[c].corr(y)
    print('Correlação entre:', c, 'x Atraso de Chegada:', corr)
    fig = plt.figure(figsize=(8, 5))
    plt.scatter(x[c], y)
    plt.xlabel(c)
    plt.ylabel('Atraso de Chegada (min)')
    plt.title(f'{c} x Atraso de Chegada | Corr (Pearson): {corr:.3f}')
    plt.savefig('processed_analysis/' + 'Relação ' + str(c) + '_x_Atraso_de_Chegada.png',bbox_inches='tight')
    plt.close(fig)



# Criando Visualizações de Média por Dado
x = voos[['Mês','Dia','Dia da Semana','Companhia Aérea','Aeroporto de Origem','Aeroporto de Destino','Horário Programado para Partida (HHMM)','Atraso na Partida','Tempo de Voo Planejado','Distância','Atraso por Controle de Espaço Aéreo','Atraso por Segurança','Atraso da Companhia','Atraso por Aeronave Anterior','Atraso por Condições Meteorológicas']]
media_atraso_chegada_global = y.mean()

for c in x.columns:
    media_por_x = voos.groupby(c)['Atraso de Chegada'].mean()

    plt.figure(figsize=(8, 5))

    plt.bar(range(len(media_por_x)), media_por_x.values)
    plt.axhline(media_atraso_chegada_global, linestyle='--')

    plt.xlabel(c)
    plt.ylabel('Média de Atraso de Chegada')
    plt.title(f'Média de Atraso por {c}')

    n_ticks = min(31, len(media_por_x))
    idx = np.linspace(0, len(media_por_x) - 1, n_ticks, dtype=int)
    plt.xticks(idx,media_por_x.index.astype(str)[idx],rotation=45,ha='right')
    plt.tight_layout()
    plt.savefig('processed_analysis/' + 'Média de ' + str(c) + '_x_Atraso_de_Chegada.png',bbox_inches='tight')
    plt.close(fig)


# Criação de HeatMap
df_num = voos.select_dtypes(include='number')
corr_atraso = df_num.corr()['Atraso de Chegada'].sort_values(ascending=False)
corr_atraso_df = corr_atraso.to_frame(name='Correlação')
plt.figure(figsize=(6, 10))
sns.heatmap(
    corr_atraso_df,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0,
    cbar=True
)

plt.title('Correlação das Variáveis com Atraso de Chegada')
plt.tight_layout()
plt.savefig('processed_analysis/heatmap_correlacao_atraso_chegada.png',dpi=300,bbox_inches='tight')
plt.close(fig)