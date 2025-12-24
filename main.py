from api.stream_prices import stream_prices
from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from simulation.ma_cross import run_ma_sim
from dateutil import parser
from infrastructure.collect_data import run_collection
from simulation.ema_macd_mp import run_ema_macd

if __name__ == "__main__":
    oanda_api = OandaApi()
    instrumentCollection.load_instruments("./data")
    stream_prices(["GBP_JPY", "EUR_USD"])
