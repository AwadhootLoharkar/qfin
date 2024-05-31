import csv

def read_stock_symbols(filepath, num_symbols=10):
    stock_symbols = []
    with open(filepath, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for i, row in enumerate(csvreader, start=1):
            if num_symbols and i > num_symbols:
                break
            stock_symbols.append(row[1])
    return stock_symbols
    