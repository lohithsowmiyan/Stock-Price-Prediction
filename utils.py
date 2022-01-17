import joblib
import numpy as np

def preprocess(Open,High,Low,Close,Adjclose):
    test_data = np.array([[Open,High,Low,Close,Adjclose]])
    trained_model= joblib.load('rmodel.pkl')
   
    prediction = trained_model.predict(test_data)
    
    return prediction

