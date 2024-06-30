# Strategy Optimizer

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
   git clone https://github.com/anh0001/strategy-optimizer.git
   cd strategy-optimizer
   ```

2. Create and activate the Conda environment:
   ```sh
   conda env create -f environment.yml
   conda activate opt-strategy
   ```

3. Install the package:
   ```sh
   pip install -e .
   ```

4. Set the PYTHONPATH environment variable:
   ```sh
   export PYTHONPATH=$PYTHONPATH:$(pwd)
   ```

4. Run Jupyter Notebook:
   ```sh
   jupyter notebook
   ```

5. Run unit tests to ensure everything is set up correctly:
   ```sh
   python -m unittest discover -s tests
   ```

## Usage

- Use the Jupyter notebook `notebooks/optimization.ipynb` to optimize strategy parameters.
- The source code in `src/` contains the core functionality for data loading, strategy optimization, and TradingView integration.
