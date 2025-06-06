import json
import asyncio
import logging

from pathlib import Path
import sys

# Ensure project root is on the Python path so imports work when running `pytest`
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import client  # noqa: E402


def test_load_ref_data(tmp_path):
    file = tmp_path / "data.json"
    file.write_text('[{"id": 1, "symbol": "BTC"}]')
    data = client.load_ref_data(str(file))
    assert len(data) == 1
    assert data[0]["symbol"] == "BTC"


def test_find_product_by_id():
    client.ref_data = [{"id": 1, "symbol": "BTC"}, {"id": 2, "symbol": "ETH"}]
    assert client.find_product_by_id("2") == "ETH"


def test_find_product_by_id_without_data(caplog):
    client.ref_data = None
    result = client.find_product_by_id("1")
    assert result == "Error"
    assert any("No Reference data loaded" in r.message for r in caplog.records)



def test_process_message_top_of_book(monkeypatch, caplog):
    client.ref_data = [{"id": 1, "symbol": "BTC"}]
    monkeypatch.setattr(client, "lookup_conversion_number_by_id", lambda *args, **kwargs: (1, 1))
    message = json.dumps({
        "top_of_book": {
            "timestamp": "ts",
            "tradeable_entity_id": "1",
            "market_id": "m",
            "buy_price": "10",
            "buy_quantity": "1",
            "sell_price": "11",
            "sell_quantity": "1"
        }
    })
    caplog.clear()
    caplog.set_level(logging.INFO)
    asyncio.run(client.process_message(message, "endpoint"))
    assert any("Received Top Of Book" in r.message for r in caplog.records)
