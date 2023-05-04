from lista4_zadanie1_node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Θ(1)
    def push_front(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        # previous nie ustawiamy, bo już w inicie jest jako None i tak ma zostać dla 1. elementu listy
        if self.is_empty():
            self.tail = new_node
        else:
            # jeśli lista nie była pusta, ustawiamy previous poprzedniej głowy na nową głowę
            self.head.set_previous(new_node)
        self.head = new_node

    # Θ(1)
    def push_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.set_next(new_node)
            # jeśli lista nie była pusta, musimy ustawić previous nowego ogona na poprzedni ogon
            new_node.set_previous(self.tail)
            # next już z inita jest None
        self.tail = new_node

    # Θ(1)
    def pop_front(self):
        obj = self.head.get_data()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
            # musimy przestawić previous nowej głowy ze starej głowy na None
            self.head.set_previous(None)
        return obj

    # Θ(1)
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
        n = self.size()
        if self.is_empty():
            raise IndexError("The list is empty")
        if pos < 0 or pos > n - 1:
            raise IndexError("The position is out of list's range")
        if pos == 0:
            return self.pop_front()
        else:
            if pos == n - 1:
                return self.pop_back()
            if n - pos >= pos:
                curr_elem = self.head
                for _ in range(pos):
                    curr_elem = curr_elem.get_next()
            else:
                curr_elem = self.tail
                for _ in range(n - pos - 1):
                    curr_elem = curr_elem.get_previous()
            obj = curr_elem.get_data()
            previous_elem = curr_elem.get_previous()
            next_elem = curr_elem.get_next()
            previous_elem.set_next(next_elem)
            next_elem.set_previous(previous_elem)
            return obj

    def insert(self, data, pos=0):
        n = self.size()
        if pos < 0 or pos > n:
            raise IndexError("The position is out of list's range")
        new_node = Node(data)
        if pos == 0:
            return self.push_front(data)
        else:
            if pos == n:
                return self.push_back(data)
            if n - pos >= pos:
                curr_elem = self.head
                for _ in range(pos):
                    curr_elem = curr_elem.get_next()
            else:
                curr_elem = self.tail
                for _ in range(pos):
                    curr_elem = curr_elem.get_previous()
            previous_elem = curr_elem.get_previous()
            new_node.set_next(curr_elem)
            new_node.set_previous(previous_elem)
            previous_elem.set_next(new_node)
            curr_elem.set_previous(new_node)


if __name__ == "__main__":
    lst = LinkedList()  # -> lst: []
    for i in range(5):
        lst.push_back(i)  # -> lst: [0, 1, 2, 3, 4]
    print(lst.pop(3))  # -> lst: [0, 1, 2, 4]
    print(lst.pop(3))  # -> lst: [0, 1, 2]
    print("-----")
    lst.insert(10000, 1)  # -> lst: [0, 10000, 1, 2]
    while not lst.is_empty():
        print(lst.pop_front())
