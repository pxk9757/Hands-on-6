import time
import random
import matplotlib.pyplot as plt

# Non-random pivot quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Random pivot quicksort
def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_random(left) + middle + quicksort_random(right)

def benchmark(sort_function, array):
    start = time.time()
    sort_function(array)
    end = time.time()
    return end - start

# Generate your input data
sizes = list(range(100, 1001, 100))  # Sizes of the arrays to sort
best_case_times = []
worst_case_times = []
average_case_times = []

for size in sizes:
    best_case = list(range(size))  # Already sorted data
    worst_case = list(range(size, 0, -1))  # Reverse sorted data
    average_case = [random.randint(0, size) for _ in range(size)]  # Random data

    best_case_times.append(benchmark(quicksort, best_case))
    worst_case_times.append(benchmark(quicksort, worst_case))
    average_case_times.append(benchmark(quicksort, average_case))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, best_case_times, label='Best Case')
plt.plot(sizes, worst_case_times, label='Worst Case')
plt.plot(sizes, average_case_times, label='Average Case')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Benchmark')
plt.legend()
plt.show()
