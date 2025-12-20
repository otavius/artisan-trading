

from api.oanda_api import OandaApi
from models.trade_decision import TradeDecision


def trade_is_open(pair, api: OandaApi):

    open_trades = api.get_open_trades()

    for ot in open_trades:
        if ot.instrument == pair:
            return ot
        
    return None 

def place_trade(trade_decision: TradeDecision, api: OandaApi, log_message, log_error):
    open_trade = trade_is_open(trade_decision.pair, api)

    if open_trade is not None:
        log_message(f"Failed to place trade {trade_decision}, already open: {open_trade}", trade_decision.pair)
        return None

    trade_id = api.place_trade(
        trade_decision.pair,
        1000, 
        trade_decision.signal,
        trade_decision.sl,
        trade_decision.tp
    )

    if trade_id is not None:
        log_error(f"ERROR placing {trade_decision}")
        log_message(f"Error placing {trade_decision}", trade_decision.pair)
    else:
        log_message(f"placed trade_id {trade_id} for {trade_decision}", trade_decision.pair)
