# 💓 FitPulse: Health Anomaly Detection System

FitPulse is an intelligent health monitoring dashboard designed to detect physiological anomalies in fitness tracker data. Using a combination of **medical-rule thresholds** and **statistical analysis**, the system identifies potential health risks such as Tachycardia, Bradycardia, and Hypoxia.



## 🚀 Features
* **Multi-Source Data Sync**: Support for CSV and JSON fitness data exports.
* **Real-time Anomaly Engine**: Detects heart rate and SpO2 irregularities based on clinical standards.
* **Interactive Visualizations**: Dynamic timelines and distribution charts powered by Plotly.
* **Behavioral Analysis**: Distinguishes between active states and sleep-state anomalies.
* **Intelligence Export**: Generate instant PDF/TXT summary reports and cleaned anomaly logs.

## 🛠️ Tech Stack
* **Language**: Python 3.9+
* **Dashboard**: [Streamlit](https://streamlit.io/)
* **Data Science**: Pandas, NumPy
* **Visualization**: Plotly Express, Graph Objects
* **License**: MIT

## 📋 Medical Logic & Thresholds
The system calculates an **Anomaly Score** by aggregating the following triggers:
| Condition | Threshold | Indicator |
| :--- | :--- | :--- |
| **Tachycardia** | > 120 BPM | High heart rate during rest/light activity |
| **Bradycardia** | < 45 BPM | Abnormally low heart rate |
| **Hypoxia** | < 94% SpO2 | Low blood oxygen saturation |
| **Sleep Conflict** | > 50 Steps | High movement detected during sleep state |

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/FitPulse.git](https://github.com/YOUR_USERNAME/FitPulse.git)
   cd FitPulse


   # 💓 FitPulse: Health Anomaly Detection System

## 🚀 Live Demo
**[Click here to view the live dashboard](https://fitpulse-health-monitor-an-ai-powered-dashboard.streamlit.app/)**

---