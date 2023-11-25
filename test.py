import numpy as np
import pickle
import json
import config


class HousePricePrediction():
    def __init__(self,MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude):
        self.MedInc = MedInc
        self.HouseAge = HouseAge
        self.AveRooms = AveRooms
        self.AveBedrms = AveBedrms
        self.Population = Population
        self.AveOccup = AveOccup
        self.Latitude = Latitude
        self.Longitude = Longitude
        
    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)
            
    def predict_house_price(self):
        self.load_model()
        
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.MedInc
        test_array[1] = self.HouseAge
        test_array[2] = self.AveRooms
        test_array[3] = self.AveBedrms
        test_array[4] = self.Population
        test_array[5] = self.AveOccup
        test_array[6] = self.Latitude
        test_array[7] = self.Longitude

        predict_price  = self.model.predict([test_array])

        return predict_price
        