# 🌾 Farm Input Price Volatility Analysis & Forecasting

📉 *Forecasting fertilizer, diesel, and seed price swings across Indian states*

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

This project uses **time-series forecasting** (ARIMA & Prophet) to predict the price volatility of key agricultural inputs — fertilizers, diesel, and seeds — across 10+ Indian states. With an emphasis on seasonality and price shock detection, it aims to support **farmer profitability** and **policy planning**.

---

## 🛠️ Tech Stack

- **Python**: `Pandas`, `NumPy`, `Prophet`, `Statsmodels`, `Matplotlib`, `Seaborn`
- **Forecasting Models**: ARIMA, Prophet
- **Data Cleaning & Wrangling**
- **SQL**: MySQL for multi-source backend storage
- **Visualization**: Power BI (interactive dashboards, slicers, maps)
- **Web Scraping**: `Requests`, `BeautifulSoup`, `Selenium`
- **Automation**: `schedule`, `cron` jobs
- **Metrics**: MAPE, RMSE, MAE

---

## 📊 Project Highlights

- 🔮 **Forecasted** fertilizer, diesel, and seed prices with **80%+ accuracy** across Indian states
- 🌾 Created **seasonal cost trend dashboards** in Power BI for **Rabi/Kharif crop cycle** planning
- 🧠 Performed **anomaly detection** and **seasonal decomposition** on historical input price data
- 🗃️ **SQL backend** integration for dynamic, multi-dimensional queries
- ⚙️ **Automated pipeline** for weekly updates and live forecasts

---

## 📈 Unique KPIs Tracked

- **Input Price Volatility Index (IPVI)**
- **Forecast Accuracy Score**
- **Early Price Spike Alert Lead Time**
- **State-wise Seasonal Price Deviation (%)**
- **Estimated Savings from Forecast Adoption**

---

## 📂 Project Structure

```bash
farm-input-price-forecasting/
├── data/                  # Raw & processed data
├── notebooks/             # Jupyter notebooks for EDA & modeling
├── src/                   # Core scripts (scraping, forecasting, automation)
├── dashboards/            # Power BI files (.pbix)
├── sql/                   # DB schema and query scripts
├── reports/               # Charts & visual outputs
├── requirements.txt       # Python dependencies
└── README.md              # This file
```
