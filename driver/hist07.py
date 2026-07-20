import matplotlib.pyplot as plt
import numpy as np
import sys
import pathlib
from norm import parserutils
from norm import logutils
import argparse

def norm(options=None):
    vals = np.random.normal(options.loc, options.scale, options.size)

    fig, ax = plt.subplots()
    ax.hist(vals, edgecolor="white")

    if options.INTERACTIVE:
        plt.show()
    filename = f'{options.JOBNAME}.svg'
    fig.savefig(filename)
    logger.info(f'Figure saved as {filename}')


def get_parser(file):
    parser = argparse.ArgumentParser(prog='normal distribution',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-loc',
                        default=40.,
                        type=float,
                        help='Mean of the distribution')
    parser.add_argument('-scale',
                        metavar='FLOAT',
                        type=parserutils.type_positive_float,
                        default=1.5,
                        help='Width of the distribution')
    parser.add_argument('-size',
                        metavar='INT',
                        type=parserutils.type_positive_int,
                        default=200,
                        help='Width of the distribution')
    parser.add_argument('-INTERAC',
                        action='store_true',
                        help='Enable interactive mode')
    parser.add_argument('-seed',
                        metavar='INT',
                        type=parserutils.type_seed,
                        help='The integer to set random state')
    parser.add_argument('-JOBNAME',
                        default=pathlib.Path(file).stem,
                        help='The jobname to name output files')
    return parser


if __name__ == '__main__':
    parser = get_parser(sys.argv[0])
    options = parser.parse_args(sys.argv[1:])
    if options.seed is None:
        options.seed = np.random.randint(0, 2**32)
        np.random.seed(options.seed)
    logger = logutils.Logger.get(options.JOBNAME)
    logger.infoJob(options)
    norm(options)
    logger.info('Finished', timestamp=True)
