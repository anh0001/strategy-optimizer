import unittest
from src.tradingview_integration import get_tradingview_data

class TestTradingViewIntegration(unittest.TestCase):
    def test_get_tradingview_data(self):
        data = get_tradingview_data('BTCUSD')
        self.assertIsInstance(data, dict)

if __name__ == '__main__':
    unittest.main()
