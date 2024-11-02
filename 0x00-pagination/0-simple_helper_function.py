#!/usr/bin/env python3

'''
Function that take two argu and return tuple containing start and an end index
params - (page, page_size)
return - tuple()
'''


def index_range(page, page_size):

    '''
    Function that take two argu and return tuple containing start, end index
    '''
    if page == 0:
        return (page - 1, page_size)
    else:
        return ((page - 1) * page_size, page_size * page)
