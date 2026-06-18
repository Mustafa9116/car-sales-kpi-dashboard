import sqlite3
import pandas as pd

# KPI 1 
def get_connection():
    return sqlite3.connect("car_sales.db")

def top_manufacturers_by_sales():
    conn = get_connection()
    query = """
     SELECT Manufacturer, ROUND(SUM(Sales_in_thousands),2) AS Total_Sales
     FROM sales
     GROUP BY Manufacturer
     ORDER BY Total_Sales DESC
     LIMIT 10;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

  
# KPI 2
def avg_price_by_vehicle_type():
    conn = get_connection()
    query = """
     SELECT Vehicle_type, ROUND(AVG(Price_in_thousands),2) AS Avg_Price
     FROM sales
     WHERE Price_in_thousands IS NOT NULL
     GROUP BY Vehicle_type
     ORDER BY Avg_Price DESC;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df



#KPI 3 

def top_fuel_efficient_cars():
    conn = get_connection()
    query = """
        SELECT Manufacturer, Model, Fuel_efficiency
        FROM sales
        WHERE Fuel_efficiency IS NOT NULL
        ORDER BY Fuel_efficiency DESC
        LIMIT 10
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df



#KPI 4

def top_models_by_resale_value():
    conn = get_connection()
    query = """
        SELECT Manufacturer, Model, ROUND(__year_resale_value, 2) AS resale_value
        FROM sales
        WHERE __year_resale_value IS NOT NULL
        ORDER BY resale_value DESC
        LIMIT 10
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df



#KPI 5

def horsepower_vs_price():
    conn = get_connection()
    query = """
        SELECT Manufacturer, Model, Horsepower, Price_in_thousands
        FROM sales
        WHERE Horsepower IS NOT NULL AND Price_in_thousands IS NOT NULL
        ORDER BY Horsepower DESC
        LIMIT 15
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

print(top_models_by_resale_value())