# Fraud Detection Analysis Project

## Overview
This project focuses on detecting and analyzing fraudulent transactions in a financial dataset. The goal is to identify patterns, trends, and key insights related to fraudulent activities using **data analysis** and **visualization tools**. The project includes:
- Data preprocessing and feature engineering.
- Exploratory data analysis (EDA).
- Machine learning model development.
- A **Power BI dashboard** for interactive visualization.

---

## Dataset
The dataset used in this project contains the following columns:
- `step`: Represents a unit of time (e.g., hour, day).
- `type`: Type of transaction (e.g., CASH_IN, CASH_OUT, DEBIT, PAYMENT, TRANSFER).
- `amount`: The transaction amount.
- `nameOrig`: Origin account name.
- `oldbalanceOrg`: Old balance of the origin account.
- `newbalanceOrig`: New balance of the origin account.
- `nameDest`: Destination account name.
- `oldbalanceDest`: Old balance of the destination account.
- `newbalanceDest`: New balance of the destination account.
- `isFraud`: Indicates whether the transaction is fraudulent (1) or not (0).

---

## Steps in the Project

### 1. Data Loading
- Load the dataset into a Pandas DataFrame.
- Display the first few rows to understand its structure.

### 2. Data Exploration
- Check for missing values and data types.
- Identify unique transaction types and class distributions.

### 3. Exploratory Data Analysis (EDA) and Visualization
- Analyze the distribution of fraudulent vs non-fraudulent transactions.
- Identify high-risk transaction types (e.g., CASH_OUT, TRANSFER).
- Visualize trends in fraudulent transactions over time.
- Generate correlation heatmaps to understand relationships between features.

### 4. Feature Engineering
- Create new features such as `balanceOrig_diff` (difference between old and new balances for the origin account).
- Encode categorical variables (e.g., `type`).
- Drop unnecessary columns (e.g., `nameOrig`, `nameDest`).

### 5. Data Preprocessing and Model Training
- Split the data into training and testing sets.
- Apply **SMOTE** to handle class imbalance.
- Train machine learning models, including:
  - Random Forest Classifier
  - XGBoost
  - Logistic Regression
  - SVM (Support Vector Machine)
- Perform hyperparameter tuning for optimal performance.

### 6. Model Evaluation
- Evaluate models using the following metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - ROC Curve
- Analyze false positives and false negatives.

### 7. Financial Impact Analysis
- **Key Questions Addressed**:
  1. What is the model's precision and accuracy in detecting fraudulent transactions?
  2. How reliable is the model in classifying transactions as legitimate or fraudulent?
  3. What are the potential losses due to model errors?
     - Analyze false negatives (missed fraud cases) and estimate the financial loss.
     - Evaluate false positives (legitimate transactions incorrectly flagged as fraud) and their impact on user experience.

### 8. Power BI Dashboard
- Created an interactive dashboard to visualize key insights:
  - Fraud by transaction type.
  - Fraudulent transactions over time.
  - Total monetary loss by account.
  - Old balance vs new balance for fraudulent transactions.

---

## Tools and Technologies
- **Jupyter Notebook**: For exploratory analysis and model development.
- **Power BI**: For creating the interactive dashboard.
- **GitHub**: For version control and project sharing.

---
### 2. Set Up the Environment
Install the required Python libraries:

```bash
pip install -r requirements.txt


