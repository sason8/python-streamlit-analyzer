# Python Streamlit Analyzer 📊

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

An interactive data analysis dashboard built entirely in Python using Streamlit, Pandas, and Numpy.

## Overview
This application demonstrates real-time data visualization and analysis. It generates dynamic datasets (Stock Market, E-Commerce, Cryptocurrencies) and displays them using interactive charts and metrics.

## Quick Start
```bash
# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app.py
```

## Features
- **Interactive Filtering:** Sidebars to manipulate data dynamically.
- **Data Caching:** High performance with `@st.cache_data`.
- **Metrics & KPIs:** Clear display of average values, peaks, and volatility.

## License
MIT License
