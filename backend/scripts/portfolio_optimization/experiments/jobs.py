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
