#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index=None, page_size=10):
        """
        Returns a dictionary with pagination details for querying by index.

        Args:
        - index (int): The starting index (default is None).
        - page_size (int): Number of items per page (default is 10).

        Returns:
        - dict: A dictionary containing pagination details.
        """
        # Validate the index if it's provided
        dataset = self.dataset()
        if index is not None:
            assert isinstance(index, int), "index must be an integer"
            assert 0 <= index < len(dataset), "index is out of range"

        # If no index is provided, default to the first item
        if index is None:
            index = 0

        # Get the current slice of the dataset
        data = dataset[index:index + page_size]

        # Calculate the next index
        if index + page_size < len(dataset):
            next_index = index + page_size
        else:
            None

        # Return the pagination details
        return {
            'index': index,  # The current start index of the page
            'next_index': next_index,  # The next index to query
            'page_size': len(data),  # Number of items on the page
            'data': data,  # The data for the current page
        }
