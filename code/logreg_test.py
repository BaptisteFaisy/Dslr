import numpy as np
import pandas as pd
import sys
from collections import OrderedDict

class LogisticRegressionOVR_predict(object):
    def __init__(self, eta=5e-5, n_iter=30000):
        self.eta = eta
        self.n_iter = n_iter
        
    def _scaling(self,X):
        for i in range(len(X)):
            X[i] = ( X[i] - X.mean())  / X.std()
        return X

    def _processing(self,hptest):
        hptest = hptest.iloc[:,5:]
        hptest = hptest.fillna(hptest.mean()) 
        hp_features = np.array(hptest)
        
        np.apply_along_axis(self._scaling, 0, hp_features)
        return hp_features

        

    
    
    def _predict_one(self, x, weights):
        return max((x.dot(w), c) for w, c in weights)[1]

    def predict(self, X, weights):
        X = self._processing(X)
        return [self._predict_one(i, weights) for i in np.insert(X, 0, 1, axis=1)]





    
    
if __name__ == "__main__":
    hptest = pd.read_csv(sys.argv[1], index_col = "Index")
    predicts = LogisticRegressionOVR_predict().predict(hptest, np.load(sys.argv[2], allow_pickle=True))
    houses = pd.DataFrame(OrderedDict ({'Index':range(len(predicts)), 'Hogwarts House':predicts}))
    houses.to_csv('houses.csv', index=False)