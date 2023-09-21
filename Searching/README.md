## Searching Algorithms

Searching Algorithms are used to determine whether a specific piece of data exists within a data structure. Efficiently searching data in complex data structures is one of the most important functionalities.

Here are some of the algorithms used for searching:

* Linear search
* Binary search
* Interpolation search

### Linear Search
Linear search is a sequential searching algorithm where we start from one end and check every element of the list until the desired element is found. It is one of the simplest strategies for searching data is to simply loop through each element looking for the target.
As discussed, linear search is a simple algorithm that performs an exhaustive search. Its worst-case behavior is $O(N)$.

### Binary Search
Binary Search is a searching algorithm for finding an element's position in a sorted array. The algorithm iteratively
divides a list into two parts and keeps a track of the lowest and highest indices until it findsthe value it is looking for.

Binary search is so named because at each iteration, the algorithm bifurcates the data into two parts. If the data has N items, it will take a maximum of $O(logN)$ steps to iterate.
