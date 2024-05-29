import pandas as pd
from extract.extract_data import extract_data
from transform.transform_data import transform_data
from load.load_data import load_data

def test_etl_process():
    products, customers, sales = extract_data()
    assert not products.empty, "products data extraction failed"
    assert not customers.empty, "customers data extraction failed"
    assert not sales.empty, "sales data extraction failed"

    transformed_data = transform_data(products, customers, sales)
    assert 'product_id' in transformed_data.columns, "Transformation failed for product_id"
    assert 'customer_id' in transformed_data.columns, "Transformation failed for customer_id"

    try:
        load_data(transformed_data)
        print("ETL process completed successfully")
    except Exception as e:
        print(f"ETL process failed: {e}")

if __name__ == '__main__':
    test_etl_process()
