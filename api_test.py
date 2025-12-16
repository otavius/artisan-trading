from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from simulation.ma_cross import run_ma_sim
from dateutil import parser
from infrastructure.collect_data import run_collection
from simulation.ema_macd_mp import run_ema_macd
import time


if __name__ == "__main__":
    oanda_api = OandaApi()

    instrumentCollection.load_instruments("./data")
    #trade_id = oanda_api.place_trade("EUR_USD", 100, 1)
    #print("Opened", trade_id)
    #time.sleep(10)
    print(f"Closing {76}", oanda_api.close_trade(76))
    time.sleep(8)
    [print(x) for x in oanda_api.get_open_trades()]