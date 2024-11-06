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

    def get_hyper(self, page=1, page_size=10):
        """
        Returns a dictionary with pagination details.

        Args:
        - page (int): The current page number (default is 1).
        - page_size (int): Number of items per page (default is 10).

        Returns:
        - dict: A dictionary containing pagination details.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset)
        total_pages = math.ceil(total_items / page_size)

        # Calculate next and previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Construct the dictionary to return
        return {
            'page_size': len(data),  # The length of the dataset on this page
            'page': page,            # The current page number
            'data': data,            # The dataset for this page
            'next_page': next_page,  # The next page number or None
            'prev_page': prev_page,  # The previous page number or None
            'total_pages': total_pages  # The total number of pages
        }
