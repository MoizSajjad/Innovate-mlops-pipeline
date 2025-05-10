from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.joblib")

# Define expected features
features = ['temperature', 'humidity', 'windSpeed', 'pressure', 'precipIntensity',
            'hour', 'day_of_week', 'month', 'season']

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Model API is running"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read JSON input
        data = request.get_json()

        # Convert to DataFrame
        input_df = pd.DataFrame([data], columns=features)

        # Predict
        prediction = model.predict(input_df)[0]
        return jsonify({
            "prediction": round(prediction, 2)
        })
    except Exception as e:
        return jsonify({
            "error": str(e),
            "expected_features": features
        }), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
