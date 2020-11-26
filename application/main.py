import navigation as Navigation_Manager
from seeder import seed_categories, seed_products
from loginManager import LoginManager

manager = LoginManager()

categories = seed_categories()
products = seed_products()

print()
print('Welcome to Women\'s Market! Please select one of the following options:')
print()

Navigation_Manager.show_init_menu()

operation = int(input())

while(operation != 4):
	if operation == 1:
		login_info = LoginManager.login_input()
		if manager.login(login_info[0], login_info[1]):
			Navigation_Manager.show_category_menu()
			operation = int(input())
			print('---------------------------')
			while(operation != 0):
				if operation == 6:
					for product in products:
						if product.categoryId == 0:
							print(f'{product.id}.{product.name} - ${product.price}')
				elif operation == 7:
					for product in products:
						if product.categoryId == 1:
							print(product.name, product.description, product.price, product.categoryId)
				elif operation == 8:
					for product in products:
						if product.categoryId == 2:
							print(product.name, product.description, product.price, product.categoryId)
				elif operation == 0:
					Navigation_Manager.show_init_menu()
				print("0.Go back")
				operation = int(input())
				print('---------------------------')
			if operation == 0:
				Navigation_Manager.show_logged_user_menu()
				operation = int(input())
				print('---------------------------')
				if operation == 5:
					Navigation_Manager.show_category_menu()
					operation = int(input())
					print('---------------------------')
		else:
			Navigation_Manager.show_init_menu()
	elif operation == 2:
		usr = LoginManager.register_input()
		if manager.register(usr):
			Navigation_Manager.show_category_menu()
			operation = int(input())
			print('---------------------------')
			while(operation != 0):
				if operation == 6:
					for product in products:
						if product.categoryId == 0:
							print(f'{product.id}.{product.name} - ${product.price}')
				elif operation == 7:
					for product in products:
						if product.categoryId == 1:
							print(product.name, product.description, product.price, product.categoryId)
				elif operation == 8:
					for product in products:
						if product.categoryId == 2:
							print(product.name, product.description, product.price, product.categoryId)
				elif operation == 0:
					Navigation_Manager.show_init_menu()
				print("0.Go back")
				operation = int(input())
				print('---------------------------')
			if operation == 0:
				Navigation_Manager.show_logged_user_menu()
				operation = int(input())
				print('---------------------------')
				if operation == 5:
					Navigation_Manager.show_category_menu()
					operation = int(input())
					print('---------------------------')
		else:
			Navigation_Manager.show_init_menu()
			operation = int(input())
			print('---------------------------')
	elif operation == 3:
		print('---------------------------')
		manager.logout()
		Navigation_Manager.show_init_menu()
		operation = int(input())


print('Thank you for using Women\'s Market! We hope will see you soon. Have a nice day :)')
print()
