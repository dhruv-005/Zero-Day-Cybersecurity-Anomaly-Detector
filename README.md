<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D0D0D,50:1A1A2E,100:16213E&height=200&section=header&text=Zero-Day%20Detector&fontSize=70&fontColor=00FF41&fontAlignY=38&desc=Autonomous%20Cybersecurity%20Anomaly%20Detection%20Engine&descAlignY=60&descSize=20&animation=fadeIn" width="100%"/>

# 🛡️ When Signatures Fail — Intelligence Prevails 🛡️

### *No Labels. No Signatures. No Mercy for Anomalies.*

<br/>

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Engine-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Live%20Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Layer-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Computation-013243?style=for-the-badge&logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00FF41?style=for-the-badge&logo=opensourceinitiative&logoColor=black)

<br/>

> 🔴 Traditional cybersecurity relies on **known signatures** — useless against zero-day attacks.
> This project **flips the paradigm** by learning the exact mathematical baseline of normal
> network traffic and **instantly flagging any deviation** as a potential zero-day threat —
> with **no labeled attack data required**.

<br/>

[![⭐ Star this repo](https://img.shields.io/github/stars/dhruv-005/Zero-Day-Cybersecurity-Anomaly-Detector?style=for-the-badge&logo=github&color=00FF41&logoColor=black&label=⭐%20Star%20This%20Repo)](https://github.com/dhruv-005/Zero-Day-Cybersecurity-Anomaly-Detector)
[![🍴 Fork](https://img.shields.io/github/forks/dhruv-005/Zero-Day-Cybersecurity-Anomaly-Detector?style=for-the-badge&logo=github&color=FF4B4B&logoColor=white&label=🍴%20Fork)](https://github.com/dhruv-005/Zero-Day-Cybersecurity-Anomaly-Detector/fork)

</div>

---

<div align="center">

## ⚡ The Detection Pipeline at a Glance

```
╔═══════════════════╗    ╔═══════════════════╗    ╔═════════════════════════╗
║ 📡 Data Generator  ║──▶║  🧠 ML Training    ║──▶║  🖥️  Live Dashboard      ║
║                   ║    ║                   ║    ║                         ║
║ normal_traffic    ║    ║ IsolationForest   ║    ║ Real-Time Threat Scores ║
║ live_traffic .csv ║    ║ scaler .pkl       ║    ║ Visual Anomaly Alerts   ║
╚═══════════════════╝    ╚═══════════════════╝    ╚═════════════════════════╝
        │                         │                           │
   generate_data.py          train_model.py               app.py
```

</div>

---

## 📖 Table of Contents

| # | Section | Description |
|---|---------|-------------|
| 1 | [🚀 Project Overview](#-project-overview) | What this project is and why it matters |
| 2 | [✨ Key Features](#-key-features) | All major capabilities at a glance |
| 3 | [🛠️ Architecture & Tech Stack](#️-architecture--tech-stack) | Technologies powering the system |
| 4 | [📂 Project Structure](#-project-structure) | File and folder layout |
| 5 | [⚙️ Installation & Setup](#️-installation--setup) | Step-by-step setup guide |
| 6 | [🧭 Usage Guide](#-usage-guide) | How to run the full pipeline |
| 7 | [🔬 How It Works Under the Hood](#-how-it-works-under-the-hood) | Deep-dive into the ML internals |
| 8 | [🖼️ Screenshots & Output](#️-screenshots--output) | Visual results and dashboard preview |
| 9 | [🚀 Future Enhancements](#-future-enhancements) | Planned features and roadmap |
| 10 | [📜 License](#-license) | Licensing information |
| 11 | [👤 Author](#-author) | About the creator |

---

## 🚀 Project Overview

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════╗
║              🔴  THE ZERO-DAY PROBLEM                                ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Signature-Based IDS  →  Knows only PAST threats. Blind to new ones  ║
║  Zero-Day Detector    →  Learns NORMAL. Flags EVERYTHING else.       ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

</div>

In real-world enterprise environments, **novel cyber attacks (zero-day exploits)** emerge before security vendors can patch or even classify them. Signature-based Intrusion Detection Systems (IDS) are completely blind to these attacks — they only recognize what they have seen before.

**Zero-Day Detector** solves this by deploying an **Isolation Forest** — an unsupervised ML algorithm that trains exclusively on benign network traffic. It needs no attack examples, no labels, and no prior knowledge of threats. It simply learns what *normal looks like* — and flags everything that deviates.

<br/>

### 🎯 What It Does

```
📡 Synthetic Network Logs  ──▶  🧠 Unsupervised Training  ──▶  🖥️ Live Dashboard  ──▶  🔴 Threat Alerts
    (generate_data.py)              (train_model.py)               (app.py)            (real-time)
```

<br/>

### 💡 What You Will Learn From This Project

| Concept | How This Project Demonstrates It |
|---------|----------------------------------|
| 🧠 **Unsupervised ML** | Isolation Forest detects anomalies with zero labeled attack data |
| 📡 **Synthetic Data Engineering** | Realistic network telemetry generated programmatically with injected anomalies |
| ⚙️ **MLOps Pipeline** | Train → Scale → Serialize → Load → Predict in a clean modular flow |
| 🖥️ **Real-Time Dashboards** | Streamlit simulates a live Security Operations Center (SOC) feed |
| 🔢 **Anomaly Scoring Math** | Isolation path-length scoring interpreted as a threat probability |
| 🛡️ **Security AI Thinking** | Designing AI systems for adversarial, label-scarce environments |

---

## ✨ Key Features

<div align="center">

```
┌────────────────────────────────────────────────────────────────────────┐
│                    DETECTOR FEATURE SET                                │
├────────────────────────────────────────────────────────────────────────┤
│  📡  Synthetic Network Data Gen    🧠  Unsupervised Isolation Forest    │
│  ⚙️  Automated MLOps Pipeline      🖥️  Live Streamlit SOC Dashboard     │
│  📊  Feature-Rich Telemetry        🔴  Real-Time Anomaly Alerts         │
│  💾  Joblib Model Serialization    📈  Anomaly Score Visualization      │
└────────────────────────────────────────────────────────────────────────┘
```

</div>

| # | 🏷️ Feature | 📝 Description |
|---|------------|----------------|
| 1 | 📡 **Synthetic Data Generation** | Custom script generates realistic network telemetry — bytes, duration, missed packets — with injected randomized anomalies |
| 2 | 🧠 **Unsupervised ML Detection** | Scikit-Learn's `IsolationForest` detects threats without a single labeled attack example |
| 3 | ⚙️ **Automated MLOps Pipeline** | Seamlessly handles data scaling (`StandardScaler`), model training, and artifact serialization (`Joblib`) |
| 4 | 🖥️ **Live SOC Dashboard** | Streamlit UI simulates live network packet ingestion, predicts threats in real-time, and triggers visual alerts |
| 5 | 📊 **6-Feature Telemetry** | Captures bytes sent/received, duration, missed bytes, packets sent/received per connection |
| 6 | 🔴 **Instant Threat Flagging** | Anomalous packets are flagged in milliseconds with color-coded threat indicators |

---

## 🛠️ Architecture & Tech Stack

<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║                   TECHNOLOGY LAYERS                          ║
╠══════════════════════════════════════════════════════════════╣
║  🖥️  Streamlit              →  Live SOC Monitoring Dashboard ║
║  🧠  Scikit-Learn           →  Isolation Forest ML Engine    ║
║  💾  Joblib                 →  Model Artifact Serialization  ║
║  🐼  Pandas + NumPy         →  Data Generation & Processing  ║
║  🔢  StandardScaler         →  Feature Normalization Layer   ║
║  🐍  Python 3.8+            →  Core Runtime                  ║
╚══════════════════════════════════════════════════════════════╝
```

</div>

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | **Python** | `3.8+` | Core runtime |
| ![Sklearn](https://img.shields.io/badge/-Scikit--Learn-F7931E?logo=scikitlearn&logoColor=white) | **Scikit-Learn** | Latest | Isolation Forest anomaly detection |
| ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white) | **Streamlit** | Latest | Real-time SOC monitoring dashboard |
| ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white) | **Pandas** | Latest | Data manipulation and CSV handling |
| ![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white) | **NumPy** | Latest | Numerical computation and data generation |
| ![Joblib](https://img.shields.io/badge/-Joblib-FF6B6B?logo=python&logoColor=white) | **Joblib** | Latest | ML model and scaler serialization |

---

## 📂 Project Structure

```
📦 zero_day_detector/
│
├── 📄 app.py                    ← 🖥️  Streamlit dashboard — live threat monitoring UI
├── 📄 generate_data.py          ← 📡 Synthetic network log generator with anomaly injection
├── 📄 train_model.py            ← 🧠 Unsupervised ML training pipeline & artifact export
├── 📄 requirements.txt          ← 📦 Pinned Python dependencies
├── 📄 .gitignore                ← 🚫 Git exclusion rules (models, data, cache)
├── 📄 README.md                 ← 📖 You are reading this file
│
├── 📁 data/                     ← Auto-generated datasets (excluded from Git)
│   ├── 📄 normal_traffic.csv    ← Baseline benign network traffic logs
│   └── 📄 live_traffic.csv      ← Simulated live packet stream for dashboard
│
└── 📁 models/                   ← Serialized ML artifacts (excluded from Git)
    ├── 🧠 isolation_forest.pkl  ← Trained Isolation Forest model
    └── ⚙️  scaler.pkl            ← Fitted StandardScaler transformer
```

> 💡 **Note:** The `data/` and `models/` directories are listed in `.gitignore`
> and will be **auto-created** when you run the pipeline scripts locally.

---

## ⚙️ Installation & Setup

### ✅ Prerequisites

| Requirement | Details |
|-------------|---------|
| 🐍 **Python** | Version `3.8` or higher |
| 📦 **pip** | Latest version recommended |
| 🐙 **Git** | For cloning the repository |

---

### 📋 Step 1 — Clone the Repository

```bash
git clone https://github.com/dhruv-005/Zero-Day-Cybersecurity-Anomaly-Detector.git
cd Zero-Day-Cybersecurity-Anomaly-Detector
```

---

### 📋 Step 2 — Create & Activate Virtual Environment

```bash
# ── Create the environment ───────────────────────────────────────────
python -m venv venv

# ── Activate on Linux / macOS ────────────────────────────────────────
source venv/bin/activate

# ── Activate on Windows ──────────────────────────────────────────────
venv\Scripts\activate

# Your terminal prompt should now show (venv)
```

---

### 📋 Step 3 — Install All Dependencies

```bash
pip install -r requirements.txt
```

---

### 📋 Step 4 — Create Required Directories

```bash
mkdir data models
```

> ✅ You are now fully set up and ready to run the pipeline.

---

## 🧭 Usage Guide

> ⚠️ **Important:** Run these three steps **in order** for a complete end-to-end demo.

---

### ▶️ Step 1 — Generate Synthetic Network Data

```bash
python generate_data.py
```

```
✅ Expected Output:
   → data/normal_traffic.csv   (benign baseline traffic)
   → data/live_traffic.csv     (mixed stream with injected anomalies)
```

---

### ▶️ Step 2 — Train the Anomaly Detection Model

```bash
python train_model.py
```

```
✅ Expected Output:
   → models/isolation_forest.pkl   (trained Isolation Forest)
   → models/scaler.pkl             (fitted StandardScaler)
```

---

### ▶️ Step 3 — Launch the Live Monitoring Dashboard

```bash
streamlit run app.py
```

```
✅ Expected Output:
   → Local URL:   http://localhost:8501
   → Network URL: http://your-ip:8501

   Dashboard opens automatically in your default browser.
```

---

## 🔬 How It Works Under the Hood

### 1️⃣ End-to-End Pipeline Flow

```
╔═══════════════════════════════════════════════════════════════════════╗
║                        FULL SYSTEM PIPELINE                           ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║  ┌───────────────┐    ┌───────────────┐    ┌───────────────────────┐  ║
║  │ generate_     │    │  train_       │    │       app.py          │  ║
║  │ data.py       │───▶│  model.py     │───▶│  Streamlit Dashboard  │  ║
║  └───────────────┘    └───────────────┘    └───────────────────────┘  ║
║         │                    │                          │             ║
║         ▼                    ▼                          ▼             ║
║   normal_traffic        isolation_forest          Live Packet         ║
║   live_traffic          scaler.pkl                Stream Scoring      ║
║   .csv files            .pkl artifacts            + 🔴 Threat Alerts  ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---

### 2️⃣ The Isolation Forest Algorithm

<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║            🧠  HOW ISOLATION FOREST THINKS                    ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  NORMAL traffic   →  Dense & structured                      ║
║                   →  Needs MANY splits to isolate            ║
║                   →  HIGH path length → LOW anomaly score    ║
║                                                              ║
║  MALICIOUS traffic →  Sparse & extreme                       ║
║                   →  Needs VERY FEW splits to isolate        ║
║                   →  LOW path length → HIGH anomaly score    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

</div>

The **Isolation Forest** operates on a beautifully simple principle — **anomalies are easier to isolate than normal points**.

The algorithm builds an ensemble of random binary decision trees. For any data point:

- 🟢 **Normal traffic** is dense and clustered → requires **many random splits** to isolate → **low anomaly score**
- 🔴 **Malicious traffic** is sparse and extreme → requires **very few splits** to isolate → **high anomaly score**

```
                    Anomaly Score Formula
         ┌────────────────────────────────────────┐
         │                                        │
         │   Score  =  2 ^ ( -E(h) / c(n) )       │
         │                                        │
         │   E(h)  →  Average path length         │
         │            across all trees            │
         │                                        │
         │   c(n)  →  Expected path length        │
         │            for dataset of size n       │
         │                                        │
         │   Score → 1.0  =  ANOMALY  🔴          │
         │   Score → 0.0  =  NORMAL   🟢          │
         │                                        │
         └────────────────────────────────────────┘
```

---

### 3️⃣ Feature Engineering

| 📡 Feature | 📝 Description | 📊 Normal Range |
|------------|----------------|-----------------|
| `bytes_sent` | Total bytes from source to destination | `500 – 5,000` |
| `bytes_received` | Total bytes from destination to source | `200 – 3,000` |
| `duration` | Connection lifetime in seconds | `0.1 – 30` |
| `missed_bytes` | Dropped / unacknowledged packet bytes | `0 – 50` |
| `packets_sent` | Total packets transmitted from source | `5 – 100` |
| `packets_received` | Total packets received at destination | `5 – 80` |

---

### 4️⃣ MLOps Artifact Flow

```
Raw CSV Data
     │
     ▼
StandardScaler  ──▶  Normalized Features  ──▶  IsolationForest.fit()
     │                                                  │
     ▼                                                  ▼
scaler.pkl                                   isolation_forest.pkl
     │                                                  │
     └──────────────────┬───────────────────────────────┘
                        │
                        ▼
              app.py loads both artifacts
                        │
                        ▼
             Live packet scored in real-time
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
          🟢 NORMAL           🔴 ANOMALY
```

---

## 🖼️ Screenshots & Output

> 📸 **Visual results generated after a successful pipeline run.**

---

### 🖥️ Live SOC Monitoring Dashboard

<div align="center">

> *The Streamlit dashboard simulating a real-time Security Operations Center feed —
> each packet is scored and flagged instantly.*

Live Dashboard<img width="1366" height="700" alt="Screenshot_2026-04-27_11_10_23" src="https://github.com/user-attachments/assets/27adfb41-c73c-4100-8bfa-2e1461910c17" /><img width="1366" height="698" alt="Screenshot_2026-04-27_11_13_01" src="https://github.com/user-attachments/assets/91277310-b218-4414-bac7-a32abcf30b14" /><img width="1366" height="692" alt="Screenshot_2026-04-27_11_10_59" src="https://github.com/user-attachments/assets/341eb6f2-6633-4b5d-b3d4-e7b955bd7297" />


*Real-time threat detection with color-coded anomaly alerts at `http://localhost:8501`*

</div>

---

### 📊 Anomaly Score Distribution

<div align="center">

> *Distribution of Isolation Forest anomaly scores across the live packet stream —
> scores near 1.0 represent high-confidence zero-day threats.*

Anomaly Scores<img width="1366" height="692" alt="Screenshot_2026-04-27_11_10_59" src="https://github.com/user-attachments/assets/ecc20651-b4ac-4e68-b462-527c32d38ea6" />


*Normal traffic clusters near 0.0 — anomalies spike toward 1.0*

</div>

---

### 📁 Generated Pipeline Artifacts

<div align="center">

> *Auto-generated files after running all three pipeline steps.*

Pipeline Output <img width="1366" height="601" alt="Screenshot_2026-04-27_17_59_44" src="https://github.com/user-attachments/assets/8f14d798-b9d1-4a4a-9e24-573da29f6acc" />
<img width="1366" height="600" alt="Screenshot_2026-04-27_17_59_56" src="https://github.com/user-attachments/assets/597c88bc-f6ef-447b-a742-437d94c8ca52" />


*`data/` CSVs and `models/` PKL artifacts — all verified and ready for the dashboard*

</div>

---

## 🚀 Future Enhancements

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║           🗺️  ZERO-DAY DETECTOR ROADMAP                   ║
╚══════════════════════════════════════════════════════════╝
```

</div>

| Status | 🏷️ Feature | 📝 Description |
|--------|------------|----------------|
| 🔲 | **🔍 SHAP Explainability** | Integrate SHAP values to explain *why* each packet was flagged |
| 🔲 | **📡 Real PCAP Ingestion** | Replace synthetic data with live capture via `Scapy` or `PyShark` |
| 🔲 | **🚨 Alert Severity Tiers** | Tiered risk scoring — Low / Medium / High / Critical |
| 🔲 | **📧 Email & Slack Alerting** | Push real-time threat notifications to security teams |
| 🔲 | **🐳 Docker Deployment** | Containerize the full stack for one-command deployment |
| 🔲 | **🤖 AutoML Benchmarking** | Compare against DBSCAN, One-Class SVM, and Autoencoder models |
| 🔲 | **📊 Threat Analytics Dashboard** | Historical threat trend visualization and session replay |
| 🔲 | **🔐 GeoIP Threat Mapping** | Map flagged IPs to geographic locations on a live threat map |

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
Copyright (c) 2024 Dhruv Sonani
```

---

## 👤 Author

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:16213E,50:0F3460,100:533483&height=120&section=footer&fontSize=16&fontColor=00FF41&text=Built%20with%20%F0%9F%9B%A1%EF%B8%8F%20for%20the%20Cybersecurity%20Community&fontAlignY=65&animation=fadeIn" width="100%"/>

### 🛡️ Dhruv Sonani

*"Building intelligent systems that make the digital world safer."*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-dhruv--005-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dhruv-005)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit%20Now-FF4B4B?style=for-the-badge&logo=google-chrome&logoColor=white)](https://dhruv-005.github.io/Dhruv-s_Portfolio/)
[![Email](https://img.shields.io/badge/Email-dhruvsonani3312%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dhruvsonani3312@gmail.com)

<br/>

---

**🔴 Built with the cybersecurity community — contributions welcome! 🔴**

**⭐ Star this repo if it helped you think differently about AI security ⭐**

<br/>

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/-Scikit--Learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Joblib](https://img.shields.io/badge/-Joblib-FF6B6B?style=flat-square&logo=python&logoColor=white)

</div>
