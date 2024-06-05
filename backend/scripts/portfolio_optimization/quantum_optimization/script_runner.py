import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from portfolio import calculate_portfolio_stats
from get_optimal_stocks import get_optimal_stocks
from portfolio import define_portfolio_optimization_problem
from monte_carlo_simulation import run_monte_carlo_simulation
from get_stocks_data import get_yahoo_data, get_stocks_dataframe
from solver import solve_using_numpy_minimum_eigensolver, solve_using_qaoa, solve_using_sampling_vqe

def CVARScriptRunner(
    stocks, 
    solver, 
    start_date, 
    end_date, 
    portfolio_total_value, 
    budget, 
    risk_factor, 
    confidence_level, 
    print_info=True, 
    display_plots=True
):
    """
    This function runs the portfolio optimization script using CVAR. It fetches the stock data, defines the portfolio optimization problem, solves it using the specified solver, and calculates the portfolio statistics. It also visualizes the results.
    
    Args:
        stocks (list): List of stock symbols.
        solver (str): The solver to be used for optimization.
        start_date (str): Start date for fetching the stock data.
        end_date (str): End date for fetching the stock data.
        portfolio_total_value (float): Total value of the portfolio.
        budget (float): The budget, i.e. the number of assets to be selected.
        risk_factor (float): Risk factor for the portfolio.
        confidence_level (float): Confidence level for the CVaR calculation.
        print_info (bool): Whether to print the results.
        display_plots (bool): Whether to display the plots.
    
    Returns:
        results (dict): Dictionary containing the portfolio optimization results:
            - Selected Stocks By User: This is the list of stocks selected by the user.
            - How many Stocks to select?: This is the number of stocks selected by the user.
            - Start Date: This is the start date for the data.
            - End Date: This is the end date for the data.
            - Duration: This is the number of days for which the data is available.
            - Portfolio Value: This is the total value of the portfolio.
            - Risk Factor: This is the risk factor for the portfolio.
            - Confidence Level: This is the confidence level for the CVaR calculation.
            - Solver: This is the solver used for optimization.
            - Optimal Weights: This is the list of optimal weights for the portfolio.
            - Optimal Stocks: This is the list of optimal stocks selected for the portfolio.
            - Expected Return: This is the expected return on the portfolio.
            - Expected Volatility: This is the standard deviation of the portfolio return.
            - Sharpe Ratio: This is the ratio of the expected return to the expected volatility.
            - CVaR: This is the expected loss (in percentage) that will not be exceeded with the given confidence level.
            - Cumulative Return: This is the return on the portfolio over the given period.
            - Recomended Investment: This is the recommended investment in each stock based on the optimal weights.        
    """
    data, tickers, mu, sigma = get_yahoo_data(stocks, start_date, end_date)
    portfolio, portfolio_quadratic_program = define_portfolio_optimization_problem(
        expected_returns=mu, 
        covariances=sigma, 
        risk_factor=risk_factor, 
        budget=budget
    )
    
    if(solver == 'numpy_minimum_eigensolver'):
        result = solve_using_numpy_minimum_eigensolver(portfolio_quadratic_program)
    elif(solver == 'qaoa'):
        result = solve_using_qaoa(portfolio_quadratic_program)
    elif(solver == 'sampling_vqe'):
        result = solve_using_sampling_vqe(portfolio_quadratic_program, len(stocks))
    else:
        raise ValueError("Invalid solver")
    
    stock_symbols = get_optimal_stocks(tickers, result)

    stock_data = get_stocks_dataframe(stock_symbols, start_date, end_date)
    results = calculate_portfolio_stats(stock_data, confidence_level)

    if(print_info):
        print(f"Optimal Weights: {results['optimal_weights']}")
        print(f"Expected Return: {results['expected_return'] * 100:.2f}%")
        print(f"Expected Volatility: {results['expected_volatility'] * 100:.2f}%")
        print(f"Sharpe Ratio: {results['sharpe_ratio']:.2f}")
        print(f"CVaR (95%): {results['cvar'] * 100:.2f}%")
        print(f"Values to be invested in each stock for portfolio of value {portfolio_total_value} $")
    
    recomended_investment = {}
    for i, symbol in enumerate(stock_symbols):
        recomended_investment[symbol] = results["optimal_weights"][i] * portfolio_total_value
        if(print_info):
            print(f'{symbol} : ${results["optimal_weights"][i] * portfolio_total_value:.2f}')

    # Visualization
    if(display_plots):
        plt.figure(figsize=(17, 9))
        plt.scatter(results['vol_arr'], results['ret_arr'], c=results['sharpe_arr'], cmap='plasma')
        plt.colorbar(label='Sharpe Ratio')
        plt.xlabel('Volatility')
        plt.ylabel('Return')
        plt.scatter(results['vol_arr'][results['sharpe_arr'].argmax()], results['ret_arr'][results['sharpe_arr'].argmax()], c='red', s=50, edgecolors='black')
        plt.title('Portfolio Optimization')
        plt.show()

    # Combine the position values into a single DataFrame and calculate the total position
    portfolio_val = pd.concat([stock_data[symbol]['Normed Return'] * results['optimal_weights'][i] * portfolio_total_value for i, symbol in enumerate(stock_symbols)], axis=1)
    portfolio_val.columns = [f"{symbol} Pos" for symbol in stock_symbols]
    portfolio_val['Total Pos'] = portfolio_val.sum(axis=1)

    # Plot the total portfolio value
    if(display_plots):
        portfolio_val['Total Pos'].plot(figsize=(10, 8))
        plt.title('Total Portfolio Value')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value')
        plt.show()

    # Plot the individual stock position values
    if(display_plots):
        portfolio_val.drop('Total Pos', axis=1).plot(kind='line', figsize=(10, 8))
        plt.title('Individual Stock Position Values')
        plt.xlabel('Date')
        plt.ylabel('Position Value')
        plt.show()

    portfolio_val['Daily Return'] = portfolio_val['Total Pos'].pct_change(1)
    cum_ret = 100 * (portfolio_val['Total Pos'][-1] / portfolio_val['Total Pos'][0] - 1)
    if(print_info):
        print(f'Cumulative Return: {cum_ret:.2f}%')

    return {
        'Selected Stocks By User': stocks,
        'How many Stocks to select?': budget,
        'Start Date': start_date,
        'End Date': end_date,
        'Duration': (datetime.date(*end_date) - datetime.date(*start_date)).days,
        'Portfolio Value': portfolio_total_value,
        'Risk Factor': risk_factor,
        'Confidence Level': confidence_level,
        'Solver': solver,
        'Optimal Weights': results['optimal_weights'],
        'Optimal Stocks': stock_symbols,
        'Expected Return': results['expected_return'],
        'Expected Volatility': results['expected_volatility'],
        'Sharpe Ratio': results['sharpe_ratio'],
        'CVaR': results['cvar'],
        'Cumulative Return': cum_ret,
        'Recomended Investment': recomended_investment
    }
    

def MVOScriptRunner(
    stocks, 
    solver, 
    start_date, 
    end_date, 
    portfolio_total_value,
    budget, 
    risk_factor, 
    confidence_level, 
    num_iters = 5000,
    print_info=True, 
    display_plots=True
):
    """
    This function runs the portfolio optimization using MVO script. It fetches the stock data, defines the portfolio optimization problem, solves it using the specified solver, and calculates the portfolio statistics. It also visualizes the results.
    
    Args:
        stocks (list): List of stock symbols.
        solver (str): The solver to be used for optimization.
        start_date (str): Start date for fetching the stock data.
        end_date (str): End date for fetching the stock data.
        portfolio_total_value (float): Total value of the portfolio.
        budget (float): The budget, i.e. the number of assets to be selected.
        risk_factor (float): Risk factor for the portfolio.
        confidence_level (float): Confidence level for the CVaR calculation.
        num_iters (int): Number of iterations for Monte Carlo simulation.
        print_info (bool): Whether to print the results.
        display_plots (bool): Whether to display the plots.
    
    Returns:
        results (dict): Dictionary containing the portfolio optimization results:
            - Selected Stocks By User: This is the list of stocks selected by the user.
            - How many Stocks to select?: This is the number of stocks selected by the user.
            - Start Date: This is the start date for the data.
            - End Date: This is the end date for the data.
            - Duration: This is the number of days for which the data is available.
            - Portfolio Value: This is the total value of the portfolio.
            - Risk Factor: This is the risk factor for the portfolio.
            - Confidence Level: This is the confidence level for the CVaR calculation.
            - Solver: This is the solver used for optimization.
            - Optimal Weights: This is the list of optimal weights for the portfolio.
            - Optimal Stocks: This is the list of optimal stocks selected for the portfolio.
            - Logarithmic Returns: This is the logarithmic returns of the stocks.
            - Mean Logarithmic Returns: This is the mean logarithmic returns of the stocks.
            - Pairwise Covariance: This is the pairwise covariance of the stocks.
            - Expected Return: This is the expected return on the portfolio.
            - Expected Volatility: This is the standard deviation of the portfolio return.
            - Sharpe Ratio: This is the ratio of the expected return to the expected volatility.
            - Adjusted Sharpe Ratio: This is the adjusted Sharpe ratio.
            - CVaR: This is the expected loss (in percentage) that will not be exceeded with the given confidence level.
            - Cumulative Return: This is the return on the portfolio over the given period.
            - Recomended Investment: This is the recommended investment in each stock based on the optimal weights.
    """  
    data, tickers, mu, sigma = get_yahoo_data(stocks, start_date, end_date)
    portfolio, portfolio_quadratic_program = define_portfolio_optimization_problem(
        expected_returns=mu, 
        covariances=sigma, 
        risk_factor=risk_factor, 
        budget=budget
    )
    
    if(solver == 'numpy_minimum_eigensolver'):
        result = solve_using_numpy_minimum_eigensolver(portfolio_quadratic_program)
    elif(solver == 'qaoa'):
        result = solve_using_qaoa(portfolio_quadratic_program)
    elif(solver == 'sampling_vqe'):
        result = solve_using_sampling_vqe(portfolio_quadratic_program, len(stocks))
    else:
        raise ValueError("Invalid solver")
    
    
    # Define the stock symbols (Yahoo Finance uses different symbols compared to Quandl)
    stock_symbols = get_optimal_stocks(tickers, result)
    stock_data = get_stocks_dataframe(stock_symbols, start_date, end_date)

    # Generate random allocations
    allocations = np.random.rand(len(stock_symbols))
    # Normalize allocations so they add up to 1
    allocations /= allocations.sum()

    # Calculate and add position values to each dataframe
    for stock_symbol, allocation in zip(stock_symbols, allocations):
        stock_df = stock_data[stock_symbol]
        stock_df['Allocation'] = stock_df['Normed Return'] * allocation
        stock_df['Position Values'] = stock_df['Allocation'] * portfolio_total_value

    # Display the head of the first dataframe with allocation and position values
    if(print_info):
        print("\n DataFrame with Allocation and Position Values Head:")
        print(stock_data[stock_symbols[0]].head())

    # Combine the position values into a single DataFrame and calculate the total position
    portfolio_val = pd.concat([stock_data[symbol]['Position Values'] for symbol in stock_symbols], axis=1)
    portfolio_val.columns = [f"{symbol} Pos" for symbol in stock_symbols]
    portfolio_val['Total Pos'] = portfolio_val.sum(axis=1)
    
    # Display the head of the portfolio valuation DataFrame
    if(print_info):
        print("\nPortfolio Valuation DataFrame Head:")
        print(portfolio_val.head())

    # Plot the total portfolio value
    if(display_plots):
        portfolio_val['Total Pos'].plot(figsize=(10, 8))
        plt.title('Total Portfolio Value')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value')
        plt.show()

    # Plot the individual stock position values
    if(display_plots):
        portfolio_val.drop('Total Pos', axis=1).plot(kind='line', figsize=(10, 8))
        plt.title('Individual Stock Position Values')
        plt.xlabel('Date')
        plt.ylabel('Position Value')
        plt.show()

    portfolio_val['Daily Return'] = portfolio_val['Total Pos'].pct_change(1)

    # Calculate the cumulative return
    cum_ret = 100 * (portfolio_val['Total Pos'][-1] / portfolio_val['Total Pos'][0] - 1)
    if(print_info):
        print('Our cumulative return is {} percent!'.format(cum_ret))
    
    mean = portfolio_val['Daily Return'].mean()
    std = portfolio_val['Daily Return'].std()
    SR = portfolio_val['Daily Return'].mean()/portfolio_val['Daily Return'].std()
    ASR = (252**0.5)*SR
    
    # Extract and combine the adjusted close prices into a single DataFrame for daily returns
    close_data = {symbol: stock_data[symbol]['Adj Close'] for symbol in stock_symbols}

    # Combine daily close prices into a single DataFrame
    stocks_df = pd.DataFrame(close_data)

    # Display the head of the daily returns DataFrame
    if(print_info):
        print("\nDaily Returns DataFrame Head:")
        print(stocks_df.head())

    # Calculate logarithmic returns
    log_ret = np.log(stocks_df / stocks_df.shift(1))

    # Display the head of the logarithmic returns DataFrame
    if(print_info):
        print("\nLogarithmic Returns DataFrame Head:")
        print(log_ret.head())
    
    #calculate the log return mean of each stock
    log_return_mean = log_ret.mean() * 252
    
    # Compute pairwise covariance of columns
    pairwise_covariance = log_ret.cov()*252
    
    all_weights, ret_arr, vol_arr, sharpe_arr, cvar_arr = run_monte_carlo_simulation(num_iters, stock_symbols, stocks_df, log_ret);
    
    Max_sharpe =sharpe_arr.max()
    arr_sharpe = sharpe_arr.argmax()
    
    all_weights[arr_sharpe,:]

    optimal_weights = all_weights
    
    if(print_info):
        print('Max sharpe ratio in array :', Max_sharpe)
        print('Max sharpe ratio index :', arr_sharpe)
        print(optimal_weights[0])

    recomended_investment = {}
    for i in range(len(stock_symbols)):
        recomended_investment[stock_symbols[i]] = optimal_weights[0][i]* portfolio_total_value
        if(print_info):
            print(f'{stock_symbols[i]} : ${optimal_weights[0][i]* portfolio_total_value} ')
    
    max_sr_ret = ret_arr[arr_sharpe]
    max_sr_vol = vol_arr[arr_sharpe]
    
    if(display_plots):
        plt.figure(figsize=(17,9))
        plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')
        plt.colorbar(label='Sharpe Ratio')
        plt.xlabel('Volatility')
        plt.ylabel('Return')
        # Add red dot for max SR
        plt.scatter(max_sr_vol,max_sr_ret,c='red',s=50,edgecolors='black')
    
    return {
        'Selected Stocks By User': stocks,
        'How many Stocks to select?': budget,
        'Start Date': start_date,
        'End Date': end_date,
        'Duration': (datetime.date(*end_date) - datetime.date(*start_date)).days,
        'Portfolio Value': portfolio_total_value,
        'Risk Factor': risk_factor,
        'Confidence Level': confidence_level,
        'Solver': solver,
        'Optimal Weights': optimal_weights[0],
        'Optimal Stocks': stock_symbols,
        'Logarithmic Returns': log_ret,
        'Mean Logarithmic Returns': log_return_mean,
        'Pairwise Covariance': pairwise_covariance,
        'Expected Return': mean,
        'Expected Volatility': std,
        'Sharpe Ratio': SR,
        'Adjusted Sharpe Ratio': ASR,
        'CVaR': cvar_arr,
        'Cumulative Return': cum_ret,
        'Recomended Investment': recomended_investment
    }
    