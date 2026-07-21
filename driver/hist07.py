import numpy as np
import sys
from norm import parserutils
from norm import logutils
from norm import plotutils


def norm(options):
    vals = np.random.normal(options.loc, options.scale, options.size)
    with plotutils.ax(options=options, logger=logger) as ax:
        ax.hist(vals, edgecolor="white")


class Parser(parserutils.DistribParser):

    def setUp(self):
        self.add_argument('-loc',
                            metavar='FLOAT',
                            type=float,
                            default=40.,
                            help='Mean of the distribution')
        self.add_argument('-scale',
                            metavar='FLOAT',
                            type=parserutils.Float.typePositive,
                            default=1.5,
                            help='Width of the distribution')
        super().setUp()


if __name__ == '__main__':
    options = Parser(prog='normal distribution').parse_args(sys.argv[1:])
    with logutils.Script(options) as logger:
        norm(options)
