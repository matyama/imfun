import cv2
import numpy as np


def edge_mask(img, line_size, blur_value):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_blur = cv2.medianBlur(gray, blur_value)
  return cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)


def color_quantization(img, ncolors):
    # Transform the image
    data = np.float32(img).reshape((-1, 3))

    # Determine criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

    # Implementing K-Means
    ret, label, center = cv2.kmeans(data, ncolors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    return center[label.flatten()].reshape(img.shape)


def convert(img, line_size=7, blur_value=7, ncolors=9):
    # Create edge mask
    edges = edge_mask(img, line_size, blur_value)

    # Reduce the color palette
    img = color_quantization(img, ncolors)

    # Apply bilateral filter
    blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200,sigmaSpace=200)

    # Combine edge mask with the colored image
    return cv2.bitwise_and(blurred, blurred, mask=edges)

