from models import (Base, session, 
Products, engine)
import datetime
import csv
import time

Base.metadata.create_all(engine)



def read_csv(filename = 'inventory.csv'):
    products_list = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = {
                'product_name': row['product_name'],
                'product_quantity': int(row['product_quantity']),
                'product_price': clean_price(row['product_price']),
                'date_updated': clean_date(row['date_updated'])
            }
            products_list.append(product)
    return products_list



def add_products_from_csv():
    products = read_csv()
    for product in products:
        new_product = Products(
            product_name = product['product_name'],
            product_quantity = product['product_quantity'],
            product_price = product['product_price'],
            date_updated = product['date_updated']
        )
        session.add(new_product)
    session.commit()


if __name__ == '__main__':
    add_products_from_csv()
    main()

def clean_date(date_str):
    try:
        date = datetime.datetime.strptime(date_str, '%B %d, %Y').date()
        return date
    except ValueError:
        print("\n****** DATE ERROR ******")
        print("The date format should be: Month Day, Year (Ex: January 13, 2003)")
        return None

def clean_price(price_str):
    try:
        price_str = price_str.replace(',', '')
        price = int(float(price_str) * 100)
        return price
    except ValueError:
        print("\n****** PRICE ERROR ******")
        print("The price should be a valid number without a currency symbol (Ex: 10.99)")
        return None

def menu():
    while True:
        print('''
        \nSTORE INVENTORY MANAGEMENT
        \rV) View all products
        \rA) Add product
        \rB) Backup database
        \rQ) Quit''')
        choice = input('What would you like to do ? ')
        if choice in ['V', 'A', 'B', 'Q']:
            return choice
        else:
            input('''
              \rPlease choose from one of the options above.
              \rPress Enter to try again''')

def add_product():
    product_name = input('Enter the product name: ')
    product_quantity = int(input('Enter the product quantity: '))
    product_price_str = input('Enter the price of the product (Ex: 2.99): ')
    product_price = int(float(product_price_str) * 100)

    new_product = Products(
        product_name = product_name,
        product_quantity = product_quantity,
        product_price = product_price,
        date_updated = datetime.date.today()
    )
    session.add(new_product)
    session.commit()
    print('The product has successfully been added !')

def view_all_products():
    products = session.query(Products).all()
    if products:
        print('\nAll Products:')
        for product in products:
            print(f'Product ID: {product.product_id}')
            print(f'Product Name: {product.product_name}')
            print(f'Product Quantity: {product.product_quantity}')
            print(f'Product Price: ${product.product_price / 100:.2f}')
            print(f'Date Updated: {product.date_updated.strftime("%Y-%m-%d")}')
            print('-' * 30)
    else:
        print('\nThere are no products in the database at the moment.')

def backup_to_csv():
    products = session.query(Products).all()
    if products:
        with open('backup.csv', 'w', newline='') as csvfile:
            fieldnames = ['product_name', 'product_quantity', 'product_price', 'date_updated']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product in products:
                writer.writerow({
                    'product_name': product.product_name,
                    'product_quantity': product.product_quantity,
                    'product_price': product.product_price / 100.0,
                    'date_updated': product.date_updated.strftime('%Y-%m-%d')
                })
        print('Backup has been exported to backup.csv')
    else:
        print('There are no products in the database to export at the moment.')

def main():
    while True:
        choice = menu()
        if choice == 'V':
            view_all_products()
        elif choice == 'A':
            add_product()
        elif choice == 'B':
            backup_to_csv()
        elif choice == 'Q':
            print('Goodbye !')
            break

if __name__ == '__main__':
    main()
