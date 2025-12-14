import streamlit as st
import requests  # добавлен импорт

st.title("Property Details Form 🏡")
st.markdown("Please fill in the details of the property:")

col1, col2, col3 = st.columns(3)

with col1:
    square_feet = st.number_input("🏠 Area (m²)", min_value=30, max_value=500, value=60)
    num_bedrooms = st.number_input("🛏 Bedrooms", min_value=1, max_value=10, value=2)
    num_bathrooms = st.number_input("🛁 Bathrooms", min_value=0, max_value=10, value=1)

with col2:
    Num_Floors = st.number_input("🏢 Floors", min_value=0, max_value=10, value=1)
    Year_Built = st.number_input("📅 Year Built", min_value=1800, max_value=2025, value=2000)
    Has_Garden = st.selectbox("🌳 Has Garden?", [0, 1])

with col3:
    Has_Pool = st.selectbox("🏊 Has Pool?", [0, 1])
    Garage_Size = st.number_input("🚗 Garage Size (m²)", min_value=0, max_value=200, value=20)
    Location_Score = st.slider("📍 Neighborhood Score", min_value=0, max_value=10, value=5)
    Distance_to_Center = st.number_input("🗺 Distance to Center (km)", min_value=0, max_value=50, value=5)

if st.button("✅ Predict"):
    data = {
        "square_feet": square_feet,
        "num_bedrooms": num_bedrooms,
        "num_bathrooms": num_bathrooms,
        "Num_Floors": Num_Floors,
        "Year_Built": Year_Built,
        "Has_Garden": Has_Garden,
        "Has_Pool": Has_Pool,
        "Garage_Size": Garage_Size,
        "Location_Score": Location_Score,
        "Distance_to_Center": Distance_to_Center
    }
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        result = response.json()
        # Исправлено: ожидаем ключ "price" (бэкенд теперь возвращает "price")
        st.success(f"Predicted price: ${result['price']:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")