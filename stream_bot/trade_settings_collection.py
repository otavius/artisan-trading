import os 


import json
from time import time
import threading

from models.trade_settings import TradeSettings
FILENAME = "settings.json"



class TradeSettingsCollection:

    FILENAME = "settings.json"

    def __init__(self):
        self.trade_settings_dict = {}
        self.granularity = "M1"
        self.trade_risk = 1.0 
        self.setting_path = f"./stream_bot/{self.FILENAME}"
        self.lock = threading.Lock()

    # def load_trade_settings(self):
    #     self.trade_settings_dict = {}
    #     filename = self.setting_path
    #     with open(filename, "r") as f:
    #         data = json.loads(f.read())
    #         self.granularity = data["granularity"]
    #         self.trade_risk = data["trade_risk"]
    #         for pair, pair_settings in data["pairs"].items():
    #             self.trade_settings_dict[pair] = TradeSettings(pair_settings, pair)

    def load_trade_settings(self):
        filename = self.setting_path
        with open(filename, "r") as f: 
            data = json.loads(f.read())

        new_settings_dict = {}
        for pair, pair_settings in data["pairs"].items():
            new_settings_dict[pair] = TradeSettings(pair_settings, pair)

        with self.lock: 
            self.granularity = data["granularity"]
            self.trade_risk = data["trade_risk"]
            self.trade_settings_dict = new_settings_dict

    def watch_trade_settings(self):
        self.last_mtime = os.path.getmtime(self.setting_path)
        while True: 
            time.sleep(10)
            current_mtime = os.path.getmtime(self.setting_path)
            if current_mtime != self.last_mtime:
                try:
                    self.load_trade_settings()
                    self.last_mtime = current_mtime
                    print(f"Trade settings reloaded at {time.time()}")
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error loading trade settings: {e}")
                

    def print_collection(self):
        print(f"Granularity: {self.granularity}")
        print(f"Trade Risk: {self.trade_risk}")
        [print(f"{k} : {v}") for k, v in self.trade_settings_dict.items()]

    def pair_list(self)-> list:
        return list(self.trade_settings_dict.keys())
    
    def get_trade_settings(self, pair: str) -> TradeSettings:
        with self.lock:
            return self.trade_settings_dict[pair]

tradeSettingCollection = TradeSettingsCollection()
