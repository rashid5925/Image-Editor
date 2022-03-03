from tkinter import *
import cv2 as cv

root = Tk()
root.title("Image Editor")
root.geometry("700x450")

path = ""


def submit():
    global path
    path = entry.get()
    root.destroy()
    win = Tk()
    win.title("Image Editor")
    win.geometry("450x500")

    def gray():
        global path
        image = cv.imread(path)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        cv.imshow("Gray", gray)
        cv.imwrite("image_g.jpg", gray)

    def blur():
        global path
        image = cv.imread(path)
        blur_i = cv.GaussianBlur(image, (7, 7), cv.BORDER_DEFAULT)
        cv.imshow("Blur", blur_i)
        cv.imwrite("image_b.jpg", blur_i)

    def edge():
        global path
        image = cv.imread(path)
        edge_i = cv.Canny(image, 125, 175)
        cv.imshow("Gray", edge_i)
        cv.imwrite("image_e.jpg", edge_i)

    def cartoon():
        global path
        image = cv.imread(path)
        gray_c = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        gray_c = cv.medianBlur(gray_c, 5)
        edges = cv.adaptiveThreshold(gray_c, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)
        color = cv.bilateralFilter(image, 9, 250, 250)
        cartoon_1 = cv.bitwise_and(color, color, mask=edges)
        cv.imshow("Cartoon", cartoon_1)
        cv.imwrite("image_c.jpg", cartoon_1)

    button_g = Button(win, text="Convert to Gray", font=("Arial", 20), bg="#eb9834", command=gray)
    button_g.grid(row=0, column=0, ipady=10, ipadx=20, pady=20, padx=100)
    button_b = Button(win, text="Blur", font=("Arial", 20), bg="#eb9834", command=blur)
    button_b.grid(row=1, column=0, ipady=10, ipadx=93, pady=20, padx=100)
    button_e = Button(win, text="Drawing", font=("Arial", 20), bg="#eb9834", command=edge)
    button_e.grid(row=2, column=0, ipady=10, ipadx=68, pady=20, padx=100)
    button_r = Button(win, text="Cartoon", font=("Arial", 20), bg="#eb9834", command=cartoon)
    button_r.grid(row=3, column=0, ipady=10, ipadx=68, pady=20, padx=100)

    win.mainloop()


label = Label(root, text="IMAGE EDITOR", font=("Arial", 32), fg="Blue")
label.grid(row=0, column=0, padx=80, pady=10)

label_p = Label(root, text="Enter path to image with name", font=("Arial", 12), fg="green")
label_p.grid(row=1, column=0, padx=80, pady=50)

entry = Entry(root, font=("Arial", 22), width=40)
entry.grid(row=2, column=0, ipady=10, padx=30)

button = Button(root, text="Submit", font=("Arial", 20), bg="#eb9834", command=submit)
button.grid(row=3, column=0, ipady=10, ipadx=20, pady=20, padx=30)

root.mainloop()
