import cv2
import numpy as np

def get_contours_text_image(img):
    blurred = cv2.GaussianBlur(img, (9, 9), 0)

    im_th = cv2.adaptiveThreshold(blurred.copy(), 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

    kernel = np.ones((1,70),np.uint8)
    im_morp2 = cv2.morphologyEx(im_th, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(im_morp2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return sort_contours_by_y_then_x(contours)

def sort_contours_by_y_then_x(contours, tolerance=10):
    filtered_contours = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        
        aspect_ratio = w / h
        if aspect_ratio >= 1 and w > 40 and h > 30:
            filtered_contours.append((contour, (x, y, w, h)))
    
    sorted_contours = sorted(filtered_contours, key=lambda b: (b[1][1] // tolerance, b[1][0]))
    return sorted_contours