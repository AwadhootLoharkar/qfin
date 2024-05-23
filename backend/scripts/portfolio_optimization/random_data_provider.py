import datetime
from qiskit_finance.exceptions import QiskitFinanceError
from qiskit_finance.data_providers import RandomDataProvider

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