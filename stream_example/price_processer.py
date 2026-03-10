import copy
from queue import Queue

import threading
import time 
from stream_example.stream_base import StreamBase

class PriceProcessor(StreamBase):

    def __init__(self, shared_prices, price_lock: threading.Lock, price_events, logname, pair):
        super().__init__(shared_prices, price_lock, price_events, logname)
        self.pair = pair


    def process_price(self):

        try:
            self.price_lock.acquire()
            price = copy.deepcopy(self.shared_prices[self.pair])
            print("PriceProcessor: ", price)
        except Exception as error:
            self.log_message("CRASH: {error}", error=True)
        finally: 
            self.price_lock.release()


    def run(self):
        while True:
            self.price_events[self.pair].wait()
            self.process_price()
            self.price_events[self.pair].clear()



