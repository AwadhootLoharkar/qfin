import random
import sys, os

# Setting import path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'quantum_optimization'))

from save_result import save_result
from import_stocks import read_stock_symbols
from script_runner import CVARScriptRunner, MVOScriptRunner

# Settings
mcs_num_iters = 5000 # Number of iterations for Monte Carlo simulation.
print_info = False
display_plots = False
output_csv_file_name = 'results_01.csv'

all_stocks = ['AAPL', 'MSFT', 'GOOG', 'GOOGL', 'AMZN', 'NVDA', 'PEP', 'QCOM', 'NFLX', 'PYPL', 'AMGN']


def run(num_iter=1):
    for i in range(0, num_iter):
        print("Starting Iteration: ", 1);
        
        try:
            no_of_stocks = random.randint(4, len(all_stocks)-1)
            stocks = random.sample(all_stocks, no_of_stocks)

            start_year = random.randint(2014, 2022)
            start_month = random.randint(1, 12)
            start_day = random.randint(1, 29)
            start_date=(start_year, start_month, start_day) # Start date for fetching the stock data.

            end_year = random.randint(start_year+1, 2024)
            end_month = random.randint(1, 12)
            end_day = random.randint(1, 29)
            end_date=(end_year, end_month, end_day) # End date for fetching the stock data.

            portfolio_total_value = random.randint(10000, 10000000)  # Total portfolio value in dollars
            budget = random.randint(1, no_of_stocks-1) # The budget, i.e. the number of assets to be selected.
            risk_factor = 0.5  # The risk factor, i.e. the maximum risk that can be taken by the investor.
            confidence_level = 0.95 # Confidence level for the CVaR calculation.
            
            ####################################
            solver = 'numpy_minimum_eigensolver'
            
            cvar_numpy_minimum_eigensolver_results = CVARScriptRunner(
                stocks=stocks,
                solver=solver,
                start_date=start_date,
                end_date=end_date,
                portfolio_total_value=portfolio_total_value,
                budget=budget,
                risk_factor=risk_factor,
                confidence_level=confidence_level,
                print_info=print_info,
                display_plots=display_plots
            )
            
            mvo_numpy_minimum_eigensolver_results = MVOScriptRunner(
                stocks=stocks,
                solver=solver,
                start_date=start_date,
                end_date=end_date,
                portfolio_total_value=portfolio_total_value,
                budget=budget,
                risk_factor=risk_factor,
                confidence_level=confidence_level,
                num_iters=mcs_num_iters,
                print_info=print_info,
                display_plots=display_plots
            )
            
            ####################################
            solver = 'qaoa'
            
            cvar_qaoa_results = CVARScriptRunner(
                stocks=stocks,
                solver=solver,
                start_date=start_date,
                end_date=end_date,
                portfolio_total_value=portfolio_total_value,
                budget=budget,
                risk_factor=risk_factor,
                confidence_level=confidence_level,
                print_info=print_info,
                display_plots=display_plots
            )
            
            mvo_qaoa_results = MVOScriptRunner(
                stocks=stocks,
                solver=solver,
                start_date=start_date,
                end_date=end_date,
                portfolio_total_value=portfolio_total_value,
                budget=budget,
                risk_factor=risk_factor,
                confidence_level=confidence_level,
                num_iters=mcs_num_iters,
                print_info=print_info,
                display_plots=display_plots
            )
            
            ####################################
            solver = 'sampling_vqe'
            
            cvar_sampling_vqe_results = CVARScriptRunner(
                stocks=stocks,
                solver=solver,
                start_date=start_date,
                end_date=end_date,
                portfolio_total_value=portfolio_total_value,
                budget=budget,
                risk_factor=risk_factor,
                confidence_level=confidence_level,
                print_info=print_info,
                display_plots=display_plots
            )
            
            mvo_sampling_vqe_results = MVOScriptRunner(
                stocks=stocks,
                solver=solver,
                start_date=start_date,
                end_date=end_date,
                portfolio_total_value=portfolio_total_value,
                budget=budget,
                risk_factor=risk_factor,
                confidence_level=confidence_level,
                num_iters=mcs_num_iters,
                print_info=print_info,
                display_plots=display_plots
            )
            
            ####################################
            results = {
                'Selected Stocks By User': stocks,
                'How many Stocks to select?': budget,
                'Start Date': start_date,
                'End Date': end_date,
                'Duration': cvar_qaoa_results['Duration'],
                'Portfolio Value': portfolio_total_value,
                'Risk Factor': risk_factor,
                'Confidence Level': confidence_level,
                
                'Optimal Stocks Selected by Numpy': cvar_numpy_minimum_eigensolver_results['Optimal Stocks'],
                'Optimal weigths by MVO for Numpy': mvo_numpy_minimum_eigensolver_results['Optimal Weights'],
                'Amount to Invest in each Stock by MVO for Numpy': mvo_numpy_minimum_eigensolver_results['Recomended Investment'],
                'Optimal weigths by CVAR for Numpy': cvar_numpy_minimum_eigensolver_results['Optimal Weights'],
                'Amount to Invest in each Stock by CVAR for Numpy': cvar_numpy_minimum_eigensolver_results['Recomended Investment'],
                
                'Optimal Stocks Selected by QAOA': cvar_qaoa_results['Optimal Stocks'],
                'Optimal weigths by MVO for QAOA': mvo_qaoa_results['Optimal Weights'],
                'Amount to Invest in each Stock by MVO for QAOA': mvo_qaoa_results['Recomended Investment'],
                'Optimal weigths by CVAR for QAOA': cvar_qaoa_results['Optimal Weights'],
                'Amount to Invest in each Stock by CVAR for QAOA': cvar_qaoa_results['Recomended Investment'],
                
                'Optimal Stocks Selected by Sampling VQE': cvar_sampling_vqe_results['Optimal Stocks'],
                'Optimal weigths by MVO for Sampling VQE': mvo_sampling_vqe_results['Optimal Weights'],
                'Amount to Invest in each Stock by MVO for Sampling VQE': mvo_sampling_vqe_results['Recomended Investment'],
                'Optimal weigths by CVAR for Sampling VQE': cvar_sampling_vqe_results['Optimal Weights'],
                'Amount to Invest in each Stock by CVAR for Sampling VQE': cvar_sampling_vqe_results['Recomended Investment'],
            }
            
        
        except Exception as e:  # Catch any exception
            print(f"Error encountered in Iteration {i + 1}: {e}")
            continue  # Skip to the next iteration
        
        save_result(file_name=output_csv_file_name, result=results)
        print("Ending Iteration: ", 1);


run(30);