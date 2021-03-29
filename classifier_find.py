# -*- coding: utf-8 -*-

from dados import load_find
import pandas as pd

x, y = load_find()

print(x[0])
print(y[0])

df = pd.read_csv('cursos.csv')
#print(df.head())

df_X = df[['home','busca','logado']]
df_Y = df['comprou']

X_dummies_df = pd.get_dummies(df_X)
#Y_dummies = pd.get_dummies(Y)[1] #para pegar a coluna 1
Y_dummies_df = df_Y

X = X_dummies_df.values
Y = Y_dummies_df.values

print(X)

