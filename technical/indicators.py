import pandas as pd 

def BollingerBands(df: pd.DataFrame, n = 20, s= 2):
    typical_price = (df.mid_c + df.mid_h + df.mid_l) / 3 
    stddev = typical_price.rolling(window=n).std()
    df["BB_MA"] = typical_price.rolling(window=n).mean()
    df["BB_UP"] = df["BB_MA"] + stddev * s
    df["BB_LW"] = df["BB_MA"] - stddev * s
    return df

def ATR(df: pd.DataFrame, n=14):
    prev_close = df.mid_c.shift(1)
    true_range_1 = df.mid_h - df.mid_l
    true_range_2 = abs(df.mid_h - prev_close)
    true_range_3 = abs(prev_close - df.mid_l)

    true_range = pd.DataFrame({"tr1": true_range_1, "tr2": true_range_2, "tr3": true_range_3}).max(axis=1)
    df[f"ATR_{n}"] = true_range.rolling(window=n).mean()
    return df

def keltner_channels(df: pd.DataFrame, n_ema=20, n_atr=10):
    df["EMA"] = df.mid_c.ewm(span=n_ema, min_periods=n_ema).mean()
    df = ATR(df, n=n_atr)
    c_atr = f"ATR_{n_atr}"
    df["KeUp"] = df[c_atr] * 2 + df.EMA
    df["KeLo"] = df.EMA - df[c_atr] * 2 
    df.drop(c_atr, axis=1, inplace=True)
    return df

def rsi(df: pd.DataFrame, n=14):
    alpha = 1.0 / n
    gains = df.mid_c.diff()

    wins = pd.Series([x if x >= 0 else 0.0 for x in gains], name="wins")
    losses = pd.Series([x * -1 if x < 0 else 0.0 for x in gains], name="losses")

    wins_rma = wins.ewm(min_periods=n, alpha=alpha).mean()
    losses_rma = losses.ewm(min_periods=n, alpha=alpha).mean()

    rs = wins_rma / losses_rma
    df[f"RSI_{n}"] = 100.0 - (100.0 / (1.0 + rs))
    return df 

def macd(df: pd.DataFrame, n_slow=26, n_fast=12, n_signal=9):
    ema_long = df.mid_c.ewm(min_periods=n_slow, span=n_slow).mean()
    ema_short = df.mid_c.ewm(min_periods=n_fast, span=n_fast).mean()

    df["MACD"] = ema_short - ema_long
    df["SIGNAL"] = df.MACD.ewm(min_periods=n_signal, span=n_signal).mean()
    df["HIST"] = df.MACD - df.SIGNAL
    return df 

