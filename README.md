# 🧠 Telco Customer Churn 

A fully Dockerized **FastAPI + Streamlit** application that predicts customer churn using a trained ML model and provides rich exploratory data analysis (EDA) visualizations.

---

## 🚀 Features

- 🧩 **FastAPI Backend** — serves churn prediction using a trained XGBoost model (`best_xgb.pkl`)
- 📊 **Streamlit Frontend** — interactive dashboard for customer churn prediction & EDA visualization
- 🐳 **Dockerized Architecture** — separate containers for API & App connected via custom Docker network
- 📈 **Reproducible Reports** — auto-generated EDA plots in `/reports/eda_results/`
- ⚙️ **Configurable via `.env`** — set `API_URL` and model path easily

---

## 🏗️ Project Structure
```
├── LICENSE
├── Makefile
├── README.md 
├── __pycache__
│   └── test_eda_run.cpython-311-pytest-8.4.2.pyc
├── data
│   ├── processed
│   │   └── telco_processed.csv
│   └── raw
│       └── Telco-Customer-Churn.csv
├── docker
│   ├── Dockerfile.api
│   ├── Dockerfile.app
│   ├── docker-compose.yml
│   └── env
│       ├── api.env
│       └── app.env
├── main.py
├── models
│   ├── baseline_rf.pkl
│   ├── best_xgb.pkl
│   ├── final_model.pkl
│   └── xgboost_tuned.pkl
├── reports
│   ├── eda_results
│   │   ├── categorical_overview.png
│   │   ├── correlation_heatmap.png
│   │   ├── eda_summary.html
│   │   ├── numerical_boxplots_p1.png
│   │   ├── numerical_boxplots_p2.png
│   │   ├── numerical_boxplots_p3.png
│   │   ├── numerical_boxplots_p4.png
│   │   ├── numerical_distributions_p1.png
│   │   ├── numerical_distributions_p2.png
│   │   ├── numerical_distributions_p3.png
│   │   ├── numerical_distributions_p4.png
│   │   └── overview_churn_distribution.png
│   └── model_eval
│       ├── RandomForest_pr.png
│       ├── RandomForest_report.txt
│       ├── RandomForest_roc.png
│       ├── XGBoost_pr.png
│       ├── XGBoost_report.txt
│       └── XGBoost_roc.png
├── requirements.txt
├── run_api.sh
├── run_app.sh
├── src
│   ├── api
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routers
│   │   ├── schemas
│   │   └── services
│   ├── app
│   │   ├── components
│   │   └── streamlit_app.py
│   ├── config.py
│   ├── eda
│   │   ├── categorical_analysis.py
│   │   ├── correlation_analysis.py
│   │   ├── numerical_analysis.py
│   │   ├── overview.py
│   │   ├── report_generator.py
│   │   └── utils_eda.py
│   ├── model_eval.py
│   ├── model_train.py
│   ├── preprocess.py
│   └── utils.py
├── test_eda_run.py
└── tests
    ├── conftest.py
    ├── test_api.py
    ├── test_model_train.py
    └── test_preprocess.py

```

## 🐳 Run Locally with Docker

### 1️⃣ Clean and Rebuild Everything
```bash
docker stop $(docker ps -aq) 2>/dev/null || true
docker rm -f $(docker ps -aq) 2>/dev/null || true
docker network rm telco-net 2>/dev/null || true
docker network create telco-net
```

### 2️⃣ Build Images
```bash
docker build --no-cache -f docker/Dockerfile.api -t churn-api .
docker build --no-cache -f docker/Dockerfile.app -t churn-app .

```
### 3️⃣ Run Containers
```bash
docker run -d --name telco-api --network telco-net -p 8000:8000 churn-api
docker run -d --name telco-app --network telco-net -p 8501:8501 churn-app
```
### 4️⃣ Access
- 🌐 Streamlit UI: http://localhost:8501

- ⚙️ FastAPI docs: http://localhost:8000/docs

## 🧠 Model Overview
The backend uses a tuned XGBoost classifier trained on Telco churn data.
It predicts churn probability (churn_probability) given key customer features such as:

- Gender
- Tenure
- Monthly Charges
- Total Charges
- Partner
- Dependents

## 📊 Exploratory Data Analysis (EDA)
Streamlit automatically displays all `.png` visualizations found in `reports/eda_results/`,including churn distribution, correlation heatmaps, and boxplots.

## 👩‍💻 Author
Developed by Xinmei Ma (Leah)
Data Science & Society MSc — Tilburg University

