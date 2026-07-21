import sys

import argparse

import pathlib
import random
import functools

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
    def partial(cls, *args, **kwargs):
        return functools.partial(cls.type, *args, **kwargs)

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


class ArgumentParser(argparse.ArgumentParser):

    FLAG_INTERAC = '-INTERAC'
    FLAG_JOBNAME = '-JOBNAME'
    JFLAGS = [FLAG_INTERAC, FLAG_JOBNAME]

    def __init__(self,
                 formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                 valids=None,
                 **kwargs):
        super().__init__(formatter_class=formatter_class, **kwargs)
        self.valids = set() if valids is None else valids
        self.setUp()

    def setUp(self):
        if self.FLAG_JOBNAME in self.JFLAGS:
            self.add_argument(self.FLAG_JOBNAME,
                              default=pathlib.Path(sys.argv[0]).stem,
                              help='The jobname to name output files')
        if self.FLAG_INTERAC in self.JFLAGS:
            self.add_argument('-INTERAC',
                                action='store_true',
                                help='Enable interactive mode')


    def parse_args(self, args=None, **kwargs):
        options = super().parse_args(args=args, **kwargs)
        for Valid in self.valids:
            val = Valid(options)
            try:
                val.run()
            except (ValueError, FileNotFoundError) as err:
                self.error(err)
        return options


class Valid:

    def __init__(self, options):
        self.options = options

    def run(self):
        pass


class SeedValid(Valid):

    def run(self):
        if self.options.seed is not None:
            return
        self.options.seed = np.random.randint(0, 2 ** 32)
        np.random.seed(self.options.seed)


class RandomParser(ArgumentParser):

    FLAG_SEED = '-seed'

    def setUp(self):
        self.add_argument('-seed',
                            metavar='INT',
                            type=Int.typeSeed,
                            help='The integer to set random state')
        self.valids.add(SeedValid)
        super().setUp()


class DistribParser(RandomParser):

    FLAG_SIZE = '-size'
    DEFAULT_SIZE = 200

    def setUp(self):
        self.add_argument('-size',
                            metavar=self.FLAG_SIZE,
                            type=Int.typePositive,
                            default=self.DEFAULT_SIZE,
                            help='Sample size')
        super().setUp()