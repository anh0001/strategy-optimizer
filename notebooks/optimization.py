import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import load_data  # Custom module
from src.strategy_optimizer import StrategyOptimizer  # Custom module
from src.strategies.rsi_ema_crossover import RSIEMACrossover  # Custom module

# Load data
data = load_data('data/processed/BATS_SPY, 240_5dfaa.csv')  # Update with your data path

# Optimize strategy
optimizer = StrategyOptimizer(RSIEMACrossover, data)
results = optimizer.optimize(range(4, 34), range(3, 21))

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# List of metrics to plot
# metrics = ['Profit Factor', 'Maximum Drawdown', 'Sharpe Ratio', 'ROI', 'Expectancy', 'Risk-Reward Ratio']
metrics = ['Win Rate', 'Maximum Drawdown', 'ROI', 'Risk-Reward Ratio']

# Plot heatmaps for each metric in separate figures
for metric in metrics:
    pivot_table = results_df.pivot(index='RSI Period', columns='EMA Period', values=metric)
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap="YlGnBu")
    plt.title(f'RSI-EMA Crossover Strategy Optimization - {metric}')

# Show all figures at once
plt.show()
