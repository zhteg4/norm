import numpy as np
import sys
from norm import parserutils
from norm import logutils
from norm import plotutils


def norm(options=None):
    vals = np.random.normal(options.loc, options.scale, options.size)
    with plotutils.ax(options=options, logger=logger) as ax:
        ax.hist(vals, edgecolor="white")


def get_parser():
    parser = parserutils.get_parser(prog='normal distribution')
    parser.add_argument('-loc',
                        default=40.,
                        type=float,
                        help='Mean of the distribution')
    parser.add_argument('-scale',
                        metavar='FLOAT',
                        type=parserutils.Float.typePositive,
                        default=1.5,
                        help='Width of the distribution')
    parserutils.add_size(parser)
    parserutils.add_seed(parser)
    return parser


if __name__ == '__main__':
    parser = get_parser()
    options = parser.parse_args(sys.argv[1:])
    parserutils.set_seed(options)
    logger = logutils.Logger.get(options.JOBNAME)
    logger.infoJob(options)
    norm(options)
    logger.info('Finished', timestamp=True)
