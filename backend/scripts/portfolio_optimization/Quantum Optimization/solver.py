from qiskit_aer.primitives import Sampler
from qiskit.circuit.library import TwoLocal
from qiskit_algorithms.optimizers import COBYLA
from qiskit_algorithms.utils import algorithm_globals
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_algorithms import NumPyMinimumEigensolver, QAOA, SamplingVQE

def solve_using_numpy_minimum_eigensolver(qp):
    """
    This function solves the Quadratic Program using the `NumPyMinimumEigensolver` class of `qiskit_algorithms`.
    
    Args:
        qp (QuadraticProgram): Quadratic Program to solve.
    
    Returns:
        result (dict): Dictionary containing the optimal value and solution.    
    """
    exact_mes = NumPyMinimumEigensolver()
    exact_eigensolver = MinimumEigenOptimizer(exact_mes)

    result = exact_eigensolver.solve(qp)
    return result

def solve_using_sampling_vqe(qp, num_assets, random_seed=1234, cobyla_maxiter=500):
    """
    This function solves the Quadratic Program using the `SamplingVQE` class of `qiskit_algorithms`.
    
    Args:
        qp (QuadraticProgram): Quadratic Program to solve.
        num_assets (int): Number of assets.
        random_seed (int): Random seed for the algorithm. The default value is 1234.
        cobyla_maxiter (int): Maximum number of iterations for the COBYLA optimizer. The default value is 500.
    
    Returns:
        result (dict): Dictionary containing the optimal value and solution.
    """
    algorithm_globals.random_seed = random_seed

    cobyla = COBYLA()
    cobyla.set_options(maxiter=cobyla_maxiter)
    ry = TwoLocal(num_assets, "ry", "cz", reps=3, entanglement="full")
    svqe_mes = SamplingVQE(sampler=Sampler(), ansatz=ry, optimizer=cobyla)
    svqe = MinimumEigenOptimizer(svqe_mes)
    result = svqe.solve(qp)
    return result

def solve_using_qaoa(qp, random_seed=1234, cobyla_maxiter=250):
    """
    This function solves the Quadratic Program using the `QAOA` class of `qiskit_algorithms`.
    
    Args:
        qp (QuadraticProgram): Quadratic Program to solve.
        random_seed (int): Random seed for the algorithm. The default value is 1234.
        cobyla_maxiter (int): Maximum number of iterations for the COBYLA optimizer. The default value is 250.
    
    Returns:
        result (dict): Dictionary containing the optimal value and solution.
    """
    algorithm_globals.random_seed = random_seed

    cobyla = COBYLA()
    cobyla.set_options(maxiter=cobyla_maxiter)
    qaoa_mes = QAOA(sampler=Sampler(), optimizer=cobyla, reps=3)
    qaoa = MinimumEigenOptimizer(qaoa_mes)
    result = qaoa.solve(qp)
    return result