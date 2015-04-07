import unittest
from mockito import *
from project.lib.options import Options
from project.lib.project import Project


class TestProject(unittest.TestCase):
    def _default_options(self):
        options = Options()
        opts = options.parse()
        return opts

    def setUp(self):
        self.machine = Project(self._default_options())
        self.mock_process = mock() # boring empty mock
        when(self.mock_process).execute('date').thenReturn("The date might be: "\
                                                            +self.machine.process.execute("date").strip('\n')\
                                                            +"\nbut on the other hand it might just be the"\
                                                            +" 1st of April instead.")
        self.machine.process = self.mock_process 

    def test_machine_should_get_date(self):
        self.machine.date()
        verify(self.mock_process).execute('date')

if __name__ == '__main__':
    unittest.main()