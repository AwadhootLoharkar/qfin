def get_optimal_stocks(tickers, result):
    selection = result.x
    optimal_tickers = [tickers[i] for i, s in enumerate(selection) if s == 1]
    return optimal_tickers