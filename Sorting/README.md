## Sorting Algorithms

Sorting data is needed by many modern algorithms, it is used to rearrange a given array or list of elements according to a comparison operator on the elements. The right way to sort a data depend on the type an the size of the data.

Here are some of the algorithms used for sorting:
* Bubble Sort
* Merge Sort
* Insertion Sort
* Shell Sort
* Selection Sort

### Bubble Sort
Bubble sort is based on various iterations, called passes. For a list of size $N$, bubble sort will have $N-1$ passes. The goal of pass one is pushing the highest value to the top of the list.
Due to two levels of looping, the worst-case runtime complexity would be $O(n^2).$

### Merge Sort
The worst case is when each of the inner loops has to move all the elements in the list. If the inner loop is defined by i, the worst-case performance of the insertion sort algorithm is $O(n^2)$. In general, insertion can be used on small data structures. For larger data structures,
insertion sort is not recommended due to quadratic average performance.

### Insertion Sort
Merge Sort is based on a divide and conquer strategy and was developed in 1940 by John von Neumann.

As we can see the algorithm has the following three steps:
1. It divides the input list into two equal parts
2. It uses recursion to split until the length of each list is 1
3. Then, it merges the sorted parts into a sorted list and returns it

### Shell Sort
Shell sort is not for big data. It is used for medium-sized datasets. In a best-case scenario the performance of the shell Sort algorithm is $O(N)$.


### Selection Sort
Selection sort is an improvement on bubble sort, where we try to minimize the total number of swaps required with the algorithm. Selection sort's worst-case performance is $O(n^2)$. Note that its worst performance is similar to bubble sort and it should not be used for sorting larger datasets.

