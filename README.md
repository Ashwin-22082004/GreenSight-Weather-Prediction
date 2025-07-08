
# 🌦️ GreenSight – Weather Prediction System

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
  <img src="https://img.shields.io/github/languages/top/yourusername/GreenSight?style=for-the-badge" />
  <img src="https://img.shields.io/github/license/yourusername/GreenSight?style=for-the-badge"/>
</p>

## 🧠 Overview

**GreenSight** is a smart, machine learning-powered weather prediction system designed to forecast essential weather parameters like **temperature**, **humidity**, **rainfall**, and **wind speed**. It offers both real-time weather data via APIs and predictive analytics trained on historical datasets.

Whether you're a researcher, student, farmer, or traveler, GreenSight helps you stay prepared for what the sky holds.

---

## 🔍 Features

- 🧠 **ML-Based Prediction** using regression and time-series models  
- 🌐 **Live Data** fetched via OpenWeatherMap API  
- 📍 **Location-Specific Forecasts** via latitude/longitude or city name  
- 📈 **Historical Trend Visualization**  
- ⚠️ **Alerts for Abnormal Conditions** like storms or heavy rainfall  
- 🌱 Designed to assist agriculture, travel, and environmental planning

---

## 🛠️ Tech Stack

| Category       | Technologies |
|----------------|--------------|
| **Languages**  | Python |
| **Libraries**  | Pandas, NumPy, Matplotlib, Scikit-learn, Seaborn |
| **Web/UI**     | Streamlit / Flask |
| **API**        | OpenWeatherMap API |
| **ML Models**  | Linear Regression, Random Forest, XGBoost |

---

## 📊 Screenshots

| Prediction Page | Dashboard |
|-----------------|-----------|
| ![Prediction](![image](https://github.com/user-attachments/assets/a3f51964-2c2d-4357-bf81-6806823dae94)![image](https://github.com/user-attachments/assets/ac5feaa1-b5ba-40ea-8a84-360bf2a270ab)) | ![Dashboard](![image](https://github.com/user-attachments/assets/1cc01e5c-4c8a-4688-ad0f-505d506d8da6)) |

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/GreenSight.git
cd GreenSight

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
