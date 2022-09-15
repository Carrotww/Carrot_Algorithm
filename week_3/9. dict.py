class Dict:
    def __init__(self) -> None:
        self.items = [None] * 8
    
    def put(self, key, value):
        self.items[hash(key) % len(self.items)] = value
        return
    
    def get(self, key):
        return self.items[hash(key) % len(self.items)]

test = Dict()
test.put('test', 3)
print(test.get('test'))