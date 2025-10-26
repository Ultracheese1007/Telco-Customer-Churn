# src/app/streamlit_app.py
import streamlit as st
import requests
import os
from src.app.components.charts import display_eda_charts
from src.app.components.layout import set_page_style


# ===============================
# PAGE SETUP
# ===============================
st.set_page_config(page_title="Telco Churn Dashboard", layout="wide")
set_page_style()

st.title("📊 Telco Customer Churn Prediction App")
st.markdown(
    "This interactive dashboard allows you to predict **customer churn** "
    "using a trained ML model and view exploratory data insights."
)


# ===============================
# API CONFIGURATION
# ===============================
# The FastAPI service name in Docker Compose is 'telco-api'
API_URL = os.getenv("API_URL", "http://telco-api:8000/api/predict")


# ===============================
# SIDEBAR INPUT FORM
# ===============================
st.sidebar.header("🔧 Customer Features")

# Example feature inputs (must match the backend schema)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
partner = st.sidebar.selectbox("Has Partner?", ["Yes", "No"])
dependents = st.sidebar.selectbox("Has Dependents?", ["Yes", "No"])
tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", 0.0, 150.0, 70.0)
total_charges = st.sidebar.number_input("Total Charges ($)", 0.0, 9000.0, 500.0)


# ===============================
# FORMAT INPUT JSON
# ===============================
# The feature keys must align with the Pydantic model in FastAPI
input_data = {
    "gender": 1 if gender == "Male" else 0,
    "SeniorCitizen": senior_citizen,
    "Partner": 1 if partner == "Yes" else 0,
    "Dependents": 1 if dependents == "Yes" else 0,
    "tenure": tenure,
    "PhoneService": 1,
    "MultipleLines": 0,
    "InternetService": 1,
    "OnlineSecurity": 0,
    "OnlineBackup": 0,
    "DeviceProtection": 0,
    "TechSupport": 0,
    "StreamingTV": 0,
    "StreamingMovies": 0,
    "Contract": 1,
    "PaperlessBilling": 1,
    "PaymentMethod": 1,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
}


# ===============================
# PREDICTION SECTION
# ===============================
if st.button("🔮 Predict Churn"):
    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()

            # Support both naming conventions from backend:
            # Prefer 'churn_probability', fallback to 'probability'
            prob = result.get("churn_probability", result.get("probability"))
            prediction = result.get("prediction", "Unknown")

            st.success(f"Prediction: **{prediction}**")

            # If probability exists, display it as a percentage
            if prob is not None:
                try:
                    prob = float(prob)
                    if prob > 1:  # Convert from 0–100 scale if necessary
                        prob = prob / 100.0
                    st.metric(label="Churn Probability", value=f"{prob:.2%}")
                except Exception:
                    st.warning("⚠️ Churn probability format is invalid.")
            else:
                st.warning("⚠️ Churn probability not available.")
        else:
            st.error(f"❌ API Error: {response.text}")
    except Exception as e:
        st.error(f"🚫 Connection failed: {e}")


# ===============================
# EDA VISUALIZATION SECTION
# ===============================
st.markdown("---")
st.subheader("📈 Exploratory Data Analysis")
display_eda_charts()

st.caption("App developed by Leah Ma — Telco Customer Churn Project 🌱")
