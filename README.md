[![Python Code Checks(Ruff)](https://github.com/laisee/client-python-async/actions/workflows/python-app.yml/badge.svg)](https://github.com/laisee/client-python-async/actions/workflows/python-app.yml)[![Security Check(Bandit)](https://github.com/laisee/client-python-async/actions/workflows/code-security.yml/badge.svg)](https://github.com/laisee/client-python-async/actions/workflows/code-security.yml)[![PyTest](https://github.com/laisee/client-python-async/actions/workflows/python-test.yml/badge.svg)](https://github.com/laisee/client-python-async/actions/workflows/python-test.yml)
# client-python-async
[Power Trade](power.trade) client for receiving market data updates via async (websocket) channel

## Getting Started
 - Install Python (any version above 3.10)
 - Install Python libraries used in client.py and other files
```shell 
    pip install -r requirements.txt
```
- Ensure the data & log folders exist in home/root directory
```shell
    ls data
    ls log
```
- Run the APi client
```shell
    python client.py
```
- Monitor message processing using the log file in /data folder using current UTC data e.g. 'client.2024-10-09.log' for date 09-10-2024
```shell
    tail -f log/client.20241009.log
```
- Adjust the endpoints in client.py to include/exclude data required. By default all 3 endpoints are listed.
```python
    endpoints = [
        "wss://api.wss.prod.power.trade/v1/feeds?type[]=top_of_book"
        "wss://api.wss.prod.power.trade/v1/feeds?type[]=reference_price",
        "wss://api.wss.prod.power.trade/v1/feeds?type[]=last_trade_price"
    ]
```
- Run the python client using installed version of Python
```
    python client.py
```
- Monitor message processing using the log file in /data folder using current UTC data e.g. 'client.2024-10-09.log' for date 09-10-2024
```
    tail -f log/client.20241009.log
```
- Adjust the endpoints to include/exclude data required. By default all 3 endpoints are listed.

    See [here](https://power-trade.github.io/api-docs-source/ws_feeds.html#Market_Feeds_Connection_Parameters) for more details on configuring the target WS endspoints to filter product type (spot, perpetuals, options, ...) and message types (risk, top_of_book, ...)

## API Endpoints

### List of tradeable entities
REST Url: https://api.rest.prod.power.trade/v1/market_data/tradeable_entity/all/summary

[Tradeable Entity](https://power-trade.github.io/api-docs-source/rest_api.html#_get_v1market_datatradeable_entityallsummary)

### Top of Book
| Environment | URL |
|-------------|-----|
| Test | wss://api.wss.test.power.trade/v1/feeds?type[]=top_of_book |
| Production | wss://api.wss.prod.power.trade/v1/feeds?type[]=top_of_book |

[Top of Book data structure](https://power-trade.github.io/api-docs-source/ws_feeds.html#top_of_book)

### Last Traded Price
| Environment | URL |
|-------------|-----|
| Test | wss://api.wss.test.power.trade/v1/feeds?type[]=last_trade_price |
| Production | wss://api.wss.prod.power.trade/v1/feeds?type[]=last_trade_price |

[Last Trade Price data structure](https://power-trade.github.io/api-docs-source/ws_feeds.html#last_trade_price)

### Reference Price

| Environment | URL |
|-------------|-----|
| Test | wss://api.wss.test.power.trade/v1/feeds?type[]=reference_price |
| Production | wss://api.wss.prod.power.trade/v1/feeds?type[]=reference_price|

[Reference Price data structure](https://power-trade.github.io/api-docs-source/ws_feeds.html#reference_price)
