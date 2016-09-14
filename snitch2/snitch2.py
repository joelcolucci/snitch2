"""Module contains core program logic
"""


from collections import deque
import re

from bs4 import BeautifulSoup
import requests


def snitch(origin_domain, target_url, max_depth):
    """Return Response of query including list of pages and target results"""
    # Validate origin domain
    pass


def crawl(graph, origin_domain, start_url):
    # Initialize data structures
    visited = set()
    queue = deque()

    queue.append(start_url)

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)

            # Fetch html document
            html_page = requests.get(start_url).text
            # Add origin domain link to queue
            soup = BeautifulSoup(html_page, 'html.parser')
            for link in soup.find_all('a'):
                href = link.get('href')
                if contains(href, origin_domain):
                    #queue.append(link.get('href'))
                    print("heyo")

    return graph


def crawl_page(start_url, target_uri):
    """Crawl single page looking for target_uri"""
    # Fetch html page
    html_page = requests.get(start_url).text

    soup = BeautifulSoup(html_page, 'html.parser')
    results = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if contains(href, target_uri):
            results.append({
                "href": href,
                "page_uri": start_url
            })

    result = {
        "start_url": start_url,
        "target_uri": target_uri,
        "results_total": len(results),
        "results": results
    }

    return result


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
    print crawl_page('http://www.joelcolucci.com', 'github.com')