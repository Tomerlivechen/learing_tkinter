# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:20:30 2023

@author: tomer
"""

from tkinter import *

root = Tk()
root.title("Main Window")
root.geometry("660x460")


def pistol_check(sequence):
    # Pistol
    # nnnnnnNNNNNNGUNNNN
    # 12_GU_4
    index = 0
    viable_sequence = 0
    while index <= len(sequence) or index != -1:
        index = sequence.find("GU", index, len(sequence))
        print(index)
        if index >= 12 and len(sequence)-index >= 6:
            print(sequence[index-12:index+6])
            print("Pistol")
            set_buttons(pistol_button, [3, 1])
            return True
        else:
            if index >= 0:
                index += 1
            else:
                forget_buttons(pistol_button)
                return False


def pistol_II_check(sequence):
    # Pistol II
    # nnnnnnNNNNNNNNNNGUNNNN
    # 16_GU_4
    index = 0
    viable_sequence = 0
    while index <= len(sequence) or index != -1:
        index = sequence.find("GU", index, len(sequence))
        print(index)
        if index >= 16 and len(sequence)-index >= 6:
            print(sequence[index-16:index+6])
            print("Pistol II")
            set_buttons(pistol_II_button, [4, 1])
            return True
        else:
            if index >= 0:
                index += 1
            else:
                forget_buttons(pistol_II_button)
                return False


def Minimal_Hammerhead_check(sequence):
    # Minimal Hammerhead
    # nnnnnnnnnnNNGUCNNNNnnnnnnnnnn
    # 12_GUC_14
    index = 0
    viable_sequence = 0
    while index <= len(sequence) or index != -1:
        index = sequence.find("GUC", index, len(sequence))
        print(index)
        if index >= 12 and len(sequence)-index >= 17:
            print(sequence[index-12:index+17])
            print("Minimal Hammerhead")
            set_buttons(Minimal_Hammerhead_button, [5, 1])
            return True
        else:
            if index >= 0:
                index += 1
            else:
                forget_buttons(Minimal_Hammerhead_button)
                return False


def Extended_Hammerhead_check(sequence):
    # Extended Hammerhead
    # nnnnnnnnnnNNNGUCNNNNNNNnnnnnnnn
    # 13_GUC_15
    index = 0
    viable_sequence = 0
    while index <= len(sequence) or index != -1:
        index = sequence.find("GUC", index, len(sequence))
        print(index)
        if index >= 13 and len(sequence)-index >= 15:
            print(sequence[index-13:index+18])
            print("Extended Hammerhead")
            set_buttons(Extended_Hammerhead_button, [6, 1])
            return True
        else:
            if index >= 0:
                index += 1
            else:
                forget_buttons(Extended_Hammerhead_button)
                return False


def Theophylline_Aptazyme_check(sequence):
    # Theophylline Aptazyme
    # nnnnnnnnnnNNNGUCNNNNNNnnnnnnnnnnnn
    # 13_GUC_18
    index = 0
    viable_sequence = 0
    while index <= len(sequence) or index != -1:
        index = sequence.find("GUC", index, len(sequence))
        print(index)
        if index >= 13 and len(sequence)-index >= 21:
            print(sequence[index-13:index+21])
            print("Theophylline Aptazyme")
            set_buttons(Theophylline_Aptazyme_button, [7, 1])
            return True
        else:
            if index >= 0:
                index += 1
            else:
                forget_buttons(Theophylline_Aptazyme_button)
                return False


def set_buttons(button_name, grid_position):
    button_name.grid(row=grid_position[0], column=grid_position[1], sticky="w")


def forget_buttons(button_name):
    button_name.grid_forget()


def check():
    potential_sequence = binding_site.get().upper()
    pistol_check(potential_sequence)
    pistol_II_check(potential_sequence)
    Minimal_Hammerhead_check(potential_sequence)
    Extended_Hammerhead_check(potential_sequence)
    Theophylline_Aptazyme_check(potential_sequence)


# widget
label_binding_site = Label(root, text="Enter a potential Ribozyme")

check_compatibelity = Button(
    root, text="Check Compatibility", command=lambda: check())

binding_site = Entry(root, width=50)

pistol_button = Button(root, text="Pistol Ribozyme", command=lambda: check())
pistol_II_button = Button(
    root, text="PistolII Ribozyme", command=lambda: check())
Minimal_Hammerhead_button = Button(
    root, text="Minimal Hammerhead Ribozyme", command=lambda: check())
Extended_Hammerhead_button = Button(
    root, text="Extended Hammerhead Ribozyme", command=lambda: check())
Theophylline_Aptazyme_button = Button(
    root, text="Theophylline Aptazyme Ribozyme", command=lambda: check())


# placment

counter = 0
label_binding_site.grid(row=counter, column=1, columnspan=4)
counter += 1
binding_site.grid(row=counter, column=1, columnspan=4, sticky="e")
counter += 1
check_compatibelity.grid(row=counter, column=1, columnspan=4, sticky="e")


# Run system
root.mainloop()
