import numpy as np 

class LinearRegression:
    def __init__(self):
        self.coefficient=None
        self.intercept=None

    def fit(self,x_train,y_train):

        x_mean=x_train.mean()
        y_mean=y_train.mean()
        self.coefficient = np.sum(((x_train-x_mean).values)*((y_train-y_mean).values))/np.sum(((x_train-x_mean).values)**2)
        self.intercept = y_mean.values-(self.coefficient*x_mean.values)

    def predict(self,x_test):

        list=[]
        for i in x_test.values:
            list.append((self.coefficient*(i))+self.intercept)
            

        return np.asarray(list)