import hashlib

class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, data):
        new_Node = Node(data)
        new_Node.Next = self.head
        self.head = new_Node

    def insertAtTail(self, data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            return
        if self.head.Next is None:
            self.insertAtHead(data)

        temp = self.head
        while temp.Next:
            temp = temp.Next
        temp.Next = new_Node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.Next

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(value)
        else:
            current = self.table[index]
            while current.Next:
                current = current.Next
            current.Next = Node(value)

    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            return current.data
            current = current.Next
        return None

class Users:
    def __init__(self):
        self.Name = LinkedList()
        self.passwords = HashTable(100)  # Initialize a hash table specifically for passwords
        self.Address = LinkedList()

    def add_user(self, name, password, address):
        self.Name.insertAtTail(name)
        self.passwords.insert(name, password)  # Store password in the hash table
        self.Address.insertAtTail(address)

    def verify_password(self, username, password):
        stored_password = self.passwords.get(username)
        if stored_password is not None and stored_password == password:
            return True
        return False

    def login(self, username, password):
        return self.verify_password(username, password)

def main():
    users_Obj = Users()
    users_Obj.add_user("Tabish", "pass123", "UET")
    users_Obj.add_user("Akhtar", "456", "Chung")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if users_Obj.login(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()
