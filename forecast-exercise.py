%matplotlib inline
import pandas as pd
data = pd.read_csv("IPG2211A2N.csv",index_col=0)
data.head()


data.reset_index(inplace=True)
data['Date'] = pd.to_datetime(data['DATE'])
data = data.set_index('Date')
data = data.dropna(how='any',axis=0) 

#https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/
import pandas as pd
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose
data = Series.from_csv('IPG2211A2N.csv', header=0)
result = seasonal_decompose(data, model='multiplicative')
result.plot()
pyplot.show()

import plotly
# plotly.tools.set_credentials_file()
from plotly.plotly import plot_mpl
from statsmodels.tsa.seasonal import seasonal_decompose

result=sm.tsa.seasonal_decompose(data)

result = seasonal_decompose(data, model='multiplicative')
fig = result.plot()
plot_mpl(fig)

#pip install pyramid-arima
from pyramid.arima import auto_arima

#m greater is much great m=1000 is good
stepwise_model = auto_arima(data, start_p=1, start_q=1,
                           max_p=1, max_q=1, m=3,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)

stepwise_model.aic()

train = data.loc['1985-01-01':'2016-12-01']

test = data.loc['2015-01-01':]

stepwise_model.fit(train)

future_forecast = stepwise_model.predict(n_periods=43)

future_forecast = pd.DataFrame(future_forecast,index = test.index,columns=['Prediction'])

future_forecast.head()

pd.concat([test,future_forecast],axis=1).iplot()

#future_forecast2 = future_forcast
#pd.concat([data,future_forecast2],axis=1).iplot()

b = pd.concat([data,future_forecast2],axis=1)

b.plot()
pyplot.show()

#https://www.kaggle.com/cgaydon/forecasting-product-demand-with-simple-models
