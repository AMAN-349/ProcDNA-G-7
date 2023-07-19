import pandas as pd
from datetime import datetime, timedelta

# Read the dataset into a DataFrame
df = pd.read_csv('dataset.csv')

# Data Quality Questions:

def identify_data_quality_issues(df):
    issues = []

    # Data Quality Issue 1: Duplicate Transactions
    duplicate_transactions = df[df.duplicated('Transaction ID', keep=False)]
    if not duplicate_transactions.empty:
        issues.append("Duplicate Transactions:\n" + str(duplicate_transactions) + "\n")

    # Data Quality Issue 2: Date Format Consistency
    try:
        df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y', errors='raise')
    except Exception as e:
        issues.append(f"Date Format Consistency Issue: {str(e)}\n")

    # Data Quality Issue 3: Missing Values
    missing_values = df.isnull().sum()
    if any(missing_values):
        issues.append("Missing Values:\n" + str(missing_values) + "\n")

    # Data Quality Issue 4: Incorrect Data Types for Numeric Columns
    numeric_cols = ['Dollar Sales', 'Returns', 'Quantity']
    for col in numeric_cols:
        if df[col].dtype not in ['int64', 'float64']:
            issues.append(f"Incorrect Data Type for {col}: Expected numeric type (int or float).\n")

    return issues

# Call the function to identify data quality issues
data_quality_issues = identify_data_quality_issues(df)

# Print data quality issues
print("Data Quality Issues:")
for issue in data_quality_issues:
    print(issue)
