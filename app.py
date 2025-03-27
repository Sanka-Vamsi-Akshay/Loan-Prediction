import streamlit as st
import joblib
model = joblib.load("loan.joblib")
st.title("Loan Prediction App")
st.markdown("### Input Data")
gender = st.number_input("Gender (Male : 0, Female : 1)", min_value = 0, max_value = 1, step = 1)
married = st.number_input("Marital Status (Unmarried : 0, Married : 1)", min_value = 0, max_value = 1, step = 1)
income = st.number_input("Income", min_value = 1000, step = 1)
loan_amount = st.number_input("Loan Amount", min_value = 1000, step = 1)

if st.button("Loan Status"):
    prediction = model.predict([[gender, married, income, loan_amount]])
    if prediction == 'Y':
        st.success("Loan is Approved")
    else:
        st.error("Loan is Rejected")
