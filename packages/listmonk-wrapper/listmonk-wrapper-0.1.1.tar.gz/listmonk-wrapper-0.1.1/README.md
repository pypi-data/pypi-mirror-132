# ListmonkWrapper


Light Python wrapper for listmonk.app


* PyPI: <https://pypi.org/project/listmonk-wrapper/>
* Free software: BSD-3-Clause


## Setup

* `pip install listmonk-wrapper`

## Usage
```
    from listmonk_wrapper import ListMonkClient

    client = ListMonkClient(host="http://localhost", port=9000, username="password", password="password")
    my_campaigns = client.get_campaigns()
```
