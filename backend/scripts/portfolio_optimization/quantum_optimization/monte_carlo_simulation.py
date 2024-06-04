import numpy as np

def run_monte_carlo_simulation(num_iters, stock_symbols, stocks, log_ret):
    """
    This function runs a Monte Carlo simulation to generate random portfolios.
    
    Args:
        num_iters (int): Number of iterations for Monte Carlo simulation.
        stock_symbols (list): List of stock symbols.
        stocks (DataFrame): Stock prices.
        log_ret (DataFrame): Logarithmic returns of the stocks.
        
    Returns:
        all_weights (ndarray): Weights of the stocks in the portfolios.
        ret_arr (ndarray): Portfolio returns.
        vol_arr (ndarray): Portfolio volatilities.
        sharpe_arr (ndarray): Portfolio Sharpe ratios.
        cvar_arr (ndarray): Portfolio Conditional Value at Risk (CVaR).
    """
    all_weights = np.zeros((num_iters, len(stocks.columns)))
    ret_arr = np.zeros(num_iters)
    vol_arr = np.zeros(num_iters)
    sharpe_arr = np.zeros(num_iters)
    cvar_arr = np.zeros(num_iters)
    
    for ind in range(num_iters):
        weights = np.random.random(len(stock_symbols))
        weights /= np.sum(weights)
        
        all_weights[ind, :] = weights
        ret_arr[ind] = np.sum((log_ret.mean() * weights) * 252)
        vol_arr[ind] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))
        sharpe_arr[ind] = ret_arr[ind] / vol_arr[ind]
        
        # Calculate portfolio returns for CVaR
        portfolio_returns = log_ret.dot(weights)
        portfolio_returns = portfolio_returns.dropna()  # Drop NaN values
        
        # Calculate Value at Risk (VaR)
        VaR = np.percentile(portfolio_returns, 5)
        
        # Calculate CVaR
        cvar_arr[ind] = portfolio_returns[portfolio_returns <= VaR].mean()
        
    return all_weights, ret_arr, vol_arr, sharpe_arr, cvar_arr