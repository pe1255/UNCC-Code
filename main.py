import tkinter as tk
import PyPDF2
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import asksaveasfile
from tkinter import *
import io
import numpy as np
import yaml
import matplotlib.pyplot as plt


# =======================================


def yamlConstructor(loader, node):
    mapping = loader.construct_mapping(node, deep=True)

    mat = np.array(mapping["data"])

    if mapping["cols"] > 1:

        mat.resize(mapping["rows"], mapping["cols"])

    else:

        mat.resize(mapping["rows"], )

    return mat


def fig2img(fig):
    """Convert a Matplotlib figure to a PIL Image and return it"""

    #    import io

    buf = io.BytesIO()

    fig.savefig(buf)

    buf.seek(0)

    img = Image.show(buf)

    return img


# logo this is where the graph will be located need to fix

def start_plot():
    x = [10, 20, 30]

    y = [10, 50, 7]

    plt.plot(x, y)

    plt.xlabel("X-axis")

    plt.ylabel("Z value")

    plt.title("GUI Graph")

    plt.show()

    return


def save_file():
    file = asksaveasfile(initialfile='Untitled.txt',
                         defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    plt.savefig("fig.png",bbox_inches="tight")
    return


def clear_text():
    diameter.delete(0, END)
    plt.close()
    x0 = [0, 0, 0]

    y0 = [0, 0, 0]

    plt.plot(x0, y0)

    plt.show()
    return


# =========================================

# MAIN PROGRAM

# ========================================

root = tk.Tk()
root.title("EPRI")
# root.wm_iconbitmap('epri.png')
root.geometry('1000x800')

# =============================


# Diameter input
instructions = tk.Label(root, text="Diameter of pipe: ", font="Raleway")

instructions.place(x=200, y=450)

diameter = tk.Entry(root, width=20)

diameter.place(x=340, y=450)

x = [10, 20, 30]

y = [10, 50, 7]



# start button
startText = tk.StringVar()

startButton = tk.Button(root, textvariable=startText, font="Raleway", bg="orange", fg="black", height=2, width=10)

Button(startButton, text="Start", command=start_plot, font=('Helvetica bold', 10)).pack(pady=5)

startButton.place(x=200, y=600)

# clear button
clearText = tk.StringVar()
clearButton = tk.Button(root, textvariable=clearText, font="Raleway", bg="orange", fg="black", height=2, width=10)

clearText.set("Clear")

clearButton.place(x=400, y=600)

Button(clearButton, text="Clear", command=clear_text, font=('Helvetica bold', 10)).pack(pady=5)

# save button
saveText = tk.StringVar()

saveButton = tk.Button(root, textvariable=saveText, command=lambda: save_file(), font="Raleway", bg="orange",
                       fg="black", height=2, width=10)

saveText.set("Save")

saveButton.place(x=600, y=600)

root.mainloop()
