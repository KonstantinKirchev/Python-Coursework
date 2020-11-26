from user import User
from roles import Role
from category import Category
from product import Product

users_count = -1
categories_count = -1
products_count = -1

def seed_users():
	users = []
	users.append(User(users_counter(), 'Konstantin', 'Blueeagle', 'qwerty', Role.ADMIN, '38 Petko Karavelov str.'))
	users.append(User(users_counter(), 'Anna', 'AnnaTopolska', 'qwerty', Role.CUSTOMER, '38 Solunska str.'))
	users.append(User(users_counter(), 'Ivan', 'IvanIvanov', 'qwerty', Role.CUSTOMER, '38 Petko Karavelov str.'))
	users.append(User(users_counter(), 'Georgi', 'GeorgiKirchev', 'qwerty', Role.CUSTOMER, '38 Petko Karavelov str.'))

	return users
	
def users_counter():
	global users_count
	users_count += 1
	return users_count

def seed_categories():
	return [
		Category(categories_counter(), "fruits", False),
		Category(categories_counter(), "vegetables", False),
		Category(categories_counter(), "fishes", False)
	]

def categories_counter():
	global categories_count
	categories_count += 1
	return categories_count

def seed_products():
	return [
		Product(products_counter(), 'bananas', 'very delicious fruits', 1.99, 1000, 0),
		Product(products_counter(), 'tomatoes', 'very delicious vegetables', 2.99, 5000, 1),
		Product(products_counter(), 'salmon', 'very delicious fish', 12.99, 100, 2)
	]

def products_counter():
	global products_count
	products_count += 1
	return products_count
