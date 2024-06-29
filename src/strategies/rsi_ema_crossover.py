import backtrader as bt

class RSIEMACrossover(bt.Strategy):
    params = (
        ('rsi_period', 14),
        ('ema_period', 9),
    )

    def __init__(self):
        self.rsi = bt.indicators.RelativeStrengthIndex(period=self.params.rsi_period)
        self.ema = bt.indicators.ExponentialMovingAverage(self.rsi, period=self.params.ema_period)

    def next(self):
        if self.rsi > self.ema and not self.position:
            self.buy()
        elif self.rsi < self.ema and self.position:
            self.sell()
