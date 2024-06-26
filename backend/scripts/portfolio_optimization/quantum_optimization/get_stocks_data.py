import datetime
import yfinance as yf
from qiskit_finance.exceptions import QiskitFinanceError
from qiskit_finance.data_providers import RandomDataProvider, YahooDataProvider

def get_random_data(num_assets, seed, start_date, end_date):
    """
    This function generates random time-series data for a given number of assets using the `RandomDataProvider` class of `qiskit_finance.data_providers`.
    
    Args:
        num_assets (int): Number of assets.
        seed (int): Seed for the random data provider.
        start_date (list): Start date of the time-series data in the format [year, month, day].
        end_date (list): End date of the time-series data in the format [year, month, day].
        
    Returns:
        data (RandomDataProvider): RandomDataProvider object.
        stocks (list): List of asset names.
        mu (numpy.ndarray): Expected returns for the assets.
        sigma (numpy.ndarray): Covariance matrix of the assets.
    
    Raises:
        QiskitFinanceError: If an error occurs during the generation of the random data.
    """
    # Generate expected return and covariance matrix from (random) time-series
    try:
        # set number of assets (= number of qubits)
        stocks = [("TICKER %s" % i) for i in range(num_assets)]
        
        data = RandomDataProvider(
            tickers=stocks,
            start=datetime.datetime(start_date[0], start_date[1], start_date[2]),
            end=datetime.datetime(end_date[0], end_date[1], end_date[2]),
            seed=seed,
        )
        data.run()
        mu = data.get_period_return_mean_vector()
        sigma = data.get_period_return_covariance_matrix()

        return data, stocks, mu, sigma
    except QiskitFinanceError as e:
        print(e)
        raise e

def get_yahoo_data(tickers, start_date, end_date):
    """
    This function fetches historical stock price data for a given list of tickers using the `YahooDataProvider` class of `qiskit_finance.data_providers`.
    
    Args:
        tickers (list): List of stock tickers.
        start_date (list): Start date of the time-series data in the format [year, month, day].
        end_date (list): End date of the time-series data in the format [year, month, day].
    
    Returns:
        data (YahooDataProvider): YahooDataProvider object.
        tickers (list): List of stock tickers.
        mu (numpy.ndarray): Expected returns for the assets.
        sigma (numpy.ndarray): Covariance matrix of the assets.
    
    Raises:
        QiskitFinanceError: If an error occurs during the fetching of the historical stock price data.
    """
    try:
        data = YahooDataProvider(
            tickers=tickers,
            start=datetime.datetime(start_date[0], start_date[1], start_date[2]),
            end=datetime.datetime(end_date[0], end_date[1], end_date[2]),
        )
        data.run()
        mu = data.get_period_return_mean_vector()
        sigma = data.get_period_return_covariance_matrix()

        return data, tickers, mu, sigma
    except QiskitFinanceError as e:
        print(e)
        raise e

def get_stocks_dataframe(tickers, start_date, end_date):
    """
    This function fetches detailed stock data for a given list of stock symbols using the `yfinance` library. The data includes the following columns:
        - Date
        - Open
        - High
        - Low
        - Close
        - Adj Close
        - Volume
        - Normed Return

    Args:  
        tickers (list): List of stock symbols.
        start (str): Start date of the time-series data in the format 'yyyy-mm-dd'.
        end (str): End date of the time-series data in the format 'yyyy-mm-dd'.
    
    Returns:
        stock_data (dict): Dictionary containing the stock data for each stock symbol.
    """
    # Create an empty dictionary to store dataframes
    stock_data = {}
    start=datetime.datetime(start_date[0], start_date[1], start_date[2])
    end=datetime.datetime(end_date[0], end_date[1], end_date[2])
    
    # Fetch data from Yahoo Finance
    for stock_symbol in tickers:
        try:
            stock_df = yf.download(stock_symbol, start=start, end=end)
            stock_df['Normed Return'] = stock_df['Adj Close'] / stock_df.iloc[0]['Adj Close']
            stock_data[stock_symbol] = stock_df
        except Exception as e:
            print(f"Error retrieving data for symbol: {stock_symbol}. Error message: {e}")
    return stock_data
