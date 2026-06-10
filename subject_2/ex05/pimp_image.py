import cv2
import numpy as np
from load_image import ft_load

def ft_invert(image: np.ndarray) -> np.ndarray:
    """
    Function to invert the image colors
    """
    h, w = image.shape[:2]

    if len(image) == 3:
        channels = image.shape[2]
        inverted = np.zeros((h, w, channels), dtype=image.dtype)

        for y in range(h):
            for x in range(w):
                for c in range(channels):
                    original = image[y, x, c]
                    inverted_value = 255 - original
                    inverted[y, x, c] = inverted_value
    else:
        inverted = np.zeros((h, w), dtype=image.dtype)
        for y in range(h):
            for x in range(w):
                inverted[y, x] = 255 - image[y, x]

    return inverted

def ft_red(image: np.ndarray) -> np.ndarray:
   """
   Function to apply a red filter to the image
   """


def ft_green(array) -> array:
    pass

def ft_blue(array) -> array:
    pass

def ft_grey(array) -> array:
    pass
