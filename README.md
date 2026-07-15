# 🎓 Placement Prediction System

An end-to-end Machine Learning web application that predicts whether a student is likely to be placed based on academic performance, educational background, work experience, and specialization.

🌐 **Live Demo:** https://placement-predictor-1-p2ry.onrender.com

---

## 🚀 Overview

This project demonstrates the complete Machine Learning workflow—from data preprocessing and exploratory data analysis to model training, hyperparameter tuning, and deployment.

Users can enter their academic profile through an intuitive web interface, and the application predicts:

- ✅ Placement Status
- 📈 Placement Probability
- 🎯 Prediction Confidence

The application is powered by an XGBoost classifier and deployed using Flask on Render.

---

## ✨ Features

- Interactive Flask Web Application
- Real-time Placement Prediction
- Placement Probability using `predict_proba()`
- Confidence Level Estimation
- Clean & Responsive UI
- XGBoost Classifier
- Hyperparameter Tuning using GridSearchCV
- Model Serialization with Joblib

---

## 📊 Dataset Features

- Gender
- SSC Percentage
- SSC Board
- HSC Percentage
- HSC Board
- HSC Subject
- Degree Percentage
- Undergraduate Degree
- Work Experience
- Employability Test Percentage
- MBA Percentage
- MBA Specialization

---

## 🧠 Machine Learning Pipeline

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Label Encoding
- One-Hot Encoding
- Train/Test Split
- XGBoost Training
- Hyperparameter Optimization (GridSearchCV)
- Model Evaluation
- Model Serialization
- Flask Deployment

---

## 📈 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | **84%** |
| Precision | **85%** |
| Recall | **94%** |
| F1 Score | **89%** |

*Performance may vary slightly depending on the train-test split.*

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost

### Data Visualization
- Matplotlib
- Seaborn

### Backend
- Flask

### Frontend
- HTML
- CSS

### Deployment
- Render

---

## 📂 Project Structure

```
Placement_Predictor
│
├── app.py
├── model_xgb.pkl
├── requirements.txt
├── LICENSE
├── README.md
│
└── templates
    └── index.html
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/VasudevCodeReaper/Placement_Predictor.git
```

Move into the project

```bash
cd Placement_Predictor
```

Create a virtual environment

```bash
python -m venv myenv
```

Activate it

Windows

```bash
myenv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

## 🌍 Live Demo

https://placement-predictor-1-p2ry.onrender.com

---

## 🔮 Future Improvements

- SHAP Explainability
- Docker Support
- REST API
- User Authentication
- Prediction History
- Cloud Model Storage
- Mobile Responsive Enhancements

---

## 👨‍💻 Author

**Vasudev Varshney**

GitHub:
https://github.com/VasudevCodeReaper

---

## 📜 License

This project is licensed under the MIT License.
