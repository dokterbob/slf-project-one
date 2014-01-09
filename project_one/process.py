import numpy as np


def process_data(data):
    """
    Process data. Expects a list of lists with numbers.

    * Convert data to 2D numpy array
    * Rotate the 2D array
    """
    # Convert to Numpy float32
    data = np.array(data, np.float32)

    # Normalise data
    if data == -9999:
        data = 0
    else: data /= 9999

    # Rotate the array by 90 degrees
    data = np.rot90(data)

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
