import streamlit as st
import joblib
model = joblib.load("loan.joblib")
st.title("Loan Prediction App")
st.markdown("### Input Data")
gender = st.radio("Select Gender", ["Male", "Female"])
gender = 0 if gender == "Male" else 1 
married = st.radio("Marital Status", ["Unmarried", "Married"])
married = 0 if married == "Unmarried" else 1
income = st.number_input("Income", min_value = 1000, step = 1000)
loan_amount = st.number_input("Loan Amount", min_value = 1000, step = 1000)

if st.button("Loan Status"):
    prediction = model.predict([[gender, married, income, loan_amount]])
    if prediction == 'Y':
        st.success("✅ Loan is Approved")
    else:
        st.error("❌ Loan is Rejected")

st.markdown("---")

st.markdown("### Loan Prediction App")
st.markdown("*Built using Decision Tree Machine Learning Algorithm*")

st.write("")

st.markdown("> Initial concept by **Kiran Kalla**, refined and developed further by **Vamsi Akshay Sanka**.")

st.write("---")

st.markdown("⚠️ *Disclaimer: This is a basic implementation for learning purposes. Predictions may not be accurate.*")
