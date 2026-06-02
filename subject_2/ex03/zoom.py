import cv2
import numpy as np
from load_image import ft_load


def zoom_image(image: np.ndarray, y_start: int, y_end: int, x_start: int,
               x_end: int, scale_factor: float = 2.0) -> np.ndarray:
    """
    This function will crop and scale the image to a specified region.
    Arguments:
        image: image as numpy array
        y_start: Starting row index (top)
        y_end: Ending row index (bottom)
        x_start: Starting column index (left)
        x_end: Ending column index (right)
        scale_factor: zoom factor to scale the croped part of the image

    This function returns the cropped/zoomed image.
    """
    # validate the coordinates
    h, w = image.shape[:2]
    if not (0 <= y_start < y_end <= h) or not (0 <= x_start < x_end <= w):
        raise ValueError(f"Crop region out of bounds. Image size: ({h}, {w})")
    
    cropped = image[y_start:y_end, x_start:x_end]
    
    new_size = (int(cropped.shape[1] * scale_factor),
                int(cropped.shape[0] * scale_factor))

    zoomed = cv2.resize(cropped, new_size, interpolation=cv2.INTER_LINEAR)

    return zoomed

def add_axis_scale(image: np.ndarray, step: int = 100) -> np.ndarray:
    """
    This function adds coordinate scale to the x and y axis of the image
    Args: image: input image, step: interval between marks in pixels
    Returns image with axis labels
    """
    result = image.copy()
    h, w = image.shape[:2]

    # Check if image is grayscale or not to define color of text
    if len(image.shape) == 2:
        text_color = (255, 255, 255)
        result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
    else:
        text_color = (255, 255, 255)

    # Add the numbers to the x and y axis
    for y in range(0, h, step):
        cv2.putText(result, str(y), (5, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)
        cv2.line(result, (0, y), (10, y), text_color, 1)

    for x in range(0, w, step):
        cv2.putText(result, str(x), (x, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1)
        cv2.line(result, (x, 0), (x, 10), text_color, 1)

    return result


def main():
    try:
        # first load image with ft_load
        img = ft_load("animal.jpeg")
        print(f"Original image shape: {img.shape}")

        # print channels
        if len(img.shape) == 3:
            print(f"Number of channels: {img.shape[2]} (RGB)")
        else:
            print(f"Number of channels: 1 (Grayscale)")

        print("Original image data (first/last rows):")
        print(img)

        h, w = img.shape[:2]
        print(f"Image dimensions: {w} pixels (width) x {h} pixels (height)")

        # calculate the coordinates of the center to crop
        zoom_size = 400
        y_start = (h // 2) - (zoom_size // 2)
        y_end = (h // 2) + (zoom_size // 2)
        x_start = (w // 2) - (zoom_size // 2)
        x_end = (w // 2) + (zoom_size // 2)

        zoomed_img = zoom_image(img, y_start, y_end, x_start, x_end)
        print(f"\nZoomed image shape: {zoomed_img.shape}")
        print("Zoomed image data (first/last rows):")
        print(zoomed_img)

        img_with_scale = add_axis_scale(img)
        zoomed_with_scale = add_axis_scale(zoomed_img)

        cv2.imshow("Original Image", img_with_scale)
        cv2.imshow("Zoomed Image", zoomed_with_scale)

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
