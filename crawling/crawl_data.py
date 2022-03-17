from operator import index, le
import pandas as pd
import os

import get
import indicator

tickers = ['KRW-BTC', 'KRW-ETH','KRW-XRP', 'KRW-ETC','KRW-DOT', 'KRW-EOS']
intervals = ["minute15"]
counts = [71000]

# maLists = [360, 60]
# atrLists = [60,30]
interval_number = intervals[0][6:]
os.makedirs('./testdata/min{}'.format(interval_number),exist_ok=True)

for i in range(len(tickers)):
    data = get.get_data(tickers[i],counts[0],intervals[0])
    # for j in range(len(maLists)):
    #     ma = indicator.MA(data, maLists[j])
    #     data['{}MA'.format(maLists[j])] = ma
    # for k in range(len(atrLists)):
    #     atr = indicator.ATR(data,atrLists[k])  
    #     data['{}ATR'.format(atrLists[k])] = atr
    delta = indicator.delta(data)
    data['delta'] = delta
    data.to_excel('./testdata/min{}/{}_{}.xlsx'.format(interval_number,tickers[i],intervals[0]),index=True)
    print("{} finish".format(tickers[i]))
    
    