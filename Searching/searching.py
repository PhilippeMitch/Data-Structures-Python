"""
Date: 2023-09-20
"""

class Search:
    """
    This class is to experiment the different
    searching algorithms
    """
    def linear_search(self, list_, elem):
        """This method receive a list and an item to search, 
            when the item is found, the results is returned 
            and the algorithm exits the loop
        """
        for item in list_:
            if item == elem:
                return f"{elem} is found at position {list_.index(elem)}"
        return f"{elem} is not found in the list"

    def binary_search(self, list_, elem):
        """This method receive a list and an item to search, 
            when the item is found, the results is returned 
            and the algorithm exits the loop
        """
        first = 0
        last = len(list_)-1
        found = False
        while first<=last and not found:
            midpoint = (first + last)//2
            if list_[midpoint] == elem:
                found = True
            else:
                if elem < list_[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        return f"{elem} is found at position {list_.index(elem)}"

