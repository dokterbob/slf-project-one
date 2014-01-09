import numpy as np

@np.vectorize
def clean_values(value):
    """
    Process data. Expects a list of lists with numbers.
    * normalises a number
    """

    if value == -9999:
        value = np.NaN

    return value

def normalize(data):
    """
    Process data. Expects a list of lists with numbers.
    """
    # Normalize it!
    data = data / np.max(data)

    return data

def process_data(data):
    """
    Process data. Expects a list of lists with numbers.

    * Convert data to 2D numpy array
    * Rotate the 2D array
    """
    # Convert to Numpy float32
    data = np.array(data, np.float32)

    data = clean_values(data)

    return data

def rotate_data(data):
    """
    Rotate data. Requires numpy 2D array.
    """
    if 'ndarray' in str(type(data)) == 'False':
        data = process_data(data)

    #ask user what he wants
    nrotation = raw_input("How many 90deg rotations you want? (e.g. -1 for 90deg clockwise) ")
    nrotation = int(nrotation)

    #do what he is up for!
    data = np.rot90(data, nrotation)

    return data
