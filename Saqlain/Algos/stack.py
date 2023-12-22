class Stack:
    # dynamic stack
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"push__ {item} __ into stack")

    def popAtIndex(self, index):
        if index < len(self.stack):
            tempStack = Stack()
            for i in range(len(self.stack)-1, index, -1):
                tempStack.push(self.stack[i])
                self.stack.pop()
            popped_item = self.stack.pop()
            while not tempStack.is_empty():
                self.stack.append(tempStack.pop())
            return popped_item
        else:
            print("Stack is empty.")
            return None

    def pop(self):
        if not self.is_empty():
            popped_item = self.stack.pop()
            print(f"pop__ {popped_item} from  stack")
            return popped_item
        else:
            print("Stack is empty.")
            return None
        
    def clearStack(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    

if __name__ == "__main__":
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.push('d')
    print(stack.popAtIndex(3))
    print(stack.stack)