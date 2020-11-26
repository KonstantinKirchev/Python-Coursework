from roles import Role

class User:
    def __init__(self, id: str, name: str, username: str, password: str, role: Role, address: str):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.role = role
        self.address = address
