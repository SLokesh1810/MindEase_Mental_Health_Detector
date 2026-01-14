from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)  # allow Flutter (or any frontend) to call this

# Load the model once
MODEL_PATH = 'finalisedModel.pkl'
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"{MODEL_PATH} not found. Place your .pkl here.")

model = joblib.load(MODEL_PATH)

# Home route for testing in browser
@app.route('/', methods=['GET'])
def home():
    return "Mental Health Detector API is running! 🚀"


@app.route('/info', methods=['GET'])
def info():
    return {
        "n_features_in_": getattr(model, "n_features_in_", None),
    }


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'features' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    features = data['features']
    try:
        prediction = model.predict([features])[0]
        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
