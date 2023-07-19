import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv('dataset.csv')


df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y')



eligible_customers = df[df['Order Date'] < '2022-01-01']


transactions_per_customer = eligible_customers.groupby('Customer ID')['Transaction ID'].nunique().reset_index()
transactions_per_customer.rename(columns={'Transaction ID': 'Transaction Count'}, inplace=True)


total_purchases_per_customer = eligible_customers.groupby('Customer ID')['Dollar Sales'].sum().reset_index()
total_purchases_per_customer.rename(columns={'Dollar Sales': 'Total Purchases'}, inplace=True)


customer_data = pd.merge(transactions_per_customer, total_purchases_per_customer, on='Customer ID')


def classify_discount(customer):
    if customer['Transaction Count'] > 8 or customer['Total Purchases'] > 5000:
        return '30%'
    elif 5 <= customer['Transaction Count'] <= 8 or 2000 < customer['Total Purchases'] < 5000:
        return '20%'
    else:
        return '10%'


customer_data['Discount Bracket'] = customer_data.apply(classify_discount, axis=1)


discount_counts = customer_data['Discount Bracket'].value_counts()

print(discount_counts)
