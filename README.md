# Equity-Data-Scraper

Web scraper that stores fundamental stock data, analyst estimates, and earnings surprises as .pkl and/or .csv


### Prerequisites

$ pip install pandas

$ pip install beautifulsoup4


### Usage
```
import data_scraper as ds

#initialize list of tickers to get data for
tickers = ['OSUR', 'COHR', 'ENTG', 'HSKA', 'FIVE', 'MDSO', 'LOPE', 'MBUU', 'OLLI', 'TRU']

#this will store all the data as .pkl and .csv files in ./equity data [date]/
ds.get_data(tickers, pkl=True, csv=True)
```
Thats it!  Please be sure to keep the time.sleep(1) between scrapes so that the web host doesn't ban
you from the site.  This code can easily be modified to store in a database as well.

## Authors

* **James Whiteley IV** 

