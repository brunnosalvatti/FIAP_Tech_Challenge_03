import pandas as pd
import os

os.makedirs('raw_processed', exist_ok=True)

# Carregamento dos Data Frames

companias = pd.read_csv('raw/airlines.csv')
aeroporto = pd.read_csv('raw/airports.csv')
voos = pd.read_csv('raw/flights.csv')



# Análise de Data Frames em airlines.csv

companias.columns = ['Código de Companhia', 'Companhia']
companias_nan_coluna = companias.isna().sum()
print(companias_nan_coluna)
print('\n')

if companias_nan_coluna.isna().sum() == 0:
    companias.to_csv('raw_processed/processed_airlines.csv')



# Análise de Data Frames em airports.csv

aeroporto.columns = [
    'Código de Aeroporto','Aeroporto','Cidade','Estado',
    'País','Latitude','Longitude'
]

processed_aeroporto = aeroporto[['Código de Aeroporto','Aeroporto','Cidade','Estado']]
print(processed_aeroporto.isna().sum())

if processed_aeroporto.isna().sum().sum() == 0:
    processed_aeroporto.to_csv('raw_processed/processed_airports.csv')



# Análise de Data Frames em flights.csv

voos.columns = ['Ano','Mês','Dia','Dia da Semana','Companhia Aérea','Número do Voo',
    'Número Aeronave','Aeroporto de Origem','Aeroporto de Destino',
    'Horário Programado de Partida','Horário de Partida','Atraso de Partida',
    'Tempo de Taxi até Decolagem','Momento de Decolagem',
    'Tempo de Voo Planejado','Tempo Total do Voo','Tempo em Voo','Distância',
    'Momento do Pouso','Tempo do Pouso até Desembarque',
    'Horário Previsto de Chegada','Horário de Chegada','Atraso de Chegada',
    'Desvio de Voo','Cancelado','Motivo de Cancelamento',
    'Tempo de Atraso por Controle de Espaço Aéreo','Tempo de Atraso por Segurança',
    'Atraso da Companhia','Atraso por Atraso de Aeronave Anterior',
    'Atraso pelo Tempo']


selected_columns_voos = voos[['Mês','Dia','Dia da Semana','Companhia Aérea','Aeroporto de Origem','Aeroporto de Destino',
                        'Horário Programado de Partida', 'Atraso de Partida', 'Tempo de Voo Planejado', 'Distância', 
                        'Horário Previsto de Chegada','Atraso de Chegada','Cancelado', 'Motivo de Cancelamento','Tempo de Atraso por Controle de Espaço Aéreo',
                        'Tempo de Atraso por Segurança','Atraso da Companhia','Atraso por Atraso de Aeronave Anterior','Atraso pelo Tempo']]


# Manipular dados completando com a mediana

selected_columns_voos['Atraso de Partida'] = (selected_columns_voos['Atraso de Partida'].fillna(selected_columns_voos['Atraso de Partida'].median()))
selected_columns_voos = selected_columns_voos.dropna(subset=['Tempo de Voo Planejado'])
selected_columns_voos['Atraso de Chegada'] = (selected_columns_voos['Atraso de Chegada'].fillna(selected_columns_voos['Atraso de Chegada'].median()))
selected_columns_voos['Tempo de Atraso por Controle de Espaço Aéreo'] = (selected_columns_voos['Tempo de Atraso por Controle de Espaço Aéreo'].fillna(selected_columns_voos['Tempo de Atraso por Controle de Espaço Aéreo'].median()))
selected_columns_voos['Tempo de Atraso por Segurança'] = (selected_columns_voos['Tempo de Atraso por Segurança'].fillna(selected_columns_voos['Tempo de Atraso por Segurança'].median()))
selected_columns_voos['Atraso da Companhia'] = (selected_columns_voos['Atraso da Companhia'].fillna(selected_columns_voos['Atraso da Companhia'].median()))
selected_columns_voos['Atraso por Atraso de Aeronave Anterior'] = (selected_columns_voos['Atraso por Atraso de Aeronave Anterior'].fillna(selected_columns_voos['Atraso por Atraso de Aeronave Anterior'].median()))
selected_columns_voos['Atraso pelo Tempo'] = (selected_columns_voos['Atraso pelo Tempo'].fillna(selected_columns_voos['Atraso pelo Tempo'].median()))


columns_remotion = [
    'Atraso de Partida',
    'Tempo de Atraso por Controle de Espaço Aéreo',
    'Tempo de Atraso por Segurança',
    'Atraso da Companhia',
    'Atraso por Atraso de Aeronave Anterior',
    'Atraso pelo Tempo',
    'Motivo de Cancelamento'
]

selected_columns_voos = selected_columns_voos.drop(columns=columns_remotion)



# Pontos de corte
p005 = selected_columns_voos['Atraso de Chegada'].quantile(0.005)
p995 = selected_columns_voos['Atraso de Chegada'].quantile(0.995)

# Filtragem correta (DataFrame, não lista)
flights_filtrado = selected_columns_voos[
    (selected_columns_voos['Atraso de Chegada'] >= p005) &
    (selected_columns_voos['Atraso de Chegada'] <= p995)
]

# Salvar
flights_filtrado.to_csv('raw_processed/processed_flights.csv', index=False)
