import pandas as pd
import numpy as np
from faker import Faker
import faker_commerce

if __name__ == "__main__":
    fake = Faker()
    fake.add_provider(faker_commerce.Provider)

    num_customers = 30  # Set the desired number of customers
    num_products = 10   # Set the desired number of products
    num_orders = 600  # Set the desired number of orders

    # Generating unique customer names and IDs
    customers_df = pd.DataFrame({
        'Customer ID': range(1, num_customers + 1),
        'Customer Name': [fake.name() for _ in range(num_customers)]
    })

    # Generating unique product names and IDs
    products_df = pd.DataFrame({
        'Product ID': range(1, num_products + 1),
        'Product Name': [fake.ecommerce_name() for _ in range(num_products)],
    })

    # Creating sample data
    data = {
        'Order Date': pd.date_range(start='2023-01-01', end='2023-12-31', periods=num_orders),
        'Customer ID': np.random.choice(customers_df['Customer ID'], size=num_orders),
        'Product ID': np.random.choice(products_df['Product ID'], size=num_orders),
        'Product Price': np.random.randint(10, 50, size=num_orders),
        'Quantity': np.random.randint(1, 10, size=num_orders),
    }

    # Finding customer name and product name
    data['Customer Name'] = customers_df.loc[data['Customer ID'] -
                                             1, 'Customer Name'].values
    data['Product Name'] = products_df.loc[data['Product ID'] -
                                           1, 'Product Name'].values

    # Calculating total value
    data['Total Value'] = data['Product Price'] * data['Quantity']

    # Creating DataFrame
    orders_df = pd.DataFrame(data)

    # Rearranging columns in the DataFrame
    desired_order = ['Order Date', 'Customer ID', 'Customer Name',
                     'Product ID', 'Product Name', 'Product Price', 'Quantity', 'Total Value']
    orders_df = orders_df[desired_order]

    # Saving the DataFrame
    orders_df.to_csv('orders.csv', index=False)
    print(f'{num_orders} orders generated and saved in orders.csv')
