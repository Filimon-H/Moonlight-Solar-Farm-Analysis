# 🌞 Moonlight Solar Farm Analysis

This project analyzes solar irradiance and environmental data to help identify the most suitable location for a solar panel installation across multiple countries.

## 📌 Objective

- Compare GHI, DNI, and DHI across regions
- Analyze how temperature, humidity, and wind affect solar output
- Evaluate the impact of sensor/module cleaning

## 📊 Key Features

- Time series analysis (hourly/monthly)
- Outlier detection and cleaning
- Correlation and scatter plots
- Wind rose visualizations
- Cleaning impact on ModA and ModB
- Exportable cleaned dataset

## 📁 Data Columns

Includes:
- `GHI`, `DNI`, `DHI`: Solar irradiance (W/m²)
- `Tamb`: Temperature (°C)
- `RH`: Humidity (%)
- `WS`, `WSgust`, `WD`: Wind metrics
- `Cleaning`: Module cleaning flag
- `TModA`, `TModB`: Module temperatures

## 🚀 How to Use

1. Clone the repo
2. Run Jupyter notebooks
3. View visualizations and insights per country

## 📦 Tools

- Python, Pandas, Matplotlib, Seaborn, Windrose, SciPy

---

📁 Data-driven insights to power smarter solar panel placement.