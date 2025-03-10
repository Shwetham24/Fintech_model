from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import joblib  # For loading the saved model
import xgboost as xgb
import os

app = Flask(__name__)

# Load the trained model (Ensure you have saved it beforehand)
model = joblib.load("model_xgboost.pkl")  # Replace with your actual saved model file

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Extract features from request JSON
        features = [
            data["step"], data["amount"], data["oldbalanceOrg"],
            data["newbalanceOrig"], data["oldbalanceDest"], 
            data["newbalanceDest"], data["type_encoded"],
            data["Collision_score"], data["restricted_country"], data["account_age"]
        ]
        
        # Convert to numpy array (reshape for a single prediction)
        input_data = np.array(features).reshape(1, -1)
        
        # Predict (returns probability, we take class prediction)
        prediction = model.predict(input_data)[0]
        
        # Send response
        return jsonify({"is_fraud": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # ✅ Get port from env variable
    app.run(host='0.0.0.0', port=port, debug=True)  
