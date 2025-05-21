#  End-to-End Machine Learning Project with MLflow 

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/Ashish570raj/End-To-End-Machine-Learning-with-MLflow-/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![MLflow Tracking](https://img.shields.io/badge/mlflow-active-blue)](https://mlflow.org)
[![DagsHub Integration](https://img.shields.io/badge/DagsHub-Enabled-yellowgreen)](https://dagshub.com/)
[![Python Version](https://img.shields.io/badge/Python-3.8-blue.svg)](https://www.python.org/)

A complete end-to-end machine learning pipeline using `MLflow` for tracking, `DagsHub` for collaboration, and Python for development. Includes training, evaluation, logging, and deployment steps.

---

## 📌 Workflow Overview

1. ✅ Update `config.yaml`
2. ✅ Update `schema.yaml`
3. ✅ Update `params.yaml`
4. ✅ Define `entity` classes
5. ✅ Configure settings in `ConfigurationManager` (`src/config`)
6. ✅ Implement core logic in `components`
7. ✅ Create pipelines for each ML stage
8. ✅ Connect everything in `main.py`
9. ✅ Launch your app via `app.py`

---

## How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Ashish570raj/End-To-End-Machine-Learning-with-MLflow-
cd End-To-End-Machine-Learning-with-MLflow-
```

### 2️⃣ Create a Conda Environment

```bash
conda create -n mlproj python=3.8 -y
conda activate mlproj
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Setup Environment Variables with `.env`

### 1️⃣ Create a `.env` file in the root of the project:

```env
MLFLOW_TRACKING_URI=https://dagshub.com/<username>/<repo>.mlflow
MLFLOW_TRACKING_USERNAME=your_username
MLFLOW_TRACKING_PASSWORD=your_dagshub_token
```

### 2️⃣ Load the `.env` file in your code:

```python
from dotenv import load_dotenv
load_dotenv()
```

Add the above two lines in the entry script (e.g., `main.py`, `pipeline/stage.py`, or `app.py`).

---

## 📊 MLflow for Experiment Tracking

### Start MLflow UI (Local)

```bash
mlflow ui
```

Open `http://127.0.0.1:5000` in your browser.

---

## ☁️ Connect to DagsHub for Remote Tracking

### ✨ Initialize DagsHub

```python
import dagshub

dagshub.init(
    repo_owner='Ashish570raj',
    repo_name='End-To-End-Machine-Learning-with-MLflow-',
    mlflow=True
)
```

### 🔍 Log Parameters and Metrics with MLflow

```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("param_name", "value")
    mlflow.log_metric("metric_name", 0.95)
```

---

## 📚 Documentation & Resources

* [MLflow Docs](https://mlflow.org/docs/latest/index.html)
* [DagsHub Docs](https://dagshub.com/docs/)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

Created by **Ashish Raj** – [LinkedIn](https://linkedin.com/in/ashish570raj)

---


