# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:03:26 2023

@author: tomer
"""
from tkinter import *


def open_window_1(button_name):
    new_window_1 = Toplevel(root)
    new_window_1.title("New Window 1")
    new_window_1.geometry("660x460")

    label = Label(new_window_1, text="This is a new window 1!")
    label.pack()
    # Disable the button in the main window
    button_name.config(state=DISABLED)
    new_window_1.protocol("WM_DELETE_WINDOW",
                          lambda: on_new_window_close(new_window_1, button_name))


def open_window_2(button_name):
    new_window_2 = Toplevel(root)
    new_window_2.title("New Window 2")
    new_window_2.geometry("660x460")

    label = Label(new_window_2, text="This is a new window 2!")
    label.pack()
    button_name.config(state=DISABLED)
    new_window_2.protocol("WM_DELETE_WINDOW",
                          lambda: on_new_window_close(new_window_2, button_name))


def on_new_window_close(window_name, button_name):
    # Enable the button in the main window when the new window is closed
    button_name.config(state=NORMAL)
    window_name.destroy()


# Create the main window
root = Tk()
root.title("Main Window")
root.geometry("660x460")
# Button to open a new window
window_1_button = Button(root, text="Open Window 1",
                         command=lambda: open_window_1(window_1_button))
window_2_button = Button(root, text="Open Window 2",
                         command=lambda: open_window_2(window_2_button))
window_1_button.grid(row=0, column=0)
window_2_button.grid(row=0, column=1)

# Run the main loop
root.mainloop()
