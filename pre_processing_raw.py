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
    'País','Latitude','Longitude']

processed_aeroporto = aeroporto[['Código de Aeroporto','Aeroporto','Cidade','Estado']]
print(processed_aeroporto.isna().sum())

if processed_aeroporto.isna().sum().sum() == 0:
    processed_aeroporto.to_csv('raw_processed/processed_airports.csv')



# Análise de Data Frames em flights.csv

voos.columns = ['Ano', 'Mês', 'Dia', 'Dia da Semana', 'Companhia Aérea', 'Número do Voo', 'Número de Registro da Aeronave', 
    'Aeroporto de Origem', 'Aeroporto de Destino', 'Horário Programado para Partida (HHMM)', 'Horário Real de Partida (HHMM)', 
    'Atraso na Partida', 'Tempo Gasto até Decolagem', 'Horário em que o Avião Decolou (HHMM)', 'Tempo de Voo Planejado', 
    'Tempo Real de Voo', 'Tempo no Ar', 'Distância', 'Momento do Pouso (HHMM)', 'Tempo do Pouso até Desembarque', 
    'Horário de Chegada Programado (HHMM)', 'Horário de Chegada Real (HHMM)', 'Atraso de Chegada', 
    'Desvio de Voo', 'Status de Cancelamento', 'Motivo de Cancelamento', 'Atraso por Controle de Espaço Aéreo', 
    'Atraso por Segurança', 'Atraso da Companhia', 'Atraso por Aeronave Anterior', 'Atraso por Condições Meteorológicas']


# Removendo voos cancelados e voos desviados

voos = voos[voos['Status de Cancelamento'] == 0].copy()
voos = voos[voos['Desvio de Voo'] == 0].copy()


selected_columns_voos = voos[['Mês','Dia','Dia da Semana','Companhia Aérea','Aeroporto de Origem','Aeroporto de Destino',
                        'Horário Programado para Partida (HHMM)', 'Atraso na Partida', 'Tempo de Voo Planejado', 'Distância', 
                        'Atraso de Chegada','Atraso por Controle de Espaço Aéreo',
                        'Atraso por Segurança','Atraso da Companhia','Atraso por Aeronave Anterior','Atraso por Condições Meteorológicas']]

print(selected_columns_voos.info())







# Manipular dados completando com a mediana

selected_columns_voos['Atraso na Partida'] = (selected_columns_voos['Atraso na Partida'].fillna(selected_columns_voos['Atraso na Partida'].median()))
selected_columns_voos = selected_columns_voos.dropna(subset=['Tempo de Voo Planejado'])
selected_columns_voos['Atraso de Chegada'] = (selected_columns_voos['Atraso de Chegada'].fillna(selected_columns_voos['Atraso de Chegada'].median()))
selected_columns_voos['Atraso por Controle de Espaço Aéreo'] = (selected_columns_voos['Atraso por Controle de Espaço Aéreo'].fillna(selected_columns_voos['Atraso por Controle de Espaço Aéreo'].median()))
selected_columns_voos['Atraso por Segurança'] = (selected_columns_voos['Atraso por Segurança'].fillna(selected_columns_voos['Atraso por Segurança'].median()))
selected_columns_voos['Atraso da Companhia'] = (selected_columns_voos['Atraso da Companhia'].fillna(selected_columns_voos['Atraso da Companhia'].median()))
selected_columns_voos['Atraso por Aeronave Anterior'] = (selected_columns_voos['Atraso por Aeronave Anterior'].fillna(selected_columns_voos['Atraso por Aeronave Anterior'].median()))
selected_columns_voos['Atraso por Condições Meteorológicas'] = (selected_columns_voos['Atraso por Condições Meteorológicas'].fillna(selected_columns_voos['Atraso por Condições Meteorológicas'].median()))



# Eliminação de Outliers Superiores e Inferiores
p005 = selected_columns_voos['Atraso de Chegada'].quantile(0.005)
p995 = selected_columns_voos['Atraso de Chegada'].quantile(0.995)




# Filtragem correta (DataFrame, não lista)

flights_filtrado = selected_columns_voos[
    (selected_columns_voos['Atraso de Chegada'] >= p005) &
    (selected_columns_voos['Atraso de Chegada'] <= p995)]

# Salvar

flights_filtrado.to_csv('raw_processed/processed_flights.csv', index=False)
