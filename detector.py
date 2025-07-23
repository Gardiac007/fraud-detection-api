from sklearn.ensemble import RandomForestClassifier
import numpy as np

class FraudDetector:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=10, random_state=42)
        self.is_trained = False
        self.train_model()

    def train_model(self):
        print("Training fraud detection model...")

        #I'm using a fake dataset for learning purpose instead of datasets
        x = np.array([
            # [amount, location, hour, age, balance]
            [50, 1, 14, 30, 1000],    
            [25, 1, 9, 25, 500],      
            [100, 1, 18, 40, 2000],   
            [75, 1, 12, 35, 1500],    
            [200, 1, 20, 45, 3000],
            [45, 1, 10, 28, 800],
            [120, 1, 15, 42, 2500],
            [30, 1, 11, 33, 1200],
            [85, 1, 16, 38, 1800],
            [60, 1, 13, 29, 900],
            [150, 1, 17, 45, 2800],
            [35, 1, 8, 26, 650],
            [90, 1, 19, 41, 2200],
            [55, 1, 12, 31, 1100],
            [110, 1, 14, 36, 1600],
            [40, 1, 9, 27, 750],
            [95, 1, 18, 39, 1900],
            [70, 1, 21, 34, 1400],
            [125, 1, 16, 43, 2600],
            [80, 1, 11, 32, 1300],
            [65, 1, 15, 37, 1700],
            [48, 1, 13, 30, 950],
            [115, 1, 17, 44, 2400],
            [52, 1, 10, 28, 850],
            [88, 1, 19, 40, 2100],
            [5000, 0, 3, 20, 100],    
            [3000, 0, 2, 25, 50],     
            [10000, 0, 4, 30, 200],   
            [2000, 0, 1, 22, 80],     
            [8000, 0, 5, 28, 150],
            [4500, 0, 2, 24, 120],
            [6200, 0, 1, 26, 85],
            [3800, 0, 4, 21, 95],
            [7500, 0, 3, 29, 140],
            [2200, 0, 0, 23, 70],
            [9200, 0, 5, 31, 180],
            [3500, 0, 23, 20, 110],
            [5800, 0, 2, 27, 130],
            [4200, 0, 4, 22, 90],
            [6800, 0, 1, 25, 160],
            [2800, 0, 3, 24, 75],
            [8500, 0, 0, 28, 190],
            [3200, 0, 5, 21, 105],
            [5500, 0, 23, 26, 135],
            [4800, 0, 2, 23, 115],
            [7200, 0, 4, 30, 170],
            [2500, 0, 1, 19, 65],
            [6500, 0, 3, 27, 155],
            [3900, 0, 0, 22, 125],
            [8200, 0, 5, 29, 185]
        ])

        y = np.array([0]*25 + [1]*25) # 0 = safe, 1 = fraud

        self.model.fit(x,y)
        self.is_trained = True
        print("Model trained!")

        """ Train Part Completed! """

    def check_transaction(self, transaction):

        safe_locations = ['domestic','local','home']
        location_code = 1 if transaction.location.lower() in safe_locations else 0

        features = np.array([[
            transaction.amount,
            location_code,
            transaction.time,
            transaction.age,
            transaction.balance
        ]])

        is_fraud = self.model.predict(features)[0] == 1
        risk_score = self.model.predict_proba(features)[0][1]

        if risk_score > 0.8:
            message = "HIGH RISK: Transaction blocked for security reasons!"
        elif risk_score >= 0.5:
            message = "MEDIUM RISK: Please verify your identity!"
        else:
            message = "LOW RISK: Transaction approved!"

        return is_fraud, risk_score, message