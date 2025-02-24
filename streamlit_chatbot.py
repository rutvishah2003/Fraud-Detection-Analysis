import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt

# Page title and description
st.title("Fraud Detection App")
st.markdown("""
Welcome to the Fraud Detection App! This app predicts whether a transaction is fraudulent or not.
Enter the transaction details and the app will provide a prediction.
""")

# Load the trained model and preprocessing objects
@st.cache_resource
def load_artifacts():
    model = joblib.load('random_forest_model.joblib')  
    encoder = joblib.load('label_encoder.joblib')      
    scaler = joblib.load('standard_scaler.joblib')    
    return model, encoder, scaler

model, encoder, scaler = load_artifacts()

# Sidebar for user inputs
with st.sidebar:
    st.header("Enter Transaction Details")
    step = st.number_input("Step", min_value=0, step=1)
    type_options = ['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER']
    type = st.selectbox("Transaction Type", type_options)
    amount = st.number_input("Amount", min_value=0.0)
    oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0)
    newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0)
    oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0)
    newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0)
    nameDest = st.text_input("Destination Account Name (e.g., C123456789 or M123456789)")
    submitted = st.button("Submit")

# Preprocess input data and make predictions
if submitted:
    # Create a DataFrame from user input
    input_data = pd.DataFrame({
        'step' : [step],
        'type': [type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest],
        'nameDest': [nameDest]
    })

    # Feature engineering
    input_data['type_encoded'] = encoder.transform(input_data['type'])  # Encode transaction type
    input_data['balanceOrig_diff'] = input_data['oldbalanceOrg'] - input_data['newbalanceOrig']
    input_data['balanceDest_diff'] = input_data['oldbalanceDest'] - input_data['newbalanceDest']
    input_data['amount_to_oldbalanceOrg_ratio'] = np.where(input_data['oldbalanceOrg'] > 0, input_data['amount'] / input_data['oldbalanceOrg'], 0)
    input_data['amount_to_oldbalanceDest_ratio'] = np.where(input_data['oldbalanceDest'] > 0, input_data['amount'] / input_data['oldbalanceDest'], 0)
    input_data['is_zero_oldbalanceOrg'] = (input_data['oldbalanceOrg'] == 0).astype(int)
    input_data['is_zero_newbalanceOrig'] = (input_data['newbalanceOrig'] == 0).astype(int)
    input_data['is_zero_oldbalanceDest'] = (input_data['oldbalanceDest'] == 0).astype(int)
    input_data['is_zero_newbalanceDest'] = (input_data['newbalanceDest'] == 0).astype(int)
    input_data['is_merchant'] = input_data['nameDest'].str.startswith('M').astype(int)

    # Drop unnecessary columns
    input_data.drop(columns=['type','nameDest'], inplace=True)

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)

    # Make prediction
    with st.spinner("Making prediction..."):
        prediction = model.predict(input_data_scaled)
        prediction_proba = model.predict_proba(input_data_scaled)
        st.success("Prediction complete!")

    # Display results in columns
    col1, col2 = st.columns(2)

    with col1:
        st.header("Prediction Result")
        if prediction[0] == 1:
            st.error("🚨 **Fraudulent Transaction**")
        else:
            st.success("✅ **Not Fraudulent**")

    with col2:
        st.header("Confidence Score")
        st.write(f"{np.max(prediction_proba) * 100:.2f}%")

    # Pie chart for prediction probabilities
    st.header("Prediction Probabilities")
    labels = ['Not Fraudulent', 'Fraudulent']
    sizes = [prediction_proba[0][0] * 100, prediction_proba[0][1] * 100]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#ff9999'])
    ax.axis('equal')
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("""
**Fraud Detection App**  
Developed by Rutvi Shah  
[GitHub](https://github.com/rutvishah2003) | [LinkedIn](https://linkedin.com/in/rutvishah03)""")