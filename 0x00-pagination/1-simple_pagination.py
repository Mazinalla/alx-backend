#!/usr/bin/env python3


'''
simple pagination
'''

import csv
import math
from typing import List


def index_range(page, page_size):

    '''
    Function that take two argu and return tuple containing start, end index
    '''
    if page == 0:
        return (page - 1, page_size)
    else:
        return ((page - 1) * page_size, page_size * page)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        function that retrive data acoriding to the pagination
        '''
        assert (isinstance(page, int))
        assert (page > 0)
        assert (isinstance(page_size, int))
        assert (page_size > 0)

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # Check if the start index is out of range
        if start_index >= len(dataset):
            return []  # Return an empty list if the page is out of range

        return dataset[start_index:end_index]  # Return the sliced dataset
