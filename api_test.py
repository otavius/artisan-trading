from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from models.candle_timing import CandleTiming
from simulation.ma_cross import run_ma_sim
from dateutil import parser
from infrastructure.collect_data import run_collection
from simulation.ema_macd_mp import run_ema_macd
import time
from bot.trade_risk_calculated import get_trade_units
import defs.constants as defs

def lm(msg, pair):
    print(msg, pair)

if __name__ == "__main__":
    oanda_api = OandaApi()

    instrumentCollection.load_instruments("./data")
    # dd = oanda_api.last_complete_candle("EUR_USD", granularity="M5")
    # print(CandleTiming(dd))
    #print(oanda_api.get_prices(["GBP_USD", "EUR_USD"]))
    print(get_trade_units(oanda_api, "AUD_NZD", defs.BUY, 0.005, 30, lm))