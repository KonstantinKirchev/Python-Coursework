from seeder import seed_users, users_counter
from user import User
from roles import Role

class LoginManager:

	def __init__(self):
		self.current_user = None
		self.users = seed_users()

	def login_input():
		username = input("Username:")
		password = input("Password:")
		return (username, password)

	def register_input():
		name = input("Name:")
		username = input("Username:")
		password = input("Password:")
		email = input("Email:")
		address = input("Address:")
		return (name, username, password, email, address)
  
	def login(self,username, password):
		for user in self.users:
			if username == user.username and password == user.password:
				self.current_user = user
				
		if self.current_user != None:
			print('---------------------------')
			print(f'Welcome {self.current_user.name}. Please select one of the following options:')
			print('---------------------------')
			return True
		else:
			print("No such user. Please try again.")
			return False

	def logout(self):
		if self.current_user != None:
			print("Logging out:", self.current_user.name)
			for user in self.users:
				print(user.id, user.name, user.username, user.password, user.role)
		else:
			print("No user to logout")

	def register(self,currentUser):

		for user in self.users:
			if currentUser[1] == user.username and currentUser[2] == user.password:
				print("Such a user already exists. Please login with your credentails.")
				return False
			else:
				tempUser = User(users_counter(), currentUser[0], currentUser[1], currentUser[2], currentUser[3], Role.CUSTOMER, currentUser[4])
				self.users.append(tempUser)
				for user in self.users:
					print(user.id, user.name, user.username, user.password, user.role)
				self.current_user = tempUser
				print('---------------------------')
				print(f'Welcome {self.current_user.name}. Please select one of the following options:')
				print('---------------------------')
				return True
