import numpy as np
import sys
from norm import parserutils
from norm import logutils
from norm import plotutils
import argparse


def triangular(options):
    vals = np.random.triangular(options.left, options.mode, options.right, options.size)
    with plotutils.ax(options=options, logger=logger) as ax:
        ax.hist(vals, edgecolor="white", bins=100)


class Valid(parserutils.Valid):

    def run(self):
        if self.options.left < self.options.mode < self.options.right:
            return
        raise argparse.ArgumentTypeError(f"Invalid left ({self.options.left}) < mode ({self.options.mode}) < right ({self.options.right})")


class Parser(parserutils.DistribParser):
    DEFAULT_SIZE = 200000
    def setUp(self):
        self.add_argument('-left',
                            metavar='FLOAT',
                            type=float,
                            default=-3,
                            help='Lower limit of the distribution')
        self.add_argument('-mode',
                            metavar='FLOAT',
                            type=float,
                            default=0,
                            help='Peak of the distribution')
        self.add_argument('-right',
                            metavar='FLOAT',
                            type=float,
                            default=5,
                            help='Upper limit of the distribution')
        self.valids.add(Valid)
        super().setUp()


if __name__ == '__main__':
    options = Parser(prog='triangular distribution').parse_args(sys.argv[1:])
    with logutils.Script(options) as logger:
        triangular(options)

