import backtrader as bt
import pandas as pd
from strategies.rsi_ema_crossover import RSIEMACrossover

class StrategyOptimizer:
    def __init__(self, strategy, data):
        self.strategy = strategy
        if not pd.api.types.is_datetime64_any_dtype(data.index):
            data.index = pd.to_datetime(data.index, unit='s')
        self.data = data

    def optimize(self, rsi_periods, ema_periods):
        results = []
        for rsi_period in rsi_periods:
            for ema_period in ema_periods:
                cerebro = bt.Cerebro()
                cerebro.addstrategy(self.strategy, rsi_period=rsi_period, ema_period=ema_period)
                data_feed = bt.feeds.PandasData(dataname=self.data)
                cerebro.adddata(data_feed)
                cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trade_analyzer')
                result = cerebro.run()[0]
                trade_analyzer = result.analyzers.trade_analyzer.get_analysis()
                try:
                    profit_factor = trade_analyzer.profit_factor
                except:
                    profit_factor = 0
                results.append((rsi_period, ema_period, profit_factor))
        return pd.DataFrame(results, columns=['RSI Period', 'EMA Period', 'Profit Factor'])

# Example usage
# optimizer = StrategyOptimizer(RSIEMACrossover, data)
# results = optimizer.optimize(range(10, 20), range(10, 20))
# print(results)
