
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)


#create the queue
my_queue = Queue()


my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Front item ", my_queue.peek())

# Dequeueing an item
dequeued_item = my_queue.dequeue()
print("Dequeued item ", dequeued_item)

# Checking size
print("size of the queue", my_queue.size())

# enqueue
my_queue.enqueue(42)
my_queue.enqueue(512)

# dequeueing all items
while not my_queue.is_empty():
    print("item:", my_queue.dequeue())


