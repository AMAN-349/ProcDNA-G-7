import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dataset.csv')


df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y')

# Data Visualization Questions:

# Question 1: Create a time series graph showing month over month absolute sales and sales growth

df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Dollar Sales'].sum()


monthly_sales.index = monthly_sales.index.to_timestamp()


monthly_sales_growth = monthly_sales.pct_change()

# Question 2: Visualize sales distribution by products in each category

product_sales = df.groupby(['Category', 'Product Name'])['Dollar Sales'].sum()


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))


axes[0].plot(monthly_sales.index, monthly_sales, label='Absolute Sales', marker='o')
axes[0].plot(monthly_sales.index, monthly_sales_growth, label='Sales Growth', marker='o')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Sales')
axes[0].set_title('Monthly Sales and Sales Growth')
axes[0].legend()
axes[0].tick_params(rotation=45)
axes[0].grid()


product_sales.plot(kind='bar', ax=axes[1])
axes[1].set_xlabel('Category, Product Name')
axes[1].set_ylabel('Sales')
axes[1].set_title('Sales Distribution by Products in Each Category')
axes[1].tick_params(rotation=45)
axes[1].grid()

plt.tight_layout()
plt.show()
