import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import joblib

os.makedirs('models', exist_ok=True)

voos = pd.read_csv('raw_processed/processed_flights.csv')


# Transformação das Colunas Categóricas
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
voos['Companhia Aérea'] = le.fit_transform(voos['Companhia Aérea'])



ml = voos[['Atraso na Partida', 'Atraso por Aeronave Anterior', 'Atraso da Companhia', 'Atraso por Controle de Espaço Aéreo',
           'Atraso por Condições Meteorológicas', 'Horário Programado para Partida (HHMM)', 'Companhia Aérea', 'Atraso de Chegada']].sample(3000000)
    


# Seleção das Colunas Explicativas e de Interesse

x = ml[['Atraso na Partida', 'Atraso por Aeronave Anterior', 'Atraso da Companhia', 'Atraso por Controle de Espaço Aéreo',
        'Atraso por Condições Meteorológicas', 'Horário Programado para Partida (HHMM)','Companhia Aérea']]
y = ml['Atraso de Chegada']



# Separação Treino e Teste
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)


# Importação das Métricas
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Criação de Modelos de Regressão
modelo = LinearRegression()
modelo.fit(x_train, y_train)
y_pred = modelo.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print("-----------------------")
print("Regressão Linear:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)



from sklearn.ensemble import RandomForestRegressor

modelo = RandomForestRegressor()
modelo.fit(x_train, y_train)
y_pred = modelo.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print("-----------------------")
print("Random Forest Regressor:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)

joblib.dump(modelo, 'models/regressão_atraso_voos.joblib')



from sklearn.tree import DecisionTreeRegressor

modelo = DecisionTreeRegressor()
modelo.fit(x_train, y_train)
y_pred = modelo.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print("-----------------------")
print("Decision Tree Regressor:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)




from sklearn.ensemble import ExtraTreesRegressor

modelo = ExtraTreesRegressor()
modelo.fit(x_train, y_train)
y_pred = modelo.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print("-----------------------")
print("Extra Trees Regressor:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)
