import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import load_data
from src.strategy_optimizer import StrategyOptimizer
from src.strategies.rsi_ema_crossover import RSIEMACrossover

# Load data
data = load_data('data/processed/BATS_SPY, 240_5dfaa.csv')  # Update with your data path

# Optimize strategy
optimizer = StrategyOptimizer(RSIEMACrossover, data)
results = optimizer.optimize(range(10, 21), range(10, 21))

# Plot heatmap
pivot_table = results.pivot(index='RSI Period', columns='EMA Period', values='Profit Factor')
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap="YlGnBu")
plt.title('RSI-EMA Crossover Strategy Optimization')
plt.show()
