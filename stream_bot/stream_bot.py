from stream_bot.trade_settings_collection import tradeSettingCollection

def run_bot():
    tradeSettingCollection.load_trade_settings()
    tradeSettingCollection.print_collection()