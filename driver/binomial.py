import numpy as np
import sys
from norm import parserutils
from norm import logutils
from norm import plotutils


def binomial(options, bins=10):
    vals = np.random.binomial(options.num, options.prob, options.size)
    with plotutils.ax(options=options, logger=logger) as ax:
        min_val, max_val = min(vals), max(vals)
        bins = min([bins, max_val - min_val + 1])
        ax.hist(vals, edgecolor="white", bins=bins, range=(min(vals)-0.5, max(vals)+0.5))


class Parser(parserutils.DistribParser):

    def setUp(self):
        self.add_argument('-num',
                            metavar='INT',
                            default=10,
                            type=parserutils.Int.typePositive,
                            help='Number of trials')
        self.add_argument('-prob',
                            metavar='FLOAT',
                            type=parserutils.Float.partial(bot=0, top=1),
                            default=0.5,
                            help='Probability of success')
        super().setUp()


if __name__ == '__main__':
    options = Parser(prog='binomial distribution').parse_args(sys.argv[1:])
    with logutils.Script(options) as logger:
        binomial(options)