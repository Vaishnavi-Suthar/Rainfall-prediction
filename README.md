<h1 align="center">🌧️ Rainfall Prediction Using Machine Learning</h1>

<p align="center">
A desktop application built using Python, Tkinter, and Machine Learning models to predict rainfall using weather parameters.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Machine%20Learning-RandomForest-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">
</p>

---

## 🔍 **Overview**

This project predicts **rainfall** using Machine Learning models trained on historical weather data (temperature, humidity, dew point, wind speed, sunshine hours, etc.).

The system is designed to help:

✔ Farmers
✔ Disaster management teams
✔ Irrigation planners
✔ Weather forecasting departments

by making accurate and faster rainfall predictions.

---

## 🎯 **Purpose**

To build a **high-accuracy ML model** capable of predicting rainfall and provide a **user-friendly Tkinter interface** for real-world usage.

---

## 🎯 **Objectives**

* Develop an ML model for rainfall prediction
* Analyze multiple ML algorithms (Random Forest, SVM, Logistic Regression, etc.)
* Implement a Tkinter-based GUI for predictions
* Store prediction history for users
* Support data-driven agricultural decision-making

---

## 🧠 **Machine Learning Models Used**

| Model               | Train Accuracy | Test Accuracy | F1 Score   | Fit Status    |
| ------------------- | -------------- | ------------- | ---------- | ------------- |
| Logistic Regression | 0.8710         | 0.8539        | 0.9039     | Good Fit      |
| SVM                 | 0.8796         | 0.8516        | 0.9023     | Good Fit      |
| **Random Forest**   | **1.0000**     | **0.8470**    | **0.8986** | ⚠ Overfitting |
| Extra Trees         | 1.0000         | 0.8447        | 0.8973     | Overfitting   |
| k-NN                | 0.8921         | 0.8402        | 0.8958     | Underfitting  |
| Naive Bayes         | 0.8545         | 0.8402        | 0.8906     | Good Fit      |
| Decision Tree       | 1.0000         | 0.7900        | 0.8576     | Overfitting   |

✔ Best Model Selected: **Random Forest (after optimization)**
✔ Interfaces built for: **Admin & User**

---

## 🛠️ **Technology Stack**

### 🔹 **Software**

| Part                 | Technology                       |
| -------------------- | -------------------------------- |
| Frontend             | Python Tkinter                   |
| Backend              | Machine Learning (Random Forest) |
| Programming Language | Python                           |
| Operating System     | Windows 11                       |

---

## ⚙️ **Functionality**

### 👨‍💼 **Admin Module**

* Train and update ML models
* Evaluate multiple ML algorithms
* View model accuracy, F1 score, and error rate
* Manage user data
* View prediction history
* Audit user login/logout data

### 👤 **User Module**

* Input weather parameters:

  * Temperature
  * Humidity
  * Pressure
  * Wind speed
  * Cloud
  * Sunshine
  * Dewpoint
* Get rainfall prediction instantly
* View past predictions

---

## 📁 **Project Structure**

```
rainfall-prediction/
│── model/                  # ML model files
│── dataset/                # CSV data
│── gui/                    # Tkinter UI files
│── app.py                  # Main application
│── requirements.txt        # Dependencies
│── README.md               # Documentation
```

---

## 📸 **Screenshots**

<img width="931" height="537" alt="r_login" src="https://github.com/user-attachments/assets/bf6e7d47-fed2-4b48-9d47-dd9d634aa274" />
<img width="928" height="537" alt="r_register" src="https://github.com/user-attachments/assets/c3d88317-3d06-4087-8426-6d8f45572c3a" />
<img width="706" height="761" alt="r_yespr" src="https://github.com/user-attachments/assets/380deaf3-fa8e-4781-aa51-0491e67d5134" />
<img width="705" height="760" alt="r_nopr" src="https://github.com/user-attachments/assets/8fccdfd3-3f5c-4f8b-bf58-678f680ae79c" />
<img width="1237" height="487" alt="r_prhistory" src="https://github.com/user-attachments/assets/c73a31d0-f8fa-41f0-88b7-379095c86dee" />
<img width="653" height="486" alt="r_audit" src="https://github.com/user-attachments/assets/3bd235c9-0499-4771-856a-98663ec61f57" />

---

## 🏁 **Conclusion**

This project shows that **Machine Learning techniques significantly improve rainfall forecasting accuracy**.
With Random Forest performing the best, the system can support:

✔ Agricultural planning
✔ Flood prevention
✔ Water resource management

Future improvements include:
✔ Live API weather data
✔ Deep Learning models
✔ Web-based version

---
