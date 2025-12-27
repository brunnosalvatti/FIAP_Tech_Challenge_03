import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns

os.makedirs('processed_analysis', exist_ok=True)
flights = pd.read_csv('raw_processed/processed_flights.csv')
media_atraso_global = flights['Atraso de Chegada'].mean()


# Histograma de Atraso
plt.figure(figsize=(10, 4))
sns.histplot(
    flights['Atraso de Chegada'],bins=50,kde=False)

plt.title('Distribuição do Atraso de Chegada')
plt.xlabel('Atraso de Chegada (min)')
plt.ylabel('Frequência')

plt.savefig(
    'processed_analysis/hist_atraso_chegada.png',dpi=300,bbox_inches='tight')
plt.show()


# Pair Plot
num_cols = flights.select_dtypes(include='number').columns     # Seleção de colunas com número
x_vars = [c for c in num_cols if c != 'Atraso de Chegada']     # Seleção das colunas diferentes do Atraso de Chegada

g = sns.pairplot(flights,x_vars=x_vars,y_vars=['Atraso de Chegada'],height=3,aspect=1.2)

g.fig.set_size_inches(24, 6) 

for ax in g.axes.flat:
    ax.set_xlabel(ax.get_xlabel(), fontsize=9)

plt.savefig('processed_analysis/atraso_chegada_vs_todos.png',
            dpi=300, bbox_inches='tight')
plt.show()



# Cálculo da Relação Média por Dia x Média Global
media_por_dia = (flights.groupby('Dia')['Atraso de Chegada'].mean().sort_index())
plt.figure(figsize=(10, 5))
plt.plot(media_por_dia.index,media_por_dia.values,marker='o',label='Média de Atraso por Dia')
plt.axhline(y=media_atraso_global,linestyle='--',linewidth=2,label=f'Média Global = {media_atraso_global:.2f}')
plt.xlabel('Dia')
plt.ylabel('Atraso de Chegada (min)')
plt.title('Média de Atraso de Chegada por Dia')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('processed_analysis/media_atraso_dia.png')
plt.show()



# Cálculo da Relação Mês x Média Global
media_mensal= flights.groupby('Mês')['Atraso de Chegada'].mean().sort_index()
plt.figure(figsize=(10, 5))
plt.plot(media_mensal.index,media_mensal.values,marker='o',label='Média de Atraso por Mês')
plt.axhline(y=media_atraso_global,linestyle='--',linewidth=2,label=f'Média Global = {media_atraso_global:.2f}')
plt.xlabel('Mês')
plt.ylabel('Atraso de Chegada (min)')
plt.title('Média de Atraso de Chegada por Mês')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('processed_analysis/media_atraso_mes.png')
plt.show()



# Cálculo da Relação Dia da Semana x Média Global
media_semanal = flights.groupby('Dia da Semana')['Atraso de Chegada'].mean().sort_index()
plt.figure(figsize=(10, 5))
plt.plot(media_semanal.index,media_semanal.values,marker='o',label='Média de Atraso por Dia da Semana')
plt.axhline(y=media_atraso_global,linestyle='--',linewidth=2,label=f'Média Global = {media_atraso_global:.2f}')
plt.xlabel('Dia da Semana')
plt.ylabel('Atraso de Chegada (min)')
plt.title('Média de Atraso de Chegada por Dia da Semana')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('processed_analysis/media_atraso_por_dia_semana.png')
plt.show()



# Cálculo da Relação Companhia x Média Global 
media_companhia = flights.groupby('Companhia Aérea')['Atraso de Chegada'].mean().sort_index()
plt.figure(figsize=(10, 5))
plt.plot(media_companhia.index,media_companhia.values,marker='o',label='Média de Atraso por Companhia')
plt.axhline(y=media_atraso_global,linestyle='--',linewidth=2,label=f'Média Global = {media_atraso_global:.2f}')
plt.xlabel('Companhia')
plt.ylabel('Atraso de Chegada (min)')
plt.title('Média de Atraso de Chegada por Companhia')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('processed_analysis/media_atraso_por_companhia.png')
plt.show()


# Cálculo da Relação Distância x Média Global
media_partida = flights.groupby('Distância')['Atraso de Chegada'].mean().sort_index()
plt.figure(figsize=(10, 5))
plt.scatter(media_partida.index,media_partida.values,marker='o',label='Média de Atraso por Distância')
plt.axhline(y=media_atraso_global,linestyle='--',linewidth=2,label=f'Média Global = {media_atraso_global:.2f}')
plt.xlabel('Distância')
plt.ylabel('Atraso de Chegada (min)')
plt.title('Média de Atraso de Chegada por Distância')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('processed_analysis/media_atraso_por_distancia.png')
plt.show()



# Cálculo da Relação do Tempo de Voo Planejado x Média Global
media_partida = flights.groupby('Tempo de Voo Planejado')['Atraso de Chegada'].mean().sort_index()
plt.figure(figsize=(10, 5))
plt.scatter(media_partida.index,media_partida.values,marker='o',label='Média de Atraso por Distância')
plt.axhline(y=media_atraso_global,linestyle='--',linewidth=2,label=f'Média Global = {media_atraso_global:.2f}')
plt.xlabel('Tempo de Voo Planejado')
plt.ylabel('Atraso de Chegada (min)')
plt.title('Média de Atraso de Chegada por Tempo de Voo Planejado')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('processed_analysis/media_atraso_por_tempo_de_voo.png')
plt.show()



# Cálculo da Relação do Tempo de Partida x Média Global
media_horario_partida = flights.groupby('Horário Programado de Partida')['Atraso de Chegada'].mean().sort_index()
plt.figure(figsize=(10, 5))
plt.scatter(media_horario_partida.index,media_horario_partida.values,marker='o',label='Média de Atraso por Distância')
plt.axhline(y=media_atraso_global,linestyle='--',linewidth=2,label=f'Média Global = {media_atraso_global:.2f}')
plt.xlabel('Horário de Partida')
plt.ylabel('Atraso de Chegada (min)')
plt.title('Média de Atraso de Chegada por Horário de Partida')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('processed_analysis/media_atraso_por_horario_partida.png')
plt.show()




# Cálculo da Matriz de Correlação
numeric_cols = flights.select_dtypes(include=['number'])
corr_matrix = numeric_cols.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    linewidths=0.5,
    square=True,
    cbar=True
)

plt.title('Matriz de Correlação – Variáveis Numéricas (Flights)')
plt.tight_layout()
plt.savefig('processed_analysis/matriz_correlacao_heatmap.png')
plt.show()