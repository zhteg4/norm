import argparse
import numpy as np
import pathlib
import sys

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


def get_parser(*args, formatter_class=argparse.ArgumentDefaultsHelpFormatter, **kwargs):
    parser = argparse.ArgumentParser(*args,
                                     formatter_class=formatter_class, **kwargs)
    parser.add_argument('-INTERAC',
                        action='store_true',
                        help='Enable interactive mode')
    parser.add_argument('-JOBNAME',
                        default=pathlib.Path(sys.argv[0]).stem,
                        help='The jobname to name output files')
    return parser


def add_seed(parser):
    parser.add_argument('-seed',
                        metavar='INT',
                        type=type_seed,
                        help='The integer to set random state')

def set_seed(options):
    if options.seed is not None:
        return
    options.seed = np.random.randint(0, 2**32)
    np.random.seed(options.seed)

def add_size(parser, default=200):
    parser.add_argument('-size',
                        metavar='INT',
                        type=type_positive_int,
                        default=default,
                        help='Sample size')