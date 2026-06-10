import numpy as np


def ft_invert(array) -> np.ndarray:
    """
    Function to invert the image colors
    """
    result = 255 - array
    print(f"Shape after invert: {result.shape}")
    print(result)

    return result


def ft_red(array) -> np.ndarray:
    """
    Function to apply a red filter to the image
    """
    result = np.zeros(array.shape, dtype=array.dtype)
    result[:, :, 0] = array[:, :, 0]

    return result


def ft_green(array) -> np.ndarray:
    """
    Function to apply the green filter to the image
    """
    result = np.zeros(array.shape, dtype=array.dtype)
    result[:, :, 1] = array[:, :, 1]

    return result


def ft_blue(array) -> np.ndarray:
    """
    Function to apply the blue filter to the image
    """
    result = np.zeros(array.shape, dtype=array.dtype)
    result[:, :, 1] = array[:, :, 1]

    return result


def ft_grey(array) -> np.ndarray:
    """
    Function to apply the grey filter to the image
    """
    return np.mean(array, axis=2).astype(array.dtype)
