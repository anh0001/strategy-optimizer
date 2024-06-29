import backtrader as bt

class IndicatorTwo(bt.Indicator):
    lines = ('indicator_two',)
    
    params = (
        ('period', 14),
    )
    
    def __init__(self):
        self.addminperiod(self.params.period)
        self.lines.indicator_two = bt.indicators.ExponentialMovingAverage(
            self.data.close, period=self.params.period
        )
