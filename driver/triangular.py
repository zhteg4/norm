import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys
import pathlib

def triangular (options=None):
    vals = np.random.triangular (options.left, options.mode, options.right, options.size)

    fig, ax = plt.subplots()
    ax.hist(vals, edgecolor="white", bins=100)

    if options.INTERACTIVE:
        plt.show()
    filename = f'{options.JOBNAME}.svg'
    fig.savefig(filename)
    print(f'Figure saved as {filename}')

def type_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        raise argparse.ArgumentTypeError(f'invalid float value: {val}')

def type_int(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        raise argparse.ArgumentTypeError(f'invalid int value: {val}')


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


def get_parser(file):
    parser = argparse.ArgumentParser(prog='normal distribution',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-size',
                        metavar='INT',
                        type=type_positive_int,
                        default=200000,
                        help='Width of the distribution')
    parser.add_argument('-INTERAC',
                        action='store_true',
                        help='Enable interactive mode')
    parser.add_argument('-seed',
                        metavar='INT',
                        type=type_seed,
                        help='The integer to set random state')
    parser.add_argument('-JOBNAME',
                        default=pathlib.Path(file).stem,
                        help='The jobname to name output files')
    parser.add_argument('-left',
                        metavar='FLOAT',
                        type=float,
                        default=-3,
                        help='Lower of the distribution')
    parser.add_argument('-mode',
                        metavar='FLOAT',
                        type=type_positive_int,
                        default=0,
                        help='Peak of the distribution')
    parser.add_argument('-right',
                        metavar='FLOAT',
                        type=type_positive_int,
                        default=5,
                        help='Upper of the distribution')
    return parser


parser = get_parser(sys.argv[0])
options = parser.parse_args(sys.argv[1:])
if options.seed is None:
    options.seed = np.random.randint(0, 2**32)
    print(f'Random seed: {options.seed}')
    np.random.seed(options.seed)
triangular(options)

