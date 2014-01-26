import sys

from lib import Project
from lib import Options

if __name__ == '__main__':
    options = Options()
    opts = options.parse(sys.argv[1:])

    v = Project(opts)

    v.date()
    v.print_example_arg()
