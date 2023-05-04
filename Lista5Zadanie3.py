import random
from time import perf_counter
import matplotlib.pyplot as plt

def find_min_from_index(lst, start):
    i = start
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[i]:
            i = j
    return i

def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = find_min_from_index(lst, i)
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1

    return lst

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(lst):
    if len(lst) < 2:
        return lst

    n = len(lst) // 2
    left = lst[:n]
    right = lst[n:]
    return merge(merge_sort(left), merge_sort(right))

# Zadanie 3

def hybrid_sort(lst):
    if len(lst) < 16:
        return insertion_sort(lst)

    n = len(lst) // 2
    left = lst[:n]
    right = lst[n:]
    return merge(hybrid_sort(left), hybrid_sort(right))
    
# Zadanie 4

def partition_rand(lst, lo, hi):
    # pivot musi być ostatnim elementem fragmentu
    n = len(lst)
    pivot_index = random.randint(0, n-1)
    pivot = lst[pivot_index]
    lst[pivot_index], lst[hi] = lst[hi], lst[pivot_index]
    i = lo
    for j in range(lo, hi):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1

    lst[i], lst[hi] = lst[hi], lst[i]
    return i


def quick_sort_rand(lst):
    def quick_sort_segment(lo, hi):
        if lo >= hi:
            return
        i = partition_rand(lst, lo, hi)
        quick_sort_segment(lo, i - 1)
        quick_sort_segment(i + 1, hi)

    quick_sort_segment(0, len(lst) - 1)

def partition(lst, lo, hi):
    # pivot musi być ostatnim elementem fragmentu
    pivot = lst[hi]
    i = lo
    for j in range(lo, hi):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1

    lst[i], lst[hi] = lst[hi], lst[i]
    return i


def quick_sort(lst):
    def quick_sort_segment(lo, hi):
        if lo >= hi:
            return
        i = partition(lst, lo, hi)
        quick_sort_segment(lo, i - 1)
        quick_sort_segment(i + 1, hi)

    quick_sort_segment(0, len(lst) - 1)

def plot_sorting(sorting_algo):
    for i in range(1, 1000, 10):
        a = random.sample(range(10, 1000000), i)

        t1_start = perf_counter()
        sorting_algo(a)
        t1_stop = perf_counter()
        plt.scatter(i, t1_stop - t1_start, c = 'black', s=5)

        t2_start = perf_counter()
        sorting_algo(a)
        t2_stop = perf_counter()
        plt.scatter(i, t2_stop - t2_start, c = 'red', s = 5)

        a = list(reversed(a))
        t3_start = perf_counter()
        sorting_algo(a)
        t3_stop = perf_counter()
        plt.scatter(i, t3_stop - t3_start, c = 'blue', s = 5)



    
if __name__ == "__main__":
    algs = [hybrid_sort, quick_sort_rand, insertion_sort, selection_sort, quick_sort, sorted]
    for index, alg in enumerate(algs):
        plt.subplot(2, 3, index + 1)
        plot_sorting(alg)
        plt.title(alg.__name__)
        plt.legend(["shuffled", "sorted", "reversed"])
        
    plt.show()


    