##import the data

import pandas as pd
dataset = pd.read_csv("diabetes.csv")
print(dataset.head())

x  = dataset.drop(["Outcome"] ,axis = 1)
y = dataset['Outcome']

print(x)
print(y)

##import numpy for array format
import numpy as np
x = np.array(x)
y = np.array(y)

print(x)
print(y)

##train test and split
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x, y , test_size=0.2)

print("x_train data :" , x_train)
print("y_train :" , y_train)

print("length of x_train : " , len(x_train))
print("length of y_train : " , len(y_train))

##for linear regression::
from sklearn.linear_model import LinearRegression
linear = LinearRegression()
linear.fit(x_train , y_train)

acc = linear.score(x_test, y_test)
print( " linear reg. :", acc)

##from decision tree
from sklearn.tree import DecisionTreeClassifier
dtc  = DecisionTreeClassifier()
dtc.fit(x_train , y_train)
acc = dtc.score(x_test , y_test)
print( "decision tree clf : ",acc)

##for knn algorithm
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train , y_train)
acc = knn.score(x_test  ,y_test)
print(" knn accuracy" , acc)


'''
##for logistic regression:
from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression(random_state=0)
logistic.fit(x_train ,y_train)
'''




