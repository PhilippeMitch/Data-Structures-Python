"""
Date: 2023-07-03
"""
class Sorting:
    """
    This class is to experiment the different
    sorting algorithms
    """
    def bubble_sort(self, list_):
        """
        This function receive an unorderded list
        and return an ordered list
        """
        tail_idx = len(list_) - 1
        for pass_ in range(tail_idx, 0, -1):
            for idx in range(pass_):
                if list_[idx] > list_[idx + 1]:
                    list_[idx], list_[idx + 1] = list_[idx + 1], list_[idx]
        return list

    def bubble_sort_recursive(self, list_, flag=False):
        """
        This function receive an unorderded list
        and return an ordered list
        """
        tail_idx = len(list_) - 1
        while flag:
            flag = True
            for idx in range(tail_idx):
                if list[idx] > list[idx + 1]:
                    flag = False
                    list_[idx], list_[idx + 1] = list_[idx + 1], list_[idx]
            self.bubble_sort_recursive(list_, flag)
        return list_

    def insertion_sort(self, list_):
        """
        This function receive an unorderded list
        and return an ordered list
        """
        for i in range(1, len(list_)):
            j = i -1
            next_item = list_[i]
            while(list_[j+1] > next_item) and (j >= 0):
                list_[j + 1] = list_[j]
                list_[j] = next_item
                j -= 1
        return list_

