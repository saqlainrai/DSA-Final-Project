class Stack:
    # dynamic stack
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"push__ {item} __ into stack")

    def pop(self):
        if not self.is_empty():
            popped_item = self.stack.pop()
            print(f"pop__ {popped_item} from  stack")
            return popped_item
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push("sami")

    print("after push operation", stack.stack)  #display function

    stack.pop()  #pop sami from stack.
    stack.pop()  # pop 10 from

    print("after pop operatoin", stack.stack)
