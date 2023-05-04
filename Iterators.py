from random import random
from copy import copy
from itertools import count, tee

class Integers:
    def __init__(self):
        self.n = None
    
    def __next__(self):
        if self.n is None:
            self.n = 0
            return self.n
        elif self.n == 0:
            self.n = 1
            return self.n
        elif self.n > 0:
            self.n *= -1
            return self.n
        else:
            self.n = abs(self.n) + 1
            return self.n 
    
    def __iter__(self):
        return self
    
class Contract:
    def __init__(self, r) -> None:
        self.r = r

    def __next__(self):
        self.r = self.r * random()
        return self.r

    def __iter__(self):
        return self
    
class MovingAverage1:
    def __init__(self, it):
        self.iterator = iter(it)
        self.lst = [0]
        
        for i in range(2):
            self.lst.append(next(self.iterator))

    def __next__(self):
        # avg = 0
        self.lst.append(next(self.iterator))
        
        self.lst.pop(0)

        return sum(self.lst) / 3
        

    def __iter__(self):
        return self

class MovingAverage2:
    def __init__(self, it, k=1):
        self.step = k
        self.iterator = iter(it)
        self.lst = [0]
        
        for i in range(self.step - 1):
            self.lst.append(next(self.iterator))

    def __next__(self):
        # avg = 0
        self.lst.append(next(self.iterator))
        
        self.lst.pop(0)

        # # iterator_copy = copy(self.iterator)
        # # for i in range(self.step - 1):
        # #     avg += next(self.iterator)

        # # self.iterator = iterator_copy

        # # return avg / self.step

        return sum(self.lst) / self.step
        

    def __iter__(self):
        return self

if __name__ == "__main__":
    lst = [0,8,2,7,0,5,6]
    for i in MovingAverage1((i for i in range(10))):
        print(i)

        

    