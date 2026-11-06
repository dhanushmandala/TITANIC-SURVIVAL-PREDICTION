import streamlit as st
import pandas as pd
import joblib


# ==================================
# Load Model
# ==================================

model = joblib.load(
    "titanic_logistic_model.pkl"
)


# ==================================
# Page Configuration
# ==================================

st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="centered"
)


# ==================================
# Title
# ==================================

st.title("🚢 Titanic Survival Prediction")

st.write(
    "Logistic Regression model to predict "
    "whether a passenger survived the Titanic."
)


# ==================================
# User Inputs
# ==================================

st.sidebar.header("Passenger Information")


pclass = st.sidebar.selectbox(
    "Passenger Class",
    [1, 2, 3]
)


sex = st.sidebar.selectbox(
    "Gender",
    ["male", "female"]
)


age = st.sidebar.number_input(
    "Age",
    min_value=0.0,
    max_value=100.0,
    value=30.0
)


sibsp = st.sidebar.number_input(
    "Siblings / Spouses",
    min_value=0,
    max_value=10,
    value=0
)


parch = st.sidebar.number_input(
    "Parents / Children",
    min_value=0,
    max_value=10,
    value=0
)


fare = st.sidebar.number_input(
    "Fare",
    min_value=0.0,
    max_value=600.0,
    value=32.0
)


embarked = st.sidebar.selectbox(
    "Embarked",
    ["S", "C", "Q"]
)


# ==================================
# Create Input DataFrame
# ==================================

input_data = pd.DataFrame({
    "Pclass": [pclass],
    "Sex": [sex],
    "Age": [age],
    "SibSp": [sibsp],
    "Parch": [parch],
    "Fare": [fare],
    "Embarked": [embarked]
})


# ==================================
# Display Input
# ==================================

st.subheader("Passenger Details")

st.dataframe(
    input_data,
    use_container_width=True
)


# ==================================
# Prediction
# ==================================

if st.button(
    "Predict Survival",
    type="primary"
):

    prediction = model.predict(
        input_data
    )[0]

    probability = model.predict_proba(
        input_data
    )[0][1]


    # ==============================
    # Result
    # ==============================

    st.subheader("Prediction Result")


    if prediction == 1:

        st.success(
            "🟢 Passenger is predicted to SURVIVE."
        )

    else:

        st.error(
            "🔴 Passenger is predicted NOT TO SURVIVE."
        )


    st.metric(
        "Survival Probability",
        f"{probability * 100:.2f}%"
    )


    st.progress(
        float(probability)
    )