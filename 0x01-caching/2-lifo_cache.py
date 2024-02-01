#!/usr/bin/env python3
"""0x01. Caching"""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """FIFOCache implementation"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                val, _ = self.cache_data.popitem()
                print("DISCARD: {}".format(val))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """retrieves a key from the cache dictionary"""
        if key is None:
            return None

        return self.cache_data.get(key)
