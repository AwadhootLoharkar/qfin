import datetime
from script_runner import CVARScriptRunner, MVOScriptRunner

# Settings
mcs_num_iters = 5000  # Number of iterations for Monte Carlo simulation.
print_info = False
display_plots = False
output_csv_file_name = "results_01.csv"


def run_job(job):
    results = {
        "Selected Stocks By User": job["stocks"],
        "How many Stocks to select?": job["budget"],
        "Start Date": job["start_date"],
        "End Date": job["end_date"],
        "Duration": (
            datetime.date(*job["end_date"]) - datetime.date(*job["start_date"])
        ).days,
        "Portfolio Value": job["portfolio_total_value"],
        "Risk Factor": job["risk_factor"],
        "Confidence Level": job["confidence_level"],
    }

    try:
        if job["solver"] == "numpy_minimum_eigensolver" or job["solver"] == "":
            print("Using numpy minimum eigensolver...")
            solver = "numpy_minimum_eigensolver"

            if job["method"] == "cvar" or job["method"] == "":
                cvar_numpy_minimum_eigensolver_results = CVARScriptRunner(
                    stocks=job["stocks"],
                    solver=solver,
                    start_date=job["start_date"],
                    end_date=job["end_date"],
                    portfolio_total_value=job["portfolio_total_value"],
                    budget=job["budget"],
                    risk_factor=job["risk_factor"],
                    confidence_level=job["confidence_level"],
                    print_info=print_info,
                    display_plots=display_plots,
                )

                results["Optimal weigths by CVAR for Numpy"] = (
                    cvar_numpy_minimum_eigensolver_results["Optimal Weights"].tolist(),
                )
                results["Amount to Invest in each Stock by CVAR for Numpy"] = (
                    cvar_numpy_minimum_eigensolver_results["Recomended Investment"],
                )

            if job["method"] == "mvo" or job["method"] == "":
                mvo_numpy_minimum_eigensolver_results = MVOScriptRunner(
                    stocks=job["stocks"],
                    solver=solver,
                    start_date=job["start_date"],
                    end_date=job["end_date"],
                    portfolio_total_value=job["portfolio_total_value"],
                    budget=job["budget"],
                    risk_factor=job["risk_factor"],
                    confidence_level=job["confidence_level"],
                    num_iters=mcs_num_iters,
                    print_info=print_info,
                    display_plots=display_plots,
                )

                results["Optimal weigths by MVO for Numpy"] = (
                    mvo_numpy_minimum_eigensolver_results["Optimal Weights"].tolist()
                )
                results["Amount to Invest in each Stock by MVO for Numpy"] = (
                    mvo_numpy_minimum_eigensolver_results["Recomended Investment"]
                )

            if job["method"] == "cvar" or job["method"] == "":
                results["Optimal Stocks Selected by Numpy"] = (
                    cvar_numpy_minimum_eigensolver_results["Optimal Stocks"]
                )
            else:
                results["Optimal Stocks Selected by Numpy"] = (
                    mvo_numpy_minimum_eigensolver_results["Optimal Stocks"]
                )

        if job["solver"] == "qaoa" or job["solver"] == "":
            print("Using qaoa...")
            solver = "qaoa"

            if job["method"] == "cvar" or job["method"] == "":
                cvar_qaoa_results = CVARScriptRunner(
                    stocks=job["stocks"],
                    solver=solver,
                    start_date=job["start_date"],
                    end_date=job["end_date"],
                    portfolio_total_value=job["portfolio_total_value"],
                    budget=job["budget"],
                    risk_factor=job["risk_factor"],
                    confidence_level=job["confidence_level"],
                    print_info=print_info,
                    display_plots=display_plots,
                )

                results["Optimal weigths by CVAR for QAOA"] = (
                    cvar_qaoa_results["Optimal Weights"].tolist(),
                )
                results["Amount to Invest in each Stock by CVAR for QAOA"] = (
                    cvar_qaoa_results["Recomended Investment"],
                )

            if job["method"] == "mvo" or job["method"] == "":
                mvo_qaoa_results = MVOScriptRunner(
                    stocks=job["stocks"],
                    solver=solver,
                    start_date=job["start_date"],
                    end_date=job["end_date"],
                    portfolio_total_value=job["portfolio_total_value"],
                    budget=job["budget"],
                    risk_factor=job["risk_factor"],
                    confidence_level=job["confidence_level"],
                    num_iters=mcs_num_iters,
                    print_info=print_info,
                    display_plots=display_plots,
                )

                results["Optimal weigths by MVO for QAOA"] = mvo_qaoa_results[
                    "Optimal Weights"
                ].tolist()
                results["Amount to Invest in each Stock by MVO for QAOA"] = (
                    mvo_qaoa_results["Recomended Investment"]
                )

            if job["method"] == "cvar" or job["method"] == "":
                results["Optimal Stocks Selected by QAOA"] = cvar_qaoa_results[
                    "Optimal Stocks"
                ]
            else:
                results["Optimal Stocks Selected by QAOA"] = mvo_qaoa_results[
                    "Optimal Stocks"
                ]

        if job["solver"] == "sampling_vqe" or job["solver"] == "":
            print("Using sampling vqe...")
            solver = "sampling_vqe"

            if job["method"] == "cvar" or job["method"] == "":
                cvar_sampling_vqe_results = CVARScriptRunner(
                    stocks=job["stocks"],
                    solver=solver,
                    start_date=job["start_date"],
                    end_date=job["end_date"],
                    portfolio_total_value=job["portfolio_total_value"],
                    budget=job["budget"],
                    risk_factor=job["risk_factor"],
                    confidence_level=job["confidence_level"],
                    print_info=print_info,
                    display_plots=display_plots,
                )

                results["Optimal weigths by CVAR for Sampling VQE"] = (
                    cvar_sampling_vqe_results["Optimal Weights"].tolist(),
                )
                results["Amount to Invest in each Stock by CVAR for Sampling VQE"] = (
                    cvar_sampling_vqe_results["Recomended Investment"],
                )

            if job["method"] == "mvo" or job["method"] == "":
                mvo_sampling_vqe_results = MVOScriptRunner(
                    stocks=job["stocks"],
                    solver=solver,
                    start_date=job["start_date"],
                    end_date=job["end_date"],
                    portfolio_total_value=job["portfolio_total_value"],
                    budget=job["budget"],
                    risk_factor=job["risk_factor"],
                    confidence_level=job["confidence_level"],
                    num_iters=mcs_num_iters,
                    print_info=print_info,
                    display_plots=display_plots,
                )

                results["Optimal weigths by MVO for Sampling VQE"] = (
                    mvo_sampling_vqe_results["Optimal Weights"].tolist()
                )
                results["Amount to Invest in each Stock by MVO for Sampling VQE"] = (
                    mvo_sampling_vqe_results["Recomended Investment"]
                )

            if job["method"] == "cvar" or job["method"] == "":
                results["Optimal Stocks Selected by QAOA"] = mvo_sampling_vqe_results[
                    "Optimal Stocks"
                ]
            else:
                results["Optimal Stocks Selected by QAOA"] = mvo_sampling_vqe_results[
                    "Optimal Stocks"
                ]

    except Exception as e:  # Catch any exception
        print(f"Error encountered whil running job: {e}")

    return results


def run_jobs(jobs):
    results = [run_job(job) for job in jobs]
    return results

