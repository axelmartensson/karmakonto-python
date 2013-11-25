from twisted.trial import unittest
from karma import Group

class TestGroup(unittest.TestCase):
    def test_GET(self):
        expected = "axel"
        mock_db_proxy = None
        group = Group(mock_db_proxy, expected)
        actual = group.render_GET(None)
        self.assertEqual(actual, expected)
                            
