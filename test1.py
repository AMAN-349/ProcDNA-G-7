import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv('dataset.csv')


df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y')



# Convert the 'Customer ID' column to integers and 'Dollar Sales' column to numeric values
# df['Customer ID'] = df['Customer ID'].astype(int)
df['Dollar Sales'] = pd.to_numeric(df['Dollar Sales'])

# Filter customers who made transactions before January 1st, 2022
eligible_customers = df[df['Order Date'] < '2022-01-01']

# Calculate the number of transactions made by each customer in the last 2 years
transactions_per_customer = eligible_customers.groupby('Customer ID')['Transaction ID'].nunique().reset_index()
transactions_per_customer.rename(columns={'Transaction ID': 'Number of Transactions'}, inplace=True)

# Calculate the total purchases made by each customer
total_purchases_per_customer = eligible_customers.groupby('Customer ID')['Dollar Sales'].sum().reset_index()
total_purchases_per_customer.rename(columns={'Dollar Sales': 'Total Dollar Purchase'}, inplace=True)

# Merge the two dataframes to get all the required metrics for each customer
customer_data = pd.merge(transactions_per_customer, total_purchases_per_customer, on='Customer ID')

# Function to apply discount criteria and classify customers
def classify_discount(row):
    transactions = row['Number of Transactions']
    total_purchase = row['Total Dollar Purchase']

    if transactions > 8 or total_purchase > 5000:
        return '30% discount'
    elif 5 <= transactions <= 8 or 2000 < total_purchase <= 5000:
        return '20% discount'
    else:
        return '10% discount'

# Apply the classify_discount function to each row and create a new column for discount bracket
customer_data['Discount Category'] = customer_data.apply(classify_discount, axis=1)

# Print the final table containing Customer ID, number of transactions made, category of discount coupon,
# and their total dollar purchase in the last 2 years
print(customer_data)