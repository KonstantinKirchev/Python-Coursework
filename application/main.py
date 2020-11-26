import login_manager as Login_Manager
from seeder import seed_users, seed_categories, seed_products
from loginManager import LoginManager

manager = LoginManager()
users = seed_users()
categories = seed_categories()
products = seed_products()

# for user in users:
# 	print(user.id, user.name)

# for category in categories:
# 	print(category.id, category.name)

# for product in products:
# 	print(product.name, product.description, product.price, product.categoryId)

print('Welcome to Womens Market! Please select one of the following options:')
print()

Login_Manager.show_menu()

operation = int(input())

while(operation != 4):
	if operation == 1:
		login_info = Login_Manager.login()
		manager.login(login_info[0], login_info[1])
	elif operation == 2:
		usr = Login_Manager.register()
		manager.register(usr)
	elif operation == 3:
		print()
		manager.logout()
	Login_Manager.show_menu()
	operation = int(input())
