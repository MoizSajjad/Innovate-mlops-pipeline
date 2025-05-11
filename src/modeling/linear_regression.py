import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

def train_linear_regression(data_path='data_nextday.csv', model_path='model.joblib'):
    # Load data
    df = pd.read_csv(data_path)

    # Feature selection
    features = ['temperature', 'humidity', 'windSpeed', 'pressure', 'precipIntensity',
                'hour', 'day_of_week', 'month', 'season']
    X = df[features]
    y = df['demand_next_day']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    # Save model
    joblib.dump(lr, model_path)
    print(f"[✔] Trained model saved as {model_path}")

    # Predictions
    y_pred = lr.predict(X_test)

    # Evaluation
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mape = (abs(y_test - y_pred) / y_test).mean() * 100

    # Output results
    print("[✔] Linear Regression Evaluation")
    print(f"MAE:  {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"MAPE: {mape:.2f}%")

if __name__ == "__main__":
    train_linear_regression()
