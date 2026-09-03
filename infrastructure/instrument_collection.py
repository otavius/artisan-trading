import json
from db.db import DataDB
from models.instruments import Instrument
class InstrumentCollection:
    FILENAME = "instruments.json"
    API_KEYS = ['name', 'type', 'displayName', 'pipLocation', 'displayPrecision', 'tradeUnitsPrecision', 'minimumTradeSize','marginRate']

    def __init__(self):
        self.instruments_dict = {}

    def load_instruments(self, path):
        self.instruments_dict = {}
        file_name = f"{path}/{self.FILENAME}"
        with open(file_name, "r") as f:
            data = json.loads(f.read())
            for k, v in data.items():
                self.instruments_dict[k] = Instrument.fromApiObject(v)

    def load_instrumentsDB(self):
        self.instruments_dict = {}
        data = DataDB().query_single(DataDB.INSTRUMENT_COLL)
        for k, v in data.items():
            self.instruments_dict[k] = Instrument.fromApiObject(v)

    def create_file(self, data, path):
        if data is None:
            print("Instrument file creation failed")
            return 
        
        instrument_dict = {}
        for i in data:
            key = i["name"]
            instrument_dict[key] = {k: i[k] for k in self.API_KEYS}
        file_name = f"{path}/{self.FILENAME}"
        with open(file_name, "w") as f:
            f.write(json.dumps(instrument_dict, indent=2))


    def create_db(self, data):
        if data is None:
            print("Instrument file creation failed")
            return 
        
        instrument_dict = {}
        for i in data:
            key = i["name"]
            instrument_dict[key] = {k: i[k] for k in self.API_KEYS}
        
        database = DataDB()
        database.delete_many(DataDB.INSTRUMENT_COLL)
        database.add_one(DataDB.INSTRUMENT_COLL, instrument_dict)



    def print_instruments(self):
        [print(k, v) for k, v in self.instruments_dict.items()]
        print(len(self.instruments_dict.keys()), "instruments")

instrumentCollection = InstrumentCollection()