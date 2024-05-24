import csv

def read_stock_symbols(csv_filename, num_symbols=None):
    stock_symbols = []
    with open(csv_filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for i, row in enumerate(csvreader, start=1):
            if num_symbols and i > num_symbols:
                break
            stock_symbols.append(row[1])
    return stock_symbols
    