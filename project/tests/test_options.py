import unittest

from lib import Options


class TestCommandLineParameters(unittest.TestCase):

    def setUp(self):
        self.options = Options()

    def test_defaults_options_are_set(self):
        opts = self.options.parse()
        self.assertEquals(opts.example, 'example-value')

    def test_options_example_is_set(self):
        opts = self.options.parse(['-x', 'foobar'])
        self.assertEquals(opts.example, 'foobar')

        opts = self.options.parse(['--example', 'not-a-foobar'])
        self.assertEquals(opts.example, 'not-a-foobar')


if __name__ == '__main__':
    unittest.main()
