#Subject: CSP2348
#Assignment: Assignment 2 – Algorithm Implementation and Analysis
#Student Name: Kaveesha Hansani
#Date:11/04/2025

import time
import random
import sys
import math


# Q1: Array-Based Sorting Algorithms
# Each function sorts a copy of the input array, counts comparisons,
# and measures the run time (in milliseconds). The functions return a tuple:
# (sorted array, number of comparisons, elapsed time in ms).

# 1. Selection Sort
def selection_sort(arr):
    """Sorts an array using Selection Sort.
       Returns: (sorted_array, comparisons, runtime_ms)"""
    a = arr.copy()
    n = len(a)
    comparisons = 0
    start_time = time.time()
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    return a, comparisons, elapsed

# 2. Insertion Sort
def insertion_sort(arr):
    """Sorts an array using Insertion Sort.
       Returns: (sorted_array, comparisons, runtime_ms)"""
    a = arr.copy()
    n = len(a)
    comparisons = 0
    start_time = time.time()
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    return a, comparisons, elapsed

# 3. Merge Sort
def merge_sort(arr):
    """Sorts an array using Merge Sort.
       Returns: (sorted_array, comparisons, runtime_ms)"""
    comparisons = [0]  # Mutable counter for nested functions

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort_recursive(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = merge_sort_recursive(a[:mid])
        right = merge_sort_recursive(a[mid:])
        return merge(left, right)

    a_copy = arr.copy()
    start_time = time.time()
    sorted_arr = merge_sort_recursive(a_copy)
    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    return sorted_arr, comparisons[0], elapsed

# 4. Quick Sort
def quick_sort(arr):
    """Sorts an array using Quick Sort.
       Returns: (sorted_array, comparisons, runtime_ms)"""
    comparisons = [0]

    def quick_sort_recursive(a, low, high):
        if low < high:
            p = partition(a, low, high)
            quick_sort_recursive(a, low, p - 1)
            quick_sort_recursive(a, p + 1, high)

    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    a_copy = arr.copy()
    start_time = time.time()
    quick_sort_recursive(a_copy, 0, len(a_copy) - 1)
    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    return a_copy, comparisons[0], elapsed

# 5. Heap Sort
def heap_sort(arr):
    """Sorts an array using Heap Sort.
       Returns: (sorted_array, comparisons, runtime_ms)"""
    a = arr.copy()
    n = len(a)
    comparisons = [0]

    def heapify(a, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n:
            comparisons[0] += 1
            if a[left] > a[largest]:
                largest = left
        if right < n:
            comparisons[0] += 1
            if a[right] > a[largest]:
                largest = right
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, n, largest)

    start_time = time.time()
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    return a, comparisons[0], elapsed

# 6. Bubble Sort (Basic)
def bubble_sort(arr):
    """Basic Bubble Sort.
       Returns: (sorted_array, comparisons, runtime_ms)"""
    a = arr.copy()
    n = len(a)
    comparisons = 0
    start_time = time.time()
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    return a, comparisons, elapsed

# 7. Obs1-Bubble Sort (Reduced Scanning)
def obs1_bubble_sort(arr):
    """Obs1-Bubble Sort using reduced scanning.
       Returns: (sorted_array, comparisons, runtime_ms)"""
    return bubble_sort(arr)

# 8. Obs2-Bubble Sort (Early Termination)
def obs2_bubble_sort(arr):
    """Obs2-Bubble Sort with early termination.
       Returns: (sorted_array, comparisons, runtime_ms)"""
    a = arr.copy()
    n = len(a)
    comparisons = 0
    start_time = time.time()
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    return a, comparisons, elapsed

# 9. Obs3-Bubble Sort (Combined Improvements)
def obs3_bubble_sort(arr):
    """Obs3-Bubble Sort: Combines reduced scanning with early termination.
       Returns: (sorted_array, comparisons, runtime_ms)"""
    return obs2_bubble_sort(arr)

# 10. Sink-down Sort Algorithm
def sink_down_sort(arr):
    """Sink-down Sort: Sinks the smallest element from right-to-left.
       Returns: (sorted_array, comparisons, runtime_ms)"""
    a = arr.copy()
    n = len(a)
    comparisons = 0
    start_time = time.time()
    for i in range(n - 1):
        swapped = False
        # Traverse from the end down to index i + 1.
        for j in range(n - 1, i, -1):
            comparisons += 1
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    return a, comparisons, elapsed

# 11. Bi-Directional Bubble (BDB) Sort Algorithm
def bdb_sort(arr):
    """Bi-Directional Bubble Sort: Alternates left-to-right and right-to-left scans.
       Returns: (sorted_array, comparisons, runtime_ms)"""
    a = arr.copy()
    n = len(a)
    comparisons = 0
    left = 0
    right = n - 1
    start_time = time.time()
    while left < right:
        swapped = False
        for i in range(left, right):
            comparisons += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        right -= 1
        for i in range(right, left, -1):
            comparisons += 1
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                swapped = True
        left += 1
        if not swapped:
            break
    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    return a, comparisons, elapsed

# Q3: Experimental System
# This system allows the user to test sorting algorithms in two modes:
# a) Manual testing (individual and multiple algorithms)
# b) Automatic testing (running experiments over multiple array sizes & runs)

# Mapping for sorting algorithms for the menu.
sorting_algorithms = {
    "1": ("Selection Sort", selection_sort),
    "2": ("Insertion Sort", insertion_sort),
    "3": ("Merge Sort", merge_sort),
    "4": ("Quick Sort", quick_sort),
    "5": ("Heap Sort", heap_sort),
    "6": ("Bubble Sort", bubble_sort),
    "7": ("Obs1-Bubble Sort", obs1_bubble_sort),
    "8": ("Obs2-Bubble Sort", obs2_bubble_sort),
    "9": ("Obs3-Bubble Sort", obs3_bubble_sort),
    "A": ("Sink-down Sort", sink_down_sort),
    "B": ("Bi-Directional Bubble Sort", bdb_sort)
}

# Menu printing functions.
def print_main_menu():
    print("\nMain Menu:")
    print("1. Manual Testing")
    print("2. Automatic Testing")
    print("3. Exit")

def print_manual_menu():
    print("\nManual Testing Menu:")
    print("1. Test an individual sorting algorithm")
    print("2. Test multiple sorting algorithms on the same array")
    print("3. Back to Main Menu")

def print_sub_menu():
    print("\nSub-Menu: Choose a sorting algorithm to test:")
    print("1. Selection Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")
    print("5. Heap Sort")
    print("6. Bubble Sort")
    print("7. Obs1-Bubble Sort")
    print("8. Obs2-Bubble Sort")
    print("9. Obs3-Bubble Sort")
    print("A. Sink-down Sort")
    print("B. Bi-Directional Bubble Sort")

# Manual testing functions.
def manual_individual_test():
    print_sub_menu()
    choice = input("Enter your choice: ").strip().upper()
    if choice not in sorting_algorithms:
        print("Invalid choice. Returning to Manual Menu.")
        return
    alg_name, alg_func = sorting_algorithms[choice]
    try:
        n = int(input("Enter the size of the array (n > 0): "))
        if n <= 0:
            print("Array size must be positive.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    array_data = [random.randint(0, 1000) for _ in range(n)]
    print(f"\nTesting {alg_name} with array size = {n}")
    sorted_array, comparisons, runtime_ms = alg_func(array_data)
    print(f"Number of comparisons: {comparisons}")
    print(f"Run time: {runtime_ms:.2f} ms")
    # Uncomment below to print the sorted array.
    # print("Sorted Array:", sorted_array)

def manual_multiple_test():
    try:
        n = int(input("Enter the size of the array (n > 0): "))
        if n <= 0:
            print("Array size must be positive.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    array_data = [random.randint(0, 1000) for _ in range(n)]
    print("\n" + "=" * 70)
    print(f"{'Sorting algorithm name':25} | {'Array size':10} | {'Num. of Comparisons':20} | {'Run time (ms.)':15}")
    print("=" * 70)
    for key in sorted(sorting_algorithms.keys(), key=lambda x: x.upper()):
        alg_name, alg_func = sorting_algorithms[key]
        test_arr = array_data.copy()
        sorted_arr, comparisons, runtime_ms = alg_func(test_arr)
        print(f"{alg_name:25} | {n:10d} | {comparisons:20d} | {runtime_ms:15.2f}")
    print("=" * 70)

def manual_testing_menu():
    while True:
        print_manual_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            manual_individual_test()
        elif choice == "2":
            manual_multiple_test()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Automatic testing function.
def automatic_testing():
    try:
        start_n = int(input("Enter the starting array size (n > 0): "))
        end_n = int(input("Enter the ending array size (n > start_n): "))
        step = int(input("Enter the step size: "))
        runs = int(input("Enter the number of runs per array size: "))
        if start_n <= 0 or end_n <= start_n or step <= 0 or runs <= 0:
            print("Invalid parameters. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter integers.")
        return

    print("\nAutomatic Testing Results (Averaged over runs):")
    # Table header
    header = f"{'Algorithm':25} | {'Array Size':10} | {'Avg Comparisons':18} | {'Avg Runtime (ms.)':18}"
    print("=" * len(header))
    print(header)
    print("=" * len(header))

    # For each algorithm, for each array size, compute average comparisons and runtime.
    # We will run each algorithm 'runs' times per array size.
    for key in sorted(sorting_algorithms.keys(), key=lambda x: x.upper()):
        alg_name, alg_func = sorting_algorithms[key]
        for n in range(start_n, end_n + 1, step):
            total_comp = 0
            total_time = 0
            for r in range(runs):
                data = [random.randint(0, 1000) for _ in range(n)]
                _, comp, t = alg_func(data)
                total_comp += comp
                total_time += t
            avg_comp = total_comp // runs
            avg_time = total_time / runs
            print(f"{alg_name:25} | {n:10d} | {avg_comp:18d} | {avg_time:18.2f}")
        print("-" * len(header))
    print("=" * len(header))

# Main menu.
def main_menu():
    while True:
        print_main_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            manual_testing_menu()
        elif choice == "2":
            automatic_testing()
        elif choice == "3":
            print("Exiting the experimental system. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

# Entry Point
if __name__ == "__main__":
    main_menu()
