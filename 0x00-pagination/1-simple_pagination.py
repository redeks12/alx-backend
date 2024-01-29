#!/usr/bin/env python3
"""0x00. Pagination"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """Write a function named index_range that
    takes two integer arguments page and page_size."""
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return tuple([start, end])


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) == int == type(page_size)
        assert page > 0 and page_size > 0
        val = index_range(page, page_size)
        return self.dataset()[val[0] : val[1]]
