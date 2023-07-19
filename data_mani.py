import pandas as pd
from datetime import datetime, timedelta

# Read the dataset into a DataFrame
df = pd.read_csv('dataset.csv')

# Data Quality Questions:

# Q1. List the data quality issues found in the datasets with examples
def list_data_quality_issues(df):
    issues = []

    # Data Quality Issue 1: Duplicate Transactions
    duplicate_transactions = df[df.duplicated('Transaction ID', keep=False)]
    if not duplicate_transactions.empty:
        issues.append("Duplicate Transactions:\n" + str(duplicate_transactions.head()) + "\n")

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

# Call the function to list data quality issues with examples
data_quality_issues = list_data_quality_issues(df)

# Print data quality issues with examples
print("Data Quality Issues:")
for issue in data_quality_issues:
    print(issue)

# Q2. Write a logic/algorithm to identify and report data quality issues
def identify_data_quality_issues(df):
    issues = []

    # Check for duplicate transactions
    duplicate_transactions = df[df.duplicated('Transaction ID', keep=False)]
    if not duplicate_transactions.empty:
        issues.append("Duplicate Transactions:\n" + str(duplicate_transactions) + "\n")

    # Check for date format consistency and convert to standardized format
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y', errors='coerce')

    # Check for missing values
    missing_values = df.isnull().sum()
    if any(missing_values):
        issues.append("Missing Values:\n" + str(missing_values) + "\n")

    # Check data types of numeric columns
    numeric_cols = ['Dollar Sales', 'Returns', 'Quantity']
    for col in numeric_cols:
        if df[col].dtype not in ['int64', 'float64']:
            issues.append(f"Incorrect Data Type for {col}: Expected numeric type (int or float).\n")

    return issues

# Call the function to identify data quality issues
data_quality_issues = identify_data_quality_issues(df)

# Report data quality issues
print("\nData Quality Issues:")
for issue in data_quality_issues:
    print(issue)

# Q3. Identify critical quality issues impacting results in data manipulation questions.
# In this case, we don't need any additional code. The identified data quality issues can impact the results.
# You can refer to the data quality issues found in Q1 and Q2 to understand the potential impact.

