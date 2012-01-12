import unittest

from lib import Options
from lib import Project

class MockProcess:

  def __init__(self):
    self.commands = []

  def execute(self, command):
    self.commands.append(command)



class TestProject(unittest.TestCase):
  def _default_options(self):
    options = Options()
    opts, args = options.parse()
    
    return opts
  
  def setUp(self):
    self.machine = Project(self._default_options())

    self.mock_process = MockProcess()
    self.machine.process = self.mock_process
  
  def test_machine_should_get_date(self):
    self.machine.date()
    
    self.assertTrue("date" in self.mock_process.commands)
