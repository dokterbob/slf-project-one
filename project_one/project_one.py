# System imports first
import sys

# Module (local) imports
from import_data import import_data
from process import process_data, normalize, rotate_data
from output import plot_data


def main(argv=None):
    """ Main function, executed when running 'project_one'. """
    # Read the data
    data = import_data('data.txt')
    data = process_data(data)
    # data = normalize(data)
    # data = rotate_data(data)
    plot_data(data)

# If we're being run with `python project_one.py`, execute main() and exit
# afterwards with the return value of main().
if __name__ == "__main__":
    sys.exit(main())
