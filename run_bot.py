#from bot.bot import Bot 
from infrastructure.instrument_collection import instrumentCollection
from stream_bot.stream_bot import run_bot

if __name__ == "__main__":
    instrumentCollection.load_instruments("./data")
    #bot = Bot()
    #bot.run()
    run_bot()