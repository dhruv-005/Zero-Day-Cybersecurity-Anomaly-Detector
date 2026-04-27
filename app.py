import streamlit as st
import pandas as pd
import joblib
import time
import os

# --- Page Config ---
st.set_page_config(page_title="Zero-Day IDS", layout="wide", page_icon="🛡️")
st.title("🛡️ Zero-Day Cybersecurity Anomaly Detector")
st.markdown("Live Network Traffic Monitoring Dashboard utilizing Unsupervised Machine Learning.")

# --- Load Models & Data ---
@st.cache_resource
def load_ml_assets():
    if not os.path.exists('models/isolation_forest.pkl') or not os.path.exists('models/scaler.pkl'):
        st.error("Model files not found! Please run `python train_model.py` first.")
        st.stop()
    model = joblib.load('models/isolation_forest.pkl')
    scaler = joblib.load('models/scaler.pkl')
    return model, scaler

model, scaler = load_ml_assets()

if not os.path.exists('data/network_traffic.csv'):
    st.error("Data file not found! Please run `python generate_data.py` first.")
    st.stop()

# Load a sample of data to act as our "live stream"
df_stream = pd.read_csv('data/network_traffic.csv').sample(n=100, random_state=99).reset_index(drop=True)

# --- Dashboard Layout ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Live Network Traffic Log")
    log_placeholder = st.empty()
    
with col2:
    st.subheader("System Alerts")
    alert_placeholder = st.empty()

# --- Simulation Logic ---
if st.button("Start Live Network Stream"):
    # Clear previous alerts
    alert_placeholder.empty()
    
    # Lists to keep track of the rolling window of data
    display_data = pd.DataFrame(columns=df_stream.columns)
    alert_messages = []

    for index, row in df_stream.iterrows():
        # 1. Capture the single incoming packet
        packet_features = pd.DataFrame([row.drop('label')])
        true_label = row['label'] # Only used to show if the AI was right!

        # 2. Scale and Predict using the pre-trained model
        packet_scaled = scaler.transform(packet_features)
        prediction = model.predict(packet_scaled)
        
        # 3. Interpret Result (-1 is Anomaly, 1 is Normal)
        is_anomaly = True if prediction[0] == -1 else False

        # Add result to our display table
        row_display = row.copy()
        row_display['AI Status'] = "🚨 ANOMALY" if is_anomaly else "✅ Normal"
        
        # Add to top of dataframe
        display_data = pd.concat([pd.DataFrame([row_display]), display_data]).head(15) 
        
        # Update UI Table
        log_placeholder.dataframe(
            display_data[['duration', 'orig_bytes', 'resp_bytes', 'missed_bytes', 'AI Status']], 
            use_container_width=True
        )

        # Update Alert Box if Anomaly Detected
        if is_anomaly:
            alert_text = f"**ALERT:** Suspicious packet detected! (Bytes sent: {row['orig_bytes']:.2f}, Missed: {row['missed_bytes']})"
            alert_messages.insert(0, alert_text)
            
            # Show only last 5 alerts
            with alert_placeholder.container():
                for msg in alert_messages[:5]:
                    st.error(msg, icon="🚨")

        # Simulate network latency
        time.sleep(0.4)
        
    st.success("Network Stream Simulation Completed.")
