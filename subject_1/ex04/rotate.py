import cv2
import numpy as np
from load_image import ft_load


def crop_image(image: np.ndarray, y_start: int, y_end: int,
               x_start: int, x_end: int) -> np.ndarray:
    """
    This function crops/zoom the image to a specified region
    Args:
        image: Input as a NumPy array
        y_start: start row index (top)
        y_end: ending row index (bottom)
        x_start: starting column index (left)
        x_end: endig column index (right)
    Returns the cropped (zoomed) image
    """
    h, w = image.shape[:2]
    if not (0 <= y_start < y_end <= h) or not (0 <= x_start < x_end <= w):
        raise ValueError(f"Crop region out of bounds. Image size ({h}, {w})")

    cropped = image[y_start:y_end, x_start:x_end]

    return cropped


def add_axis_scale(image: np.ndarray, step: int = 100) -> np.ndarray:
    """
    This function adds coordinate scale to the x and y axis of the image
    Args: image: input image, step: interval between marks in pixels
    Returns image with axis labels
    """
    result = image.copy()
    h, w = image.shape[:2]

    if len(image.shape) == 2:
        text_color = (255, 255, 255)
        result = cv2.cvtColor(result, cv2.COLOR_GRAY2BR)
    else:
        text_color = (255, 255, 255)

    for y in range(0, h, step):
        cv2.putText(result, str(y), (5, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)
        cv2.line(result, (0, y), (10, y), text_color, 1)

    for x in range(0, w, step):
        cv2.putText(result, str(x), (x, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)
        cv2.line(result, (x, 0), (x, 10), text_color, 1)

    return result


def ft_transpose(image: np.ndarray) -> np.ndarray:
    """
    This function swaps rows with columns transposing the array and returns
    the rotated array.
    """
    h, w = image.shape[:2]

    if len(image.shape) == 3:
        channels = image.shape[2]
        # emtpy array for the transposed image
        transposed = np.zeros((w, h, channels), dtype=image.dtype)

        for y in range(h):
            for x in range(w):
                transposed[x, y] = image[y, x]
    else:
        transposed = np.zeros((w, h), dtype=image.dtype)

        for y in range(h):
            for x in range(w):
                transposed[x, y] = image[y, x]

    return transposed


def main():
    """
    This program loads an image, crops a square part from it and transpose
    it to display the rotated image of the selected region of the image.
    """
    try:
        img = ft_load("animal.jpeg")

        if len(img.shape) == 3:
            print(f"Number of channels {img.shape[2]} (RGB)")
        else:
            print("Number of channels: 1 (Grayscale)")

        h, w = img.shape[:2]
        print(f"Image dimensions: {w} pixels (width) x {h} pixels (height)")

        crop_size = 400
        y_start = (h // 2) - (crop_size // 2)
        y_end = (h // 2) + (crop_size // 2)
        x_start = (w // 2) - (crop_size // 2)
        x_end = (w // 2) + (crop_size // 2)

        cropped_img = crop_image(img, y_start, y_end, x_start, x_end)
        print(f"Cropped image shape: {cropped_img.shape} or "
              f"{cropped_img.shape[:2]}")
        print("Cropped image data (first/last rows):")
        print(cropped_img)

        transposed_img = ft_transpose(cropped_img)
        print(f"Transposed image shape: {transposed_img.shape} or "
              f"{transposed_img.shape[:2]}")
        print("Transposed image data (firts/last rows):")
        print(transposed_img)

        img_with_scale = add_axis_scale(img)
        transposed_with_scale = add_axis_scale(transposed_img)

        cv2.imshow("Original Image", img_with_scale)
        cv2.imshow("Transposed Image", transposed_with_scale)

        print("\nPress any key to close the image windows...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
