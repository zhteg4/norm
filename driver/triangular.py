import numpy as np
import sys
from norm import parserutils
from norm import logutils
from norm import plotutils


def triangular(options=None):
    vals = np.random.triangular(options.left, options.mode, options.right, options.size)
    with plotutils.ax(options=options, logger=logger) as ax:
        ax.hist(vals, edgecolor="white", bins=100)


def get_parser():
    parser = parserutils.get_parser(prog='triangular distribution')
    parser.add_argument('-left',
                        metavar='FLOAT',
                        type=float,
                        default=-3,
                        help='Lower limit of the distribution')
    parser.add_argument('-mode',
                        metavar='FLOAT',
                        type=float,
                        default=0,
                        help='Peak of the distribution')
    parser.add_argument('-right',
                        metavar='FLOAT',
                        type=float,
                        default=5,
                        help='Upper limit of the distribution')
    parserutils.add_size(parser, default=200000)
    parserutils.add_seed(parser)
    return parser


if __name__ == '__main__':
    parser = get_parser()
    options = parser.parse_args(sys.argv[1:])
    parserutils.set_seed(options)
    logger = logutils.Logger.get(options.JOBNAME)
    logger.infoJob(options)
    triangular(options)
    logger.info('Finished', timestamp=True)

