import backtrader as bt
from indicators.indicator_one import IndicatorOne
from indicators.indicator_two import IndicatorTwo

class StrategyOptimizer:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data
    
    def optimize(self, params):
        cerebro = bt.Cerebro()
        cerebro.addstrategy(self.strategy, **params)

        data_feed = bt.feeds.PandasData(dataname=self.data)
        cerebro.adddata(data_feed)

        optimized_result = cerebro.run()
        return optimized_result

# Example Strategy using indicators
class MyStrategy(bt.Strategy):
    params = (
        ('period_one', 14),
        ('period_two', 14),
    )
    
    def __init__(self):
        self.indicator_one = IndicatorOne(self.data, period=self.params.period_one)
        self.indicator_two = IndicatorTwo(self.data, period=self.params.period_two)

    def next(self):
        if self.indicator_one > self.indicator_two:
            self.buy()
        elif self.indicator_one < self.indicator_two:
            self.sell()
