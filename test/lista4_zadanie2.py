from lista4_zadanie1_node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.reversed = False

    # Θ(1)
    def push_front(self, data):
        new_node = Node(data)
        if self.reversed:
            if self.is_empty():
                self.head = new_node
            else:
                self.tail.set_next(new_node)
                # jeśli lista nie była pusta, musimy ustawić previous nowego ogona na poprzedni ogon
                new_node.set_previous(self.tail)
                # next już z inita jest None
            self.tail = new_node
        else:
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
        if self.reversed:
            new_node = Node(data)
            new_node.set_next(self.head)
            # previous nie ustawiamy, bo już w inicie jest jako None i tak ma zostać dla 1. elementu listy
            if self.is_empty():
                self.tail = new_node
            else:
                # jeśli lista nie była pusta, ustawiamy previous poprzedniej głowy na nową głowę
                self.head.set_previous(new_node)
            self.head = new_node
        else:
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
        if self.is_empty():
            raise IndexError("The list is empty")
        if self.reversed:
            obj = self.tail.get_data()
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.get_previous()
                self.tail.set_next(None)
        else:
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
        if self.is_empty():
            raise IndexError("The list is empty")
        if self.reversed:
            obj = self.head.get_data()
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next()
                # musimy przestawić previous nowej głowy ze starej głowy na None
                self.head.set_previous(None)
        else:
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

    def reverse(self):
        if self.reversed:
            self.reversed = False
        else:
            self.reversed = True


if __name__ == "__main__":
    lst = LinkedList()  # -> lst: []
    for i in range(10):
        lst.push_back(i)  # -> lst: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst.reverse()
    print(lst.pop_front())
