def binary_search(lst, obj):
    runs = 1
    low = 0
    high = len(lst) - 1
    while low <= high:
        index = ((high + low) // 2)
        if lst[index] < obj:
            low = index + 1
        elif lst[index] > obj:
            high = index - 1
        else:
            return index, runs
        runs = runs + 1
        
        
    return None, runs
        
if __name__ == "__main__":
    print(binary_search([1, 2, 5, 6, 9, 10, 19, 20], 90))