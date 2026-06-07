import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(
    page_title="Data Analyzer Pro",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Interaktywny Dashboard Analityczny")
st.markdown("Witaj w demonstracyjnym dashboardzie. Narzędzie to analizuje wygenerowane dane giełdowe i sprzedażowe za pomocą **Streamlit** oraz **Pandas**.")

# Sidebar controls
st.sidebar.header("Ustawienia Filtrowania")
days_to_predict = st.sidebar.slider("Dni do predykcji", min_value=1, max_value=30, value=7)
data_type = st.sidebar.selectbox("Wybierz zestaw danych", ["Giełda (Tech)", "E-Commerce", "Kryptowaluty"])

# Generate mock data
@st.cache_data
def load_data(type_name):
    dates = pd.date_range(start="2023-01-01", periods=100)
    if type_name == "Giełda (Tech)":
        data = np.random.randn(100, 3).cumsum(axis=0) + 100
        columns = ["AAPL", "GOOGL", "MSFT"]
    elif type_name == "E-Commerce":
        data = np.random.randn(100, 3).cumsum(axis=0) * 10 + 500
        columns = ["Ubrania", "Elektronika", "Dom"]
    else:
        data = np.random.randn(100, 3).cumsum(axis=0) * 5 + 50
        columns = ["BTC", "ETH", "SOL"]
    
    return pd.DataFrame(data, index=dates, columns=columns)

with st.spinner('Ładowanie modeli i danych...'):
    time.sleep(0.5)
    df = load_data(data_type)

st.subheader(f"📈 Trendy dla: {data_type}")
st.line_chart(df)

# Stats row
col1, col2, col3 = st.columns(3)
col1.metric("Średnia wartość", f"{df.mean().mean():.2f}", "+1.2%")
col2.metric("Najwyższy pik", f"{df.max().max():.2f}", "+5.4%")
col3.metric("Zmienność (7d)", "Wysoka", "-2.1%")

st.markdown("---")
st.markdown("Stworzone w celach demonstracyjnych do portfolio na GitHubie.")
