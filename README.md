# snitch2

## Description
Crawl a site for unwanted/curious links.

## Installation
```
pip install snitch2
```

## Getting Started
```
import snitch2


results = snitch.search(origin_domain, target_url)
```

Example results
```
{
    origin_domain: 'origin.com',
    target_url: 'query.com',
    max_depth: 5,
    pages_crawled: 2,
    pages_containing: 2,
    results_total: 5
    results: [
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

## License