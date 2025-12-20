
class ApiPrice:

    def __init__(self, api_object):
        self.instrument = api_object["instrument"]
        self.ask = float(api_object["asks"][0]["price"])
        self.bid = float(api_object["bids"][0]["price"])
        self.sell_conv = float(api_object["quoteHomeConversionFactors"]["negativeUnits"])
        self.buy_conv = float(api_object["quoteHomeConversionFactors"]["positiveUnits"])

    def __repr__(self):
        return f"ApiPrice {self.instrument} {self.ask} {self.bid} {self.sell_conv:.6f} {self.buy_conv:.6f}"
