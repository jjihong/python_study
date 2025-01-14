class Dict:
    def __init__(self):
        self.items = [None] * 8

    # 8칸이기 때문에 값이 덮어써질 수 있다. 따라서 링크드리스트로 관리한다. chaining기법

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
