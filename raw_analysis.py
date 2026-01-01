import pandas as pd

# Carregamento dos Data Frames
companias = pd.read_csv('raw/airlines.csv')
aeroporto = pd.read_csv('raw/airports.csv')
voos = pd.read_csv('raw/flights.csv')

# Análise de Data Frames em airlines.csv
companias.columns = ['Código de Companhia', 'Companhia']
companias_nan_coluna = companias.isna().sum()
print(companias_nan_coluna)
print('\n')

    
# Análise de Data Frames em airports.csv
aeroporto.columns = [
    'Código de Aeroporto','Aeroporto','Cidade','Estado',
    'País','Latitude','Longitude']

aeroporto_nan_coluna = aeroporto.isna().sum()
print(aeroporto_nan_coluna)
print('\n')

# Análise de Data Frames em flights.csv

voos.columns = ['Ano','Mês','Dia','Dia da Semana','Companhia Aérea','Número do Voo',
    'Número de Registro da Aeronave','Aeroporto de Origem','Aeroporto de Destino', 
    'Horário Programado para Partida (HHMM)','Horário Real de Partida (HHMM)','Atraso na Partida',  
    'Tempo Gasto até Decolagem','Horário em que o Avião Decolou (HHMM)',
    'Tempo de Voo Planejado', 'Tempo Real de Voo','Tempo no Ar','Distância',
    'Momento do Pouso (HHMM)','Tempo do Pouso até Desembarque',
    'Horário de Chegada Programado (HHMM)','Horário de Chegada Real (HHMM)','Atraso de Chegada',
    'Desvio de Voo','Status de Cancelamento','Motivo de Cancelamento',
    'Atraso por Controle de Espaço Aéreo','Atraso por Segurança',
    'Atraso da Companhia','Atraso por Aeronave Anterior',
    'Atraso por Condições Meteorológicas']

voos_nan_coluna = voos.isna().sum()
print(voos_nan_coluna)
print('\n')

with open('raw/raw_missing_values.txt', 'w', encoding='utf-8') as f:
    f.write("airlines.csv\n")
    f.write(f"shape: {companias.shape}\n")
    f.write(companias_nan_coluna.to_string())
    f.write("\n\n")

    f.write("airports.csv\n")
    f.write(f"shape: {aeroporto.shape}\n")
    f.write(aeroporto_nan_coluna.to_string())
    f.write("\n\n")

    f.write("flights.csv\n")
    f.write(f"shape: {voos.shape}\n")
    f.write(voos_nan_coluna.to_string())
    f.write("\n\n")


with open('raw/raw_flight_describe.txt', 'w', encoding='utf-8') as f:
    f.write(voos.describe(include='all').to_string())
