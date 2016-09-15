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

    def test_extract_uris_from_html(self):
        html = """
        <!DOCTYPE html>
        <html>
        <head>    
        </head>
        <body>
            <a href="https://google.com">Google</a>
            <a href="https://slack.com">Slack</a>
        </body>
        </html>
        """
        
        uris = snitch2.extract_uris_from_html(html)

        expected_num_links = 2

        self.assertEqual(expected_num_links, len(uris))

    def test_has_protocol(self):
        # Ensure any URI grabbed contains protocol
        uri_with_protocol = 'http://joelcolucci.com'
        uri_no_protocol = 'joelcolucci.com'

        self.assertTrue(snitch2.has_protocol(uri_with_protocol))
        self.assertFalse(snitch2.has_protocol(uri_no_protocol))

    def test_has_leading_forward_slashes(self):
        uri_with_slashes = '//joelcolucci.com'
        uri_without_leading_slahes = 'http://joelcolucci.com'

        self.assertTrue(snitch2.has_leading_forward_slashes(uri_with_slashes))
        self.assertFalse(snitch2.has_leading_forward_slashes(uri_without_leading_slahes))

    def test_is_relative_uri(self):
        uri_no_domain = '/hello'
        uri_with_domain = 'http://www.joelcolucci.com/hello'

        self.assertTrue(snitch2.is_relative_uri(uri_no_domain))
        self.assertFalse(snitch2.is_relative_uri(uri_with_domain))

    def test_fetch_html(self):
        pass



if __name__ == '__main__':
    main()