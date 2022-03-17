from operator import le
from matplotlib import ticker
import pandas as pd

def evaluate(bid_const,ask_const,loss_const,tickers,df,total, interval, sys_name):
    df = df
    bid_const = bid_const
    ask_const = ask_const

    tickers = tickers
    interval_number = interval[3:]
    box = []
    for i in range(len(tickers)):
        xlsx = pd.read_excel('./testdata/{}/{}/log/B{}A{}L{}/{}_minute{}_{}_{}_{}_{}.xlsx'.format(interval,sys_name,bid_const,ask_const,loss_const,tickers[i],interval_number,sys_name,bid_const,ask_const,loss_const))
        trade_number = len(xlsx)
        win_number = 0
        for j in range(len(xlsx)):
            if xlsx.iloc[j,4]<xlsx.iloc[j,5]:
                win_number += 1
        win_rate = win_number/trade_number*100
        impairment = min(xlsx['balance'])/1000000*100
        profit_perc = (xlsx.iloc[len(xlsx)-1,7]/1000000 - 1)*100
        evaluation = [bid_const, ask_const ,tickers[i],trade_number,win_rate,impairment,profit_perc]
        box.append(evaluation)

    if len(df.index) == 0:
        df1 = pd.DataFrame(box,columns=['bid const','ask const','ticker','trade_number','win_rate','Max impairment','Profit Perc'])
        avg_trade_num = df1['trade_number'].mean()
        avg_win_rate = df1['win_rate'].mean()
        avg_impair = df1['Max impairment'].mean()
        avg_profit_per = df1['Profit Perc'].mean()
        avg_box = [bid_const,ask_const,"Average",avg_trade_num,avg_win_rate,avg_impair,avg_profit_per]
        df1.loc[len(df1)] = avg_box
        total.append(avg_box)
        df = df1
    else:
        df2 = pd.DataFrame(box,columns=['bid const','ask const','ticker','trade_number','win_rate','Max impairment','Profit Perc'])
        avg_trade_num = df2['trade_number'].mean()
        avg_win_rate = df2['win_rate'].mean()
        avg_impair = df2['Max impairment'].mean()
        avg_profit_per = df2['Profit Perc'].mean()
        avg_box = [bid_const,ask_const,"Average",avg_trade_num,avg_win_rate,avg_impair,avg_profit_per]
        df2.loc[len(df2)] = avg_box
        total.append(avg_box)
        df = pd.concat([df,df2])
    return df, total;