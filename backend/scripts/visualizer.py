import numpy as np
import matplotlib.pyplot as plt
from qiskit.result import QuasiDistribution

def print_result(tickers, portfolio, result):
    """
    This function prints the optimal selection of assets and their corresponding probabilities.
    
    Args:
        tickers (list): List of asset names.
        portfolio (PortfolioOptimization): Portfolio optimization problem.
        result (dict): Dictionary containing the optimal value and solution.
    
    Returns:
        None
    """
    selection = result.x
    value = result.fval
    print("Optimal: selection {}, value {:.4f}".format(selection, value))

    optimal_tickers = [tickers[i] for i, s in enumerate(selection) if s == 1]
    print("Optimal Companies:", optimal_tickers)

    eigenstate = result.min_eigen_solver_result.eigenstate
    probabilities = (
        eigenstate.binary_probabilities()
        if isinstance(eigenstate, QuasiDistribution)
        else {k: np.abs(v) ** 2 for k, v in eigenstate.to_dict().items()}
    )
    print("\n----------------- Full result ---------------------")
    print("selection\tvalue\t\tprobability")
    print("---------------------------------------------------")
    probabilities = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)

    for k, v in probabilities:
        x = np.array([int(i) for i in list(reversed(k))])
        value = portfolio.to_quadratic_program().objective.evaluate(x)
        print("%10s\t%.4f\t\t%.4f" % (x, value, v))

def display_stocks_graph(data):
    """
    This function displays the historical stock price data for a given list of tickers.
    
    Args:
        data (DataProvider): DataProvider object.
    
    Returns:
        None
    """
    for (cnt, stock) in enumerate(data._tickers):
        plt.plot(data._data[cnt], label=stock)
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.1), ncol=3)
    plt.xticks(rotation=90)
    plt.show()