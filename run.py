import imp
import pandas as pd

import evaluation
import backtest

bid_const = [3.5,3.75,4,4.25,4.5,4.75,5]
ask_const = [1, 1.25, 1.5, 1.75,2,2.25,2.5]

tickers = ['KRW-BTC', 'KRW-ETH', 'KRW-NEO','KRW-LTC', 'KRW-XRP', 'KRW-ETC','KRW-QTUM','KRW-DOT', 'KRW-EOS', 'KRW-XLM']

for b in range(len(bid_const)):
    for a in range(len(ask_const)):
        backtest.backtest(bid_const[b],ask_const[a],tickers)

df = pd.DataFrame()
total = []

for b in range(len(bid_const)):
    for a in range(len(ask_const)):
        df, total = evaluation.evaluate(bid_const[b],ask_const[a],tickers,df,total)

df.to_excel('./testdata/evaluation.xlsx',index=False)

total_df = pd.DataFrame(total,columns=['bid const','ask const','ticker','trade_number','win_rate','Max impairment','Profit Perc'])
total_df.to_excel('./testdata/total_evaluation.xlsx',index=False)