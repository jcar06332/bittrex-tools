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
def ema_n(df,n): #check what span is
    df['ema'+str(n)]=df['sma'+str(n)].ewm(span=n).mean()
def slope(df,indi):
    df['slope_'+indi]=df[indi].diff()

#trend of the curve using regression
#scaled order
#set longer n to prevent pumping
#get OHLC for SMI https://wiki.timetotrade.com/Stochastic_Momentum_Index
