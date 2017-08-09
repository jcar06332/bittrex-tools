from bittrex import bittrex
import pandas as pd

api_key = "api_key"
api_secret = "api_secret"

btx = bittrex.Bittrex(api_key,api_secret)
btx.get_balances()
btx.get_balance('BTC')

from pandas.io.json import json_normalize as js
df = pd.DataFrame(btx.get_market_history('BTC-LTC',2))
market_history = js([e for e in df['result']])

def data_to_df(term,args=None):
    if args==None:
        df = pd.DataFrame(term())
    else:
        df = pd.DataFrame(term(*args))
    market_history = js([e for e in df['result']])
    return market_history
get_balance = lambda : data_to_df(btx.get_balances)
get_market_history = lambda market,count: data_to_df(btx.get_market_history,(market,count))

def buy_sell_to_df(term,args=None):
    if args==None:
        df = pd.DataFrame(term())
    else:
        df = pd.DataFrame(term(*args),index=[0])
    return df
buy = lambda market,quan,rate: buy_sell_to_df(btx.buy_limit,({'market':market,
                                                            'quantity':quan,
                                                            'rate':rate}))
sell = lambda market,quan,rate: buy_sell_to_df(btx.sell_limit,({'market':market,
                                                            'quantity':quan,
                                                            'rate':rate}))

#usage
get_balance()
get_market_history("BTC-LTC",2)

buy('btc-ltc',0.01,0.01)
sell('btc-ltc',0.01,0.01)
