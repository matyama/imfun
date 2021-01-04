import cv2
import numpy as np

LINE_SIZE = 7
BLUR_VALUE = 7
COLORS = 9
FILTER_DIAMETER = 7
SIGMA_COLOR = 200
SIGMA_SPACE = 200


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


def color_quantization(img: np.ndarray, colors: int) -> np.ndarray:
    # Transform the image
    data = np.float32(img).reshape((-1, 3))

    # Determine criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

    # Implementing K-Means
    ret, label, center = cv2.kmeans(
        data, colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
    )
    center = np.uint8(center)
    return center[label.flatten()].reshape(img.shape)


def convert(
    img: np.ndarray,
    line_size: int = LINE_SIZE,
    blur_value: int = BLUR_VALUE,
    colors: int = COLORS,
    filter_diameter: int = FILTER_DIAMETER,
    sigma_color: int = SIGMA_COLOR,
    sigma_space: int = SIGMA_SPACE,
) -> np.ndarray:
    """Converts an image to cartoon styled image"""
    # Create edge mask
    edges = edge_mask(img, line_size, blur_value)

    # Reduce the color palette
    img = color_quantization(img, colors)

    # Apply bilateral filter
    blurred = cv2.bilateralFilter(
        img,
        d=filter_diameter,
        sigmaColor=sigma_color,
        sigmaSpace=sigma_space,
    )

    # Combine edge mask with the colored image
    return cv2.bitwise_and(blurred, blurred, mask=edges)
