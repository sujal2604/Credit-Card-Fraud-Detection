import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the saved model
with open("models.pkl", "rb") as file:
    models = pickle.load(file)

st.title("Online Payment Fraud Detection System")

st.write("Please enter the transaction details:")

# Collect user inputs
step = st.number_input("Step (Time Step)", min_value=0, format="%d")
amount = st.number_input("Transaction Amount", min_value=0.0, format="%f")
oldbalanceOrg = st.number_input("Old Balance of Sender", min_value=0.0, format="%f")
newbalanceOrig = st.number_input("New Balance of Sender", min_value=0.0, format="%f")
oldbalanceDest = st.number_input("Old Balance of Receiver", min_value=0.0, format="%f")
newbalanceDest = st.number_input("New Balance of Receiver", min_value=0.0, format="%f")

# Predict button
if st.button("Predict"):
    # Prepare input data as DataFrame with column names
    input_data = pd.DataFrame([[step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]],
                              columns=['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest'])

    # Make prediction
    prediction = models.predict(input_data)

    # Display result
    if prediction[0] == 1:
        st.error("This transaction is Fraudulent! 🚨")
    else:
        st.success("This transaction is Legitimate ✅")
