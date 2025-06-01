import pandas as pd 
from infratstructure.instrument_collection import instrumentCollection as ic 

BUY = 1 
SELL = -1 
NONE = 0 
get_ma_col = lambda x: f"MA_{x}"

def is_trade(row):
    if row.DELTA >= 0 and row.DELTA_PREV < 0:
        return BUY
    elif row.DELTA < 0 and row.DELTA_PREV >= 0:
        return SELL
    return NONE

def load_price_data(pair, granularity, ma_list):
    df = pd.read_pickle(f"./data/{pair}_{granularity}.pkl")
    for ma in ma_list:
        df[get_ma_col(ma)] = df.mid_c.rolling(window=ma).mean()
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df 

def assess_pair(price_data, ma_l, ma_s, pair):
    df_analysis = price_data.copy()
    df_analysis["DELTA"] = df_analysis[ma_s] - df_analysis[ma_l]
    df_analysis["DELTA_PREV"] = df_analysis["DELTA"].shift(1)
    df_analysis["TRADE"] = df_analysis.apply(is_trade, axis=1)
    print(pair, ma_l,ma_s)
    print(df_analysis.head(3))
    return None

def analyse_pair(pair, granularity, ma_long, ma_short):
    ma_list = set(ma_long + ma_short)
    pair = pair.name 
    price_data = load_price_data(pair, granularity, ma_list)
    print(pair)
    print(price_data.head(3))

    for ma_l in ma_long:
        for ma_s in ma_short:
            if ma_l <= ma_s:
                continue

            result = assess_pair(
                price_data,
                get_ma_col(ma_l),
                get_ma_col(ma_s),
                pair
            )


def run_ma_sim(pair_list=["EUR", "USD", "CHF", "JPY"],
               granularity=["H1"],
               ma_long=[50, 200],
               ma_short=[10,20]):
    ic.load_instruments("./data")
    for g in granularity:
        for p1 in pair_list:
            for p2 in pair_list:
                pair = f"{p1}_{p2}"
                if pair in ic.instruments_dict.keys():
                    analyse_pair(ic.instruments_dict[pair], g, ma_long, ma_short)