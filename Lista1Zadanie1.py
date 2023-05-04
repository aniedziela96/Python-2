def f(lst1, lst2):
    for number1 in lst1:
        for number2 in lst2:
            if number1 > number2: # sprawdzamy czy element z pierwszej listy jest większy
                return True # gdy tylko znajdziemy pasujący element możemy opuścić algorytm 
            else:
                continue

# optymistyczny przypadek: pierwszy element z lst1 jest większy od pierwszego elementu lst2
# pesymistyczny: nie ma elementu na lst1 który byłby większy od jakiegokolwiek na lst2

from random import choices

print(choices([1, 2, 3, 4], k = 10))