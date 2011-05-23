
from optparse import OptionParser

def parse(args = None):
    usage = 'Usage %prog'
    parser = OptionParser(usage=usage)
    parser.add_option('-t', '--target', default='ubuntu', dest='target', help='The target name for the virtual server')
    parser.add_option('-d', '--distribution', default='hardy', dest='distribution', help='The distribution that is cloned for testing')
    
    options, args = parser.parse_args(args)
    return options, args
