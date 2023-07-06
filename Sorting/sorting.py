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
        return list_

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

    def merge_sort(self, list_):
        """
        This function receive an unorderded list
        and return an ordered list
        """

        mid = len(list_) // 2
        left_list = list_[:mid]
        right_list = list_[mid:]

        self.merge_sort(left_list)
        self.merge_sort(right_list)

        left_list_idx = 0
        right_list_idx = 0
        list_idx = 0

        while left_list_idx < len(left_list) and right_list_idx < len(right_list):
            if left_list[left_list_idx] < right_list[right_list_idx]:
                list_[list_idx] = left_list[left_list_idx]
                left_list_idx += 1
                list_idx += 1
            else:
                list_[list_idx] = right_list[right_list_idx]
                right_list_idx += 1
                list_idx += 1

        while left_list_idx < len(left_list):
            list_[list_idx] = left_list[left_list_idx]
            left_list_idx += 1
            list_idx += 1

        while right_list_idx < len(right_list):
            list_[list_idx] = right_list[right_list_idx]
            right_list_idx += 1
            list_idx += 1

        return list_

        