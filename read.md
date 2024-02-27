## Implement both versions of quicksort (random and non-random choice for the pivot) and share the GitHub repository with your source code.

2.  For the non-random pivot version of quicksort show the following benchmarks on the same graph:

    2a) best case (generate a set of inputs that will always be the best case, repeat for multiple array input sizes "n").

    2b) worst case (generate a set of inputs that will always be the worst case, repeat for multiple array input sizes "n").

    2c) average case (generate a set of inputs from a uniform distribution, repeat for multiple array input sizes "n").

## Ans) Uploaded the code into quicksort.py file

### 3. Mathematically derive the average runtime complexity of the non-random pivot version of quicksort.

     Here is the mathematical derivation for the average time complexity of non-randomized Quicksort:

Let T(n) = average case time complexity to sort an array of length n using non-randomized Quicksort

Steps in Quicksort:

1. Select a pivot element (constant time)
2. Partition the array into two sub-arrays based on pivot (linear time O(n))
3. Recursively sort the two sub-arrays

Let m and n-m-1 be the sizes of the two sub-arrays after partitioning, where m is a random variable between 0 to n-1.

The recurrence relation for average time complexity is:

T(n) = T(m) + T(n-m-1) + O(n)

Taking expectation over m:
E[T(n)] = E[T(m)] + E[T(n-m-1)] + O(n)

Since m is randomly uniformly distributed:
E[m] = (n-1)/2

Therefore,

E[T(n)] = 2 E[T(n/2)] + O(n)

Solving the recurrence using Master method (with a = 2, b = 2, c = 1):
E[T(n)] = Θ(n log n)

Therefore, the average case time complexity of non-randomized Quicksort is Θ(n log n).

### Author--Priyanka Kondamadugu