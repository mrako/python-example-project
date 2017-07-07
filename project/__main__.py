import sys

from lib import Project
from lib import Options

def run_project(args):
    options = Options()
    options.parse(args[1:])

    project = Project(options)

    print 'Printing date:', project.date()
    print 'Printing example arg:', project.print_example_arg()

if __name__ == '__main__':
    run_project(sys.argv)
