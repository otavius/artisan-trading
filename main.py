
from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from dateutil import parser
from stream_example.streamer import run_streamer
from db.db import DataDB

def db_tests():
    d = DataDB()
    #d.add_one(DataDB.SAMPLE_COLL, dict(age=12, name="fred", eyes="blue"))
    print(d.query_distinct(DataDB.SAMPLE_COLL, 'age'))

if __name__ == "__main__":
    # oanda_api = OandaApi()
    # instrumentCollection.load_instruments("./data")
    # run_streamer()
    d = DataDB()
    #d.test_connect()
    db_tests()


