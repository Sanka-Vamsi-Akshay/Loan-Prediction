import streamlit as st
import joblib

model = joblib.load("loan.joblib")

st.set_page_config(page_title="Loan Approval Prediction App", layout="centered")
st.title("🏦 Loan Approval Prediction App")
st.markdown("Predict whether your loan will be **approved** or **rejected** based on personal information.")

st.sidebar.title("About the App")
st.sidebar.info("""
This app uses a **Decision Tree** machine learning algorithm to predict loan approval.
Enter your details to get started.
""")

st.sidebar.markdown("---")

st.sidebar.title("Credits")
st.sidebar.info("""
Initial concept by **Kiran Kalla**, refined and developed further by **Vamsi Akshay Sanka**.
""")

st.sidebar.markdown("---")

st.sidebar.title("Disclaimer")
st.sidebar.warning("""
⚠️ This is a basic implementation for learning purposes. Predictions may not be accurate.
""")

st.header("🔍 Enter Your Details")
with st.form("loan_form"):
    gender = st.radio("Select Gender", ["Male", "Female"])
    gender = 0 if gender == "Male" else 1 
    married = st.radio("Marital Status", ["Unmarried", "Married"])
    married = 0 if married == "Unmarried" else 1
    income = st.number_input("Income", min_value = 1000, step = 1000)
    loan_amount = st.number_input("Loan Amount", min_value = 1000, step = 1000)
    submit = st.form_submit_button("Submit")

if submit:
    prediction = model.predict([[gender, married, income, loan_amount]])
    if prediction == 'Y':
        st.success("🎉 Congratulations! Your loan is likely to be approved.")
    else:
        st.error("❌ Sorry, your loan is likely to be rejected.")
