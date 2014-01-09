from import_data import import_data
from process import process_data, normalize, rotate_data
from output import plot_data

# Read the data
data = import_data('data.txt')
data = process_data(data)
data = normalize(data)
data = rotate_data(data)
plot_data(data)
