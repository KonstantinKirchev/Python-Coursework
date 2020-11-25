import services.login_manager as login_manager
from services.models.loginManager import LoginManager

manager = LoginManager()
users = []

login_manager.show_menu()

operation = int(input())

while(operation != 4):
	if operation == 1:
		login_info = login_manager.login()
		manager.login(login_info[0], login_info[1])
	elif operation == 2:
		usr = login_manager.register()
		manager.register(usr)
	elif operation == 3:
		print()
		manager.logout()
	login_manager.show_menu()
	operation = int(input())
