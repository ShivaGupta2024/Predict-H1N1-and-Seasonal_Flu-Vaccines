import streamlit as st
import pickle
import numpy as np
import time
import os

# Define correct file paths
model_files = {
    #"RF_H1N1": r"C:/Users/DELL/.spyder-py3/rf_h1n1_model.pkl",
    #"RF_Seasonal": r"C:/Users/DELL/.spyder-py3/rf_seasonal_model.pkl",
    "SVM_H1N1": r"C:/Users/DELL/.spyder-py3/SVM_h1n1.pkl",
    "SVM_Seasonal": r"C:/Users/DELL/.spyder-py3/SVM_Seasonal.pkl",
    "LOG_H1N1": r"C:/Users/DELL/.spyder-py3/log_h1n1_model.pkl",
    "LOG_Seasonal": r"C:/Users/DELL/.spyder-py3/log_seasonal_model.pkl"
}


# Function to check if the model is fitted
def is_model_fitted(model):
    try:
        getattr(model, "classes_")  # Checks if the model has been trained
        return True
    except AttributeError:
        return False

# Load models safely
models = {}
for model_name, file_path in model_files.items():
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            models[model_name] = pickle.load(f)
            if not is_model_fitted(models[model_name]):
                st.error(f"🚨 Error: {model_name} is not trained. Please retrain and save the model.")
    else:
        st.error(f"🚨 Error: File not found - {file_path}")

Body_html = """

  <style>
  h1{
    color: #7a7477;

  }
  h2{
    color:#F3005E;
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%)
  }
  h3{
    color:#898989;
    display: block;
    margin-left: auto;
    margin-right: auto;
    size: 200%;
  }

  h4{
    color: #7a7477;
  }

  h5{
    color: lightgrey;
  }

 img{
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
    #width: 300px;
    height: auto;
    #opacity:0.9;
}


   body{
    background-image: url(https://i.stack.imgur.com/HCfU2.png);
    #https://i.stack.imgur.com/9WYxT.png
    #opacity: 0.5;
}

</style>



"""
st.markdown(Body_html, unsafe_allow_html=True) #Body rendering

st.write(
"""

# Will a Person get the H1N1 Vaccine?  

![vaccine_img](https://cdn.prod.website-files.com/57ada58371bead8852a659ad/59d7e6685d96160001f437fa_Flu-fighter.png)

#### Try the tool to predict whether a person will get the H1N1 vaccine using the information they shared about their healthcare background and opinions.

***

In Spring 2009, a pandemic caused by the H1N1 influenza virus ("Swine Flu"), swept across the world. A vaccine for the H1N1 flu virus became publicly available in October 2009.
In late 2009 and early 2010, the United States conducted the National 2009 H1N1 Flu Survey. More details about this dataset and features are available at [NationalInstitutesofHealth.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC3375879/).

***

"""
)


st.write("Fill the details below and click **Predict** to see the vaccine likelihood.")





# Feature Inputs (same as before)
h1n1_concern = st.slider("Level of Concern About H1N1 Flu:", 0, 3, 2)
h1n1_knowledge = st.slider("Knowledge Level About H1N1 Flu:", 0, 3, 2)
behavioral_antiviral_meds = st.checkbox("Use of Antiviral Medication?")
behavioral_avoidance = st.checkbox("Avoidance of Public Places Due to Flu Concerns?")
behavioral_face_mask = st.checkbox("Use of Face Masks to Prevent Flu?")
behavioral_wash_hands = st.checkbox("Frequency of Hand Washing to Prevent Flu?")
behavioral_large_gatherings = st.checkbox("Avoidance of Large Gatherings?")
behavioral_outside_home = st.checkbox("Avoidance of Going Outside the Home?")
behavioral_touch_face = st.checkbox("Avoidance of Touching Face?")
doctor_recc_h1n1 = st.checkbox("Doctor's Recommendation for H1N1 Vaccine?")
doctor_recc_seasonal = st.checkbox("Doctor's Recommendation for Seasonal Flu Vaccine?")
chronic_med_condition = st.checkbox("Presence of Chronic Medical Condition?")
child_under_6_months = st.checkbox("Presence of Child Under 6 Months Old?")
health_worker = st.checkbox("Occupation as a Healthcare Worker?")
health_insurance = st.checkbox("Availability of Health Insurance?")
st.caption("On a Scale of 1 to 5 (Give your input)")
st.caption("1: Least  5: Most")
opinion_h1n1_vacc_effective = st.slider("Opinion on H1N1 Vaccine Effectiveness:", 1, 5, 4)
opinion_h1n1_risk = st.slider("Opinion on H1N1 Risk of Getting H1N1 Flu:", 1, 5, 1)
opinion_h1n1_sick_from_vacc = st.slider("Belief in H1N1 Vaccine's Ability to Make One Sick:", 1, 5, 1)
opinion_seas_vacc_effective = st.slider("Opinion on Seasonal Vaccine Effectiveness:", 1, 5, 4)
opinion_seas_risk = st.slider("Opinion on Risk of Getting Seasonal Flu:", 1, 5, 1)
opinion_seas_sick_from_vacc = st.slider("Belief in Seasonal Vaccine's Ability to Make One Sick:", 1, 5, 1)
age_group = st.selectbox("Age Group:", ['18-34', '35-44', '45-54', '55-64', '65+'])
education = st.selectbox("Select the Qualification:", ['No High School', 'High School', 'Some College', 'College Graduate'])
race = st.selectbox("Select the Race:", ['White', 'Black', 'Hispanic', 'Other'])
sex = st.selectbox("Select Sex:", ['Male', 'Female'])
income_poverty = st.selectbox("Select Income Level:", ['Low', 'Medium', 'High'])
marital_status = st.selectbox("Select Marital Status:", ['Single', 'Married'])
rent_or_own = st.selectbox("Select Housing Status:", ['Own', 'Rent'])
employment_status = st.selectbox("Select Employment Status:", ['Employed', 'Not in Labor Force'])
census_msa = st.selectbox("Select Census MSA(Metropolitan Statistical Area):", ['Non-MSA', 'MSA, Not Principle City'])
household_adults = st.slider("No of Adults:", 0, 2, 1)
household_children = st.slider("No of Children:", 0, 3, 1)

# Define category mappings
category_mappings = {
    'age_group': {'18-34': 0, '35-44': 1, '45-54': 2, '55-64': 3, '65+': 4},
    'education': {'No High School': 0, 'High School': 1, 'Some College': 2, 'College Graduate': 3},
    'race': {'White': 0, 'Black': 1, 'Hispanic': 2, 'Other': 3},
    'sex': {'Male': 0, 'Female': 1},
    'income_poverty': {'Low': 0, 'Medium': 1, 'High': 2},
    'marital_status': {'Single': 0, 'Married': 1},
    'rent_or_own': {'Own': 0, 'Rent': 1},
    'employment_status': {'Employed': 0, 'Not in Labor Force': 1},
    'census_msa': {'Non-MSA': 0, 'MSA, Not Principle City': 1}
}

# Convert categorical values to numerical values
age_group = category_mappings['age_group'][age_group]
education = category_mappings['education'][education]
race = category_mappings['race'][race]
sex = category_mappings['sex'][sex]
income_poverty = category_mappings['income_poverty'][income_poverty]
marital_status = category_mappings['marital_status'][marital_status]
rent_or_own = category_mappings['rent_or_own'][rent_or_own]
employment_status = category_mappings['employment_status'][employment_status]
census_msa = category_mappings['census_msa'][census_msa]

# Prepare input data again
data = [
    h1n1_concern, h1n1_knowledge, behavioral_antiviral_meds, behavioral_avoidance,
    behavioral_face_mask, behavioral_wash_hands, behavioral_large_gatherings, behavioral_outside_home,
    behavioral_touch_face, doctor_recc_h1n1, doctor_recc_seasonal, chronic_med_condition,
    child_under_6_months, health_worker, health_insurance, opinion_h1n1_vacc_effective,
    opinion_h1n1_risk, opinion_h1n1_sick_from_vacc, opinion_seas_vacc_effective, opinion_seas_risk,
    opinion_seas_sick_from_vacc, age_group, education, race, sex, income_poverty, marital_status,
    rent_or_own, employment_status, census_msa, household_adults, household_children
]

def predict_vaccine():
    try:
        input_array = np.array(data, dtype=object).reshape(1, -1)

        # Ensure models are trained before prediction
        if not all(is_model_fitted(models[m]) for m in models):
            st.error("🚨 Some models are not trained. Please check the logs and retrain them.")
            return

        # Variables to accumulate probabilities
        svm_h1n1_prob, log_h1n1_prob = 0, 0
        svm_seasonal_prob, log_seasonal_prob = 0, 0

        # SVM H1N1 Probability
        if hasattr(models["SVM_H1N1"], 'predict_proba'):
            svm_h1n1_prob = models["SVM_H1N1"].predict_proba(input_array)[0][1]
        else:
            svm_h1n1_prob = models["SVM_H1N1"].predict(input_array)[0]

        # Logistic Regression H1N1 Probability
        if hasattr(models["LOG_H1N1"], 'predict_proba'):
            log_h1n1_prob = models["LOG_H1N1"].predict_proba(input_array)[0][1]
        else:
            log_h1n1_prob = models["LOG_H1N1"].predict(input_array)[0]

        # SVM Seasonal Probability
        if hasattr(models["SVM_Seasonal"], 'predict_proba'):
            svm_seasonal_prob = models["SVM_Seasonal"].predict_proba(input_array)[0][1]
        else:
            svm_seasonal_prob = models["SVM_Seasonal"].predict(input_array)[0]

        # Logistic Regression Seasonal Probability
        if hasattr(models["LOG_Seasonal"], 'predict_proba'):
            log_seasonal_prob = models["LOG_Seasonal"].predict_proba(input_array)[0][1]
        else:
            log_seasonal_prob = models["LOG_Seasonal"].predict(input_array)[0]

        # Now calculate the average probability for each vaccine
        h1n1_avg_prob = np.mean([svm_h1n1_prob, log_h1n1_prob])
        seasonal_avg_prob = np.mean([svm_seasonal_prob, log_seasonal_prob])

        # Threshold of 0.5 for predicting likelihood
        final_h1n1_pred = 1 if h1n1_avg_prob >= 0.5 else 0
        final_seasonal_pred = 1 if seasonal_avg_prob >= 0.5 else 0

        with st.spinner("🔍 Predicting..."):
            time.sleep(2)

        # Display predictions
        st.success(f"✅ **H1N1 Vaccine:** {'Likely to get vaccine' if final_h1n1_pred == 1 else 'Unlikely to get vaccine'} (Average probability: {h1n1_avg_prob:.2f})")
        st.success(f"✅ **Seasonal Flu Vaccine:** {'Likely to get vaccine' if final_seasonal_pred == 1 else 'Unlikely to get vaccine'} (Average probability: {seasonal_avg_prob:.2f})")

    except Exception as e:
        st.error(f"🚨 An error occurred: {str(e)}")




if st.button("🚀 Predict"):
    predict_vaccine()


