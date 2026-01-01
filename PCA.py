import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import joblib

os.makedirs('models', exist_ok=True)

voos = pd.read_csv('raw_processed/processed_flights.csv')





ml = voos[['Atraso na Partida', 'Atraso por Aeronave Anterior', 'Atraso da Companhia', 'Atraso por Controle de Espaço Aéreo',
           'Atraso por Condições Meteorológicas', 'Horário Programado para Partida (HHMM)', 'Atraso de Chegada']].sample(3000000)
    









