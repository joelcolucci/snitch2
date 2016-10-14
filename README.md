# snitch2 [![Build Status](https://travis-ci.org/joelcolucci/snitch2.svg?branch=master)](https://travis-ci.org/joelcolucci/snitch2)

A web crawler to search a domain for target links.

## Installation
```
pip install snitch2
```

## Getting Started
```
from snitch2 import snitch

starting_url = 'http://joelcolucci.com'
target_url = 'github.com'

results = snitch.search(starting_url, target_url)
```

Example results
```
{
    "start_url": "http://joelcolucci.com"
	"target_url": "github.com",
    "pages_crawled": 1,
	"guilty_total": 1,
	"guilty_results": [{
		"page_uri": "http://joelcolucci.com",
		"target_url": "github.com",
		"guilty_link": {
			"kind": "external",
			"text": "github.com/joelcolucci",
			"uri": "https://github.com/joelcolucci",
			"href": "https://github.com/joelcolucci",
			"domain": "joelcolucci.com",
			"type": "absolute"
		}
	}]
}
```

## Be responsible
Snitch2 does not currently check robots.txt when crawling a domain. Please be responsible!

## License
MIT License (c) 2016 Joel Colucci