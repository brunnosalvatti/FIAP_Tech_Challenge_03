import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import joblib

os.makedirs('models', exist_ok=True)

voos = pd.read_csv('raw_processed/processed_flights.csv')
voos['Status Atraso'] = (voos['Atraso de Chegada'] > 0).astype(int)
print(voos['Status Atraso'].value_counts())


# Transformação das Colunas Categóricas
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
voos['Companhia Aérea'] = le.fit_transform(voos['Companhia Aérea'])



ml = voos[['Atraso na Partida', 'Atraso por Aeronave Anterior', 'Atraso da Companhia', 'Atraso por Controle de Espaço Aéreo',
           'Atraso por Condições Meteorológicas', 'Horário Programado para Partida (HHMM)', 'Companhia Aérea', 'Status Atraso']].sample(3000000)
    


# Seleção das Colunas Explicativas e de Interesse

x = ml[['Atraso na Partida', 'Atraso por Aeronave Anterior', 'Atraso da Companhia', 'Atraso por Controle de Espaço Aéreo',
           'Atraso por Condições Meteorológicas', 'Horário Programado para Partida (HHMM)']]
y = ml['Status Atraso']



# Separação Treino e Teste
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)


# Importação das Métricas

from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, precision_score, confusion_matrix


# Modelo Aleatório
from sklearn.dummy import DummyClassifier
dummy = DummyClassifier(strategy='most_frequent', random_state=42)
dummy.fit(x_train, y_train)
y_pred = dummy.predict(x_test)
f1 = f1_score(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred)
mc = confusion_matrix(y_test,y_pred)
print('-------------------------------------------------------------')
print('Dummy Model:')
print('f1: ' + str(f1))
print('acc: ' + str(acc))
print('prec: ' + str(prec))
print('auc: ' + str(auc))
print('\n')
print('Matriz de Confusão:')
print(mc)
print('\n')



### Criação de Modelos
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
f1 = f1_score(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred)
mc = confusion_matrix(y_test,y_pred)
print('-------------------------------------------------------------')
print('Logistic Regression:')
print('f1: ' + str(f1))
print('acc: ' + str(acc))
print('prec: ' + str(prec))
print('auc: ' + str(auc))
print('\n')
print('Matriz de Confusão:')
print(mc)
print('\n')
joblib.dump(model, 'models/classificação_atraso_voos.joblib')

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

f1 = f1_score(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred)
mc = confusion_matrix(y_test,y_pred)
print('-------------------------------------------------------------')
print('Random Forest Classifier:')
print('f1: ' + str(f1))
print('acc: ' + str(acc))
print('prec: ' + str(prec))
print('auc: ' + str(auc))
print('\n')
print('Matriz de Confusão:')
print(mc)
print('\n')




from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
f1 = f1_score(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred)
mc = confusion_matrix(y_test,y_pred)

print('-------------------------------------------------------------')
print('Decision Tree Classifier:')
print('f1: ' + str(f1))
print('acc: ' + str(acc))
print('prec: ' + str(prec))
print('auc: ' + str(auc))
print('\n')
print('Matriz de Confusão:')
print(mc)
print('\n')




from sklearn.ensemble import ExtraTreesClassifier

modelo = ExtraTreesClassifier()
modelo.fit(x_train, y_train)
y_pred = modelo.predict(x_test)

f1 = f1_score(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred)
mc = confusion_matrix(y_test,y_pred)

print('-------------------------------------------------------------')
print('Extra Trees Classifier:')
print('f1: ' + str(f1))
print('acc: ' + str(acc))
print('prec: ' + str(prec))
print('auc: ' + str(auc))
print('\n')
print('Matriz de Confusão:')
print(mc)
print('\n')


