import unittest

from project.lib import Options


class TestCommandLineParameters(unittest.TestCase):

    def setUp(self):
        self.options = Options()

    def test_defaults_options_are_set(self):
        self.options.parse()
        self.assertEquals(self.options.known.example, 'example-value')

    def test_set_options_example(self):
        self.options.parse(['-x', 'foobar'])
        self.assertEquals(self.options.known.example, 'foobar')
        self.options.parse(['--example', 'not-a-foobar'])
        self.assertEquals(self.options.known.example, 'not-a-foobar')

if __name__ == '__main__':
    unittest.main()
