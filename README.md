# client-python-async
power.trade client for receiving market data updates via async (websocket) channel

## API Urls

### List of tradeable entities **
REST: https://api.rest.prod.power.trade/v1/market_data/tradeable_entity/all/summary

### Top of Book **
WS: wss://api.wss.prod.power.trade/v1/feeds?type[]=top_of_book
top_of_book strusture:
https://power-trade.github.io/api-docs-source/ws_feeds.html#top_of_book

### Last Traded Price **
WS: wss://api.wss.prod.power.trade/v1/feeds?type[]=last_trade_price

last_traded_price structure:
https://power-trade.github.io/api-docs-source/ws_feeds.html#last_trade_price

### Reference Price **
WS: wss://api.wss.prod.power.trade/v1/feeds?type[]=reference_price,top_of_book

reference_price structure:
https://power-trade.github.io/api-docs-source/ws_feeds.html#reference_price
