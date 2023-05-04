class Stack:
    def __init__(self, values = []):
        self.items = []
        for item in values:
            self.push(item)

    # Θ(1)
    def is_empty(self):
        return self.items == []

    # Θ(1)
    def push(self, item):
        self.items.append(item)

    # Θ(1)
    def pop(self):
        if self.items == []:
            raise ValueError
        else:
            return self.items.pop()

    # Θ(1)
    def peek(self):
        if self.items == []:
            raise ValueError
        else:
            return self.items[-1]

    # Θ(1)
    def size(self):
        return len(self.items)
    
    def __str__(self):
        string = '['
        for item in self.items:
            string += str(item)
            string += ', '

        string2 = string.removesuffix(', ')
        string2 += ']'

        return string2
    
if __name__ == "__main__":
    s = Stack() # s -> []
    # s.pop()
    print(s.is_empty()) # True
    s.push('A') # s -> ['A']
    print(s)
    s.push('B') # s -> ['A', 'B']
    s.push('C') # s -> ['A', 'B', 'C']
    s.pop()     # s -> ['A', 'B']
    s.push('Z') # s -> ['A', 'B', 'Z']
    s.push(100) # s -> ['A', 'B', 'Z', 100]
    print(s.items)
    print(s)

    z = Stack(values = ['a', 'b', 'c'])
    print(z)