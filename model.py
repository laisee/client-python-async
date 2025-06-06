from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class TopOfBook:
    timestamp: str
    tradeable_entity_id: str
    market_id: str
    buy_price: str
    buy_quantity: str
    sell_price: str
    sell_quantity: str
    product: str = field(default="NULL")
    buy_price_conv: float = field(default=0.0) 
    buy_quantity_conv: float = field(default=0.0) 
    sell_price_conv: float = field(default=0.0) 
    sell_quantity_conv: float = field(default=0.0) 

@dataclass_json
@dataclass
class ReferencePrice:
    timestamp: str
    tradeable_entity_id: str
    market_id: str
    price: str
    price_type: str
    product: str = field(default="")
    price_conv: float = field(default=0.0)

@dataclass_json
@dataclass
class LastTradePrice:
    timestamp: str
    tradeable_entity_id: str
    market_id: str
    price: str
    price_type: str
    product: str = field(default="")
    price_conv: float = field(default=0.0)

@dataclass_json
@dataclass
class MarketData:
    reference_price: Optional[ReferencePrice] = None
    top_of_book: Optional[TopOfBook] = None
    last_trade_price: Optional[LastTradePrice] = None
