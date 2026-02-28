from dateutil import parser 
from models.base_api_price import BaseApiPrice


class LiveApiPrice(BaseApiPrice):

    def __init__(self, api_object):
        super().__init__(api_object)
        self.time = parser.parse(api_object["time"])
        



    def __repr__(self):
        return f"LiveApiPrice {self.instrument} {self.ask} {self.bid} {self.time}"

    def get_dict(self):
        return dict(
            instrument=self.instrument,
            time = self.time,
            ask = self.ask,
            bid=self.bid
        )