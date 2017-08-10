import pandas as pd
df = pd.read_csv('vwapHourlyLTCUSD.csv')
df = df[['Date','Vwap (LTCUSD)']]

def sma_n(df,n):
    df['sma'+str(n)]=df['Vwap (LTCUSD)'].rolling(window=n).mean()
def std_n(df,n):
    df['std'+str(n)]=df['Vwap (LTCUSD)'].rolling(window=n).std()
def band_n(df,n):
    df['band_'+str(n)+'+1']=df['sma'+str(n)]+df['std'+str(n)]
    df['band_'+str(n)+'+2']=df['sma'+str(n)]+2*df['std'+str(n)]
    df['band_'+str(n)+'-1']=df['sma'+str(n)]-df['std'+str(n)]
    df['band_'+str(n)+'-2']=df['sma'+str(n)]-2*df['std'+str(n)]
def ema_n(df,n):
    df['ewma'+str(n)]=pd.ewma(df['Vwap (LTCUSD)'],span=n,min_periods=n)
def ewstd_n(df,n):
    df['ewstd'+str(n)]=pd.ewmstd(df['Vwap (LTCUSD)'],span=n,min_periods=n)
def xband_n(df,mean,std):
    df[mean+std+'_band_+1']=df[mean]+df[std]
    df[mean+std+'_band_+2']=df[mean]+2*df[std]
    df[mean+std+'_band_-1']=df[mean]-df[std]
    df[mean+std+'_band_-2']=df[mean]-2*df[std]
def slope(df,indi):
    df['slope_'+indi]=df[indi].diff()

#trend of the curve using regression
#scaled order
#set longer n to prevent pumping
#get OHLC for SMI https://wiki.timetotrade.com/Stochastic_Momentum_Index
