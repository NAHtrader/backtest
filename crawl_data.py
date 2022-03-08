from operator import index, le
import pandas as pd

import get
import indicator

tickers = ['KRW-BTC', 'KRW-ETH', 'KRW-NEO','KRW-LTC', 'KRW-XRP', 'KRW-ETC','KRW-QTUM','KRW-DOT', 'KRW-EOS', 'KRW-XLM']
intervals = ["minute60"]
counts = [18000]

maLists = [192, 48, 24]


for i in range(len(tickers)):
    data = get.get_data(tickers[i],counts[0],intervals[0])
    for j in range(len(maLists)):
        ma = indicator.MA(data, maLists[j])
        data['{}MA'.format(maLists[j])] = ma
    atr = indicator.ATR(data,24)  
    data['24ATR'] = atr
    data.to_excel('./testdata/{}_minute60.xlsx'.format(tickers[i]),index=True)
    print("{} finish".format(tickers[i]))
    
    