import pandas as pd
from datetime import datetime, timedelta
# Read the dataset into a DataFrame
df = pd.read_csv('dataset.csv')

# Data Manipulation Questions:

# Question 1: Classify the customers into their discount bracket and find the counts of distinct customers falling in each discount category
def classify_discount(row):
    transactions = row['Transaction ID']
    total_purchase = row['Dollar Sales']

    if transactions > 8 or total_purchase > 5000:
        return '30% discount'
    elif 5 <= transactions <= 8 or 2000 < total_purchase <= 5000:
        return '20% discount'
    else:
        return '10% discount'

df['Discount Category'] = df.apply(classify_discount, axis=1)
discount_counts = df['Discount Category'].value_counts()

print("Discount Category Counts:")
print(discount_counts)

# Question 2: Create a table containing Customer ID, number of transactions made, category of discount coupon, and their total dollar purchase in the last 2 years
discount_table = df.groupby('Customer ID').agg({
    'Transaction ID': 'count',
    'Discount Category': 'first',
    'Dollar Sales': 'sum'
}).reset_index()

discount_table.columns = ['Customer ID', 'Number of transactions', 'Discount Category', 'Total Dollar Purchase']

# Sort the discount_table based on the 'Total Dollar Purchase' column in descending order
discount_table = discount_table.sort_values(by='Total Dollar Purchase', ascending=False)

print("\nDiscount Table:")
print(discount_table)

# Question 3: Find the top 10 customers based on their purchase amounts in the last 6 months
# Convert 'Order Date' to datetime format with the correct format string
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y')

six_months_ago = pd.Timestamp.now() - pd.DateOffset(months=6)
top_10_customers = df[df['Order Date'] >= six_months_ago].groupby('Customer ID')['Dollar Sales'].sum().nlargest(10)

print("\nTop 10 Customers based on Purchase Amount in the Last 6 Months:")
print(top_10_customers)

# Question 4: Find the top 2 salespersons of StyleMore along with their bonuses
top_salespersons = df.groupby('Sales Person Name')['Dollar Sales'].sum().nlargest(2)

print("\nTop 2 Salespersons of StyleMore with Bonuses:")
print(top_salespersons)
