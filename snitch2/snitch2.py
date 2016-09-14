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


def contains(str1, str2):
    """Return true if str1 contains str2"""
    result = str1.find(str2)

    if result == -1:
        return False

    return True



if __name__ == '__main__':
    crawl({}, 'github.com', 'http://joelcolucci.com')