<div align="center">

# 🛡️ Zero-Day Cybersecurity Anomaly Detector

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end Machine Learning pipeline that utilizes **Unsupervised Learning** to detect zero-day network intrusions. Traditional cybersecurity systems rely on signature-based detection (looking for known threats). This project flips that paradigm by learning the exact mathematical baseline of "normal" network traffic and instantly flagging any deviations as potential zero-day attacks.

</div>

---

## 📖 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Architecture & Tech Stack](#-architecture--tech-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Usage Guide](#-usage-guide)
- [How It Works Under the Hood](#-how-it-works-under-the-hood)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)
- [Author](#-author)

---

## 🚀 Project Overview

In real-world enterprise environments, novel cyber attacks (zero-day exploits) occur before security vendors can patch them. This project demonstrates how AI can mitigate this risk. By deploying an **Isolation Forest** algorithm, the model trains exclusively on benign network traffic without requiring labeled attack data. A real-time **Streamlit** dashboard simulates a live network packet stream, evaluating and flagging anomalies in milliseconds.

---

## ✨ Key Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Synthetic Data Generation** | Custom script generates realistic network telemetry (bytes transferred, duration, missed packets) with injected randomized anomalies |
| 2 | **Unsupervised ML** | Scikit-Learn's `IsolationForest` performs anomaly detection without relying on historical attack signatures |
| 3 | **Automated MLOps Pipeline** | Seamlessly handles data scaling (`StandardScaler`), model training, and artifact serialization (`Joblib`) |
| 4 | **Live Monitoring Dashboard** | Responsive Streamlit UI simulates live network ingestion, predicts threats in real-time, and generates visual alerts |

---

## 🛠️ Architecture & Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Language | Python 3.8+ | Core runtime |
| Data Layer | Pandas, NumPy | Data manipulation & generation |
| ML Layer | Scikit-Learn | Isolation Forest anomaly detection |
| Serialization | Joblib | Model artifact persistence |
| Frontend | Streamlit | Real-time monitoring dashboard |

---

## 📂 Project Structure

```text
zero_day_detector/
│
├── 📄 app.py                    # Streamlit dashboard — real-time threat monitoring UI
├── 📄 generate_data.py          # Synthetic network log generator with anomaly injection
├── 📄 train_model.py            # Unsupervised ML training pipeline & artifact export
├── 📄 requirements.txt          # Pinned Python dependencies
├── 📄 .gitignore                # Git exclusion rules (models, data, cache)
├── 📄 README.md                 # Project documentation (this file)
│
├── 📁 data/                     # Auto-generated datasets (excluded from git)
│   ├── normal_traffic.csv       # Baseline benign network traffic logs
│   └── live_traffic.csv         # Simulated live packet stream for dashboard
│
└── 📁 models/                   # Serialized ML artifacts (excluded from git)
    ├── isolation_forest.pkl     # Trained Isolation Forest model
    └── scaler.pkl               # Fitted StandardScaler transformer
```

> **Note:** The `data/` and `models/` directories are listed in `.gitignore` and will be auto-created when you run the pipeline scripts locally.

---

## ⚙️ Installation & Setup

### Prerequisites
- Python `3.8` or higher
- `pip` package manager
- Git

### Step-by-Step Setup

**1. Clone the Repository**
```bash
git clone https://github.com/dhruv-005/zero_day_detector.git
cd zero_day_detector
```

**2. Create & Activate a Virtual Environment** *(Strongly Recommended)*
```bash
# Create the environment
python -m venv venv

# Activate — Linux / macOS
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

**3. Install All Dependencies**
```bash
pip install -r requirements.txt
```

**4. Create Required Directories**
```bash
mkdir data models
```

---

## 🧭 Usage Guide

Run the following scripts **in order** for a complete end-to-end demo:

### Step 1 — Generate Synthetic Network Data
```bash
python generate_data.py
```
> Outputs `data/normal_traffic.csv` and `data/live_traffic.csv`

### Step 2 — Train the Anomaly Detection Model
```bash
python train_model.py
```
> Outputs `models/isolation_forest.pkl` and `models/scaler.pkl`

### Step 3 — Launch the Live Monitoring Dashboard
```bash
streamlit run app.py
```
> Opens the dashboard at `http://localhost:8501` in your browser

---

## 🔬 How It Works Under the Hood

```
┌─────────────────────────────────────────────────────────────────────┐
│                     END-TO-END PIPELINE                             │
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────────┐   │
│  │ generate_    │    │  train_      │    │       app.py         │   │
│  │ data.py      │───▶│  model.py    │───▶│  Streamlit Dashboard │   │
│  └──────────────┘    └──────────────┘    └──────────────────────┘   │
│         │                   │                       │               │
│         ▼                   ▼                       ▼               │
│   normal_traffic      isolation_forest        Live Packet           │
│   live_traffic        scaler.pkl              Stream Scoring        │
│   .csv files          .pkl artifacts          + Visual Alerts       │
└─────────────────────────────────────────────────────────────────────┘
```

### 🧠 Algorithm: Isolation Forest

The **Isolation Forest** works on the principle that anomalies are *rare* and *different*. The algorithm builds an ensemble of random decision trees. For any given data point:

- **Normal traffic** is dense and structured → requires **many splits** to isolate → assigned a **low anomaly score**
- **Malicious traffic** is sparse and extreme → requires **very few splits** to isolate → assigned a **high anomaly score**

```
Anomaly Score = 2^( -average_path_length / c(n) )

Where:
  average_path_length → mean number of splits needed across all trees
  c(n)               → expected path length for a dataset of size n
  Score → 1          → almost certainly an anomaly (zero-day threat)
  Score → 0          → normal network behavior
```

### 📊 Feature Engineering

| Feature | Description | Normal Range |
|---------|-------------|--------------|
| `bytes_sent` | Total bytes from source to destination | 500 – 5,000 |
| `bytes_received` | Total bytes from destination to source | 200 – 3,000 |
| `duration` | Connection lifetime in seconds | 0.1 – 30 |
| `missed_bytes` | Dropped / unacknowledged packet bytes | 0 – 50 |
| `packets_sent` | Total packets from source | 5 – 100 |
| `packets_received` | Total packets from destination | 5 – 80 |

---

## 🚀 Future Enhancements

- [ ] **SHAP Explainability** — Integrate SHAP values to explain *why* a packet was flagged as anomalous
- [ ] **Real PCAP Ingestion** — Replace synthetic data with live packet capture using `Scapy` or `PyShark`
- [ ] **Alert Severity Scoring** — Add a tiered risk scoring system (Low / Medium / High / Critical)
- [ ] **Email / Slack Alerting** — Push real-time threat notifications to security teams
- [ ] **Docker Deployment** — Containerize the full stack for one-command deployment
- [ ] **AutoML Benchmarking** — Compare Isolation Forest against DBSCAN, One-Class SVM, and Autoencoders

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

---

## 👤 Author

<div align="center">

### 

[![GitHub](https://img.shields.io/badge/GitHub-dhruv--005-181717?style=for-the-badge&logo=github)](https://github.com/dhruv-005)
[![Portfolio](https://img.shields.io/badge/Portfolio-Dhruv's%20Portfolio-FF5722?style=for-the-badge&logo=google-chrome)](https://dhruv-005.github.io/Dhruv-s_Portfolio/)
[![Email](https://img.shields.io/badge/Email-dhruvsonani3312%40gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:dhruvsonani3312@gmail.com)

*"Building intelligent systems that make the digital world safer."*

</div>

---

<div align="center">

**Built for the cybersecurity community — contributions welcome!**

⭐ Star this repo if you found it useful ⭐

</div>
