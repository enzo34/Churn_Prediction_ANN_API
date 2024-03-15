from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model('data/churn_client.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array([[data['CreditScore'], data['Geography_France'], data['Geography_Spain'], 
                          data['Geography_Germany'], data['Gender'], data['Age'], 
                          data['Tenure'], data['Balance'], data['NumOfProducts'], 
                          data['HasCrCard'], data['IsActiveMember'], data['EstimatedSalary']]])
    prediction = model.predict(features)
    predicted_probability = float(prediction[0][0])  
    prediction_result = predicted_probability < 0.5  

    response = {
        "prediction": prediction_result
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
