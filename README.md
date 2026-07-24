# 🔧 Predictive Maintenance using Machine Learning

An end-to-end Machine Learning project that predicts industrial machine failures using sensor data. This project compares multiple classification algorithms, performs hyperparameter tuning, explains predictions using SHAP, and deploys the best model through an interactive Streamlit application.

---

## 📌 Project Overview

Unexpected machine failures can lead to significant production downtime and maintenance costs in manufacturing industries.

This project aims to build a predictive maintenance system capable of identifying potential machine failures before they occur using real-time operational parameters.

The complete workflow includes:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training & Evaluation
- Hyperparameter Tuning
- Model Explainability (SHAP)
- Streamlit Web Application Deployment

---

## 📂 Dataset Features

The model predicts **Machine Failure** using the following features:

- Machine Type
- Air Temperature (K)
- Process Temperature (K)
- Rotational Speed (RPM)
- Torque (Nm)
- Tool Wear (minutes)

Target Variable:

- **Machine Failure**
  - 0 → Healthy Machine
  - 1 → Failure Likely

---

## ⚙️ Project Workflow

### 1. Data Preprocessing

- Removed unnecessary features
- Label encoded categorical variables
- Checked missing values
- Duplicate removal
- Feature selection

---

### 2. Exploratory Data Analysis

Performed analysis on:

- Failure distribution
- Feature distributions
- Correlation matrix
- Temperature analysis
- Torque & RPM relationships
- Tool wear patterns

---

### 3. Machine Learning Models

The following classification models were trained:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM

---

### 4. Hyperparameter Tuning

Applied **RandomizedSearchCV** on:

- XGBoost
- LightGBM

using Recall as the optimization metric.

---

## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|------|---------:|----------:|--------:|---------:|---------:|
| LightGBM | **98.75%** | **0.86** | **0.70** | **0.77** | **0.979** |
| Tuned LightGBM | 98.75% | 0.86 | 0.70 | 0.77 | 0.978 |
| Tuned XGBoost | 98.70% | 0.87 | 0.67 | 0.76 | 0.972 |
| XGBoost | 98.20% | 0.75 | 0.62 | 0.68 | 0.968 |
| Random Forest | 98.45% | 0.86 | 0.59 | 0.70 | 0.964 |
| Logistic Regression | 97.40% | 0.67 | 0.30 | 0.41 | 0.896 |
| Decision Tree | 97.75% | 0.61 | 0.74 | 0.67 | 0.861 |

✅ **Selected Model:** LightGBM

---

## 🔍 Model Explainability

To improve transparency, SHAP (SHapley Additive exPlanations) was used to understand feature contributions.

### Key Insights

- Tool Wear is the strongest indicator of machine failure.
- Higher Torque significantly increases failure probability.
- Rotational Speed strongly influences predictions.
- Air Temperature contributes moderately.
- Machine Type has comparatively lower importance.

---

## 🌐 Streamlit Application

The trained LightGBM model was deployed using **Streamlit Community Cloud**.

### Features

- Interactive prediction interface
- User-friendly design
- Instant failure prediction
- Failure probability estimation

### Live Demo

👉 **https://YOUR-STREAMLIT-LINK**

---

## 📸 Application Preview

_Add screenshots here_

Example:

- Home Page
- Prediction Result
- SHAP Summary Plot

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- LightGBM
- XGBoost
- SHAP
- Matplotlib
- Seaborn
- Streamlit

---

## 📁 Project Structure

```text
PredictiveMaintenance/
│
├── app.py
├── predict.py
├── predictive_maintenance_artifacts.pkl
├── predictive_maintenance.ipynb
├── predictive_maintenance.csv
├── requirements.txt
├── README.md
└── images/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/ShravanK45/predictive-maintenance-ml.git
```

Navigate into the project

```bash
cd predictive-maintenance-ml
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📌 Future Improvements

- Deep Learning based failure prediction
- Real-time IoT sensor integration
- Cloud deployment with AWS/GCP
- Predict Remaining Useful Life (RUL)
- Dashboard for industrial monitoring

---

## 👨‍💻 Author

**Shravan Kundap**

Electronics & Telecommunication Engineering  
Aspiring AI/ML Engineer

🔗 GitHub: https://github.com/ShravanK45

🔗 LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ If you found this project useful

Feel free to **Star ⭐ the repository** and connect with me on LinkedIn.
