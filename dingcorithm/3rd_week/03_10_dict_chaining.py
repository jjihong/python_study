class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v


class Dict:
    def __init__(self):
        self.items = [None] * 8

    # 8칸이기 때문에 값이 덮어써질 수 있다. 따라서 링크드리스트로 관리한다. chaining기법
    # 단순 링크드리스트로만 넣는다고 해결이 아님.
    # self.items[1] = ["333" , 7 ] -> [ "77" , 6 ]

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]

# 링크드 튜플과 Dict를 활용해서 만든다.


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

# 만약, 입력된 key가 "fast" 인데 index 값이 2가 나왔다.
# 현재 self.items[2] 가 [("slow", "느린")] 이었다!
# 그렇다면 새로 넣는 key, value 값을 뒤에 붙여주자!
# self.items[2] == [("slow", "느린") -> ("fast", "빠른")] 이렇게!


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
