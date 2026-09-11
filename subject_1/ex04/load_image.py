import cv2
import numpy as np


def ft_load(path: str) -> np.array:
    '''
    Function to load an image and print its format and pixels content
    in RGB format
    Returns an array
    '''

    if not isinstance(path, str):
        raise TypeError("The path must be a string.")

    img = cv2.imread(path)

    if img is None:
        raise AssertionError(f"Couldn't find the image at {path}")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    print(f"The shape of image is: {img.shape}")

    return img
