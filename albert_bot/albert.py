import json 
import time 

from api.oanda_api import OandaApi
import defs.constants as defs 
from models.trade_settings import TradeSettings
from infrastructure.log_wrapper import LogWrapper
from albert_bot.candle_manager import CandleManager

class AlbertBot: 

    ERROR_LOG = "error"
    MAIN_LOG = "main"
    GRANULARITY = "M30"
    SLEEP = 10 

    def __inti__(self):
        self.setup_logs()
        self.load_settings()
        self.api = OandaApi()
        self.candle_manager = CandleManager(self.api, self.trade_settings, self.log_message, AlbertBot.GRANULARITY)
        self.log_to_main("Bot started")
        self.log_to_error("Bot started")



    def load_settingsab(self):
        with open("./albert_bot/settings.json", "r") as f:
            data = json.loads(f.read())
            self.trade_settings = {k : TradeSettings(v, k) for k, v in data["pairs"].items()}
            self.trade_risk = data["trade_risk"]

    def setup_logs(self):
        self.logs = {}
        for k in self.trade_settings.keys():
            self.logs[k] = LogWrapper(k)
            self.log_message(f"{self.trade_settings[k]}", k)
        self.logs[AlbertBot.ERROR_LOG] = LogWrapper(AlbertBot.ERROR_LOG)
        self.logs[AlbertBot.MAIN_LOG] = LogWrapper(AlbertBot.MAIN_LOG)
        self.log_to_main(f"Bot started with {TradeSettings.settings_to_string(self.trade_settings)}")

    def log_message(self, msg, key):
        self.logs[key].logger.debug(msg)

    def log_to_main(self, msg):
        self.log_message(msg, AlbertBot.MAIN_LOG)

    def log_to_error(self, msg):
        self.log_message(msg, AlbertBot.ERROR_LOG)

    def process_candle(self, triggered):
        if len(triggered) > 0:
            self.log_message(f"process_candles triggered: {triggered}", AlbertBot.MAIN_LOG)
            for p in triggered:
                last_time = self.candle_manager.timings[p].last_time
                trade_decision  = get_
