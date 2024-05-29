def transform_data(products, customers, sales):
    joined_data = sales.merge(products, left_on='product_id', right_on='id') \
                              .merge(customers, left_on='customer_id', right_on='id')
    relevant_data = joined_data[['product_id', 'customer_id', 'product_name', 'sale_time', 'quantity', 'price']]
    return relevant_data
