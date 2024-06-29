from tradingview_ta import TA_Handler, Interval, Exchange

def get_tradingview_data(symbol, exchange='BINANCE'):
    handler = TA_Handler(
        symbol=symbol,
        exchange=exchange,
        screener='crypto',
        interval=Interval.INTERVAL_1_DAY
    )
    analysis = handler.get_analysis()
    return analysis.indicators
