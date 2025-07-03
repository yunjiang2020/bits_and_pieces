# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:45:16 2024

@author: yunji
"""
import numpy as np
import cv2
from scipy.stats import spearmanr

# Load the TIFF images
img_1 = cv2.imread('4h_vin_A3_Top Slide_R_p00_0_A01f01d1.TIF')
img_2 = cv2.imread('4h_vin_A3_Top Slide_R_p00_0_A01f01d2.TIF')

# Check if images are loaded properly
if img_1 is None or img_2 is None:
    print("Error: One or both images could not be loaded. Please check the file paths.")
else:
    print("213 500nM")

    # Flatten images to 1D arrays
    img_1_flat = img_1.ravel()
    img_2_flat = img_2.ravel()

    # Pearson Correlation Coefficient
    pearson_corr = np.corrcoef(img_1_flat, img_2_flat)[0, 1]
    print("Pearson Correlation Coefficient:", round(pearson_corr, 4))

    # Spearman Correlation Coefficient
    spearman_corr, _ = spearmanr(img_1_flat, img_2_flat)
    print("Spearman Correlation Coefficient:", round(spearman_corr, 4))
