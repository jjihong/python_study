class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!
    str1 = ""
    str2 = ""

    # 중복되니까 함수로 만들자.
    cur1 = linked_list_1.head
    while cur1 is not None:
        str1 += str(cur1.data)
        cur1 = cur1.next

    cur2 = linked_list_2.head
    while cur2 is not None:
        str2 += str(cur2.data)
        cur2 = cur2.next


    print(str1, str2)
    result = int(str1) + int(str2)

    return result


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))