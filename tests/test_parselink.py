"""Unit tests for parselink module
"""


from unittest import main
from unittest import TestCase

from snitch2 import parselink


class ParseLinkTestCase(TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_normalize_protocol_when_none(self):
        """Test functions returns URI with protocol when no protocol on URI"""
        domain = 'joelcolucci.com'

        expected_result = 'http://joelcolucci.com'
        actual_result = parselink.normalize_protocol(domain)
        
        self.assertEqual(actual_result, expected_result)

    def test_normalize_protocol_when_relative(self):
        """Test functions returns URI with protocol when relative protocol on URI"""
        domain = '//joelcolucci.com'

        expected_result = 'http://joelcolucci.com'
        actual_result = parselink.normalize_protocol(domain)
        
        self.assertEqual(actual_result, expected_result)

    def test_has_relative_protocol_true(self):
        """Test function returns expected True"""
        relative_uri = '//joelcolucci.com'

        result = parselink.has_relative_protocol(relative_uri)

        self.assertTrue(result)

    def test_has_relative_protocol_false(self):
        """Test function returns expected False"""
        full_uri = 'http://joelcolucci.com'

        result = parselink.has_relative_protocol(full_uri)

        self.assertFalse(result)

    def test_has_http_protocol_true(self):
        """Test function returns expected True"""
        http_uri = 'http://joelcolucci.com'
        https_uri = 'https://joelcolucci.com'

        http_result = parselink.has_http_protocol(http_uri)
        https_result = parselink.has_http_protocol(https_uri)

        self.assertTrue(http_result)
        self.assertTrue(https_result)

    def test_has_http_protocol_false(self):
        """Test function returns expected False"""
        relative_uri = '//joelcolucci.com'
        naked_uri = 'joelcolucci.com'

        relative_result = parselink.has_http_protocol(relative_uri)
        naked_result = parselink.has_http_protocol(naked_uri)
        
        self.assertFalse(relative_result)
        self.assertFalse(naked_result)

    def test_get_href_type_relative(self):
        """Test function returns 'relative' href type"""
        href1 = '/hello/world'
        href2 = '#'

        result1 = parselink.get_href_type(href1)
        result2 = parselink.get_href_type(href2)

        self.assertEqual(result1, 'relative')
        self.assertEqual(result2, 'relative')

    def test_get_href_type_absolute(self):
        """Test function returns 'absolute' href type"""
        href = 'http://joelcolucci.com'

        result = parselink.get_href_type(href)

        self.assertEqual(result, 'absolute')
        
    def test_is_relative_href_true(self):
        """Test function returns expected True"""
        href = '/hello/world'

        result = parselink.is_relative_href(href)
        
        self.assertTrue(result)

    def test_is_relative_href_false(self):
        """Test function returns expected False"""
        href1 = 'http://joelcolucci.com'
        href2 = 'www.joelcolucci.com'
        href3 = '//joelcolucci.com'
        
        result1 = parselink.is_relative_href(href1)
        result2 = parselink.is_relative_href(href2)
        result3 = parselink.is_relative_href(href3)

        self.assertFalse(result1)
        self.assertFalse(result2)
        self.assertFalse(result3)

    def test_is_fragment_true(self):
        """Test function returns expected True"""
        href = '#'

        result = parselink.is_fragment(href)

        self.assertTrue(result)

    def test_is_fragment_false(self):
        """Test function returns expected False"""
        href = '/hello'

        result = parselink.is_fragment(href)

        self.assertFalse(result)


    #TODO: href kind functions

# We want to normalize the protocol of the domain right away

# We don't want to normalize protocol of hrefs right away because they could be relative

# Normalize protocol
# Trick part is we need to know relative link versus absolute
# If we normalize fragments/paths how do we know this?

# CHALLENGE -> Allow functions to be called in any order
#IZZY MALIK


if __name__ == '__main__':
    main()