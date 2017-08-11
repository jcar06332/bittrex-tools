import bittrex_functions as bitx
class Account:
    def __init__(self):
        self.balance = bitx.get_balance()

    def check_currency_balance(self,currrency):
        return float(self.balance.loc[self.balance['Currency']==currrency,'Balance'])

    def OHLC(market):
        #market = 'BTC-LSK'
        data = bitx.get_market_history(market,2)
        price_filled = data[data['FillType']=='FILL']['Price']
        low_ = price_filled.min()
        high_ = price_filled.max()
        close_ = price.filled.head(1)
        open_ = price_filled.tail(1)
        return [open_,high_,low_,close_]

    def buy(market,rate,quantity):
        return bitx.buy(market,rate,quantity)['success'].values[0]
    def sell(market,rate,quantity):
        return bitx.buy(market,rate,quantity)['success'].values[0]
    """An account has a balance and a holder.
    All accounts share a common interest rate.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> Account.interest = 0.04
    >>> a.interest
    0.04
    """
