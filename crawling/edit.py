from matplotlib.pyplot import box
import pandas as pd

import indicator

tickers = ['KRW-BTC', 'KRW-ETH','KRW-XRP', 'KRW-ETC','KRW-DOT', 'KRW-EOS']

for ticker in tickers:
    df = pd.read_excel('./testdata/min3/{}_minute3.xlsx'.format(ticker))
    df2 = pd.read_excel('./testdata/day/{}_day.xlsx'.format(ticker))
    Date = {}
    for d in range(len(df2)):
        Date['{}'.format(str(df2.iloc[d,0])[0:10])] = [df2.iloc[d,1], df2.iloc[d,9], df2.iloc[d,7], df2.iloc[d,8]]
    df['target'] = 0
    df['delta'] = 0
    df['25MA_d'] = 0
    df['5MA_d'] = 0

    for l in range(len(df)): 
        current_date = str(df.iloc[l,0])[0:10]
        print(current_date)
        if current_date in list(Date.keys()):
            df['target'].loc[l] = Date['{}'.format(current_date)][0]
            df['delta'].loc[l] = Date['{}'.format(current_date)][1]
            df['25MA_d'].loc[l] = Date['{}'.format(current_date)][2]
            df['5MA_d'].loc[l] = Date['{}'.format(current_date)][3]
        else:
            continue

    df.to_excel('./testdata/edit/min3/{}_min3e1.xlsx'.format(ticker),index=False)