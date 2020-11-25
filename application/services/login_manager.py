def show_menu():
	print("1.Login")
	print("2.Register")
	print("3.Logout")
	print("4.Exit program")
	print()


def login():
	username = input("Username:")
	password = input("Password:")

	return (username, password)


def register():
	name = input("Name:")
	username = input("Username:")
	password = input("Password:")
	email = input("Email:")
	address = input("Address:")

	return (name, username, password, email, address)
