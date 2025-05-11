import streamlit as st
import requests

st.set_page_config(page_title="Electricity Demand Predictor", layout="centered")

st.title("⚡ Electricity Demand Prediction (Next Day)")
st.markdown("Fill in the details below to get a prediction of electricity demand for tomorrow.")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        temperature = st.number_input("Temperature (°C)", min_value=-30.0, max_value=60.0, value=25.0)
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=45.0)
        wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=100.0, value=5.0)
        pressure = st.number_input("Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1015.0)

    with col2:
        precip_intensity = st.number_input("Precipitation Intensity", min_value=0.0, max_value=10.0, value=0.1)
        hour = st.slider("Hour of the Day", 0, 23, 14)
        day_of_week = st.selectbox("Day of the Week", list(range(7)), format_func=lambda x: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][x])
        month = st.slider("Month", 1, 12, 5)
        season = st.selectbox("Season", [1, 2, 3, 4], format_func=lambda x: ["Spring", "Summer", "Autumn", "Winter"][x - 1])

    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
        "temperature": temperature,
        "humidity": humidity,
        "windSpeed": wind_speed,
        "pressure": pressure,
        "precipIntensity": precip_intensity,
        "hour": hour,
        "day_of_week": day_of_week,
        "month": month,
        "season": season
    }

    try:
        response = requests.post("http://localhost:5000/predict", json=payload)
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"✅ Predicted Electricity Demand (Next Day): **{prediction:.2f} kWh**")
        else:
            st.error("❌ Failed to get prediction from backend.")
    except Exception as e:
        st.error(f"🚫 Error connecting to backend: {e}")
