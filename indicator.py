from operator import le
import re
import numpy


def MA(data,ma_period):
    ma = [0]*(ma_period)
    for i in range(ma_period,len(data)):
        mean_data = data['close'].iloc[i-ma_period:i-1].mean()
        ma.append(mean_data)
    return ma

def ATR(data,atr_period):
    atr = [0]*(atr_period+1)
    for i in range(atr_period+1,len(data)):
        True_range_box = []
        for j in range(atr_period):
            TR1 = data['high'].iloc[i-j-1] - data['low'].iloc[i-j-1]
            TR2 = data['high'].iloc[i-j-1] - data['close'].iloc[i-j-2]
            TR3 = data['low'].iloc[i-j-1] - data['close'].iloc[i-j-2]
            True_range = max(TR1, TR2, TR3)
            True_range_box.append(True_range)
        TR = round((numpy.mean(True_range_box)*0.9),2)
        atr.append(TR)
    return atr

def delta(data):
    delta = [0]
    for i in range(1,len(data)):
        if i == len(data)-1:
            d = 0
        else:
            d = data['high'].iloc[i-1] - data['low'].iloc[i-1]
        delta.append(d)
    return delta