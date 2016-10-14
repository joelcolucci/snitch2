# snitch2 [![Build Status](https://travis-ci.org/joelcolucci/snitch2.svg?branch=master)](https://travis-ci.org/joelcolucci/snitch2)

A web crawler to search a domain for target links.

## Installation
```
pip install snitch2
```

## Getting Started
```
from snitch2 import snitch


results = snitch.search(origin_domain, target_url)
```

Example results
```
{
    "pages_crawled": 1,
    "target_uri": "github.com",
    "start_url": "//joelcolucci.com",
    "guilty_total": 1,
    "guilty_results": [
        {
            'uri': 'origin.com',
            'total': 3,
            'links': [
                'query.com/',
                'query.com/timbuck2',
                'query.com/hella'
            ]
        },
        {
            'uri': 'origin.com/hello',
            'total': 2,
            'links': [
                'query.com',
                'query.com/timbuck2'
            ]
        }
    ]
}
```
## Be responsible
Snitch2 does not currently check robots.txt when crawling a domain. Please be responsible!

## License
MIT License (c) 2016 Joel Colucci