import pandas as pd
import numpy as np
from qiskit_finance.applications.optimization import PortfolioOptimization

def define_portfolio_optimization_problem(expected_returns, covariances, risk_factor, budget):
    """
    This function defines the portfolio optimization problem using the `PortfolioOptimization` class from `qiskit_finance.applications.optimization`.
    
    Args:
        expected_returns (numpy.ndarray): Expected returns for the assets.
        covariances (numpy.ndarray): Covariance matrix of the assets.
        risk_factor (float): Risk factor for the portfolio.
        budget (float): The budget, i.e. the number of assets to be selected.
    
    Returns:
        portfolio (PortfolioOptimization): Portfolio optimization problem.
        qp (QuadraticProgram): Corresponding quadratic program.
    """
    portfolio = PortfolioOptimization(expected_returns, covariances, risk_factor, budget)
    qp = portfolio.to_quadratic_program()
    return portfolio, qp

def calculate_portfolio_stats(stock_data, confidence_level, num_ports=5000):
    """
    This function calculates the optimal weights, expected return, expected volatility, Sharpe ratio, and CVaR for a given set of stock data.
    
    Args:
        stock_data (dict): Dictionary of stock data.
        confidence_level (float): Confidence level for the CVaR calculation.
        num_ports (int): Number of portfolios to generate.
        
    Returns:
        stats (dict): Dictionary containing the optimal weights, expected return, expected volatility, Sharpe ratio, CVaR, all weights, expected returns, expected volatilities, and Sharpe ratios for the portfolios.
    """
    stock_symbols = list(stock_data.keys())
    close_data = {symbol: stock_data[symbol]['Adj Close'] for symbol in stock_symbols}
    stocks = pd.DataFrame(close_data)
    log_ret = np.log(stocks / stocks.shift(1))

    np.random.seed(101)
    all_weights = np.zeros((num_ports, len(stock_symbols)))
    ret_arr = np.zeros(num_ports)
    vol_arr = np.zeros(num_ports)
    sharpe_arr = np.zeros(num_ports)
    cvar_arr = np.zeros(num_ports)

    for ind in range(num_ports):
        weights = np.random.random(len(stock_symbols))
        weights /= np.sum(weights)
        
        all_weights[ind, :] = weights
        ret_arr[ind] = np.sum((log_ret.mean() * weights) * 252)
        vol_arr[ind] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))
        sharpe_arr[ind] = ret_arr[ind] / vol_arr[ind]
        
        portfolio_returns = log_ret.dot(weights).dropna()
        VaR = np.percentile(portfolio_returns, (1-confidence_level) * 100)
        cvar_arr[ind] = portfolio_returns[portfolio_returns <= VaR].mean()

    max_sr_idx = sharpe_arr.argmax()
    optimal_weights = all_weights[max_sr_idx, :]

    return {
        "optimal_weights": optimal_weights,
        "expected_return": ret_arr[max_sr_idx],
        "expected_volatility": vol_arr[max_sr_idx],
        "sharpe_ratio": sharpe_arr[max_sr_idx],
        "cvar": cvar_arr[max_sr_idx],
        "all_weights": all_weights,
        "ret_arr": ret_arr,
        "vol_arr": vol_arr,
        "sharpe_arr": sharpe_arr
    }
