# Customer Churn Prediction API

This Flask-based API leverages an advanced machine learning model to predict customer churn. While the specifics of the model's training and the underlying algorithms are proprietary, the API provides a user-friendly interface to make predictions based on customer data.

## Installation

Ensure Python 3.8 or later is installed on your system for optimal compatibility.

1. **Clone the Repository**: Obtain a copy of this project and navigate to its directory.
   
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install Dependencies**: Use pip to install the required Python packages.

   ```
   pip install -r requirements.txt
   ```

## Running the API

Execute the following command to start the Flask server:

```
python app.py
```

The server will run on `http://localhost:5000`. Ensure the server is active before proceeding with predictions.

## Making Predictions

To predict whether a customer is likely to churn, send a POST request to `http://localhost:5000/predict` with a JSON payload detailing the customer's profile. For example:

```json
{
  "CreditScore": 650,
  "Geography_France": 0,
  "Geography_Spain": 1,
  "Geography_Germany": 0,
  "Gender": 0,
  "Age": 30,
  "Tenure": 4,
  "Balance": 50000,
  "NumOfProducts": 1,
  "HasCrCard": 1,
  "IsActiveMember": 0,
  "EstimatedSalary": 70000
}
```

The API will return a JSON response indicating the churn prediction:

```json
{
  "prediction": false
}
```

## Note

The model's prediction is based on a comprehensive analysis of historical customer data. While detailed information on the model's training process and the algorithms it uses is not disclosed, it has been meticulously developed to provide accurate predictions to aid in decision-making processes.
