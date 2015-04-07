from argparse import ArgumentParser


class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        # overrides usage that is by default something like:
        # usage: PROG [-h] [--foo [FOO]] bar [bar ...]
        usage = 'bin/project'
        self.parser = ArgumentParser(usage=usage)
        # inits the argparser with an argument 'example' with
        # a default value 'example-value'
        self.parser.add_argument('-x',
                                 '--example',
                                 default='example-value', # specifies default value
                                 dest='example', # determines the name of the attribute that parse_args yields
                                 help='An example option') # specifies help message 

    def parse(self, args=None):
        # parses args, returns a Namespace object
        # containing the example arg + parameter args
        # May not support kwargs like -x
        return self.parser.parse_args(args)
