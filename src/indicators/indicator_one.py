import backtrader as bt

class IndicatorOne(bt.Indicator):
    lines = ('indicator_one',)
    
    params = (
        ('period', 14),
    )
    
    def __init__(self):
        self.addminperiod(self.params.period)
        self.lines.indicator_one = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.period
        )
