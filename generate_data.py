import pandas as pd
import numpy as np
import os

def create_synthetic_network_data(num_samples=5000, anomaly_rate=0.03):
    print("Generating synthetic network traffic...")
    np.random.seed(42)
    
    # 1. Generate Normal Traffic
    num_normal = int(num_samples * (1 - anomaly_rate))
    normal_data = {
        'duration': np.random.normal(loc=0.5, scale=0.1, size=num_normal),
        'orig_bytes': np.random.normal(loc=500, scale=100, size=num_normal),
        'resp_bytes': np.random.normal(loc=2000, scale=300, size=num_normal),
        'missed_bytes': np.zeros(num_normal), # Usually 0 packets missed in normal traffic
        'label': np.zeros(num_normal) # 0 means normal
    }
    df_normal = pd.DataFrame(normal_data)

    # 2. Generate Zero-Day Anomalies (Weird spikes, dropped packets, massive payloads)
    num_anomalies = num_samples - num_normal
    anomaly_data = {
        'duration': np.random.uniform(low=5.0, high=20.0, size=num_anomalies),
        'orig_bytes': np.random.uniform(low=5000, high=50000, size=num_anomalies),
        'resp_bytes': np.random.uniform(low=10000, high=100000, size=num_anomalies),
        'missed_bytes': np.random.uniform(low=100, high=5000, size=num_anomalies),
        'label': np.ones(num_anomalies) # 1 means anomaly/attack
    }
    df_anomalies = pd.DataFrame(anomaly_data)

    # Combine, shuffle, and clean up
    df_final = pd.concat([df_normal, df_anomalies]).sample(frac=1).reset_index(drop=True)
    
    # Ensure no negative bytes/durations from normal distribution spread
    df_final = df_final.clip(lower=0)
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    file_path = 'data/network_traffic.csv'
    df_final.to_csv(file_path, index=False)
    
    print(f"Success! Saved {num_samples} records to {file_path}")
    print(f"Total Anomalies Injected: {num_anomalies}")

if __name__ == "__main__":
    create_synthetic_network_data()
