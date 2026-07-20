import argparse
import numpy as np

def type_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        raise argparse.ArgumentTypeError(f'invalid float value: {val}')

def type_int(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        raise argparse.ArgumentTypeError(f'invalid float value: {val}')

def type_positive_float(val):
    val = type_float(val)
    if val > 0:
        return val
    raise argparse.ArgumentTypeError(f'invalid positive number: {val}')

def type_positive_int(val):
    val = type_int(val)
    if val > 0:
        return val
    raise argparse.ArgumentTypeError(f'invalid a positive integer: {val}')

def type_seed(val):
    val = type_int(val)
    if 0 <= val < 2**32:
        np.random.seed(val)
        return val
    raise argparse.ArgumentTypeError(f'not in [0, 2**32): {val}')


