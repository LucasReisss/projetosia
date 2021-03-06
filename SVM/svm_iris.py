# -*- coding: utf-8 -*-
"""svm_iris.ipynb

Automatically generated by Colaboratory.

"""

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()

dir(iris)

iris.feature_names

#quadro de dados
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df.head()

df['target'] = iris.target
df.head()

iris.target_names

#mostrar quais dos dados apresenta o valor 1
df[df.target==1].head()

df[df.target==2].head()

df['flower_name'] =df.target.apply(lambda x: iris.target_names[x])
df.head()

import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

#separar essas especies em 3 quadros de dados
df0 = df[df.target==0]
df1 = df[df.target==1]
df2 = df[df.target==2]

df0.head()

df1.head()

df2.head()

#desenhar uma dispersão plot
plt.xlabel('sepal length (cm)')
plt.xlabel('sepal width (cm)')
plt.scatter(df0['sepal length (cm)'],df0['sepal width (cm)'],color='green', marker='+')
plt.scatter(df1['sepal length (cm)'],df1['sepal width (cm)'],color='blue', marker='.')

plt.xlabel('petal length (cm)')
plt.xlabel('petal width (cm)')
plt.scatter(df0['petal length (cm)'],df0['petal width (cm)'],color='green', marker='+')
plt.scatter(df1['petal length (cm)'],df1['petal width (cm)'],color='blue', marker='.')

#treinar modelo com Sklearn

from sklearn.model_selection import train_test_split

#Remover colunas do quadro
X = df.drop(['target','flower_name'], axis='columns')
X.head

# Seram os números usuais
y = df.target
y

#treinar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

len(X_train)

len(X_test)

from sklearn.svm import SVC
model = SVC(kernel='linear')

model.fit(X_train, y_train)

model.score(X_test, y_test)