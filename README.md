
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
| ![Prediction](![image](https://github.com/user-attachments/assets/e9bbbfd3-ebb3-43aa-ad58-a6f1762e83f5)
) | ![Dashboard](![image](https://github.com/user-attachments/assets/ae4dcc75-e7cd-4be8-9399-b29a88e0557d)
) |

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
