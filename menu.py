def main_menu():
	while True:
		print("Main Menu: ")
		print("V: View the product details by the ID")
		print("A: Add a new product")
		print("B: Backup the database")
		print("E: Quit/Exit")
		
		choice = input("Enter your option: ")
		
		if option == 'V':
			view_product_by_id()
		elif option == 'A':
			add_new_product()
		elif option == 'B':
			backup_database()
		elif option == 'E':
			print("Quiting the application")
			break
		else:
			print("Invalid choice. Please select a valid option")
			
def view_product_by_id():
	product_id = input("Enter the product ID: ")
    product = session.query(Product).filter_by(product_id=product_id).first()
    if product:
        print(f"Product ID: {product.product_id}")
        print(f"Product Name: {product.product_name}")
        print(f"Product Quantity: {product.product_quantity}")
        print(f"Product Price (cents): {product.product_price}")
        print(f"Date Updated: {product.date_updated}")
    else:
        print("The product is not found.")
	
def add_new_product():
	product_name = input("Enter the product name: ")
    product_quantity = int(input("Enter the product quantity: "))
    product_price = int(float(input("Enter the product price (e.g., 2.99): ") * 100))
    date_updated = datetime.now()

    new_product = Product(
        product_name=product_name,
        product_quantity=product_quantity,
        product_price=product_price,
        date_updated=date_updated
    )

    session.add(new_product)
    session.commit()
    print("Product added successfully to the database !")

def backup_database():
	products = session.query(Product).all()

    with open("backup.csv", mode="w", newline="") as file:
        file.write("product_id,product_name,product_quantity,product_price,date_updated\n")
        for product in products:
            file.write(f"{product.product_id},{product.product_name},{product.product_quantity},{product.product_price},{product.date_updated}\n")

    print("Database backup is complete !")
