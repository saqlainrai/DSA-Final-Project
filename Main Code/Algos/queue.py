
class queue():
    def __init__(self):
        self._queue = []

    def enqueue(self, data):
        self._queue.append(data)

    def dequeue(self):
        if self._queue:
            return self._queue.pop(0)
        else:
            return None

    def print_queue(self):
        print(self._queue)

    def is_empty(self):
        return len(self._queue) == 0
    
    def clearQueue(self):
        self._queue = []

    def dequeueAtIndex(self, index):
        if index < len(self._queue):
            tempQueue = queue()
            for i in range(len(self._queue)-1, index, -1):
                tempQueue.enqueue(self._queue[i])
                self._queue.pop()
            dequeued_item = self._queue.pop()
            while not tempQueue.is_empty():
                self._queue.append(tempQueue.dequeue())
            return dequeued_item
        else:
            print("Queue is empty.")
            return None

def main():
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.print_queue()
    q.dequeueAtIndex(2)
    q.print_queue()

if __name__ == "__main__":
    main()