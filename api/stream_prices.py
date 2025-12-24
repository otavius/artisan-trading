import json
import requests
import defs.constants as defs 
from decouple import config

STREAM_URL = f"https://stream-fxpractice.oanda.com/v3"

def stream_prices(symbols):

    params = dict(
        instruments=",".join(symbols)
    )

    url = f"{STREAM_URL}/accounts/{config("ACCOUNT_ID")}/pricing/stream"

    response = requests.get(url, params=params, headers=defs.SECURE_HEADER, stream=True)

    for price in response.iter_lines():
        if price:
            decoded_price = json.loads(price.decode('utf-8'))
            print(decoded_price)
            print()