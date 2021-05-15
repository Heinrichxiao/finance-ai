import yfinance as yf
from os import mkdir, getcwd
cwd = getcwd()
print(cwd)

stocks = open("stocks.txt", "r").read()
stocks = stocks.split("\n")
print(stocks)
ticker_list=stocks
stocks = {}

for stockname in ticker_list:
    stockdata = yf.download(tickers=stockname,\
        period="max",\
        interval="1d",\
        group_by="ticker",\
        auto_adjust=True,\
        prepost=True,\
        threads=True,\
        proxy=None,\
        # start="",\
        # end=""\
    )
    print(stockdata)

    try:
        stockdata.to_csv(f"data/{stockname.upper()}.csv",\
            index=True, \
            # compression=dict(\
                # method='zip', archive_name=f"data/{stockname.upper()}.csv"\
            # )\
        )
    except FileNotFoundError:
        mkdir(f"{cwd}/data")
        stockdata.to_csv(f"data/{stockname.upper()}.csv",\
            index=True, \
            # compression=dict(\
                # method='zip', archive_name=f"data/{stockname.upper()}.csv"\
            # )\
        )