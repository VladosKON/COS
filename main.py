from tkinter.filedialog import askopenfilename

import numpy as np
from cv2 import cv2
filename = askopenfilename()
img_src = cv2.imread(filename)

# kernel_low_pass = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]) 
kernel_low_pass = np.array([[1/16, 1/8, 1/16], [1/8, 1/4, 1/8], [1/16, 1/8, 1/16]])
kernel_high_pass = np.array([[0.0, -1.0, 0.0], [-1.0,  4.0, -1.0], [0.0, -1.0, 0.0]])
kernel_horizontal = np.array([[-1.0, -1.0], [2.0, 2.0], [-1.0, -1.0]])


kernel_low_pass = kernel_low_pass/sum(kernel_low_pass)
img_rst = cv2.filter2D(img_src,-1,kernel_low_pass)
cv2.imwrite('results/low_pass_filter.jpg',img_rst)

kernel_high_pass = kernel_high_pass/(np.sum(kernel_high_pass) if np.sum(kernel_high_pass)!=0 else 1)
img_rst = cv2.filter2D(img_src,-1,kernel_high_pass)
cv2.imwrite('results/high_pass_filter.jpg',img_rst)

kernel_horizontal = kernel_horizontal/(np.sum(kernel_horizontal) if np.sum(kernel_horizontal)!=0 else 1)
img_rst = cv2.filter2D(img_src,-1,kernel_horizontal)
cv2.imwrite('results/horizontal.jpg',img_rst)
