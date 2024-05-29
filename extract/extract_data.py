import pandas as pd
from sqlalchemy import create_engine
from config.config import DATABASE_URI

def extract_data():
    engine = create_engine(DATABASE_URI)
    products = pd.read_sql('SELECT * FROM products', engine)
    customers = pd.read_sql('SELECT * FROM customers', engine)
    sales = pd.read_sql('SELECT * FROM sales', engine)
    return products, customers, sales
