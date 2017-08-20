Equity Data Scraper
===================

Web scraper that stores fundamental stock data, analyst estimates, and earnings surprises as .pkl and/or .csv

Installation
------------

To install Equity Data Scraper from PyPI:

.. code-block:: bash

  $ pip install equityscraper 

From git repo:

.. code-block:: bash

  $ git clone https://github.com/JamesWhiteleyIV/Equity-Data-Web-Scraper.git
  $ cd Equity-Data-Web-Scraper 
  $ python setup.py install


Documentation
-------------

.. code:: python

  import equityscraper as scrape

  #initialize list of tickers to get data for
  tickers = ['OSUR', 'COHR', 'ENTG', 'HSKA', 'FIVE', 'MDSO', 'LOPE', 'MBUU', 'OLLI', 'TRU']

  #this will store all the data as .pkl and .csv files in ./equity data [date]/
  scrape.get_data(tickers, pkl=True, csv=True)



Thats it!  Please be sure to keep the time.sleep(1) between scrapes so that the web host doesn't ban
you from the site.  This code can easily be modified to store in a database as well.


Authors
-------

**James Whiteley IV** 

