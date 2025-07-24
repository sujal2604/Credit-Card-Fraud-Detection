# 💳 Credit Card Fraud Detection

This project uses machine learning to detect fraudulent credit card transactions. Fraudulent transactions are rare compared to legitimate ones, which makes this a challenging and critical classification problem. This project is designed to build a robust fraud detection model, evaluate its performance, and provide an easy-to-use frontend for prediction.

## 🔍 Overview

- **Goal:** Predict whether a given transaction is fraudulent or legitimate.
- **Model Used:** Random Forest Classifier
- **Frontend:** Streamlit web application
- **Tech Stack:** Python, Pandas, Scikit-learn, SMOTE, Streamlit

## 📂 Dataset

The dataset contains anonymized credit card transactions, including features like transaction amount, account balances before and after, and a label indicating whether the transaction was fraudulent.

**Key Features:**
- `step`: Time step
- `amount`: Transaction amount
- `oldbalanceOrg`: Balance before transaction (sender)
- `newbalanceOrig`: Balance after transaction (sender)
- `oldbalanceDest`: Balance before transaction (receiver)
- `newbalanceDest`: Balance after transaction (receiver)
- `isFraud`: Target label (1 = Fraud, 0 = Legitimate)

## ⚙️ Model Workflow

1. **Data Preprocessing**
   - Removed unnecessary features
   - Handled class imbalance using SMOTE

2. **Model Training**
   - Trained a `RandomForestClassifier` with parameters:
     - `n_estimators=7`
     - `criterion='entropy'`
     - `random_state=7`

3. **Model Evaluation**
   - Metrics used: Accuracy, Precision, Recall, F1 Score, ROC-AUC
   - Validated using test data and a few real fraudulent transactions

4. **Deployment**
   - Built a simple **Streamlit interface** for user-friendly prediction
   - Users input transaction data and receive immediate fraud detection result

## 🖥️ Streamlit Frontend

- Users are prompted to enter all required transaction fields.
- The app uses the saved model (`models.pkl`) to predict and display:
  - `"Fraudulent"` or `"Legitimate"` transaction

