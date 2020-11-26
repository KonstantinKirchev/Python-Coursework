from user import User
from roles import Role
from category import Category
from product import Product

users_count = 0
categories_count = 0
products_count = 0

def seed_users():
	users = []
	users.append(User(users_counter(), 'Konstantin', 'Blueeagle', 'qwerty', 'kosta1@yahoo.com', Role.ADMIN, '38 Petko Karavelov str.'))
	users.append(User(users_counter(), 'Anna', 'AnnaTopolska', 'qwerty1', 'kos1@yahoo.com', Role.CUSTOMER, '38 Solunska str.'))
	users.append(User(users_counter(), 'Ivan', 'IvanIvanov', 'qwerty2', 'ko2@yahoo.com', Role.CUSTOMER, '38 Petko Karavelov str.'))
	users.append(User(users_counter(), 'Georgi', 'GeorgiKirchev', 'qwerty3', 'kosta1@gmail.co', Role.CUSTOMER, '38 Petko Karavelov str.'))

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
		Product(products_counter(), 'bananas', 'very delicious bananas', 1.99, 1000, 0),
		Product(products_counter(), 'tomatoes', 'very delicious tomatoes', 2.99, 5000, 1),
		Product(products_counter(), 'salmon', 'very delicious salmon', 12.99, 100, 2),
		Product(products_counter(), 'apples', 'very delicious apples', 2.59, 2000, 0),
		Product(products_counter(), 'grapes', 'very delicious grapes', 1.39, 3200, 0),
		Product(products_counter(), 'cucumbers', 'very delicious cucumbers', 3.19, 2600, 1),
		Product(products_counter(), 'potatoes', 'very delicious potatoes', 0.99, 10000, 1),
		Product(products_counter(), 'cod', 'very delicious cod', 8.99, 200, 2),
		Product(products_counter(), 'bass', 'very delicious bass', 9.99, 400, 2)
	]

def products_counter():
	global products_count
	products_count += 1
	return products_count
