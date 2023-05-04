from stack import Stack
from time import perf_counter
from random import choices
import matplotlib.pyplot as plt

def generate_path(n):
    directions = ['S', 'N', 'E', 'W']
    return choices(directions, k=n)

def check_directions(x, y):
    if x == 'N' and y == 'S':
        return True
    elif x == 'S' and y == 'N':
        return True
    elif x == 'W' and y == 'E':
        return True
    elif x == 'E' and y == 'W':
        return True 
    else:
        return False 
    

def optimize_path(path):
    s = Stack()
    for i in range(len(path)):

        if s.is_empty():
            s.push(path[i])
            continue
            

        if check_directions(path[i], s.peek()):
            s.pop()
        else:
            s.push(path[i])
        
        

    return s.items

if __name__ == "__main__":
    # print(optimize_path(['N', 'N', 'S']))
    # print(optimize_path(['S', 'S', 'N', 'E', 'W', 'S', 'E']))
    # print(optimize_path(['S', 'N', 'E', 'W', 'W']))

    for i in range(0, 100001, 1000):
    
        path = generate_path(i)

        t1_start = perf_counter()
    
        optimize_path(path)

        t1_stop = perf_counter()


        plt.scatter(i, t1_stop - t1_start, c = 'black', s = 10)

plt.show()
        