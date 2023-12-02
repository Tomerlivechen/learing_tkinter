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
            return True
        else:
            if index >= 0:
                index += 1
            else:
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
            return True
        else:
            if index >= 0:
                index += 1
            else:
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
            return True
        else:
            if index >= 0:
                index += 1
            else:
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
            return True
        else:
            if index >= 0:
                index += 1
            else:
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
            return True
        else:
            if index >= 0:
                index += 1
            else:
                return False


def check():
    potential_sequence = binding_site.get()
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

# placment

counter = 0
label_binding_site.grid(row=counter, column=0)
counter += 1
binding_site.grid(row=counter, column=0)
counter += 1
check_compatibelity.grid(row=counter, column=0)


# Run system
root.mainloop()
