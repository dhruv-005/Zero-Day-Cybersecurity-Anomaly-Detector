import pandas as pd
import numpy as np
import os
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

def train_unsupervised_model():
    print("Loading data...")
    df = pd.read_csv('data/network_traffic.csv')

    # Separate features and the hidden ground truth labels
    X = df.drop(columns=['label'])
    y_true = df['label']

    print("Scaling features...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Training Isolation Forest Anomaly Detector...")
    # contamination=0.03 means we assume ~3% of the data is abnormal
    model = IsolationForest(n_estimators=100, contamination=0.03, random_state=42)
    
    # Notice we fit on X_scaled ONLY. The model does not see y_true.
    model.fit(X_scaled)

    # Evaluate how well it blindly found the anomalies
    predictions = model.predict(X_scaled)
    # Isolation Forest outputs 1 for normal, -1 for anomaly. Convert to 0 and 1.
    y_pred = np.where(predictions == 1, 0, 1)

    print("\n--- Training Evaluation ---")
    print(classification_report(y_true, y_pred, target_names=['Normal (0)', 'Anomaly (1)']))

    # Create models directory and save the AI components
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/isolation_forest.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    print("Model and Scaler successfully saved to the 'models/' folder.")

if __name__ == "__main__":
    train_unsupervised_model()
