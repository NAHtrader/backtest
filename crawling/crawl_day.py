from operator import index, le
import pandas as pd
import os

import get
import indicator

tickers = ['KRW-BTC', 'KRW-ETH','KRW-XRP', 'KRW-ETC','KRW-DOT', 'KRW-EOS']
intervals = ["day"]
counts = [735]

maLists = [25, 5]
# atrLists = [60,30]

os.makedirs('./testdata/{}'.format(intervals[0]),exist_ok=True)

for i in range(len(tickers)):
    data = get.get_data(tickers[i],counts[0],intervals[0])
    for j in range(len(maLists)):
        ma = indicator.MA(data, maLists[j])
        data['{}MA'.format(maLists[j])] = ma
    # for k in range(len(atrLists)):
    #     atr = indicator.ATR(data,atrLists[k])  
    #     data['{}ATR'.format(atrLists[k])] = atr
    delta = indicator.delta(data)
    data['delta'] = delta
    data.to_excel('./testdata/{}/{}_{}.xlsx'.format(intervals[0],tickers[i],intervals[0]),index=True)
    print("{} finish".format(tickers[i]))
    
    