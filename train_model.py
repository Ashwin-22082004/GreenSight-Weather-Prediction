import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

X = pd.DataFrame({
    'temperature': [15, 20, 25],
    'humidity': [30, 45, 60],
    'co2': [400, 420, 450]  # Replace wind_speed with co2
})

y = [100, 150, 200]  # Replace with your actual target values if different

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.joblib')
