from pandas_datareader import data as pdr
from datetime import *
import yfinance as yf
from os import mkdir, getcwd
cwd = getcwd()
print(cwd)
# yf.pdr_override()
import pandas as pd
def week_open(array_like):
    return array_like[0]

def week_close(array_like):
    return array_like[-1]
stocks = open("stocks.txt", "r").read()
stocks = stocks.split("\n")
print(stocks)
ticker_list=stocks
stocks = {}

for stockname in ticker_list:
    stocks[stockname.upper()] = yf.Ticker(stockname.upper())
    stockdata = stocks[stockname.upper()].history(period="max")
    # print(stockdata)
    # stockdata.to_csv(f'/data/{stockname.upper()}.csv')
    # stockdata.to_csv('data.zip',\
    #     index=False, \
    #     compression=dict(\
    #         method='zip', archive_name=f"data/{stockname.upper()}.csv"\
    #     )\
    # )
    try:
        stockdata.to_csv(f"data/{stockname.upper()}.csv",\
            index=False, \
            # compression=dict(\
                # method='zip', archive_name=f"data/{stockname.upper()}.csv"\
            # )\
        )
    except FileNotFoundError:
        mkdir(f"{cwd}/data")
        stockdata.to_csv(f"data/{stockname.upper()}.csv",\
            index=False, \
            # compression=dict(\
                # method='zip', archive_name=f"data/{stockname.upper()}.csv"\
            # )\
        )
    stockdata = stockdata.to_dict()
    # print(stockdata['row1'])