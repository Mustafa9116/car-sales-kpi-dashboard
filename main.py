import pandas as pd

df = pd.read_csv('Car_Sales.csv', encoding = 'latin-1')

print (df.shape)
print(df.columns.tolist())
print(df.head())
print(df.isnull().sum())
print(df['Manufacturer'].unique())

import sqlite3

conn = sqlite3.connect('car_sales.db')
df.to_sql("sales", conn, if_exists='replace', index=False)
conn.close

print("Data loaded into car_sales.db")