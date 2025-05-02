import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder
import joblib

# Step 1: Load dataset
df = pd.read_csv("web_cost_dataset.csv")
df = pd.read_csv("web_cost_dataset_lower_prices.csv")


# Step 2: Encode categorical columns
label_encoders = {}
for col in ['site_type', 'design', 'urgency']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # Save encoders for later use

# Step 3: Split into features and labels
X = df.drop("cost", axis=1)
y = df["cost"]

# Step 4: Split into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", round(mae, 2))

# Step 7: Save the model and encoders
joblib.dump(model, "web_cost_model.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")
