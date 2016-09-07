"""Module contains core program logic
"""


from collections import deque

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
                print link.get('href')
                if link == origin_domain:
                    #queue.append(link.get('href'))
                    pass

    return graph


if __name__ == '__main__':
    crawl({}, 'http://joelcolucci.com', 'http://joelcolucci.com')