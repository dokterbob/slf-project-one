from import_data import import_data
from process import process_data, normalize

# Read the data
data = import_data('data.txt')
data = process_data(data)
data = normalize(data)
