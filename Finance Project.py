#Visualizing the impact of the financial crisis on US banking sector stocks

from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import cufflinks as cf
cf.go_offline()

bank_stocks = pd.read_pickle(r'C:\Users\Admin\Desktop\Programming\Python Data Science\Refactored_Py_DS_ML_Bootcamp-master\10-Data-Capstone-Projects\all_banks')
bank_stocks.head()

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()
returns = pd.DataFrame()
for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]['Close'].pct_change()

returns.head()

returns.loc['2015-01-01':'2015-12-31'].std()

sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MS Return'],color='green',bins=100)
sns.distplot(returns.loc['2008-01-01':'2008-12-31']['C Return'],color='red',bins=100)
# plot the closing price for all of the tickers using matplotlib

for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()
#using plotly
bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()

#Moving averages -> use .rolling() and pass in window=30 for 30 days then .mean() for average

plt.figure(figsize=(12,6))

bank_stocks['BAC']['Close'].loc['2008-01-01':'2008-12-31'].rolling(window=30).mean().plot(label='30 Day Avg')
bank_stocks['BAC']['Close'].loc['2008-01-01':'2008-12-31'].plot(label='BAC CLOSE')
plt.legend()

#heatmap of correlation between stocks closing price , use .xs to get multiindex cross section (since bank_stocks uses multi-level index)

sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)


sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)


# Candle plot using .iplot()
bank_stocks['BAC'][['Open', 'High', 'Low', 'Close']].loc['2015-01-01':'2016-01-01'].iplot(kind='candle')

# Simple moving Averages (SMA) plot for a stock (Morgan Stanley) for time period -> using .ta_plot(study='sma')

bank_stocks['MS'][['Close']].loc['2015-01-01':'2016-01-01'].ta_plot(study='sma')


# Create bollinger band plot for BoA yr 2015 -> captures 2 standard deviations of the price movement and measures volatility

bank_stocks['BAC'][['Close']].loc['2015-01-01':'2016-01-01'].ta_plot(study='boll')





















|
