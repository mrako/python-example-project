import os, sys

project_path = os.path.join( os.path.abspath(os.path.dirname(__file__)), '..' )
sys.path.append(project_path)

import unittest

from lib import options

class TestCommandLineParameters(unittest.TestCase):

    def setUp(self):
      pass
    
    def test_defaults_options_are_for_ubuntu(self):
      opt, args = options.parse()
      self.assertEquals(opt.target, 'ubuntu')
      self.assertEquals(opt.distribution, 'hardy')
      
    def test_options_target_is_set(self):
      opt, args = options.parse(['-t', 'debian'])
      self.assertEquals(opt.target, 'debian')
    
    def test_options_distribution_is_set(self):
      opt, args = options.parse(['-d', 'karmic'])
      self.assertEquals(opt.distribution, 'karmic')
    
    
if __name__ == '__main__':
  unittest.main()