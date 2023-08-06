# batch-async-http

This tool was designed to make batch async requests via http very simple! All you need to do is attach a decorator to your http request function and the rest is handled for you.

Behind the scenes your input is turned into a generator with batches of your specified size, and mapped asynchronously to your http request function!

See the source for this project here:
<https://https://github.com/MiesnerJacob/batch_async_http>.

## How to install:

```
pip install batch-async-http
```

## Usage

A typical function to make http requests to a REST API may look something like this:

```python
import requests

def call_api(example_input: list):

        # URL to call
        url = 'http://xx.xxx.xxx.xx/example_endpoint/'

        # Input to API
        params = {
            "raw": example_input,
        }

        # API calls
        r = requests.post(url, json=params)
        response = r.json()
        
        return response
```

A typical async function to make http requests to a REST API may look something like this:

```python
import httpx

async def call_api(example_input: list):

        # URL to call
        url = 'http://xx.xxx.xxx.xx/example_endpoint/'

        # Input to API
        params = {
            "raw": example_input,
        }

        # Concurrent API calls
        async with httpx.AsyncClient(timeout=None) as client:
            r = await client.post(url, json=params)
        response = r.json()
        
        return response
```

The power of batching your async requests is now just as easy as applying a simple decorator to your async function:

```python
import httpx
from batch_async_http import batch_async

@batch_async(size=8)
async def call_api(example_input: list):

        # URL to call
        url = 'http://xx.xxx.xxx.xx/example_endpoint/'

        # Input to API
        params = {
            "raw": example_input,
        }

        # Concurrent API calls
        async with httpx.AsyncClient(timeout=None) as client:
            r = await client.post(url, json=params)
        response = r.json()
        
        return response
```

Enjoy your increased efficiency with minimal effort!
