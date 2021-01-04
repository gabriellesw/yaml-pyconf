import unittest
from yaml_pyconf import SimpleConfig, FlaskConfig


class TestIsSingleton(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(SimpleConfig(), SimpleConfig())

    def test_flask(self):
        self.assertEqual(FlaskConfig("sample", "sample"), FlaskConfig("sample", "sample"))
