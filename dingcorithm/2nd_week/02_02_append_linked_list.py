class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self, value):
        self.head = Node(value)

    #   링크드리스트 끝에 다음 노드를 연결헤줘.
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            print(cur.data)

linked_list = linked_list(5)
print(linked_list.head.data)

linked_list.append(12)
linked_list.append(8)
linked_list.print_all()