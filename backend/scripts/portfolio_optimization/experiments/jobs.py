############## FILE 1: C&B Testers Request 01.01 ##############
jobs_01 = [
    { # series 1 A
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 B
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 C
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 D
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 E
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 F
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 G
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 H
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 2 A
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],       'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 2 B
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 2 C
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 2 D
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 2 E
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 2 F
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 2 G
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 2 H
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },    
    { # series 3 A
        'stocks': ['SBUX', 'CHTR', 'MRNA', 'AMAT', 'MU', 'ADP', 'ADI', 'BKNG', 'LRCX', 'VRTX'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 3 B
        'stocks': ['SBUX', 'CHTR', 'MRNA', 'AMAT', 'MU', 'ADP', 'ADI', 'BKNG', 'LRCX', 'VRTX'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 3 C
        'stocks': ['SBUX', 'CHTR', 'MRNA', 'AMAT', 'MU', 'ADP', 'ADI', 'BKNG', 'LRCX', 'VRTX'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 3 D
        'stocks': ['SBUX', 'CHTR', 'MRNA', 'AMAT', 'MU', 'ADP', 'ADI', 'BKNG', 'LRCX', 'VRTX'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 3 E
        'stocks': ['SBUX', 'CHTR', 'MRNA', 'AMAT', 'MU', 'ADP', 'ADI', 'BKNG', 'LRCX', 'VRTX'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 3 F
        'stocks': ['SBUX', 'CHTR', 'MRNA', 'AMAT', 'MU', 'ADP', 'ADI', 'BKNG', 'LRCX', 'VRTX'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 3 G
        'stocks': ['SBUX', 'CHTR', 'MRNA', 'AMAT', 'MU', 'ADP', 'ADI', 'BKNG', 'LRCX', 'VRTX'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 3 H
        'stocks': ['SBUX', 'CHTR', 'MRNA', 'AMAT', 'MU', 'ADP', 'ADI', 'BKNG', 'LRCX', 'VRTX'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },    
    { # series 4 A
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 4 B
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 4 C
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 4 D
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 4 E
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 4 F
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 4 G
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 4 H
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },    
    { # series 5 A
        'stocks': ['ADSK', 'MELI', 'TEAM', 'PAYX', 'TTD', 'FISV', 'CSX', 'CDNS', 'WDAY', 'MNST'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 5 B
        'stocks': ['ADSK', 'MELI', 'TEAM', 'PAYX', 'TTD', 'FISV', 'CSX', 'CDNS', 'WDAY', 'MNST'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 5 C
        'stocks': ['ADSK', 'MELI', 'TEAM', 'PAYX', 'TTD', 'FISV', 'CSX', 'CDNS', 'WDAY', 'MNST'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 5 D
        'stocks': ['ADSK', 'MELI', 'TEAM', 'PAYX', 'TTD', 'FISV', 'CSX', 'CDNS', 'WDAY', 'MNST'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 5 E
        'stocks': ['ADSK', 'MELI', 'TEAM', 'PAYX', 'TTD', 'FISV', 'CSX', 'CDNS', 'WDAY', 'MNST'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 5 F
        'stocks': ['ADSK', 'MELI', 'TEAM', 'PAYX', 'TTD', 'FISV', 'CSX', 'CDNS', 'WDAY', 'MNST'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 5 G
        'stocks': ['ADSK', 'MELI', 'TEAM', 'PAYX', 'TTD', 'FISV', 'CSX', 'CDNS', 'WDAY', 'MNST'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 5 H
        'stocks': ['ADSK', 'MELI', 'TEAM', 'PAYX', 'TTD', 'FISV', 'CSX', 'CDNS', 'WDAY', 'MNST'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },    
    { # series 6 A
        'stocks': ['ADI', 'AEP', 'CPRT', 'FTNT', 'SNOW', 'ZM', 'ABNB', 'CRWD', 'DDOG', 'DOCU'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 6 B
        'stocks': ['ADI', 'AEP', 'CPRT', 'FTNT', 'SNOW', 'ZM', 'ABNB', 'CRWD', 'DDOG', 'DOCU'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 6 C
        'stocks': ['ADI', 'AEP', 'CPRT', 'FTNT', 'SNOW', 'ZM', 'ABNB', 'CRWD', 'DDOG', 'DOCU'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 6 D
        'stocks': ['ADI', 'AEP', 'CPRT', 'FTNT', 'SNOW', 'ZM', 'ABNB', 'CRWD', 'DDOG', 'DOCU'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 6 E
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 6 F
        'stocks': ['ADI', 'AEP', 'CPRT', 'FTNT', 'SNOW', 'ZM', 'ABNB', 'CRWD', 'DDOG', 'DOCU'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 6 G
        'stocks': ['ADI', 'AEP', 'CPRT', 'FTNT', 'SNOW', 'ZM', 'ABNB', 'CRWD', 'DDOG', 'DOCU'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 6 H
        'stocks': ['ADI', 'AEP', 'CPRT', 'FTNT', 'SNOW', 'ZM', 'ABNB', 'CRWD', 'DDOG', 'DOCU'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },    { # series7 A
        'stocks': ['PDD', 'RNG', 'ROKU', 'SPLK', 'TWLO', 'UBER', 'OKTA', 'ZS', 'ESTC', 'NOW'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 7 B
        'stocks': ['PDD', 'RNG', 'ROKU', 'SPLK', 'TWLO', 'UBER', 'OKTA', 'ZS', 'ESTC', 'NOW'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 7 C
        'stocks': ['PDD', 'RNG', 'ROKU', 'SPLK', 'TWLO', 'UBER', 'OKTA', 'ZS', 'ESTC', 'NOW'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 7 D
        'stocks': ['PDD', 'RNG', 'ROKU', 'SPLK', 'TWLO', 'UBER', 'OKTA', 'ZS', 'ESTC', 'NOW'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 7 E
        'stocks': ['PDD', 'RNG', 'ROKU', 'SPLK', 'TWLO', 'UBER', 'OKTA', 'ZS', 'ESTC', 'NOW'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 7 F
        'stocks': ['PDD', 'RNG', 'ROKU', 'SPLK', 'TWLO', 'UBER', 'OKTA', 'ZS', 'ESTC', 'NOW'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 7 G
        'stocks': ['PDD', 'RNG', 'ROKU', 'SPLK', 'TWLO', 'UBER', 'OKTA', 'ZS', 'ESTC', 'NOW'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 7 H
        'stocks': ['PDD', 'RNG', 'ROKU', 'SPLK', 'TWLO', 'UBER', 'OKTA', 'ZS', 'ESTC', 'NOW'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },    
    { # series 8 A
        'stocks': ['NET', 'U', 'BILL', 'ASAN', 'VEEV', 'DOCU', 'PTON', 'ZI', 'HOOD', 'AFRM'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 8 B
        'stocks': ['NET', 'U', 'BILL', 'ASAN', 'VEEV', 'DOCU', 'PTON', 'ZI', 'HOOD', 'AFRM'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 8 C
        'stocks': ['NET', 'U', 'BILL', 'ASAN', 'VEEV', 'DOCU', 'PTON', 'ZI', 'HOOD', 'AFRM'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 8 D
        'stocks': ['NET', 'U', 'BILL', 'ASAN', 'VEEV', 'DOCU', 'PTON', 'ZI', 'HOOD', 'AFRM'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 8 E
        'stocks': ['NET', 'U', 'BILL', 'ASAN', 'VEEV', 'DOCU', 'PTON', 'ZI', 'HOOD', 'AFRM'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 8 F
        'stocks': ['NET', 'U', 'BILL', 'ASAN', 'VEEV', 'DOCU', 'PTON', 'ZI', 'HOOD', 'AFRM'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 8 G
        'stocks': ['NET', 'U', 'BILL', 'ASAN', 'VEEV', 'DOCU', 'PTON', 'ZI', 'HOOD', 'AFRM'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 8 H
        'stocks': ['NET', 'U', 'BILL', 'ASAN', 'VEEV', 'DOCU', 'PTON', 'ZI', 'HOOD', 'AFRM'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },    
    { # series 9 A
        'stocks': ['PLTR', 'SNOW', 'DATA', 'PATH', 'CFLT', 'AI', 'IOT', 'HCP', 'MNDY', 'GTLB'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 9 B
        'stocks': ['PLTR', 'SNOW', 'DATA', 'PATH', 'CFLT', 'AI', 'IOT', 'HCP', 'MNDY', 'GTLB'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 9 C
        'stocks': ['PLTR', 'SNOW', 'DATA', 'PATH', 'CFLT', 'AI', 'IOT', 'HCP', 'MNDY', 'GTLB'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 9 D
        'stocks': ['PLTR', 'SNOW', 'DATA', 'PATH', 'CFLT', 'AI', 'IOT', 'HCP', 'MNDY', 'GTLB'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 9 E
        'stocks': ['PLTR', 'SNOW', 'DATA', 'PATH', 'CFLT', 'AI', 'IOT', 'HCP', 'MNDY', 'GTLB'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 9 F
        'stocks': ['PLTR', 'SNOW', 'DATA', 'PATH', 'CFLT', 'AI', 'IOT', 'HCP', 'MNDY', 'GTLB'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 9 G
        'stocks': ['PLTR', 'SNOW', 'DATA', 'PATH', 'CFLT', 'AI', 'IOT', 'HCP', 'MNDY', 'GTLB'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 9 H
        'stocks': ['PLTR', 'SNOW', 'DATA', 'PATH', 'CFLT', 'AI', 'IOT', 'HCP', 'MNDY', 'GTLB'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },    { # series 10 A
        'stocks': ['S', 'SQSP', 'BMBL', 'DUOL', 'COUR', 'NRDS', 'HIPO', 'PRCH', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 10 B
        'stocks': ['S', 'SQSP', 'BMBL', 'DUOL', 'COUR', 'NRDS', 'HIPO', 'PRCH', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 10 C
        'stocks': ['S', 'SQSP', 'BMBL', 'DUOL', 'COUR', 'NRDS', 'HIPO', 'PRCH', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 10 D
        'stocks': ['S', 'SQSP', 'BMBL', 'DUOL', 'COUR', 'NRDS', 'HIPO', 'PRCH', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 10 E
        'stocks': ['S', 'SQSP', 'BMBL', 'DUOL', 'COUR', 'NRDS', 'HIPO', 'PRCH', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 10 F
        'stocks': ['S', 'SQSP', 'BMBL', 'DUOL', 'COUR', 'NRDS', 'HIPO', 'PRCH', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 10 G
        'stocks': ['S', 'SQSP', 'BMBL', 'DUOL', 'COUR', 'NRDS', 'HIPO', 'PRCH', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 10 H
        'stocks': ['S', 'SQSP', 'BMBL', 'DUOL', 'COUR', 'NRDS', 'HIPO', 'PRCH', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
]

jobs_02 = [
    { # series 1 A
        'stocks': ['AVGO', 'NVDA', 'TSLA', 'QCOM', 'MRNA', 'SBUX', 'ADSK', 'FISV', 'CRWD', 'PLTR'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 B
        'stocks': ['AVGO', 'NVDA', 'TSLA', 'QCOM', 'MRNA', 'SBUX', 'ADSK', 'FISV', 'CRWD', 'PLTR'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 C
        'stocks': ['AVGO', 'NVDA', 'TSLA', 'QCOM', 'MRNA', 'SBUX', 'ADSK', 'FISV', 'CRWD', 'PLTR'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 D
        'stocks': ['AVGO', 'NVDA', 'TSLA', 'QCOM', 'MRNA', 'SBUX', 'ADSK', 'FISV', 'CRWD', 'PLTR'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 E
        'stocks': ['AVGO', 'NVDA', 'TSLA', 'QCOM', 'MRNA', 'SBUX', 'ADSK', 'FISV', 'CRWD', 'PLTR'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 F
        'stocks': ['AVGO', 'NVDA', 'TSLA', 'QCOM', 'MRNA', 'SBUX', 'ADSK', 'FISV', 'CRWD', 'PLTR'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 G
        'stocks': ['AVGO', 'NVDA', 'TSLA', 'QCOM', 'MRNA', 'SBUX', 'ADSK', 'FISV', 'CRWD', 'PLTR'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 H
        'stocks': ['AVGO', 'NVDA', 'TSLA', 'QCOM', 'MRNA', 'SBUX', 'ADSK', 'FISV', 'CRWD', 'PLTR'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 A
        'stocks': ['AMZN', 'META', 'NFLX', 'LRCX', 'WDAY', 'SNOW', 'TWLO', 'U', 'DUOL', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 B
        'stocks': ['AMZN', 'META', 'NFLX', 'LRCX', 'WDAY', 'SNOW', 'TWLO', 'U', 'DUOL', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 C
        'stocks': ['AMZN', 'META', 'NFLX', 'LRCX', 'WDAY', 'SNOW', 'TWLO', 'U', 'DUOL', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 D
        'stocks': ['AMZN', 'META', 'NFLX', 'LRCX', 'WDAY', 'SNOW', 'TWLO', 'U', 'DUOL', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 E
        'stocks': ['AMZN', 'META', 'NFLX', 'LRCX', 'WDAY', 'SNOW', 'TWLO', 'U', 'DUOL', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 F
        'stocks': ['AMZN', 'META', 'NFLX', 'LRCX', 'WDAY', 'SNOW', 'TWLO', 'U', 'DUOL', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 G
        'stocks': ['AMZN', 'META', 'NFLX', 'LRCX', 'WDAY', 'SNOW', 'TWLO', 'U', 'DUOL', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 H
        'stocks': ['AMZN', 'META', 'NFLX', 'LRCX', 'WDAY', 'SNOW', 'TWLO', 'U', 'DUOL', 'RDFN'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 A
        'stocks': ['AAPL', 'GOOG', 'ASML', 'AMD', 'PYPL', 'BKNG', 'MRVL', 'ILMN', 'PDD', 'ROKU'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 B
        'stocks': ['AAPL', 'GOOG', 'ASML', 'AMD', 'PYPL', 'BKNG', 'MRVL', 'ILMN', 'PDD', 'ROKU'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 C
        'stocks': ['AAPL', 'GOOG', 'ASML', 'AMD', 'PYPL', 'BKNG', 'MRVL', 'ILMN', 'PDD', 'ROKU'],
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 D
        'stocks': ['AAPL', 'GOOG', 'ASML', 'AMD', 'PYPL', 'BKNG', 'MRVL', 'ILMN', 'PDD', 'ROKU'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 E
        'stocks': ['AAPL', 'GOOG', 'ASML', 'AMD', 'PYPL', 'BKNG', 'MRVL', 'ILMN', 'PDD', 'ROKU'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 F
        'stocks': ['AAPL', 'GOOG', 'ASML', 'AMD', 'PYPL', 'BKNG', 'MRVL', 'ILMN', 'PDD', 'ROKU'],
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 G
        'stocks': ['AAPL', 'GOOG', 'ASML', 'AMD', 'PYPL', 'BKNG', 'MRVL', 'ILMN', 'PDD', 'ROKU'],
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.     
    },
    { # series 1 H
        'stocks': ['AAPL', 'GOOG', 'ASML', 'AMD', 'PYPL', 'BKNG', 'MRVL', 'ILMN', 'PDD', 'ROKU'],
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
        
    }
]


############## FILE 2: C&B Testers Request 02.01 ##############
jobs_03 = [
    { # January 2018 to February 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to February 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

jobs_04 = [
    { # January 2019 to February 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

jobs_05 = [
    { # January 2019 to February 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

jobs_06 = [
    { # January 2019 to February 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'AVGO', 'ASML', 'COST'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

############## FILE 3: C&B Testers Request 02.02 ##############

jobs_07 = [
    { # January 2018 to February 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to February 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

jobs_08 = [
    { # January 2019 to February 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

jobs_09 = [
    { # January 2019 to February 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

jobs_10 = [
    { # January 2019 to February 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['ADBE', 'PEP', 'AMD', 'CMCSA', 'NFLX', 'INTU', 'TXN', 'QCOM', 'PYPL', 'AMGN'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

############## FILE 4: C&B Testers Request 02.03 ##############

jobs_11 = [
    { # January 2018 to February 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to February 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2019, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

jobs_12 = [
    { # January 2019 to February 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2020, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

jobs_13 = [
    { # January 2019 to February 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2021, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

jobs_14 = [
    { # January 2019 to February 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to March 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to April 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 4, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    # Continue this pattern until December 2022
    { # January 2019 to May 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 5, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to June 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to July 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 7, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to August 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 8, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to September 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to October 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 10, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to November 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 11, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # January 2019 to December 2019
        'stocks': ['KLAC', 'REGN', 'MRVL', 'ILMN', 'GILD', 'MU', 'ISRG', 'DXCM', 'ROST', 'ORLY'],
        'start_date': (2019, 1, 1),
        'end_date': (2022, 12, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    }
]

############## FILE 5: C&B Testers Request 03.01 (DOW30 Data) ##############

list_15_1 = ["AMZN", "AXP", "AMGN", "AAPL", "BA", "CAT", "CSCO", "CVX", "GS", "HD"]
list_15_2 = ["HON", "IBM", "INTC", "JNJ", "KO", "JPM", "MCD", "MMM", "MRK", "MSFT"]
list_15_3 = ["NKE", "PG", "TRV", "UNH", "CRM", "VZ", "V", "WMT", "DIS"]

jobs_15 = [
    { # series 1 A
        'stocks': list_15_1,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 1 B
        'stocks': list_15_1,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 1 C
        'stocks': list_15_1,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 1 D
        'stocks': list_15_1,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 1 E
        'stocks': list_15_1,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 1 F
        'stocks': list_15_1,
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 1 G
        'stocks': list_15_1,
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 1 H
        'stocks': list_15_1,
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 2 A
        'stocks': list_15_2,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 2 B
        'stocks': list_15_2,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 2 C
        'stocks': list_15_2,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 2 D
        'stocks': list_15_2,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 2 E
        'stocks': list_15_2,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 2 F
        'stocks': list_15_2,
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 2 G
        'stocks': list_15_2,
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 2 H
        'stocks': list_15_2,
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 3 A
        'stocks': list_15_3,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 3 B
        'stocks': list_15_3,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 3 C
        'stocks': list_15_3,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 3 D
        'stocks': list_15_3,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 3 E
        'stocks': list_15_3,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 3 F
        'stocks': list_15_3,
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 3 G
        'stocks': list_15_3,
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    },
    { # series 3 H
        'stocks': list_15_3,
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': '',
    }
]

############## FILE 6: C&B Testers Request 03.02 (DOW30 Data) ##############

list_16_1 = ["AMZN", "AXP", "AMGN", "AAPL", "BA", "CAT", "CSCO", "CVX", "GS", "HD"]
list_16_2 = ["HON", "IBM", "INTC", "JNJ", "KO", "JPM", "MCD", "MMM", "MRK", "MSFT"]
list_16_3 = ["NKE", "PG", "TRV", "UNH", "CRM", "VZ", "V", "WMT", "DIS"]

jobs_16 = [
    { # series 1 A
        'stocks': list_16_1,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 1 B
        'stocks': list_16_1,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 1 C
        'stocks': list_16_1,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 1 D
        'stocks': list_16_1,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 1 E
        'stocks': list_16_1,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 1 F
        'stocks': list_16_1,
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 1 G
        'stocks': list_16_1,
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 1 H
        'stocks': list_16_1,
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 2 A
        'stocks': list_16_2,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 2 B
        'stocks': list_16_2,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 2 C
        'stocks': list_16_2,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 2 D
        'stocks': list_16_2,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 2 E
        'stocks': list_16_2,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 2 F
        'stocks': list_16_2,
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 2 G
        'stocks': list_16_2,
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 2 H
        'stocks': list_16_2,
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 3 A
        'stocks': list_16_3,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 3, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 3 B
        'stocks': list_16_3,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 3 C
        'stocks': list_16_3,
        'start_date': (2018, 1, 1),
        'end_date': (2018, 9, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 3 D
        'stocks': list_16_3,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 3 E
        'stocks': list_16_3,
        'start_date': (2018, 1, 1),
        'end_date': (2019, 6, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 3 F
        'stocks': list_16_3,
        'start_date': (2018, 1, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 3 G
        'stocks': list_16_3,
        'start_date': (2018, 1, 1),
        'end_date': (2021, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
    { # series 3 H
        'stocks': list_16_3,
        'start_date': (2018, 1, 1),
        'end_date': (2022, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '',
        'solver': ''
    },
]

############## FILE 7: C&B Testers Request 04.01 ##############
jobs_17 = [
    { # series 1
        'stocks': ['ADBE', 'LRCX', 'BKNG', 'INTU', 'AMAT', 'ADP', 'QCOM', 'ROST', 'SBUX', 'PYPL'],
        'start_date': (2018, 2, 17),
        'end_date': (2018, 11, 14),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 2
        'stocks': ['NVDA', 'ADP', 'ROST', 'AMD', 'VRTX', 'ORLY', 'LRCX', 'AMZN', 'MRNA', 'COST'],
        'start_date': (2018, 4, 19),
        'end_date': (2018, 10, 16),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 3
        'stocks': ['META', 'MRNA', 'MSFT', 'BKNG', 'COST', 'ILMN', 'KLAC', 'NVDA', 'QCOM', 'AMAT'],
        'start_date': (2018, 12, 27),
        'end_date': (2019, 12, 22),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 4
        'stocks': ['AMD', 'PEP', 'MU', 'AMAT', 'ILMN', 'COST', 'META', 'ISRG', 'ADBE', 'BKNG'],
        'start_date': (2018, 11, 13),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 5
        'stocks': ['LRCX', 'MRNA', 'NFLX', 'META', 'CMCSA', 'MRVL', 'ORLY', 'AMD', 'SBUX', 'MU'],
        'start_date': (2018, 7, 12),
        'end_date': (2019, 4, 8),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 6
        'stocks': ['VRTX', 'MRVL', 'AAPL', 'ASML', 'ROST', 'ADP', 'ORLY', 'MU', 'ADBE', 'NVDA'],
        'start_date': (2019, 2, 6),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 7
        'stocks': ['ADI', 'AMGN', 'MRNA', 'NFLX', 'KLAC', 'SBUX', 'ORLY', 'REGN', 'TXN', 'QCOM'],
        'start_date': (2018, 4, 26),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 8
        'stocks': ['ILMN', 'AAPL', 'AMAT', 'MRNA', 'META', 'AMD', 'ADP', 'ASML', 'GILD', 'INTU'],
        'start_date': (2019, 12, 14),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 9
        'stocks': ['ORLY', 'AAPL', 'NFLX', 'AMZN', 'ADI', 'ILMN', 'MRNA', 'PYPL', 'AVGO', 'ROST'],
        'start_date': (2019, 10, 28),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 10
        'stocks': ['ADI', 'CHTR', 'MRVL', 'ORLY', 'ASML', 'MRNA', 'ISRG', 'LRCX', 'ADP', 'KLAC'],
        'start_date': (2019, 8, 30),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 11
        'stocks': ['AMZN', 'ADI', 'PEP', 'ADBE', 'PYPL', 'NFLX', 'TXN', 'SBUX', 'AMD', 'ADP'],
        'start_date': (2018, 9, 19),
        'end_date': (2019, 9, 14),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 12
        'stocks': ['AVGO', 'MU', 'BKNG', 'INTU', 'KLAC', 'PYPL', 'ADP', 'ILMN', 'TXN', 'ADI'],
        'start_date': (2018, 7, 2),
        'end_date': (2019, 3, 29),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 13
        'stocks': ['NFLX', 'ASML', 'AMZN', 'VRTX', 'MRVL', 'BKNG', 'ADP', 'MU', 'AMGN', 'KLAC'],
        'start_date': (2018, 3, 2),
        'end_date': (2018, 8, 29),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 14
        'stocks': ['ORLY', 'ADP', 'CHTR', 'MU', 'GOOG', 'ASML', 'AMD', 'NFLX', 'AMGN', 'GILD'],
        'start_date': (2018, 3, 26),
        'end_date': (2018, 6, 24),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 15
        'stocks': ['COST', 'MRNA', 'AMGN', 'ORLY', 'CHTR', 'PEP', 'DXCM', 'KLAC', 'ASML', 'ADP'],
        'start_date': (2019, 9, 2),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 16
        'stocks': ['NFLX', 'AMD', 'SBUX', 'ADP', 'MRNA', 'LRCX', 'PEP', 'ORLY', 'ADI', 'INTU'],
        'start_date': (2019, 5, 19),
        'end_date': (2019, 8, 17),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 17
        'stocks': ['ADBE', 'VRTX', 'MSFT', 'META', 'GOOG', 'AMGN', 'MU', 'NFLX', 'PYPL', 'AAPL'],
        'start_date': (2019, 11, 6),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 18
        'stocks': ['MRNA', 'ROST', 'META', 'NVDA', 'MSFT', 'ILMN', 'AMD', 'PYPL', 'ISRG', 'PEP'],
        'start_date': (2019, 7, 5),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 19
        'stocks': ['PYPL', 'SBUX', 'ORLY', 'NVDA', 'LRCX', 'MRNA', 'BKNG', 'TSLA', 'AVGO', 'ROST'],
        'start_date': (2018, 8, 14),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 20
        'stocks': ['AMD', 'MRVL', 'VRTX', 'SBUX', 'AAPL', 'AMZN', 'PYPL', 'AMAT', 'ADP', 'ISRG'],
        'start_date': (2018, 8, 16),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 21
        'stocks': ['LRCX', 'CMCSA', 'AMAT', 'MU', 'AMGN', 'ADP', 'AVGO', 'GILD', 'NVDA', 'COST'],
        'start_date': (2019, 9, 13),
        'end_date': (2019, 10, 13),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 22
        'stocks': ['VRTX', 'GOOG', 'COST', 'MSFT', 'MU', 'ASML', 'GILD', 'TSLA', 'ADBE', 'ISRG'],
        'start_date': (2018, 2, 3),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 23
        'stocks': ['PEP', 'TXN', 'QCOM', 'META', 'AMGN', 'SBUX', 'AAPL', 'PYPL', 'MSFT', 'NFLX'],
        'start_date': (2018, 5, 7),
        'end_date': (2019, 2, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 24
        'stocks': ['SBUX', 'ILMN', 'MRVL', 'TSLA', 'ROST', 'TXN', 'BKNG', 'QCOM', 'CMCSA', 'PYPL'],
        'start_date': (2019, 3, 6),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 25
        'stocks': ['MSFT', 'AMD', 'COST', 'NFLX', 'ADP', 'PYPL', 'AMGN', 'PEP', 'LRCX', 'BKNG'],
        'start_date': (2018, 7, 28),
        'end_date': (2019, 1, 24),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 26
        'stocks': ['TXN', 'AMD', 'TSLA', 'INTU', 'ADI', 'NVDA', 'PEP', 'DXCM', 'ADP', 'MU'],
        'start_date': (2019, 7, 13),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 27
        'stocks': ['MU', 'PYPL', 'ORLY', 'ROST', 'REGN', 'CMCSA', 'AMGN', 'LRCX', 'QCOM', 'AMAT'],
        'start_date': (2019, 5, 1),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 28
        'stocks': ['ROST', 'REGN', 'AMGN', 'AVGO', 'PEP', 'VRTX', 'ASML', 'ADI', 'ISRG', 'LRCX'],
        'start_date': (2018, 7, 25),
        'end_date': (2019, 1, 21),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 29
        'stocks': ['AAPL', 'AVGO', 'VRTX', 'ADI', 'CMCSA', 'NVDA', 'CHTR', 'INTU', 'MRVL', 'DXCM'],
        'start_date': (2018, 9, 8),
        'end_date': (2019, 6, 5),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 30
        'stocks': ['GILD', 'MSFT', 'ILMN', 'ADI', 'MRVL', 'NVDA', 'CHTR', 'QCOM', 'KLAC', 'VRTX'],
        'start_date': (2019, 12, 25),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 31
        'stocks': ['LRCX', 'ADBE', 'COST', 'BKNG', 'GOOG', 'INTU', 'TSLA', 'ISRG', 'MRNA', 'AAPL'],
        'start_date': (2018, 7, 21),
        'end_date': (2018, 8, 20),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 32
        'stocks': ['KLAC', 'AMAT', 'NVDA', 'DXCM', 'MSFT', 'QCOM', 'TSLA', 'ILMN', 'COST', 'ORLY'],
        'start_date': (2019, 3, 28),
        'end_date': (2019, 9, 24),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 33
        'stocks': ['CMCSA', 'AVGO', 'SBUX', 'MU', 'TXN', 'GILD', 'BKNG', 'META', 'PYPL', 'INTU'],
        'start_date': (2019, 5, 26),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 34
        'stocks': ['QCOM', 'COST', 'PYPL', 'MRNA', 'ASML', 'AMGN', 'PEP', 'INTU', 'SBUX', 'BKNG'],
        'start_date': (2019, 3, 27),
        'end_date': (2019, 12, 22),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 35
        'stocks': ['DXCM', 'TSLA', 'NVDA', 'COST', 'BKNG', 'PEP', 'PYPL', 'MU', 'GOOG', 'LRCX'],
        'start_date': (2019, 7, 28),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 36
        'stocks': ['INTU', 'AMD', 'REGN', 'BKNG', 'ASML', 'TXN', 'ROST', 'MRNA', 'META', 'MU'],
        'start_date': (2019, 2, 20),
        'end_date': (2019, 5, 21),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 37
        'stocks': ['META', 'NVDA', 'AMAT', 'MRNA', 'INTU', 'AAPL', 'SBUX', 'REGN', 'CHTR', 'VRTX'],
        'start_date': (2018, 2, 26),
        'end_date': (2019, 2, 21),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 38
        'stocks': ['REGN', 'AMZN', 'ORLY', 'DXCM', 'AMD', 'NFLX', 'PYPL', 'CMCSA', 'ILMN', 'AAPL'],
        'start_date': (2019, 7, 9),
        'end_date': (2019, 10, 7),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 39
        'stocks': ['VRTX', 'INTU', 'ILMN', 'GILD', 'NFLX', 'ORLY', 'LRCX', 'TSLA', 'DXCM', 'AMZN'],
        'start_date': (2018, 12, 20),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 40
        'stocks': ['GOOG', 'ADP', 'CHTR', 'REGN', 'ORLY', 'BKNG', 'MRVL', 'ILMN', 'VRTX', 'TXN'],
        'start_date': (2018, 2, 28),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 41
        'stocks': ['CHTR', 'TXN', 'NVDA', 'AAPL', 'VRTX', 'AMGN', 'AVGO', 'ADBE', 'ADI', 'NFLX'],
        'start_date': (2018, 4, 20),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 42
        'stocks': ['KLAC', 'GOOG', 'ADI', 'INTU', 'LRCX', 'TXN', 'ADBE', 'AMD', 'AMAT', 'AAPL'],
        'start_date': (2018, 5, 15),
        'end_date': (2019, 5, 10),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 43
        'stocks': ['VRTX', 'PYPL', 'PEP', 'AVGO', 'AMGN', 'ROST', 'NFLX', 'CMCSA', 'TSLA', 'QCOM'],
        'start_date': (2019, 4, 11),
        'end_date': (2019, 10, 8),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 44
        'stocks': ['CMCSA', 'AMZN', 'GILD', 'MRVL', 'QCOM', 'ORLY', 'MU', 'INTU', 'AMGN', 'REGN'],
        'start_date': (2018, 5, 19),
        'end_date': (2019, 11, 10),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 45
        'stocks': ['AMAT', 'INTU', 'LRCX', 'CMCSA', 'REGN', 'MRVL', 'ISRG', 'META', 'GILD', 'MRNA'],
        'start_date': (2019, 11, 6),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 46
        'stocks': ['NVDA', 'AAPL', 'ILMN', 'TXN', 'AMAT', 'KLAC', 'CMCSA', 'PYPL', 'ORLY', 'QCOM'],
        'start_date': (2018, 4, 18),
        'end_date': (2018, 10, 15),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 47
        'stocks': ['NFLX', 'AMAT', 'MSFT', 'REGN', 'MU', 'ROST', 'PEP', 'TXN', 'CMCSA', 'TSLA'],
        'start_date': (2018, 8, 19),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 48
        'stocks': ['MRNA', 'AMAT', 'VRTX', 'ISRG', 'MRVL', 'PEP', 'TSLA', 'NFLX', 'META', 'QCOM'],
        'start_date': (2018, 2, 19),
        'end_date': (2019, 2, 14),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 49
        'stocks': ['TSLA', 'ORLY', 'VRTX', 'ADI', 'AMZN', 'LRCX', 'PEP', 'MU', 'CHTR', 'CMCSA'],
        'start_date': (2019, 6, 25),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 50
        'stocks': ['ADI', 'NFLX', 'MSFT', 'ASML', 'NVDA', 'MU', 'SBUX', 'AMGN', 'GILD', 'AAPL'],
        'start_date': (2019, 9, 29),
        'end_date': (2019, 12, 28),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
]

jobs_18 = [
    { # series 1
        'stocks': ['AMZN', 'INTU', 'VRTX', 'BKNG', 'MRVL', 'ADBE', 'MRNA', 'DXCM', 'AMAT', 'AMD'],
        'start_date': (2018, 10, 28),
        'end_date': (2019, 10, 23),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 2
        'stocks': ['ILMN', 'MRVL', 'GOOG', 'ORLY', 'TSLA', 'PYPL', 'NVDA', 'BKNG', 'ISRG', 'MU'],
        'start_date': (2018, 3, 18),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 3
        'stocks': ['INTU', 'AMAT', 'LRCX', 'ROST', 'DXCM', 'SBUX', 'TXN', 'MRVL', 'ILMN', 'ORLY'],
        'start_date': (2018, 4, 6),
        'end_date': (2018, 10, 3),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 4
        'stocks': ['TSLA', 'NVDA', 'ADBE', 'VRTX', 'ISRG', 'ROST', 'AVGO', 'PEP', 'COST', 'ASML'],
        'start_date': (2018, 1, 31),
        'end_date': (2018, 10, 28),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 5
        'stocks': ['GOOG', 'NVDA', 'AMD', 'KLAC', 'SBUX', 'ADP', 'TXN', 'COST', 'CHTR', 'INTU'],
        'start_date': (2018, 6, 30),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 6
        'stocks': ['AVGO', 'MRNA', 'GILD', 'REGN', 'COST', 'MU', 'MSFT', 'AMZN', 'AMAT', 'LRCX'],
        'start_date': (2019, 2, 10),
        'end_date': (2019, 5, 11),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 7
        'stocks': ['REGN', 'ADP', 'MRVL', 'MSFT', 'NVDA', 'AMGN', 'VRTX', 'CMCSA', 'MRNA', 'META'],
        'start_date': (2019, 5, 7),
        'end_date': (2019, 11, 3),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 8
        'stocks': ['BKNG', 'ORLY', 'PEP', 'AMGN', 'AVGO', 'PYPL', 'NFLX', 'TXN', 'CHTR', 'REGN'],
        'start_date': (2019, 3, 14),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 9
        'stocks': ['AAPL', 'ORLY', 'ASML', 'GILD', 'CHTR', 'META', 'TXN', 'DXCM', 'AVGO', 'MRVL'],
        'start_date': (2018, 2, 14),
        'end_date': (2018, 5, 15),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 10
        'stocks': ['AMD', 'CMCSA', 'GOOG', 'NFLX', 'INTU', 'AMGN', 'MU', 'KLAC', 'ADI', 'REGN'],
        'start_date': (2018, 4, 18),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 11
        'stocks': ['PYPL', 'AMZN', 'ILMN', 'NVDA', 'CHTR', 'TSLA', 'INTU', 'ADP', 'AMGN', 'VRTX'],
        'start_date': (2018, 11, 6),
        'end_date': (2018, 12, 6),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 12
        'stocks': ['ISRG', 'AAPL', 'REGN', 'AMD', 'ASML', 'INTU', 'ORLY', 'KLAC', 'BKNG', 'AMZN'],
        'start_date': (2019, 11, 22),
        'end_date': (2019, 12, 22),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 13
        'stocks': ['SBUX', 'MSFT', 'NFLX', 'NVDA', 'GILD', 'META', 'AMAT', 'LRCX', 'AMZN', 'ROST'],
        'start_date': (2018, 9, 10),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 14
        'stocks': ['AMAT', 'KLAC', 'AMZN', 'REGN', 'DXCM', 'BKNG', 'MSFT', 'ILMN', 'META', 'AAPL'],
        'start_date': (2018, 5, 22),
        'end_date': (2019, 2, 16),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 15
        'stocks': ['ADI', 'MU', 'CMCSA', 'ILMN', 'SBUX', 'LRCX', 'TSLA', 'TXN', 'ORLY', 'AMD'],
        'start_date': (2019, 5, 13),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 16
        'stocks': ['MRVL', 'BKNG', 'AAPL', 'DXCM', 'AVGO', 'CHTR', 'SBUX', 'ROST', 'TXN', 'PYPL'],
        'start_date': (2019, 2, 18),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 17
        'stocks': ['AMZN', 'VRTX', 'CMCSA', 'AMD', 'AMGN', 'TXN', 'META', 'ADP', 'PYPL', 'CHTR'],
        'start_date': (2019, 5, 27),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 18
        'stocks': ['ORLY', 'BKNG', 'CHTR', 'PYPL', 'LRCX', 'AMZN', 'INTU', 'REGN', 'ADBE', 'ASML'],
        'start_date': (2018, 4, 20),
        'end_date': (2019, 10, 12),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 19
        'stocks': ['REGN', 'NVDA', 'ADP', 'MRVL', 'SBUX', 'QCOM', 'ADBE', 'AMGN', 'AMD', 'CHTR'],
        'start_date': (2019, 12, 16),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 20
        'stocks': ['INTU', 'ORLY', 'SBUX', 'CMCSA', 'AAPL', 'ADP', 'ILMN', 'AVGO', 'GILD', 'ISRG'],
        'start_date': (2019, 5, 12),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 21
        'stocks': ['PEP', 'AMZN', 'NFLX', 'GOOG', 'COST', 'TSLA', 'KLAC', 'AAPL', 'ISRG', 'ILMN'],
        'start_date': (2019, 3, 24),
        'end_date': (2019, 6, 22),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 22
        'stocks': ['MSFT', 'AVGO', 'ADI', 'CMCSA', 'GILD', 'NFLX', 'ADP', 'LRCX', 'PEP', 'AMAT'],
        'start_date': (2018, 6, 28),
        'end_date': (2019, 6, 23),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 23
        'stocks': ['DXCM', 'GOOG', 'NFLX', 'ILMN', 'CMCSA', 'GILD', 'COST', 'CHTR', 'MRVL', 'INTU'],
        'start_date': (2019, 7, 23),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 24
        'stocks': ['LRCX', 'AVGO', 'SBUX', 'MSFT', 'GOOG', 'KLAC', 'PYPL', 'BKNG', 'MRVL', 'ADI'],
        'start_date': (2019, 8, 27),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 25
        'stocks': ['META', 'SBUX', 'CMCSA', 'AMAT', 'AMZN', 'GOOG', 'INTU', 'AAPL', 'ADP', 'MRNA'],
        'start_date': (2018, 3, 3),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 26
        'stocks': ['CMCSA', 'MRVL', 'AMAT', 'ORLY', 'AVGO', 'TXN', 'LRCX', 'INTU', 'AMD', 'MU'],
        'start_date': (2018, 7, 14),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 27
        'stocks': ['ASML', 'ORLY', 'LRCX', 'VRTX', 'MSFT', 'GILD', 'GOOG', 'COST', 'KLAC', 'ADBE'],
        'start_date': (2019, 1, 5),
        'end_date': (2019, 4, 5),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 28
        'stocks': ['PYPL', 'AAPL', 'KLAC', 'CHTR', 'ADBE', 'AVGO', 'NFLX', 'ADP', 'AMAT', 'ILMN'],
        'start_date': (2018, 11, 4),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 29
        'stocks': ['MSFT', 'ASML', 'AMAT', 'INTU', 'GILD', 'ADP', 'DXCM', 'MRVL', 'PEP', 'NVDA'],
        'start_date': (2019, 8, 5),
        'end_date': (2019, 9, 4),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 30
        'stocks': ['ADBE', 'TSLA', 'AMGN', 'ASML', 'LRCX', 'CMCSA', 'VRTX', 'ISRG', 'GILD', 'COST'],
        'start_date': (2018, 10, 6),
        'end_date': (2019, 7, 3),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 31
        'stocks': ['NVDA', 'ADP', 'PYPL', 'DXCM', 'AMAT', 'SBUX', 'GILD', 'MRVL', 'AVGO', 'ROST'],
        'start_date': (2018, 4, 5),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 32
        'stocks': ['DXCM', 'QCOM', 'REGN', 'META', 'TSLA', 'NFLX', 'AVGO', 'ADI', 'ADP', 'COST'],
        'start_date': (2018, 12, 3),
        'end_date': (2019, 1, 2),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 33
        'stocks': ['AMZN', 'ORLY', 'ADBE', 'MRVL', 'DXCM', 'MRNA', 'PEP', 'NVDA', 'TXN', 'GOOG'],
        'start_date': (2019, 5, 29),
        'end_date': (2019, 11, 25),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 34
        'stocks': ['GILD', 'CMCSA', 'ORLY', 'MRNA', 'AMAT', 'META', 'COST', 'ISRG', 'ADP', 'AVGO'],
        'start_date': (2019, 11, 9),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 35
        'stocks': ['REGN', 'LRCX', 'PEP', 'AMAT', 'ADI', 'DXCM', 'TXN', 'MRVL', 'BKNG', 'COST'],
        'start_date': (2019, 5, 4),
        'end_date': (2019, 10, 31),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 36
        'stocks': ['KLAC', 'BKNG', 'ADI', 'NVDA', 'SBUX', 'VRTX', 'GOOG', 'ORLY', 'META', 'PYPL'],
        'start_date': (2018, 3, 9),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 37
        'stocks': ['NFLX', 'META', 'TXN', 'ISRG', 'LRCX', 'KLAC', 'GILD', 'MRVL', 'BKNG', 'AAPL'],
        'start_date': (2018, 12, 10),
        'end_date': (2019, 9, 6),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 38
        'stocks': ['ASML', 'GILD', 'TSLA', 'MRNA', 'CMCSA', 'REGN', 'LRCX', 'AMD', 'COST', 'SBUX'],
        'start_date': (2019, 11, 3),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 39
        'stocks': ['GOOG', 'REGN', 'KLAC', 'QCOM', 'AMZN', 'AMGN', 'ROST', 'SBUX', 'ILMN', 'GILD'],
        'start_date': (2018, 12, 27),
        'end_date': (2019, 12, 22),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 40
        'stocks': ['REGN', 'BKNG', 'GILD', 'ROST', 'MRNA', 'MRVL', 'AMGN', 'TSLA', 'MSFT', 'AMD'],
        'start_date': (2018, 11, 4),
        'end_date': (2018, 12, 4),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 41
        'stocks': ['VRTX', 'NFLX', 'ISRG', 'AMAT', 'ILMN', 'INTU', 'AMZN', 'NVDA', 'AVGO', 'TXN'],
        'start_date': (2018, 6, 17),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 42
        'stocks': ['LRCX', 'GILD', 'NFLX', 'CMCSA', 'DXCM', 'KLAC', 'META', 'ILMN', 'AMGN', 'GOOG'],
        'start_date': (2018, 7, 22),
        'end_date': (2019, 1, 18),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 43
        'stocks': ['ROST', 'NFLX', 'GILD', 'TXN', 'INTU', 'ASML', 'NVDA', 'MU', 'CMCSA', 'ORLY'],
        'start_date': (2018, 4, 10),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 44
        'stocks': ['MU', 'NVDA', 'AMGN', 'ASML', 'PYPL', 'MRVL', 'BKNG', 'QCOM', 'TXN', 'AMZN'],
        'start_date': (2019, 10, 15),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 45
        'stocks': ['QCOM', 'NFLX', 'TSLA', 'INTU', 'META', 'VRTX', 'AMZN', 'CHTR', 'GOOG', 'GILD'],
        'start_date': (2018, 10, 8),
        'end_date': (2019, 7, 5),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 46
        'stocks': ['ORLY', 'CHTR', 'AMZN', 'GOOG', 'AMD', 'NVDA', 'PEP', 'MRNA', 'BKNG', 'ADP'],
        'start_date': (2018, 10, 2),
        'end_date': (2019, 3, 31),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 47
        'stocks': ['QCOM', 'ROST', 'ORLY', 'TSLA', 'INTU', 'AMZN', 'ILMN', 'ISRG', 'DXCM', 'GOOG'],
        'start_date': (2019, 5, 22),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 48
        'stocks': ['DXCM', 'SBUX', 'MRNA', 'ILMN', 'REGN', 'MU', 'CMCSA', 'ISRG', 'KLAC', 'META'],
        'start_date': (2019, 7, 19),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 49
        'stocks': ['AVGO', 'LRCX', 'TXN', 'MSFT', 'INTU', 'AAPL', 'AMAT', 'AMD', 'AMZN', 'PYPL'],
        'start_date': (2018, 7, 23),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
    { # series 50
        'stocks': ['TXN', 'AMAT', 'DXCM', 'AMZN', 'NVDA', 'COST', 'PEP', 'LRCX', 'QCOM', 'MU'],
        'start_date': (2019, 1, 6),
        'end_date': (2020, 1, 1),
        'portfolio_total_value': 1000000,
        'budget': 5,
        'risk_factor': 0.5,
        'confidence_level': 0.95,
        'method': '', # 'cvar' or 'mvo', if not provided, both will be run.
        'solver': '', # 'numpy_minimum_eigensolver', 'qaoa', 'sampling_vqe', if not provided, all will be run.
    },
]