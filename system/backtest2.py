from operator import le
from numpy import busday_count
import pandas as pd
from pyparsing import col
import os

def backtest(bid_const, ask_const,loss_const, tickers,interval,sys_name):
    bid_const = bid_const
    ask_const = ask_const

    tickers = tickers
    os.makedirs('./testdata/{}/{}/log/B{}A{}L{}'.format(interval,sys_name,bid_const,ask_const,loss_const),exist_ok=True)
    interval_number = interval[3:]
    for i in range(len(tickers)):
        box = []
        balance = 1000000
        
        # 0 : 구매일 / 1: 판매일 / 2 : 티커 / 3: 포지션 / 4 :구매가격 / 5. 판매가격 /6 : 볼륨 / 7 :총 금액
        pos = False
        Bdate = "0000-00-00"
        Sdate = "0000-00-00"
        ticker = tickers[i]
        Bprice = 0
        Sprice = 0
        volume = 0

        xlsx = pd.read_excel('./testdata/{}/{}_minute{}.xlsx'.format(interval,tickers[i],interval_number))
        xlsx = xlsx.iloc[2:,:]
        for j in range(len(xlsx)):
            if pos == False:
                target_price = xlsx['open'].iloc[j] + (bid_const * xlsx['delta'].iloc[j])
                if (xlsx['high'].iloc[j]>target_price):
                    pos = True
                    Bdate = xlsx.iloc[j,0]
                    Bprice = target_price
                    volume = balance/xlsx.iloc[j,4]
                    
            elif pos == True:
                target_price = Bprice * ask_const
                if (xlsx['high'].iloc[j]>target_price):
                    pos = False
                    Sdate = xlsx.iloc[j,0]
                    Sprice = target_price
                    balance = volume*xlsx.iloc[j,4]
                    current_state = [Bdate,Sdate,ticker,pos,Bprice,Sprice,volume,balance]
                    box.append(current_state)

                elif xlsx['low'].iloc[j]<Bprice*loss_const:
                    pos = False
                    Sdate = xlsx.iloc[j,0]
                    Sprice = xlsx['close'].iloc[j]
                    balance = volume*xlsx.iloc[j,4]
                    current_state = [Bdate,Sdate,ticker,pos,Bprice,Sprice,volume,balance]
                    box.append(current_state)

        df = pd.DataFrame(box,columns=['Bdate','Sdate','ticker','pos','Bprice','Sprice','Volume','balance'])
        df.to_excel('./testdata/{}/{}/log/B{}A{}L{}/{}_minute{}_{}_{}_{}_{}.xlsx'.format(interval,sys_name ,bid_const,ask_const,loss_const,tickers[i],interval_number,sys_name,bid_const,ask_const,loss_const),index=False)
        print("finish {}".format(tickers[i]))

