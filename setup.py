from setuptools import setup, find_packages

setup(
    name='strategy-optimizer',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'backtrader[plotting]',
        'pandas',
        'numpy',
        'seaborn',
        'tradingview-ta',
    ],
    entry_points={
        'console_scripts': [
            # If you have any command line scripts, specify them here
        ],
    },
)
