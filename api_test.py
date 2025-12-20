from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from models.candle_timing import CandleTiming
from simulation.ma_cross import run_ma_sim
from dateutil import parser
from infrastructure.collect_data import run_collection
from simulation.ema_macd_mp import run_ema_macd
import time


if __name__ == "__main__":
    oanda_api = OandaApi()

    instrumentCollection.load_instruments("./data")
    # dd = oanda_api.last_complete_candle("EUR_USD", granularity="M5")
    # print(CandleTiming(dd))
    print(oanda_api.get_prices(["GBP_USD", "EUR_USD"]))