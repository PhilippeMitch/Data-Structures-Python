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