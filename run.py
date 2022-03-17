import pandas as pd

import evaluation
from system import backtest

system_name = "sys5" 
interval = "minute60"

bid_const = [4,5]
ask_const = [1,2]
# loss_const = [0.98, 0.99, 0.995]

tickers = ['KRW-BTC', 'KRW-ETH','KRW-XRP', 'KRW-ETC','KRW-DOT', 'KRW-EOS']

for b in range(len(bid_const)):
    for a in range(len(ask_const)):
        # for l in range(len(loss_const)):
        # backtest.backtest(bid_const[b],ask_const[a],loss_const[l],tickers,interval,system_name)
        backtest.backtest(bid_const[b],ask_const[a],tickers,interval,system_name)
  
df = pd.DataFrame()
total = []

for b in range(len(bid_const)):
    for a in range(len(ask_const)):
        # for l in range(len(loss_const)):
        #     df, total = evaluation.evaluate(bid_const[b],ask_const[a],loss_const[l],tickers,df,total,interval,system_name)
        df, total = evaluation.evaluate(bid_const[b],ask_const[a],tickers,df,total,interval,system_name)

df.to_excel('./testdata/{}/{}/every_evaluation_{}.xlsx'.format(interval,system_name,system_name),index=False)

total_df = pd.DataFrame(total,columns=['bid const','ask const','ticker','trade_number','win_rate','Max impairment','Profit Perc'])
total_df.to_excel('./testdata/{}/{}/avg_evaluation_{}.xlsx'.format(interval,system_name,system_name),index=False)

# 파일명 까지 전부 여기서 관리하게 바꿔놓을 것!!!1