import pandas
import pandas_datareader.data as web

import datetime
start = datetime.datetime(2002, 11, 1)
end = datetime.datetime(2003,9,1)
gdp = web.DataReader('GDP','fred',start, end)

gdp.loc['2003-01-01']

inflation = web.DataReader(['CPIAUCSL','CPILFESL'],'fred',start,end)
inflation.head(10)




