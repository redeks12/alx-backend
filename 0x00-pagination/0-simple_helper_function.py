#!/usr/bin/env python3
"""0x00. Pagination"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """Write a function named index_range that
    takes two integer arguments page and page_size."""
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return tuple([start, end])
