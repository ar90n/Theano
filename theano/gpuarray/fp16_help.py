from __future__ import absolute_import, print_function, division


def work_dtype(dtype):
    if dtype == 'float16':
        return 'float32'
    else:
        return dtype


def load_w(dtype):
    if dtype == 'float16':
        return 'load_half'
    else:
        return '*'


def write_w(dtype):
    if dtype == 'float16':
        return 'store_half'
    else:
        return 'store'
