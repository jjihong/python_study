# 링크드리스트로 작성,
# LIFO
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next =  self.head
        self.head = new_head
        return

    # pop 기능 구현
    def pop(self):
        if(self.is_empty()):
            return "stack is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if(self.is_empty()):
            return "stack is empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(4)
print(stack.head.data)

stack.push(3)
print(stack.head.data)

stack.push(5)
print(stack.head.data)

stack.pop()
stack.pop()
stack.pop()
print(stack.peek())

# 비어있는 데이터에서 더 빼면 에러가 뜨기때문에 예외처리 필요,