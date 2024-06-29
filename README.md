# Backtrader Strategy Optimization

This repository is designed to optimize trading strategies using the Backtrader library. The goal is to find the best input parameters for various indicators to maximize profit factor. Additionally, this repository integrates with data from TradingView and prepares the data for machine learning model training.

## Structure

- `data/`: Contains raw, processed, and TradingView data files.
- `notebooks/`: Jupyter notebooks for experimentation and optimization.
- `src/`: Source code directory containing modules for data loading, strategy optimization, and TradingView integration.
- `tests/`: Unit tests for the source code.
- `.gitignore`: Specifies files and directories to be ignored by git.
- `environment.yml`: Conda environment configuration file.
- `README.md`: Documentation for the repository.
- `setup.py`: Setup script for the project.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/backtrader-strategy-optimization.git
   cd backtrader-strategy-optimization
   ```

2. Create and activate the conda environment:
   ```sh
   conda env create -f environment.yml
   conda activate backtrader-strategy-optimization
   ```

3. Run Jupyter Notebook:
   ```sh
   jupyter notebook
   ```

## Usage

- Use the Jupyter notebook `notebooks/optimization.ipynb` to optimize strategy parameters.
- The source code in `src/` contains the core functionality for data loading, strategy optimization, and TradingView integration.
