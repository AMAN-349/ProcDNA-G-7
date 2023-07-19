import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv('dataset.csv')


df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y')





df['Dollar Sales'] = pd.to_numeric(df['Dollar Sales'])


eligible_customers = df[df['Order Date'] < '2022-01-01']


transactions_per_customer = eligible_customers.groupby('Customer ID')['Transaction ID'].nunique().reset_index()
transactions_per_customer.rename(columns={'Transaction ID': 'Number of Transactions'}, inplace=True)


total_purchases_per_customer = eligible_customers.groupby('Customer ID')['Dollar Sales'].sum().reset_index()
total_purchases_per_customer.rename(columns={'Dollar Sales': 'Total Dollar Purchase'}, inplace=True)


customer_data = pd.merge(transactions_per_customer, total_purchases_per_customer, on='Customer ID')


def classify_discount(row):
    transactions = row['Number of Transactions']
    total_purchase = row['Total Dollar Purchase']

    if transactions > 8 or total_purchase > 5000:
        return '30% discount'
    elif 5 <= transactions <= 8 or 2000 < total_purchase <= 5000:
        return '20% discount'
    else:
        return '10% discount'


customer_data['Discount Category'] = customer_data.apply(classify_discount, axis=1)

# Print the final table containing Customer ID, number of transactions made, category of discount coupon,
# and their total dollar purchase in the last 2 years
print(customer_data)
