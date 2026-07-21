import sys

import argparse

import pathlib
import random

import numpy as np


class Float:

    Type = float

    def __init__(self, arg, bot=None, top=None, incl_bot=True, incl_top=True):
        self.arg = arg
        self.bot = bot
        self.top = top
        self.incl_bot = incl_bot
        self.incl_top = incl_top
        self.typed = None

    @classmethod
    def typePositive(cls, *args, incl_bot=False, **kwargs):
        return cls.typeNonnegative(*args, incl_bot=incl_bot, **kwargs)

    @classmethod
    def typeNonnegative(cls, *args, bot=0, **kwargs):
        return cls.type(*args, bot=bot, **kwargs)

    @classmethod
    def type(cls, *args, **kwargs):
        obj = cls(*args, **kwargs)
        obj.run()
        return obj.typed

    def run(self):
        try:
            self.typed = self.Type(self.arg)
        except ValueError:
            self.error(f'invalid {self.Type.__name__} value: {self.arg}')

        if self.bot is not None:
            if self.typed < self.bot:
                self.error(f'{self.typed} < {self.bot}')
            if not self.incl_bot and self.typed == self.bot:
                self.error(f'{self.typed} == {self.bot}')
        if self.top is not None:
            if self.typed > self.top:
                self.error(f'{self.typed} > {self.top}')
            if not self.incl_top and self.typed == self.top:
                self.error(f'{self.typed} == {self.top}')

    @staticmethod
    def error(msg):
        raise argparse.ArgumentTypeError(msg)


class Int(Float):

    Type = int

    @classmethod
    def typeSeed(cls, *args, top=2**32, incl_top=False, **kwargs):
        seed = cls.typeNonnegative(*args, top=top, incl_top=incl_top, **kwargs)
        np.random.seed(seed)
        random.seed(seed)
        return seed


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
                        type=Int.typeSeed,
                        help='The integer to set random state')

def set_seed(options):
    if options.seed is not None:
        return
    options.seed = np.random.randint(0, 2**32)
    np.random.seed(options.seed)

def add_size(parser, default=200):
    parser.add_argument('-size',
                        metavar='INT',
                        type=Int.typePositive,
                        default=default,
                        help='Sample size')