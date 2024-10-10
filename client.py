import asyncio
import websockets
import csv
import json
import logging
from datetime import datetime, timezone
from model import ReferencePrice, LastTradePrice, TopOfBook
from utility import lookup_conversion_number_by_id # type: ignore

# in-mem store containing all tradeable products @ power.trade
PRODUCT_CSV_FILE = "data/product.csv"
ref_data = None

def load_ref_data(file_path):
    #
    # file is an array of json objects
    # latest version can be downloaded from 'https://api.rest.prod.power.trade/v1/market_data/tradeable_entity/all/summary'
    #
    with open(file_path, 'r') as file:
        data = json.load(file)
        assert len(data) > 0, f"Error - ref data from file {file_path} must have > 0 rows"
    return data

def find_product_by_id(entity_id: str):
    product = "Unknown"
    if ref_data is None:
        logging.error("No Reference data loaded")
        return "Error"
    for record in ref_data:
        if str(record["id"]) == entity_id:
            product = record["symbol"]
            break
    return product

async def process_message(message: str, endpoint: str):
    try:
        logging.info(f"Received message: {message}")
        data = json.loads(message)

        #
        # process selected messages and flag any others
        #
        if "top_of_book" in data:
            try:
                tob = TopOfBook.from_dict(data["top_of_book"])
                # 
                # use lookup on reference data set to get product name
                #
                product = find_product_by_id(tob.tradeable_entity_id)

                # lookup conversion factors for price, quantity based on entity Id
                price_conversion_factor, quantity_conversion_factor = lookup_conversion_number_by_id(PRODUCT_CSV_FILE, tob.tradeable_entity_id)

                #
                # assign product to TOB object, convert from internal price, qty to regular amounts
                #
                tob.product = product
                tob.buy_price_conv = float(tob.buy_price) / price_conversion_factor if tob.buy_price != 'none' else 0.00
                tob.buy_quantity_conv = float(tob.buy_quantity) / quantity_conversion_factor if tob.buy_quantity != 'none' else 0.00
                tob.sell_price_conv = float(tob.sell_price) / price_conversion_factor if tob.sell_price != 'none' else 0.00
                tob.sell_quantity_conv = float(tob.sell_quantity) / quantity_conversion_factor if tob.sell_quantity != 'none' else 0.00
                # 
                # add code here to process and/or store the TOB record
                # ...
                # 
                logging.info(f"Received Top Of Book (ask, bid) for product '{product}' -> {tob}") 
            except Exception as e:
                logging.error(f"Error decoding message {message}: {e}")

        elif "reference_price" in data:
            try:
                ref_price = ReferencePrice.from_dict(data["reference_price"])
                # 
                # use lookup on reference data set to get product name
                #
                product = find_product_by_id(ref_price.tradeable_entity_id)

                # lookup conversion factors for price, quantity based on entity Id
                price_conversion_factor, quantity_conversion_factor = lookup_conversion_number_by_id(PRODUCT_CSV_FILE, tob.tradeable_entity_id)

                ref_price.product = product
                ref_price.price_conv = float(ref_price.price) / price_conversion_factor if ref_price.price != 'none' else 0.00
                logging.info(f"Received Reference Price for product '{product}' -> {ref_price}") 
                # 
                # add code here to process and/or store the Reference Price record
                # ...
                # 
                logging.info(f"Received Top Of Book (ask, bid) for product '{product}' -> {tob}") 
            except Exception as e:
                logging.error(f"Error decoding message {message}: {e}")

        elif "last_trade_price" in data:
            try:
                last_trade_price = LastTradePrice.from_dict(data["last_trade_price"])
                # 
                # use lookup on reference data set to get product name
                #
                product = find_product_by_id(last_trade_price.tradeable_entity_id)
                
                # lookup conversion factors for price, quantity based on entity Id
                price_conversion_factor, quantity_conversion_factor = lookup_conversion_number_by_id(PRODUCT_CSV_FILE, tob.tradeable_entity_id)

                last_trade_price.product = product
                last_trade_price.price_conv = float(last_trade_price.price) / price_conversion_factor if last_trade_price.price != 'none' else 0.00
                logging.info(f"Received Last Trade Price for product '{product}' -> {last_trade_price}") 
                # 
                # add code here to process and/or store the Last Trade Price record
                # ...
                # 
            except Exception as e:
                logging.error(f"Error decoding message {message}: {e}")
        else:
            logging.warning(f"Unknown message type from {endpoint}: {data}")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding message from {endpoint}: {e}")

async def listen_to_endpoint(endpoint: str):
   while True:
        try:
            async with websockets.connect(endpoint, ping_interval=10, ping_timeout=20) as websocket:
                logging.info(f"Connected to {endpoint}")
                async for message in websocket:
                    await process_message(message, endpoint)
        except websockets.exceptions.ConnectionClosedError as e:
            logging.error(f"Connection closed with error: {e}. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)  # Wait and then attempt to reconnect
        except websockets.exceptions.ConnectionClosedOK:
            logging.info(f"Connection to {endpoint} closed cleanly.")
            break  # Exit the loop if the connection was closed cleanly
        except Exception as e:
            logging.error(f"Unexpected error: {e}. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)

async def main():

    # setup current log file details to use within async code 
    current_date = datetime.now(timezone.utc).strftime('%Y%m%d')
    log_filename = f"log/client.{current_date}.log"

    # 
    # setup basic file  logging config
    # 
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,  # Log level set to INFO; adjust as needed
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.info("Configured Logger using file '{log_filename}' level '{logging.INFO}'")

    # 
    # define message types to monitor
    # see https://power-trade.github.io/api-docs-source/ws_feeds.html#_hosts for WS specifications
    #
    endpoints = [
        "wss://api.wss.prod.power.trade/v1/feeds?type[]=top_of_book"
        #"wss://api.wss.prod.power.trade/v1/feeds?type[]=reference_price",
        #"wss://api.wss.prod.power.trade/v1/feeds?type[]=last_trade_price"
    ]
    
    # Create a task for each WebSocket connection
    tasks = [listen_to_endpoint(endpoint) for endpoint in endpoints]
    
    # Run all tasks concurrently
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # 
    # load reference data on tradeable products 
    # enables translation from entity id ("1234") to product name ("ETH-20241003-2800C")
    # 
    ref_data_filename = "data/ref_data.json"
    ref_data = load_ref_data(ref_data_filename)
    print(f"loaded {len(ref_data)} tradeable entity records from {ref_data_filename}")
    asyncio.run(main())
