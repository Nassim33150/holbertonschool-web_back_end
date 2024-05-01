#!/usr/bin/env python3


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """ function should return a tuple
    of size two containing a start
    index and an end index """
    debut_index, end_index = 0, 0

    if page > 0 and page_size > 0:
        debut_index = (page - 1) * page_size
        end_index = page * page_size
    return debut_index, end_index
