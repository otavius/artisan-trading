from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from simulation.ma_cross import run_ma_sim
from dateutil import parser
from infrastructure.collect_data import run_collection

if __name__ == "__main__":
    oanda_api = OandaApi()

    # dfr = parser.parse("2021-01-01T01:00:00Z")
    # dto = parser.parse("2021-01-28T16:00:00Z")

    # df_candles = oanda_api.get_candles_df("EUR_USD", granularity="H1", date_f=dfr, date_t=dto)
   

    # print(oanda_api.fetch_candles("EUR_USD", granularity="D", price="MBA"))

    # instrumentCollection.create_file(oanda_api.get_account_instruments(), "./data")

    # data = oanda_api.get_account_summary()
    #[print(x["name"]) for x in data] 
    #print(data)
    #instrumentCollection.load_instruments("./data")
    #instrumentCollection.print_instruments()
    run_ma_sim()
    #run_collection(instrumentCollection, oanda_api)