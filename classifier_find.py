# -*- coding: utf-8 -*-

from dados import load_find
import pandas as pd
from collections import Counter

x, y = load_find()

print(x[0])
print(y[0])

# df = pd.read_csv('cursos.csv')
df = pd.read_csv('busca.csv')
#print(df.head())

df_X = df[['home','busca','logado']]
df_Y = df['comprou']

X_dummies_df = pd.get_dummies(df_X)

Y_dummies_df = df_Y

X = X_dummies_df.values
Y = Y_dummies_df.values

correct_base = max(Counter(Y).itervalues())
taxa_correct_base = 100.0 * correct_base / len(Y)
print("taxa de acerto base Dados diretos %.2f" % taxa_correct_base)

percent_train = 0.9

size_train = int(percent_train * len(Y))

size_test = int(len(Y) - size_train)

train_data = X[:size_train]
train_mark = Y[:size_train]

test_data = X[-size_test:]
test_mark = Y[-size_test:]


from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(train_data, train_mark)

result = model.predict(test_data)
corrects = (result == test_mark)


total_correct = sum(corrects)
total_elements = len(test_data)

taxa_correct = 100.0 * total_correct / total_elements

print("taxa de acerto do algoritmo %.2f" % taxa_correct)
#print(taxa_correct)
print(total_elements)

correct_base = max(Counter(test_mark).itervalues())
taxa_correct_base = 100.0 * correct_base / len(test_mark)
print("'test_mark' - taxa de acerto base %.2f" % taxa_correct_base)