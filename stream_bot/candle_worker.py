

from queue import Queue
import threading
import datetime as dt
import time

from api.oanda_api import OandaApi
from infrastructure.log_wrapper import LogWrapper
from models.trade_settings import TradeSettings


class CandleWorker(threading.Thread):

    def __init__(self, trade_settings: TradeSettings,
                 candle_work: Queue, 
                 granularity: str):
        super().__init__()
        self.trade_settings = trade_settings
        self.candle_work = candle_work
        self.granularity = granularity

        self.log = LogWrapper(f"CandleWorker_{trade_settings.pair}")
        self.api = OandaApi()
        self.log_message(f"Created CandleWorker for {trade_settings.pair} {trade_settings}")

    def log_message(self, msg, error=False):
        if error == True:
            self.log.logger.error(msg)
        else: 
            self.log.logger.debug(msg)

    def run_analysis(self, expected_time: dt.datetime):
        attempts = 0 
        tries = 5 

        try:
            while attempts < tries:
                candles = self.api.get_candles_df(
                    self.trade_settings.pair,
                    granularity=self.granularity,
                    count=50
                )

                if candles.shape[0] == 0:
                    print("No Candles")
                elif candles.iloc[-1].time != expected_time:
                    print("No New CANDLES")
                    time.sleep(0.5)
                else: 
                    print(candles.tail())
                    break

                attempts += 1   
        except Exception as error:
            self.log_message(f"Exception: {error}", error=True)

    def run(self):
        while True:
            candle_time: dt.datetime = self.candle_work.get()
            print(f"CandleWorker new candle : {candle_time} {self.trade_settings.pair}")
            self.run_analysis(candle_time)

