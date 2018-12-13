import numpy as np
from numpy.linalg import inv
from functools import reduce
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error



X_train = np.sort(np.random.randint(0,100,100))
y_train = np.sort(np.random.randint(0,30,100))

X_test = np.sort(np.random.randint(0,100,10))
y_test = np.sort(np.random.randint(0,30,10))

class MyRegression():
         
    def fit(self,X_train,y_train):
        
        self.X_train = np.c_[np.ones_like(X_train),X_train]
        self.y_train = y_train
        
        self.beta = (reduce(
                np.matmul, [inv(np.matmul(np.transpose(self.X_train),self.X_train)),
                            np.transpose(self.X_train),self.y_train]))
    
        
    def coefficients(self):
         
         return self.beta
         
    def predict(self,X_test):
        
        self.X_test = np.c_[np.ones_like(X_test),X_test]
        self.y_predict = np.matmul(self.X_test,self.beta)
        
        return self.y_predict
    
    def plot(self):
        
        plt.scatter(self.X_train[:,1], self.y_train,  color='red')
        plt.plot(self.X_test[:,1], self.y_predict, color='blue', linewidth=1)
        plt.show()

    def score(self,y_test):
        
        return mean_absolute_error(y_test,self.y_predict)


model = MyRegression()
model.fit(X_train, y_train)
print(model.coefficients())
y_pred = model.predict(X_test)
model.plot()
print(model.score(y_test))