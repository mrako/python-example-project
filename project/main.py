import sys

from lib import options

if __name__ == '__main__':
  options, args = options.parse(sys.argv[1:])
  print options.target
  
