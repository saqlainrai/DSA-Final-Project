class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node




     #display the linklist
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()




    #search function
    def search(self, value):
        current = self.head
        index = 0
        found = False
        while current:
            if current.data == value:
                found = True
                break
            current = current.next
            index += 1
        if found:
            print(f"This value {value} is at index number {index}")
        else:
            print(f"This value  {value} does not exist in the linked list")

    def delete_node(self, value):
        current = self.head
        if current is None:
            print("Linkedlist is empty Now")
            return

        if current.data == value:
            self.head = current.next
            print(f"Node is deleted with this value {value} ")
            return

        prev = None
        while current:
            if current.data == value:
                prev.next = current.next
                print(f"Node is deleted with this value {value} ")
                return
            prev = current
            current = current.next

        print(f"This value  {value} is not exist in the linked list That's why deletion is failed ")


l = LinkedList()

#insertion opertaion

l.insert_at_end(1)
l.insert_at_end("sami")
l.insert_at_end(3)

print("Linked List:")
l.display()


#searching operation
l.search(3)
l.search(33)



#deletion opertion

l.delete_node(2)
l.delete_node(3)



l.display()