# this is for trainning Neural Network
import csv
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split,cross_val_score,learning_curve
# from plot_learning_curve import plot_learning_curve
from sklearn.externals import joblib
NPDict = dict()
NList = list()
rawPList = list()
Plist = list()
with open('SimPy\\NPfile.csv', 'r') as NPfile:
    csvReader = csv.reader(NPfile)
    for line in csvReader:
        if line != []:
            NPDict[line[0]] = line[1]

NPDictItems = list(NPDict.items())
for item in NPDictItems:
    # preparing number data for training
    strNums = item[0][4:]
    vecNums = list()
    for letter in strNums:
        vecNum = np.zeros(10, int)
        vecNum[int(letter)] = 1
        vecNums.extend(vecNum)

    # preparing price data for training
    rawPrice = int(item[1])/10000
    rawPrice = np.log10(rawPrice)

    if len(vecNums)==70:
        NList.append(vecNums)
        rawPList.append(rawPrice)

maxLogPrice = max(rawPList)
for price in rawPList:
    Plist.append(price/maxLogPrice)
# print(len(NList),len(Plist))
X = np.array(NList)
y = np.array(Plist)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1)
print(len(X_train))
Model = MLPRegressor(hidden_layer_sizes=(100,),activation='relu',max_iter=4000,alpha=0.0011,learning_rate='adaptive',learning_rate_init=0.0035)
Model.fit(X_train,y_train)
print('%0.2f'%Model.score(X_train,y_train))
print('%0.2f'%Model.score(X_test,y_test))
saveCommand = input('Do you want to save the model?(y/n)  :   ')
if saveCommand == 'y':
    joblib.dump(Model,'SimPy\\SimPy.joblib')
# plt = plot_learning_curve(Model,'Learning Curve',X_train,y_train,train_sizes=[0.1,0.3,0.5,0.7,1])
# plt.show()
# score = cross_val_score(Model,X_train,y_train,cv=3)
# print(score)
