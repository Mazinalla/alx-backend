#!/usr/bin/env python3

'''
Function that take two int argu and return tuple containing start and an end index
params - (page, page_size)
return - tuple()
'''


def index_range(page, page_size):
    if page == 0:
        return (page - 1, page_size)
    else:
        return ((page - 1) * page_size, page_size * page)
