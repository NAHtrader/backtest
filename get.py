import pyupbit

def get_data(ticker,count,interval):
    df = pyupbit.get_ohlcv(ticker,count=count,interval=interval)
    return df