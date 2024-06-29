import unittest
import backtrader as bt
from src.indicators.indicator_one import IndicatorOne

class TestIndicatorOne(unittest.TestCase):
    def test_indicator_one(self):
        cerebro = bt.Cerebro()
        data = bt.feeds.YahooFinanceData(dataname='AAPL')
        cerebro.adddata(data)
        
        indicator = IndicatorOne(data)
        cerebro.addindicator(indicator)
        
        result = cerebro.run()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
