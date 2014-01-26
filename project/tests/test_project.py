import unittest
from mockito import *
from lib import Options
from lib import Project


class TestProject(unittest.TestCase):
    def _default_options(self):
        options = Options()
        opts = options.parse()
        return opts

    def setUp(self):
        self.machine = Project(self._default_options())
        self.mock_process = mock()
        self.machine.process = self.mock_process

    def test_machine_should_get_date(self):
        self.machine.date()
        verify(self.mock_process).execute('date')
