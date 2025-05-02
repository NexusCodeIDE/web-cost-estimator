import joblib
import pandas as pd

# Load model and encoders
model = joblib.load("estimator/web_cost_model.pkl")
encoders = joblib.load("estimator/label_encoders.pkl")

def predict_cost(site_type, pages, features, design, urgency):
    # Encode categorical inputs
    encoded = {
        'site_type': encoders['site_type'].transform([site_type])[0],
        'pages': pages,
        'features': features,
        'design': encoders['design'].transform([design])[0],
        'urgency': encoders['urgency'].transform([urgency])[0],
    }

    df = pd.DataFrame([encoded])
    predicted_cost = model.predict(df)[0]
    return round(predicted_cost, 2)
