from argparse import ArgumentParser


class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/project'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument('-x',
                                 '--example',
                                 default='example-value',
                                 dest='example',
                                 help='An example option')

    def parse(self, args=None):
        return self.parser.parse_args(args)
