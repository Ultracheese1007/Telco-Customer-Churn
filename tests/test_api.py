# tests/test_api.py
import requests

def test_healthcheck():
    """Test /api/healthcheck returns OK"""
    url = "http://localhost:8000/api/healthcheck"
    res = requests.get(url)
    assert res.status_code == 200
    assert "status" in res.json()

def test_prediction():
    """Test /api/predict returns valid response"""
    url = "http://localhost:8000/api/predict"
    payload = {
        "gender": 1, "SeniorCitizen": 0, "Partner": 1, "Dependents": 0,
        "tenure": 12, "PhoneService": 1, "MultipleLines": 0,
        "InternetService": 1, "OnlineSecurity": 0, "OnlineBackup": 0,
        "DeviceProtection": 0, "TechSupport": 0, "StreamingTV": 0,
        "StreamingMovies": 0, "Contract": 1, "PaperlessBilling": 1,
        "PaymentMethod": 1, "MonthlyCharges": 70.0, "TotalCharges": 500.0
    }

    res = requests.post(url, json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "prediction" in data
    assert any(k in data for k in ["probability", "churn_probability"])
