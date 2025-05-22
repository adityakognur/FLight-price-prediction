import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load preprocessed data
df = pd.read_csv("../data/processed/processed_flight_data.csv")

# Drop any rows with missing values (optional, depends on your data quality)
df.dropna(inplace=True)

# Separate features and target
X = df.drop("Price", axis=1)
y = df["Price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Model trained successfully!")
print(f"📊 Mean Absolute Error: {mae:.2f}")
print(f"📈 R² Score: {r2:.4f}")

# Save the trained model
joblib.dump(model, "flight_price_model.pkl")
print("💾 Model saved as 'flight_price_model.pkl'")
