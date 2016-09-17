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
        href1 = '/hello/world'
        href2 = '/'

        result1 = parselink.is_relative_href(href1)
        result2 = parselink.is_relative_href(href2)
        
        self.assertTrue(result1)
        self.assertTrue(result2)

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

    def test_get_href_kind_internal(self):
        """Test function returns 'internal' href kind"""
        domain = 'joelcolucci.com'
        
        href1 = '/'
        href2 = 'joelcolucci.com/hello'

        result1 = parselink.get_href_kind(href1, domain)
        result2 = parselink.get_href_kind(href2, domain)

        self.assertEqual(result1, 'internal')
        self.assertEqual(result2, 'internal')

    def test_get_href_kind_external(self):
        """Test function returns 'external' href kind"""
        domain = 'joelcolucci.com'

        href1 = 'google.com'
        href2 = 'www.google.com'
        href3 = 'https:/www.google.com/hello'

        result1 = parselink.get_href_kind(href1, domain)
        result2 = parselink.get_href_kind(href2, domain)
        result3 = parselink.get_href_kind(href3, domain)

        self.assertEqual(result1, 'external')
        self.assertEqual(result2, 'external')
        self.assertEqual(result3, 'external')

    def test_is_external_href_true(self):
        """Test function returns expected True"""
        domain = 'joelcolucci.com'
        
        href1 = '/'
        href2 = 'joelcolucci.com/hello'

        result1 = parselink.is_internal_href(href1, domain)
        result2 = parselink.is_internal_href(href2, domain)

        self.assertTrue(result1)
        self.assertTrue(result2)

    def test_is_external_href_false(self):
        """Test function returns expected False"""
        domain = 'joelcolucci.com'

        href1 = 'google.com'
        href2 = 'www.google.com'
        href3 = 'https:/www.google.com/hello'

        result1 = parselink.is_internal_href(href1, domain)
        result2 = parselink.is_internal_href(href2, domain)
        result3 = parselink.is_internal_href(href3, domain)

        self.assertFalse(result1)
        self.assertFalse(result2)
        self.assertFalse(result3)

    def test_get_href_uri(self):
        """Test function returns full URI with protocol"""
        domain = 'joelcolucci.com'

        href1 = '/'
        href2 = '#'
        href3 = '/hello'
        href4 = 'joelcolucci.com'
        href5 = '//joelcolucci.com'
        href6 = 'http://joelcolucci.com'

        result1 = parselink.get_href_uri(href1, domain)
        result2 = parselink.get_href_uri(href2, domain)
        result3 = parselink.get_href_uri(href3, domain)
        result4 = parselink.get_href_uri(href4, domain)
        result5 = parselink.get_href_uri(href5, domain)
        result6 = parselink.get_href_uri(href6, domain)

        self.assertEqual(result1, 'http://joelcolucci.com/')
        self.assertEqual(result2, 'http://joelcolucci.com#')
        self.assertEqual(result3, 'http://joelcolucci.com/hello')
        self.assertEqual(result4, 'http://joelcolucci.com')
        self.assertEqual(result5, 'http://joelcolucci.com')
        self.assertEqual(result6, 'http://joelcolucci.com')

    def test_get_domain(self):
        """Test function returns domain"""
        uri1 = 'http://www.joelcolucci.com/hello/world'
        uri2 = 'www.joelcolucci.com/helloworld'
        uri3 = '//www.joelcolucci.com/helloworld'

        result1 = parselink.get_domain(uri1)
        result2 = parselink.get_domain(uri2)
        result3 = parselink.get_domain(uri3)

        expected_result = 'www.joelcolucci.com'

        self.assertEqual(result1, expected_result)
        self.assertEqual(result2, expected_result)
        self.assertEqual(result3, expected_result)

    def test_get_links(self):
        """Test function returns expected results"""
        uri = 'www.joelcolucci.com'
        html = """
        <!DOCTYPE html>
        <html>
        <head>    
        </head>
        <body>
            <a href="https://google.com">Google</a>
            <a href="https://slack.com">Slack</a>
            <a href="/about">About Me</a>
            <a href="www.joelcolucci.com/contact">Contact Me</a>
        </body>
        </html>
        """
        
        links = parselink.get_links(uri, html)

        expected_num_links = 4

        self.assertEqual(expected_num_links, len(links))


if __name__ == '__main__':
    main()