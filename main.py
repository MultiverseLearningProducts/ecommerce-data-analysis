from extract.extract_data import extract_data
from transform.transform_data import transform_data
from load.load_data import load_data

def main():
    products, customers, sales = extract_data()
    transformed_data = transform_data(products, customers, sales)
    load_data(transformed_data)
    print("ETL process completed successfully")

if __name__ == '__main__':
    main()
