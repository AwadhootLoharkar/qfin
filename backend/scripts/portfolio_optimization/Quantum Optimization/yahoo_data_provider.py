import datetime
from qiskit_finance.exceptions import QiskitFinanceError
from qiskit_finance.data_providers import YahooDataProvider

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
