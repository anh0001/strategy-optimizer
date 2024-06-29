import unittest
import backtrader as bt
from src.strategy_optimizer import StrategyOptimizer, MyStrategy

class TestStrategyOptimizer(unittest.TestCase):
    def test_optimize(self):
        data = bt.feeds.PandasData(dataname='data/raw/sample.csv')  # Update with actual data
        optimizer = StrategyOptimizer(MyStrategy, data)
        params = {'period_one': 10, 'period_two': 20}
        result = optimizer.optimize(params)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
