# Innovate MLOps Pipeline 🚀

This project demonstrates a complete end-to-end MLOps workflow for deploying a machine learning model using CI/CD, Airflow, MLflow, DVC, Docker, Jenkins, and Kubernetes.

---

## 📁 Project Structure

```
innovate-mlops-pipeline/
├── dags/                   # Airflow DAGs
├── data/                  # Raw and processed datasets
├── k8s/                   # Kubernetes manifests
├── logs/                  # Airflow logs
├── mlruns/                # MLflow tracking artifacts
├── screenshots/           # Project execution screenshots
├── src/                   # Core source code
│   ├── etl/
│   │   └── pre_processing.py
│   ├── modeling/
│   │   └── linear_regression.py
│   └── api/
│       └── app.py         # Flask API (if needed)
├── streamlit_app/         # Frontend built with Streamlit
├── .dvc/                  # DVC metadata
├── .github/workflows/     # GitHub Actions CI config
├── .gitignore
├── .dvcignore
├── .flake8
├── docker-compose.yaml
├── requirements.txt
├── Jenkinsfile
└── README.md
```

---

## ✅ Completed MLOps Workflow

| Step | Task |
|------|------|
| ✅ | GitHub Issues + Sprint Planning |
| ✅ | Branching Strategy (`dev`, `main`) |
| ✅ | CI with GitHub Actions (`flake8`, `pytest`) |
| ✅ | DVC for dataset versioning |
| ✅ | MLflow for model tracking |
| ✅ | Airflow for ETL & training pipeline |
| ✅ | Jenkins for Docker build + push |
| ✅ | Flask API for model serving |
| ✅ | Kubernetes deployment for backend (Flask) |
| ✅ | Streamlit frontend + deployment |
| ✅ | PostgreSQL included via Docker Compose |
| ✅ | All services orchestrated with Minikube |

---

## 🚀 Running Instructions

### 1. Clone & Install
```bash
git clone https://github.com/MoizSajjad/innovate-mlops-pipeline.git
cd innovate-mlops-pipeline
python -m venv venv && source venv/bin/activate  # or use PowerShell activation
pip install -r requirements.txt
```

### 2. DVC Setup
```bash
dvc pull  # Restore data if remote is set up
```

### 3. MLflow Model Training
```bash
python src/modeling/linear_regression.py
mlflow ui --port 5001  # Optional: to visualize tracking
```

### 4. Run Airflow Pipeline (via Docker)
```bash
docker-compose up -d
# Access at: http://localhost:8082
```

### 5. Streamlit Frontend (Manual)
```bash
cd streamlit_app
streamlit run frontend.py  # For local dev
```

---

---

## 🧠 Tech Stack

- `Python`, `pandas`, `scikit-learn`, `joblib`
- `DVC`, `MLflow`
- `Airflow` for ETL and model orchestration
- `Jenkins`, `GitHub Actions` for CI/CD
- `Docker`, `Docker Hub`, `Minikube`, `Kubernetes`
- `Streamlit` for frontend

---

## 📝 Author

**Muhammad Moiz Sajjad**  
**SM Abdulladh**
**Mohid Munir**    
FAST NUCES – BS (Data Science)
