"""Module containing function for normalizing and parsing URIs
link = {
    'type': ['internal', 'external', 'unknown'],
    'kind': ['relative', 'absolute'],
    'text': 'click here',
    'uri': 'https//joelcolucci.com',
    'domain': ''
}

"""


import re
import urlparse

from bs4 import BeautifulSoup


class LinkExtractor(object):
    """Extract and normalize links from HTML"""

    def __init__(self, page_uri, page_html):
        self.page_uri = page_uri
        self.page_html = page_html
        #self.page_domain = NormalizedLink(page_uri).domain
      
    def get_links(self, html_page):
        """Return list of anchor tags from page"""
        soup = BeautifulSoup(html_page, 'html.parser')

        anchors = soup.find_all('a')
        results = []

        for anchor in anchors:
            href = anchor.get('href')
            text = anchor.get('text')

            results.append(href)

        return results


def parse_link(href, domain):
    """Return dictionary of link attributes"""
    normalized_domain = normalize_protocol(domain)

    type = get_href_type(href)

    kind = get_href_kind(href, domain)

    uri = get_href_uri(href, domain)

    domain = get_domain(href)

    return {
        'type': type,
        'kind': kind,
        'uri': uri,
        'domain': normalized_domain
    }


def normalize_protocol(uri):
    """Return URI with full HTTP scheme"""
    if has_relative_protocol(uri):
        uri = '{}{}'.format('http:', uri)
    elif not has_http_protocol(uri):
        # Naively assume if URI does not have HTTP protocol then it has no protocol
        uri = '{}{}'.format('http://', uri)
    
    return uri

def has_relative_protocol(uri):
    """Return True if URI has relative protocol '//' """
    start = uri[:2]

    if start == '//':
        return True
    
    return False

def has_http_protocol(uri):
    """Return True if URI does not have HTTP protocol"""
    regex = '(https?\:\/\/)'

    result = re.match(regex, uri)
    if result:
        return True

    return False


def get_href_type(href):
    """Return type (relative, absolute) of href"""
    if is_relative_href(href) or is_fragment(href):
        type = 'relative'
    else:
        type = 'absolute'

    return type


def is_relative_href(href):
    """Return True if href is relative else False"""
    regex = '^\/($|[^\/ ]+)'

    result = re.match(regex, href)
    if result:
        return True

    return False

def is_fragment(href):
    """Return True if href is a fragment else False"""
    if href[0] == '#':
        return True

    return False


def get_href_kind(href, domain):
    """Return kind of href (internal or external)"""
    if is_internal_href(href, domain):
        kind = 'internal'
    else:
        kind = 'external'

    return kind

def is_internal_href(href, domain):
    """Return True if link is to an internal page else False"""
    if is_relative_href(href) or contains(href, domain):
        return True

    return False


#######################################################################
def get_href_uri(href, domain):
    pass


#######################################################################
def get_domain(href):
    uri = get_href_uri(href)

    url = urlparse(uri).netloc

    return uri


#######################################################################


def is_relative_uri(uri):
    """Return True if uri is relative

    Expects normalized URI w/ scheme
    """
    domain = urlparse.urlparse(uri).netloc
    if not domain:
        return True

    return False



    
 
def strip_path(uri):
    domain = urlparse.urlparse(uri).netloc

    return normalize_uri(domain)





def contains(str1, str2):
    """Return true if str1 contains str2"""
    try:
        result = str1.find(str2)
    except TypeError as e:
        return False # Handle if str2 is None
    except AttributeError as e:
        return False # Handle if str1 is None

    if result == -1:
        return False

    return True



if __name__ == '__main__':
    pass