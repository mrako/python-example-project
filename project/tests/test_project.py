import unittest

from lib import Options
from lib import Project

class MockProcess:
  
  def __init__(self):
    self.command = ""
  
  def execute(self, command):
    self.command = command



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
    
    self.assertEquals(self.mock_process.command, "date")
