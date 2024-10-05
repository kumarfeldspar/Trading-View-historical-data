import os
from tvDatafeed import TvDatafeed, Interval
import pandas as pd
from dotenv import load_dotenv

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
tv = TvDatafeed(username, password)
stockData = tv.get_hist(symbol='ZOMATO',exchange='NSE',interval=Interval.in_5_minute,n_bars=100000)
df=pd.DataFrame(stockData)
df.to_csv('zomato.csv',index=True)
print(stockData)
