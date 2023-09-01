from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

engine = create_engine('sqlite:///inventory.db', echo = True)
Session = sessionmaker(bind = engine)
Base = declarative_base()

class Product(Base):
	__tablename__ = 'products'

	product_id = Column(Integer, primary_key = True)
	product_name = Column(String)
	product_quantity = Column(Integer)
	product_price = Column(Integer)
	date_updated = Column(Date)
	
	def __repr__(self):
		return f"<Product(id = {self.product_id}, name = '{self.product}', quantity = {self.product_quantity}, price = {self.product_price}, updated = {self.date_updated})>"
	
Base.metadata.create_all(engine)

def add_products_from_csv(csv_filename):
	with open(csv_filename, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			product = Product(
				product_name = row['product_name'],
				product_quantity = int(float(row['product_price']) * 100),
			date_update = datetime.strptime(row['date_updated'], '%Y-%m-%d').date()
			)
			session.add(product)
		session.commit()

if __name__ == "__main_":
	add_products_from_csv('inventory.csv')
	
	main_menu()
