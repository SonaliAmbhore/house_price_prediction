from flask import Flask,render_template,jsonify,request
from test import HousePricePrediction
import config
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    print("Welcome to Home API")
    return render_template("home.html")

@app.route('/predict',methods = ['POST'])
def huose_price_pred():
   
    data = request.form
    
    MedInc = eval(data['MedInc'])
    HouseAge = eval(data['HouseAge'])
    AveRooms = eval(data['AveRooms'])
    AveBedrms = eval(data['AveBedrms'])	
    Population = eval(data['Population'])
    AveOccup = eval(data['AveOccup'])
    Latitude = eval(data['Latitude'])
    Longitude = eval(data['Longitude'])
    
    house_price = HousePricePrediction(MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude)
    
    price = house_price.predict_house_price()
    return f"Predicted house price is: {np.round(price[0], 2)}"

    
       
if __name__ == "__main__":
    app.run(port = config.PORT,debug=True,host='0.0.0.0')
    