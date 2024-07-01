import backtrader as bt
import pandas as pd
import numpy as np
from strategies.rsi_ema_crossover import RSIEMACrossover

class StrategyOptimizer:
    def __init__(self, strategy, data):
        self.strategy = strategy
        if not pd.api.types.is_datetime64_any_dtype(data.index):
            data.index = pd.to_datetime(data.index, unit='s')
        self.data = data

    """
    Calculates various performance metrics for a trading strategy based on the analysis provided by the trade analyzer.

    Parameters:
    - trade_analyzer: An object containing trade analysis data, typically from Backtrader's Analyzer.

    The function computes the following metrics:
    - Win Rate: The percentage of winning trades out of the total number of trades.
    - Profit Factor: The ratio of gross profits to gross losses.
    - Maximum Drawdown: The largest peak-to-trough decline in the equity curve of the trading strategy.
    - Sharpe Ratio: Measures the risk-adjusted return of the trading strategy.
    - ROI (Return on Investment): The profitability of the trading strategy relative to the initial investment.
    - Average Trade Duration: The average time duration of trades.
    - Expectancy: The average amount a trader can expect to win (or lose) per trade.
    - Risk-Reward Ratio: Compares the potential profit of a trade to the potential loss.

    Returns:
    A dictionary containing the calculated metrics.
    """
    def calculate_metrics(self, trade_analyzer):
        total_trades = trade_analyzer.total.closed if 'total' in trade_analyzer and 'closed' in trade_analyzer.total else 0
        winning_trades = trade_analyzer.won.total if 'won' in trade_analyzer and 'total' in trade_analyzer.won else 0
        losing_trades = trade_analyzer.lost.total if 'lost' in trade_analyzer and 'total' in trade_analyzer.lost else 0
        win_rate = (winning_trades / total_trades) * 100 if total_trades > 0 else 0
        
        gross_profit = trade_analyzer.pnl.net.total if 'pnl' in trade_analyzer and 'net' in trade_analyzer.pnl else 0
        gross_loss = abs(trade_analyzer.pnl.net.total) if 'pnl' in trade_analyzer and 'net' in trade_analyzer.pnl else 0
        profit_factor = gross_profit / gross_loss if gross_loss != 0 else np.nan
        
        peak = trade_analyzer.pnl.net.total if 'pnl' in trade_analyzer and 'net' in trade_analyzer.pnl else 0
        drawdown = (peak - trade_analyzer.pnl.net.total) / peak if peak != 0 else 0
        max_drawdown = drawdown if drawdown != 0 else np.nan
        
        average_return = trade_analyzer.pnl.net.average if 'pnl' in trade_analyzer and 'net' in trade_analyzer.pnl else 0
        std_return = np.std([trade['pnl'] for trade in trade_analyzer.trades]) if 'trades' in trade_analyzer else 0
        risk_free_rate = 0.01 / 252  # Assume annual risk-free rate of 1%
        sharpe_ratio = (average_return - risk_free_rate) / std_return if std_return != 0 else np.nan
        
        net_profit = trade_analyzer.pnl.net.total if 'pnl' in trade_analyzer and 'net' in trade_analyzer.pnl else 0
        initial_investment = 100000  # Assume initial investment of 100000
        roi = (net_profit / initial_investment) * 100
        
        average_trade_duration = np.mean([trade['duration'] for trade in trade_analyzer.trades]) if 'trades' in trade_analyzer else 0
        
        average_win = trade_analyzer.won.pnl.average if 'won' in trade_analyzer and 'pnl' in trade_analyzer.won else 0
        average_loss = abs(trade_analyzer.lost.pnl.average) if 'lost' in trade_analyzer and 'pnl' in trade_analyzer.lost else 0
        expectancy = (win_rate * average_win) - ((1 - win_rate) * average_loss)
        
        risk_reward_ratio = average_win / average_loss if average_loss != 0 else np.nan
        
        return {
            'Win Rate': win_rate,
            'Profit Factor': profit_factor,
            'Maximum Drawdown': max_drawdown,
            'Sharpe Ratio': sharpe_ratio,
            'ROI': roi,
            'Average Trade Duration': average_trade_duration,
            'Expectancy': expectancy,
            'Risk-Reward Ratio': risk_reward_ratio
        }

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
                metrics = self.calculate_metrics(trade_analyzer)
                metrics.update({'RSI Period': rsi_period, 'EMA Period': ema_period})
                results.append(metrics)
        return pd.DataFrame(results)
