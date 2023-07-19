import pandas as pd
from datetime import datetime, timedelta


df = pd.read_csv('dataset.csv')



def identify_data_quality_issues(df):
    issues = []


    duplicate_transactions = df[df.duplicated('Transaction ID', keep=False)]
    if not duplicate_transactions.empty:
        issues.append("Duplicate Transactions:\n" + str(duplicate_transactions) + "\n")


    try:
        df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y', errors='raise')
    except Exception as e:
        issues.append(f"Date Format Consistency Issue: {str(e)}\n")


    missing_values = df.isnull().sum()
    if any(missing_values):
        issues.append("Missing Values:\n" + str(missing_values) + "\n")


    numeric_cols = ['Dollar Sales', 'Returns', 'Quantity']
    for col in numeric_cols:
        if df[col].dtype not in ['int64', 'float64']:
            issues.append(f"Incorrect Data Type for {col}: Expected numeric type (int or float).\n")

    return issues


data_quality_issues = identify_data_quality_issues(df)


print("Data Quality Issues:")
for issue in data_quality_issues:
    print(issue)
