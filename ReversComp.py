# -*- coding: utf-8 -*-

"""
Created on Thu Feb  9 14:16:22 2023

@author: tomer
"""

import random
import math
from tkinter import *
import numpy as np
import warnings
root = Tk()
root.title("Revers compliment RNA")
counter = 0


def nucliotidereplace(nuc, ntype):
    ret = ""
    if nuc.lower() == "a":
        ret = "t"
    elif nuc.lower() == "g":
        ret = "c"
    elif nuc.lower() == "c":
        ret = "g"
    elif nuc.lower() == "t" and ntype == "d":
        ret = "a"
    elif nuc.lower() == "t" and ntype == "r":
        ret = "u"
    return ret


def nucliotideplace(nuc, ntype):
    ret = ""
    if nuc.lower() == "a":
        ret = "a"
    elif nuc.lower() == "g":
        ret = "g"
    elif nuc.lower() == "c":
        ret = "c"
    elif nuc.lower() == "t":
        ret = "t"
    return ret


def frevers(sequence):
    revsequence = sequence[::-1]
    return revsequence.upper()


def fcompliment(sequence):
    compsequence = ""
    for i in range(len(sequence)):
        compsequence += nucliotidereplace(sequence[i], "d")
    return compsequence.upper()


def fRNA(sequence):
    sequence = sequence.lower()
    rsequence = sequence.replace("t", "u")
    return rsequence.upper()


def Only_DNA(sequence):
    sequences = ""
    for i in range(len(sequence)):
        sequences += nucliotideplace(sequence[i], "d")
    return sequences.upper()


def runfolder():
    seq = inputseq.get()
    sequence = Only_DNA(seq)
    compliments = fcompliment(sequence)
    compliment.delete('1.0', END)
    compliment.insert(END, compliments)
    reverss = frevers(sequence)
    revers.delete('1.0', END)
    revers.insert(END, reverss)
    revcompliments = fcompliment(frevers(sequence))
    revcompliment.delete('1.0', END)
    revcompliment.insert(END, revcompliments)
    rnas = fRNA(sequence)
    RNA.delete('1.0', END)
    RNA.insert(END, rnas)
    revcompRNAs = fRNA(fcompliment(frevers(sequence)))
    revcompRNA.delete('1.0', END)
    revcompRNA.insert(END, revcompRNAs)
    # messagebox.showerror(title="Not DNA", message="Please correct sequence",)


vcmd = (root.register(Only_DNA), '%S')

# Wigets

inputseqlable = Label(root, text="Insert sequence", font='David 12 bold')
reverslable = Label(root, text="Revers", font='David 12 bold')
complimentlable = Label(root, text="Compliment", font='David 12 bold')
revcomplimentlable = Label(
    root, text="Revers compliment", font='David 12 bold')
RNAlable = Label(root, text="RNA", font='David 12 bold')
revcompRNAlable = Label(
    root, text="Revers compliment RNA", font='David 12 bold')


inputseq = Entry(root, width=100, validate='focusout', vcmd=vcmd)
revers = Text(root, bd=3, bg="gray", height=1, width=70)
compliment = Text(root, bd=3, bg="gray", height=1, width=70)
revcompliment = Text(root, bd=3, bg="gray", height=1, width=70)
RNA = Text(root, bd=3, bg="gray", height=1, width=70)
revcompRNA = Text(root, bd=3, bg="gray", height=1, width=70)


runn = Button(root, text="Run", command=lambda: runfolder())


# Placment

inputseqlable.grid(row=counter, column=0)
counter += 1
inputseq.grid(row=counter, column=0)
counter += 1
revers.grid(row=counter, column=0)
reverslable.grid(row=counter, column=1, sticky="w")
counter += 1
compliment.grid(row=counter, column=0)
complimentlable.grid(row=counter, column=1, sticky="w")
counter += 1
revcompliment.grid(row=counter, column=0)
revcomplimentlable.grid(row=counter, column=1, sticky="w")
counter += 1
RNA.grid(row=counter, column=0)
RNAlable.grid(row=counter, column=1, sticky="w")
counter += 1
revcompRNA.grid(row=counter, column=0)
revcompRNAlable.grid(row=counter, column=1, sticky="w")
counter += 1
runn.grid(row=counter, column=0, sticky="n")
size = "780x190"
root.geometry(size)
# Run system
root.mainloop()
