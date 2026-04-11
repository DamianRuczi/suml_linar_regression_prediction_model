import numpy as np
import pickle

def predict_target_value(x):
    lr_model = pickle.load(open("our_model.pkl", 'rb'))
    input = np.array([x]).reshape(-1,1)
    prediction = lr_model.predict(input.reshape(-1,1))
    return prediction[0].reshape(1,-1).flatten()[0]


print(predict_target_value(4))