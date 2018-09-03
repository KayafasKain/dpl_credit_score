from sklearn.externals import joblib
import numpy as np

class ClassifyClient():
    '''
        Loads picled score meodel and classifies client
    '''
    def __init__(self, file_path='credit_score.pkl'):
        self.clf = joblib.load(file_path)

    def classify_client(self, client):
        return self.clf.predict(np.array([ client['seniority'],
                                           client['home'],
                                           client['time'],
                                           client['age'],
                                           client['marital'],
                                           client['records'],
                                           client['job'],
                                           client['expenses'],
                                           client['income'],
                                           client['assets'],
                                           client['debt'],
                                           client['amount'],
                                           client['price']
                                           ]
                                         ).reshape(1, -1)
                                )