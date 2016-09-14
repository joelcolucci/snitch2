"""Unit tests for snitch2 module
"""


from unittest import main
from unittest import TestCase


from snitch2 import snitch2


class Snitch2TestCase(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_contains_returns_true(self):
        str1 = 'google.com/maps'
        str2 = 'google.com'

        self.assertTrue(snitch2.contains(str1, str2))

    def test_contains_fail_returns_false(self):
        str1 = 'joelcolucci.com'
        str2 = 'google.com'

        self.assertFalse(snitch2.contains(str1, str2))

    def test_contains_handles_none(self):
        str1 = None
        str2 = 'google.com'

        self.assertFalse(snitch2.contains(str1, str2))

        str1 = 'google.com'
        str2 = None

        self.assertFalse(snitch2.contains(str1, str2))


if __name__ == '__main__':
    main()