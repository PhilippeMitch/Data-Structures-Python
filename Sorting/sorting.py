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
        This method receive an unorderded list
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
        This method receive an unorderded list
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
        This method receive an unorderded list
        and return an ordered list
        """
        for i in range(1, len(list_)):
          j = i - 1
          next_item = list_[i]
          while (list_[j] > next_item) and (j >= 0):
            list_[j + 1] = list_[j]
            list_[j] = next_item
            j = j - 1
            
        return list_

    def merge_sort(self, list_):
        """
        This method receive an unorderded list
        and return an ordered list
        """

        mid = len(list_) // 2
        left_list = list_[:mid]
        right_list = list_[mid:]
        
        if len(list_) > 1:
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

    def shell_sort(self, list_):
        """
        This method receive an unorderded list
        and return an ordered list
        """
        sublist_length = len(list_) // 2
        while sublist_length > 0:
            for i in range(sublist_length, len(list_)):
                temp = list_[i]
                j = i
                # Sort this sublist
                while j >= sublist_length and list_[j - sublist_length] > temp:
                    list_[j] = list_[j - sublist_length]
                    j -= sublist_length
                list_[j] = temp
            # Reduce the sublist length for the next element
            sublist_length //= 2
        return list_

    def selection_sort(self, list_):
        """
        This method receive an unorderded list
        and return an ordered list
        """
        for pass_ in range(len(list_)-1, 0, -1):
            max_idx = 0
            for idx in range(1, len(pass_)+1):
                if list_[idx] > list_[max_idx]:
                    max_idx = idx
            list_[pass_], list_[max_idx] = list_[max_idx], list_[pass_]
        return list_