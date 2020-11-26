from roles import Role

class User:
    def __init__(self, id: str, name: str, username: str, password: str, email: str, role: Role, address: str):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.address = address
