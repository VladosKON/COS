import tkinter as tk
import tkinter.filedialog as fd

import numpy as np
from cv2 import cv2

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_file = tk.Button(self, text="Выбрать файл",
                             command=self.choose_file)
        btn_file.pack(padx=60, pady=10)

    def choose_file(self):
        filetypes = (("Изображение", "*.jpg *.gif *.png"),
                     ("Любой", "*"))
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/data/",
                                      filetypes=filetypes)
        if filename:
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

if __name__ == "__main__":
    app = App()
    app.title("7")
    app.mainloop()