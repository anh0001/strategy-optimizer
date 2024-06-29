import unittest
import backtrader as bt
from src.indicators.indicator_two import IndicatorTwo

class TestIndicatorTwo(unittest.TestCase):
    def test_indicator_two(self):
        cerebro = bt.Cerebro()
        data = bt.feeds.YahooFinanceData(dataname='AAPL')
        cerebro.adddata(data)
        
        indicator = IndicatorTwo(data)
        cerebro.addindicator(indicator)
        
        result = cerebro.run()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
