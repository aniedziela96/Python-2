from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Θ(1)
    def push_front(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        if self.is_empty():
            self.tail = new_node
        else:
            self.head.set_previous(new_node)
        self.head = new_node

    # Θ(1)
    def push_back(self, data):
        new_node = Node(data)
        new_node.set_previous(self.tail)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node


    # Θ(1)
    def pop_front(self):
        obj = self.head.get_data()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
            self.head.set_previous(None)
        
        return obj
    
    def pop_back(self):
        obj = self.tail.get_data()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_previous()
            self.tail.set_next(None)
        return obj

    # Θ(n)
    def size(self):
        n = 0
        current = self.head
        while current is not None:
            current = current.get_next()
            n += 1
        return n

    # Θ(1)
    def is_empty(self):
        return self.head is None
    
    def pop(self, pos=0):
        if pos == 0:
            return(self.pop_front())
        else:
            obj = self.head
            for i in range(pos):
                if obj is None:
                    raise ValueError("There's no such position in the list")
                obj = obj.get_next()
                
            if obj.get_next() is None:
                self.pop_back()
            else:
                obj.get_previous().set_next(obj.get_next())
                obj.get_next().set_previous(obj.get_previous())
                return obj.get_data()
            
    def insert(self, data, pos=0):
        new_node = Node(data)
        obj1 = self.head
        if self.is_empty() or pos == 0:
            self.push_front(new_node)
        else:
            for i in range(pos-1):
                obj1 = obj1.get_next()
                
            obj2 = obj1.get_next()
            if obj2 is None:
                self.push_back(data)
            else:
                obj1.set_next(new_node)
                obj2.set_previous(new_node)
                new_node.set_next(obj2)
                new_node.set_previous(obj1) 

    def __iter__(self):
        while not self.is_empty():
            yield self.pop_front()



if __name__ == "__main__":
    lst = LinkedList()  # -> lst: []
    for i in range(10):
        lst.push_back(i)  # -> lst: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for _ in range(5):
        print(lst.pop_front())  # -> 0, 1, 2, 3, 4; lst: [5, 6, 7, 8, 9]
    print('---')
    for i in range(-1, -4, -1):
        lst.push_front(i)  # lst: [-3, -2, -1, 5, 6, 7, 8, 9]
    print('---')
    print(lst.pop_back())
    lst.insert(7, pos=2)
    print('---')
    for item in lst:
        print(item)

    print('----')
    
    while not lst.is_empty():
        print(lst.pop_front())  # -3, -2, -1, 5, 6, 7, 8, 9; lst: []
