import copy
from queue import Queue
import threading

import pytz
from models.live_api_price import LiveApiPrice
from stream_example.stream_base import StreamBase
import datetime as dt

GRANULARITIES = {
    "M1": 1,
    "M5": 5, 
    "M15": 15,
    "M30": 30,
    "H1": 60,
}

class PriceProcessor(StreamBase):

    def __init__(self, shared_prices, price_lock: threading.Lock, price_events, logname, pair, granularity):
        super().__init__(shared_prices, price_lock, price_events, logname)
        self.pair = pair
        self.granularity = GRANULARITIES[granularity]

        now = dt.datetime.now(pytz.timezone("UTC"))
        self.set_last_candle(now)
        print(f"PriceProcessor: {self.last_complete_candle_time} {now}")

    
    def round_time_down(self, round_me: dt.datetime) -> dt.datetime:
        remainder = round_me.minute % self.granularity
        candle_time = dt.datetime(round_me.year, round_me.month, round_me.day, round_me.hour, round_me.minute - remainder, tzinfo=pytz.timezone("UTC"))
        return candle_time
    
    def set_last_candle(self, price_time: dt.datetime):
        self.last_complete_candle_time = self.round_time_down(
            price_time - dt.timedelta(minutes=self.granularity)
        )

    def detect_new_candle(self, price: LiveApiPrice):
        old = self.last_complete_candle_time
        self.set_last_candle(price.time)
        if old < self.last_complete_candle_time:
            msg = f"--->>>>> {self.pair} New candle : {self.last_complete_candle_time} {price.time}"
            print(msg)

    def process_price(self):

        try:
            self.price_lock.acquire()
            price: LiveApiPrice = copy.deepcopy(self.shared_prices[self.pair])
            #print("PriceProcessor: ", price)
            if price is not None:
                self.detect_new_candle(price)
        except Exception as error:
            self.log_message("CRASH: {error}", error=True)
        finally: 
            self.price_lock.release()


    def run(self):
        while True:
            self.price_events[self.pair].wait()
            self.process_price()
            self.price_events[self.pair].clear()



