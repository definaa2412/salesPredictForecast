data = read.csv('HistoricalProductDemand.csv')

data = ts(data[,5],start = c(2012,1),frequency = 12)
#plot(data, xlab='Years', ylab = 'Tractor Sales')

require(forecast)
ARIMAfit = auto.arima(log10(data), approximation=FALSE,trace=FALSE)
summary(ARIMAfit)

par(mfrow = c(1,1))
pred = predict(ARIMAfit, n.ahead = 1000)
pred
plot(data,type='l',xlim=c(2012,2018),ylim=c(1,1600),xlab = 'Year',ylab = 'Sales')
lines(10^(pred$pred),col='blue')
lines(10^(pred$pred+2*pred$se),col='orange')
lines(10^(pred$pred-2*pred$se),col='orange')
