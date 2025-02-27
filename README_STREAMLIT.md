
# 🩺 H1N1 & Seasonal Flu Vaccine Prediction System - Streamlit Application

## 📊 Project Overview
This project is a **web-based prediction tool** built using **Streamlit** to estimate whether an individual is **likely to receive the H1N1 vaccine and the seasonal flu vaccine**. The system uses **pre-trained machine learning models** (SVM and Logistic Regression) to predict the likelihood based on:

- **Demographic details**
- **Health history**
- **Behavioral patterns**
- **Opinions and concerns about vaccines**

The tool allows users to **input their information through an interactive form**, and then uses machine learning models to predict **vaccine likelihood for both H1N1 and seasonal flu vaccines**.

---

## 💻 Technologies Used

| Component        | Technology |
|------------------|-------------|
| **Web Framework** | Streamlit |
| **Machine Learning** | SVM, Logistic Regression |
| **Programming Language** | Python |
| **Libraries** | NumPy, Pickle, Time, OS |

---

## 🏛️ Application Features

### 🎯 Predict Vaccine Likelihood
- Predicts **H1N1 vaccine uptake likelihood**.
- Predicts **Seasonal flu vaccine uptake likelihood**.
- Combines results from **SVM** and **Logistic Regression** models to give an **average probability**.

### 📥 User Inputs
The tool collects:
- Personal details (age group, education, race, gender, income level, etc.)
- Health and vaccine history (doctor recommendations, chronic medical conditions, etc.)
- Behavioral data (mask usage, avoidance of public spaces, etc.)
- Personal opinions on vaccine effectiveness and risk.

### 📊 Visual and Interactive UI
- Easy-to-use interface with sliders, checkboxes, and dropdowns.
- Displays results with **likelihood predictions** and **average probabilities**.

---

## 🛠️ How It Works

1. User provides personal, health, and behavioral data using the Streamlit interface.
2. Data is **pre-processed**, including categorical encoding.
3. Trained **SVM** and **Logistic Regression** models for both H1N1 and Seasonal flu vaccines are **loaded using Pickle**.
4. Each model predicts the **probability** of the user receiving each vaccine.
5. Final prediction is the **average of SVM and Logistic Regression predictions**.
6. Results are displayed with **likelihood (Likely/Unlikely)** and **average probability scores**.

---

## 📂 Required Files

The following **pre-trained models** are required to run this application:

| Model Type | Vaccine | File Name |
|---|---|---|
| SVM | H1N1 | `SVM_h1n1.pkl` |
| SVM | Seasonal Flu | `SVM_Seasonal.pkl` |
| Logistic Regression | H1N1 | `log_h1n1_model.pkl` |
| Logistic Regression | Seasonal Flu | `log_seasonal_model.pkl` |

⚠️ **Ensure these files are placed in the correct directory or update the file paths in the application script.**

---

## ⚙️ Setup & Run Instructions

1. Clone the repository.
2. Install required packages using:
    ```bash
    pip install streamlit numpy
    ```
3. Place the **model files** in the correct directory (adjust the file paths in the code if necessary).
4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
5. Open the app in the **browser** and start entering data to get predictions.

---

## 📄 Key Logic

The predictions are based on:

- **H1N1 vaccine prediction = average(SVM prediction, Logistic Regression prediction)**
- **Seasonal Flu vaccine prediction = average(SVM prediction, Logistic Regression prediction)**

The final prediction is:
- **Likely to get vaccine** if probability >= 0.5
- **Unlikely to get vaccine** if probability < 0.5

---

## 📚 References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [National Institutes of Health H1N1 Survey Dataset](https://pmc.ncbi.nlm.nih.gov/articles/PMC3375879/)

---

## 👨‍💻 Contributors
- **Abhishek Jaydeo Bhure**  
- **Kaname Hariom Venkatrao**  
- **Kokate Neha Vitthal**  
- **Shiva Gupta**  
- **Shubhi Paliwal**  

---

## 📄 License
This project is licensed under the **MIT License**.
