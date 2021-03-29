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

#verifica numa especie de algoritmo base quais são o maiores acerto para chutes
# acertos = len(Y)
# erros = -(sum(Y) - len(Y))
acertos_1 = len(Y[Y == 1])
acertos_0 = len(Y[Y == 0])

taxa_correct_base = 100.0 * max(acertos_1, acertos_0) / len(Y)
print("taxa de acerto base %.2f" % taxa_correct_base)

percent_train = 0.9
#print(X)
size_train = int(percent_train * len(Y))
#print(size_train)
size_test = int(len(Y) - size_train)
#print(size_test)

train_data = X[:size_train]
train_mark = Y[:size_train]

test_data = X[-size_test:]
test_mark = Y[-size_test:]


from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(train_data, train_mark)

result = model.predict(test_data)
different = result - test_mark
#print(different)

corrects = [obj for obj in different if obj == 0]

total_correct = len(corrects)
total_elements = len(test_data)

taxa_correct = 100.0 * total_correct / total_elements

print("taxa de acerto do algoritmo %.2f" % taxa_correct)
#print(taxa_correct)
print(total_elements)