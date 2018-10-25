import numpy as np
from sklearn.externals import joblib
from sklearn.neural_network import MLPRegressor

strNums = input('please enter the number without 0912 : ')
vecNums = list()
for letter in strNums:
    vecNum = np.zeros(10, int)
    vecNum[int(letter)] = 1
    vecNums.extend(vecNum)

X = [vecNums]
Model = joblib.load('SimPy.joblib')
y = Model.predict(X)
y = y * 4.845098040014257
y = np.power(10,y) * 10
predictedPrice = y
print('%0.2f'%(predictedPrice))
