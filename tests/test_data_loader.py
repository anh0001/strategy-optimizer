import unittest
import pandas as pd
from src.data_loader import load_data

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        # Example test case (you'll need to update it with actual test data)
        data = load_data('data/raw/sample.csv')
        self.assertIsInstance(data, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
