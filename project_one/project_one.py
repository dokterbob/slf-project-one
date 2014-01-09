from import_data import import_data
from process import process_data
from process import rotate_data
from output import display_data

# Read the data
data = import_data('data.txt')
data = process_data(data)
data = rotate_data(data)
display_data(data)
