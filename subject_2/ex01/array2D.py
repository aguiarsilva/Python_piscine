import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    This function takes an array and returns the truncated
    version of the array sliced based on the start and end arguments
    '''
    if not isinstance(family, list) or not isinstance(start, int)\
            or not isinstance(end, int):
        raise TypeError("family must be a list, start and end must be ints")

    if not family:
        raise ValueError("family is empty")

    if not all(len(row) == len(family[0]) for row in family):
        raise ValueError("Matrix size is not correct")

    arr = np.array(family)

    print(f"My shape is :  {arr.shape}")

    sliced_array = arr[start:end]

    print(f"My new shape is : {sliced_array.shape}")

    return sliced_array.tolist()
