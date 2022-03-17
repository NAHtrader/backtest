from matplotlib.pyplot import box
import pandas as pd

import indicator

tickers = ['KRW-BTC', 'KRW-ETH','KRW-XRP', 'KRW-ETC','KRW-DOT', 'KRW-EOS']

for ticker in tickers:
    df = pd.read_excel('./testdata/min240/{}_minute240.xlsx'.format(ticker))
    df['192MA'] = indicator.MA(df,192)
    df['24MA'] = indicator.MA(df,24)
    df['48MA'] = indicator.MA(df,48)
    df['24ATR'] = indicator.ATR(df,24)

    df.to_excel('./testdata/edit/min240/{}_min240e.xlsx'.format(ticker),index=False)