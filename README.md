# Fraud Detection Analysis Project

## Overview
This project focuses on detecting and analyzing fraudulent transactions in a financial dataset. The goal is to identify patterns, trends, and key insights related to fraudulent activities using **data analysis** and **visualization tools**. The project includes:
- Data preprocessing and feature engineering.
- Exploratory data analysis (EDA).
- Machine learning model development.
- A **Power BI dashboard** for interactive visualization.

---

## Project Structure
The project is organized as follows:
fraud-detection-analysis/
├── data/
│ ├── fraud_analysis_dataset.csv # Raw dataset
│ └── processed_data.csv # Processed dataset
├── notebooks/
│ ├── data_preprocessing.ipynb # Data cleaning and feature engineering
│ ├── exploratory_data_analysis.ipynb # EDA and insights
│ └── model_training.ipynb # Machine learning model development
├── dashboard/
│ └── fraud_detection_dashboard.pbix # Power BI dashboard
├── README.md # Project documentation
└── requirements.txt # Python dependencies


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

### 1. Data Preprocessing
- **Handling Missing Values**: The dataset was checked for missing values, and no missing values were found.
- **Feature Engineering**:
  - Created new features like `balanceOrig_diff` (difference between old and new balances for the origin account).
  - Encoded categorical variables (e.g., `type`).
  - Dropped unnecessary columns (e.g., `nameOrig`, `nameDest`).

### 2. Exploratory Data Analysis (EDA)
- Analyzed the distribution of fraudulent vs non-fraudulent transactions.
- Identified high-risk transaction types (e.g., CASH_OUT, TRANSFER).
- Visualized trends in fraudulent transactions over time.

### 3. Machine Learning Model Development
- Split the data into training and testing sets.
- Applied **SMOTE** to handle class imbalance.
- Trained a **Random Forest Classifier** to predict fraudulent transactions.
- Evaluated the model using metrics like accuracy, precision, recall, and F1-score.

### 4. Power BI Dashboard
- Created an interactive dashboard to visualize key insights:
  - Fraud by transaction type.
  - Fraudulent transactions over time.
  - Total monetary loss by account.
  - Old balance vs new balance for fraudulent transactions.

---

## Tools and Technologies
- **Python**: For data preprocessing, EDA, and model training.
- **Jupyter Notebook**: For exploratory analysis and model development.
- **Power BI**: For creating the interactive dashboard.
- **GitHub**: For version control and project sharing.

---

## How to Use This Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/fraud-detection-analysis.git
cd fraud-detection-analysis

pip install -r requirements.txt
