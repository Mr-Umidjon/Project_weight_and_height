import csv
import pathlib

def read_csv_data(file_path):
    """
    Read csv file
    Args:
        file_path(str): file path
    Returns:
        list: data split row
    """
    result_data = []
    # WRITE YOUR CODE HERE
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for data in reader:
            result_data.append(data)
    return result_data

print(read_csv_data("data/weight-height.csv"))