import cv2
import numpy as np


def edge_mask(img: np.ndarray, line_size: int, blur_value: int) -> np.ndarray:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)
    return cv2.adaptiveThreshold(
        gray_blur,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        line_size,
        blur_value,
    )


def color_quantization(img: np.ndarray, ncolors: int) -> np.ndarray:
    # Transform the image
    data = np.float32(img).reshape((-1, 3))

    # Determine criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

    # Implementing K-Means
    ret, label, center = cv2.kmeans(
        data, ncolors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
    )
    center = np.uint8(center)
    return center[label.flatten()].reshape(img.shape)


def convert(
    img: np.ndarray, line_size: int = 7, blur_value: int = 7, ncolors: int = 9
) -> np.ndarray:
    """Converts an image to cartoon styled image"""
    # Create edge mask
    edges = edge_mask(img, line_size, blur_value)

    # Reduce the color palette
    img = color_quantization(img, ncolors)

    # Apply bilateral filter
    # TODO: add more params with default values
    blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200, sigmaSpace=200)

    # Combine edge mask with the colored image
    return cv2.bitwise_and(blurred, blurred, mask=edges)


def img2cartoon(in_img: str, out_img: str) -> None:
    """
    Reads an original image from `in_img` path, converts it to a cartoon
    and saves it to `out_img` path.
    """
    img = cv2.imread(in_img)
    cartoon_img = convert(img)
    cv2.imwrite(out_img, cartoon_img)
