from api.oanda_api import OandaApi
from infratstructure.instrument_collection import instrumentCollection
if __name__ == "__main__":
    oanda_api = OandaApi()

    instrumentCollection.create_file(oanda_api.get_account_instruments(), "./data")

    data = oanda_api.get_account_summary()
    #[print(x["name"]) for x in data] 
    #print(data)
    #instrumentCollection.load_instruments("./data")
    #instrumentCollection.print_instruments()
