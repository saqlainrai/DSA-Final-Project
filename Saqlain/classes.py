
class User():
    def __init__(self, name, password, index):
        self.username = name
        self.password = password
        self.index = index
        self.loginScreen = None

class UserDetail(User):
    def __init__(self, username, password, index):
        super().__init__(username, password, index)
        self.name = ""
        self.fname = ""
        self.email = ""
        self.cnic = ""
        self.contact = ""
        self.location = ""

class Order(User):
    def __init__(self, username, password, index):
        super().__init__(username, password, index)
        self.name = ""
        self.price = ""
        self.total = ""
        self.quantity = ""
        self.location = ""
        self.date = ""
