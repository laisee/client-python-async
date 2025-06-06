import json
import sys
from dataclasses import asdict
from pathlib import Path

import pytest

# Ensure project root is on the Python path so imports work when running `pytest`
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from model import TopOfBook, ReferencePrice, LastTradePrice, MarketData  # noqa: E402


def test_top_of_book_serialization_to_ensure_accuracy():
    """
    Verifies that TopOfBook serialization to JSON matches expected output.
    """
    # Create a sample TopOfBook object
    top_of_book = TopOfBook(
        timestamp="2022-01-01T12:00:00",
        tradeable_entity_id="entity1",
        market_id="market1",
        buy_price="10.0",
        buy_quantity="100",
        sell_price="11.0",
        sell_quantity="50",
        product="Product1",
        buy_price_conv=10.0,
        buy_quantity_conv=100.0,
        sell_price_conv=11.0,
        sell_quantity_conv=50.0
    )

    # Define the expected JSON output
    expected_json = {
        "timestamp": "2022-01-01T12:00:00",
        "tradeable_entity_id": "entity1",
        "market_id": "market1",
        "buy_price": "10.0",
        "buy_quantity": "100",
        "sell_price": "11.0",
        "sell_quantity": "50",
        "product": "Product1",
        "buy_price_conv": 10.0,
        "buy_quantity_conv": 100.0,
        "sell_price_conv": 11.0,
        "sell_quantity_conv": 50.0
    }

    # Compare the actual JSON output with the expected output
    assert json.loads(top_of_book.to_json()) == expected_json


def test_top_of_book_deserialization_to_ensure_accuracy():
    """
    Verifies that TopOfBook deserialization from JSON matches expected output.
    """
    # Create a sample JSON object
    json_data = {
        "timestamp": "2022-01-01T12:00:00",
        "tradeable_entity_id": "entity1",
        "market_id": "market1",
        "buy_price": "10.0",
        "buy_quantity": "100",
        "sell_price": "11.0",
        "sell_quantity": "50",
        "product": "Product1",
        "buy_price_conv": 10.0,
        "buy_quantity_conv": 100.0,
        "sell_price_conv": 11.0,
        "sell_quantity_conv": 50.0
    }

    # Deserialize the JSON object into a TopOfBook object
    top_of_book = TopOfBook.from_json(json.dumps(json_data))

    # Compare the deserialized object with the original JSON data
    assert asdict(top_of_book) == json_data


def test_reference_price_serialization_to_ensure_accuracy():
    """
    Verifies that ReferencePrice serialization to JSON matches expected output.
    """
    # Create a sample ReferencePrice object
    reference_price = ReferencePrice(
        timestamp="2022-01-01T12:00:00",
        tradeable_entity_id="entity1",
        market_id="market1",
        price="10.0",
        price_type="type1",
        product="Product1",
        price_conv=10.0
    )

    # Define the expected JSON output
    expected_json = {
        "timestamp": "2022-01-01T12:00:00",
        "tradeable_entity_id": "entity1",
        "market_id": "market1",
        "price": "10.0",
        "price_type": "type1",
        "product": "Product1",
        "price_conv": 10.0
    }

    # Compare the actual JSON output with the expected output
    assert json.loads(reference_price.to_json()) == expected_json


def test_reference_price_deserialization_to_ensure_accuracy():
    """
    Verifies that ReferencePrice deserialization from JSON matches expected output.
    """
    # Create a sample JSON object
    json_data = {
        "timestamp": "2022-01-01T12:00:00",
        "tradeable_entity_id": "entity1",
        "market_id": "market1",
        "price": "10.0",
        "price_type": "type1",
        "product": "Product1",
        "price_conv": 10.0
    }

    # Deserialize the JSON object into a ReferencePrice object
    reference_price = ReferencePrice.from_json(json.dumps(json_data))

    # Compare the deserialized object with the original JSON data
    assert asdict(reference_price) == json_data

def test_last_trade_price_serialization_to_ensure_accuracy():
    """
    Verifies that LastTradePrice serialization to JSON matches expected output.
    """
    # Create a sample LastTradePrice object
    last_trade_price = LastTradePrice(
        timestamp="2022-01-01T12:00:00",
        tradeable_entity_id="entity1",
        market_id="market1",
        price="10.0",
        price_type="type1",
        product="Product1",
        price_conv=10.0
    )

    # Define the expected JSON output
    expected_json = {
        "timestamp": "2022-01-01T12:00:00",
        "tradeable_entity_id": "entity1",
        "market_id": "market1",
        "price": "10.0",
        "price_type": "type1",
        "product": "Product1",
        "price_conv": 10.0
    }

    # Compare the actual JSON output with the expected output
    assert json.loads(last_trade_price.to_json()) == expected_json


def test_last_trade_price_deserialization_to_ensure_accuracy():
    """
    Verifies that LastTradePrice deserialization from JSON matches expected output.
    """
    # Create a sample JSON object
    json_data = {
        "timestamp": "2022-01-01T12:00:00",
        "tradeable_entity_id": "entity1",
        "market_id": "market1",
        "price": "10.0",
        "price_type": "type1",
        "product": "Product1",
        "price_conv": 10.0
    }

    # Deserialize the JSON object into a LastTradePrice object
    last_trade_price = LastTradePrice.from_json(json.dumps(json_data))

    # Compare the deserialized object with the original JSON data
    assert asdict(last_trade_price) == json_data

def test_market_data_serialization_to_ensure_accuracy():
    """
    Verifies that MarketData serialization to JSON matches expected output.
    """
    # Create sample nested objects
    reference_price = ReferencePrice(
        timestamp="2022-01-01T12:00:00",
        tradeable_entity_id="entity1",
        market_id="market1",
        price="10.0",
        price_type="type1",
        product="Product1",
        price_conv=10.0
    )
    top_of_book = TopOfBook(
        timestamp="2022-01-01T12:00:00",
        tradeable_entity_id="entity1",
        market_id="market1",
        buy_price="10.0",
        buy_quantity="100",
        sell_price="11.0",
        sell_quantity="50",
        product="Product1",
        buy_price_conv=10.0,
        buy_quantity_conv=100.0,
        sell_price_conv=11.0,
        sell_quantity_conv=50.0
    )
    last_trade_price = LastTradePrice(
        timestamp="2022-01-01T12:00:00",
        tradeable_entity_id="entity1",
        market_id="market1",
        price="10.0",
        price_type="type1",
        product="Product1",
        price_conv=10.0
    )

    # Create a sample MarketData object
    market_data = MarketData(
        reference_price=reference_price,
        top_of_book=top_of_book,
        last_trade_price=last_trade_price
    )

    # Define the expected JSON output
    expected_json = {
        "reference_price": {
            "timestamp": "2022-01-01T12:00:00",
            "tradeable_entity_id": "entity1",
            "market_id": "market1",
            "price": "10.0",
            "price_type": "type1",
            "product": "Product1",
            "price_conv": 10.0
        },
        "top_of_book": {
            "timestamp": "2022-01-01T12:00:00",
            "tradeable_entity_id": "entity1",
            "market_id": "market1",
            "buy_price": "10.0",
            "buy_quantity": "100",
            "sell_price": "11.0",
            "sell_quantity": "50",
            "product": "Product1",
            "buy_price_conv": 10.0,
            "buy_quantity_conv": 100.0,
            "sell_price_conv": 11.0,
            "sell_quantity_conv": 50.0
        },
        "last_trade_price": {
            "timestamp": "2022-01-01T12:00:00",
            "tradeable_entity_id": "entity1",
            "market_id": "market1",
            "price": "10.0",
            "price_type": "type1",
            "product": "Product1",
            "price_conv": 10.0
        }
    }

    # Compare the actual JSON output with the expected output
    assert json.loads(market_data.to_json()) == expected_json

def test_market_data_deserialization_with_all_fields():
    """
    Verifies that MarketData deserialization from JSON with all fields matches expected output.
    """
    # Create a sample JSON object
    json_data = {
        "reference_price": {
            "timestamp": "2022-01-01T12:00:00",
            "tradeable_entity_id": "entity1",
            "market_id": "market1",
            "price": "10.0",
            "price_type": "type1",
            "product": "Product1",
            "price_conv": 10.0
        },
        "top_of_book": {
            "timestamp": "2022-01-01T12:00:00",
            "tradeable_entity_id": "entity1",
            "market_id": "market1",
            "buy_price": "10.0",
            "buy_quantity": "100",
            "sell_price": "11.0",
            "sell_quantity": "50",
            "product": "Product1",
            "buy_price_conv": 10.0,
            "buy_quantity_conv": 100.0,
            "sell_price_conv": 11.0,
            "sell_quantity_conv": 50.0
        },
        "last_trade_price": {
            "timestamp": "2022-01-01T12:00:00",
            "tradeable_entity_id": "entity1",
            "market_id": "market1",
            "price": "10.0",
            "price_type": "type1",
            "product": "Product1",
            "price_conv": 10.0
        }
    }

    # Deserialize the JSON object into a MarketData object
    market_data = MarketData.from_json(json.dumps(json_data))

    # Verify deserialized object
    assert market_data.reference_price.timestamp == "2022-01-01T12:00:00"
    assert market_data.top_of_book.tradeable_entity_id == "entity1"
    assert market_data.last_trade_price.price == "10.0"


def test_market_data_deserialization_with_missing_fields():
    """
    Verifies that MarketData deserialization from JSON with missing fields matches expected output.
    """
    # Create a sample JSON object with missing fields
    json_data = {
        "reference_price": {
            "market_id": "market1",
            "price": "10.0",
            "timestamp": "2022-01-01T12:00:00",
            "tradeable_entity_id": "entity1"
        },
        "top_of_book": {
            "market_id": "market1",
            "price": "10.0",
            "timestamp": "2022-01-01T12:00:00"
        }
    }

    # Deserialize the JSON object into a MarketData object
    with pytest.raises(KeyError):
        MarketData.from_json(json.dumps(json_data))

def test_market_data_deserialization_with_empty_json():
    """
    Verifies that MarketData deserialization from empty JSON matches expected output.
    """
    # Create an empty JSON object
    json_data = {}

    # Deserialize the JSON object into a MarketData object
    market_data = MarketData.from_json(json.dumps(json_data))

    # Verify deserialized object
    assert market_data.reference_price is None
    assert market_data.top_of_book is None
    assert market_data.last_trade_price is None


def test_market_data_deserialization_with_invalid_json():
    """
    Verifies that MarketData deserialization from invalid JSON raises an exception.
    """
    # Create an invalid JSON object
    json_data = "{ invalid json }"

    # Attempt to deserialize the JSON object into a MarketData object
    with pytest.raises(json.JSONDecodeError):
        MarketData.from_json(json_data)
