"""
RNA Reverse Complement Tool

This script provides a GUI for processing DNA and RNA sequences. 
It calculates reverse, complement, reverse complement, and RNA transcription.
"""

import random
import math
from tkinter import *
import numpy as np
import warnings

# Initialize the main Tkinter window
root = Tk()
root.title("Reverse Complement RNA")
counter = 0  # Counter to manage grid placement of widgets

# Function to replace a nucleotide with its complement (DNA or RNA)
def nucliotidereplace(nuc, ntype):
    """
    Replace a nucleotide with its complement.
    'ntype' specifies DNA ("d") or RNA ("r").
    """
    ret = ""
    if nuc.lower() == "a":  # Adenine pairs with Thymine (or Uracil in RNA)
        ret = "t"
    elif nuc.lower() == "g":  # Guanine pairs with Cytosine
        ret = "c"
    elif nuc.lower() == "c":  # Cytosine pairs with Guanine
        ret = "g"
    elif nuc.lower() == "t" and ntype == "d":  # Thymine pairs with Adenine in DNA
        ret = "a"
    elif nuc.lower() == "t" and ntype == "r":  # Thymine converts to Uracil in RNA
        ret = "u"
    return ret

# Function to verify a nucleotide is valid and return itself (for DNA validation)
def nucliotideplace(nuc, ntype):
    """
    Validate and return the input nucleotide if it's a valid DNA base.
    """
    ret = ""
    if nuc.lower() in "agct":  # Only allow valid DNA bases
        ret = nuc.lower()
    return ret

# Function to reverse a sequence
def frevers(sequence):
    """
    Reverse a DNA sequence and return it in uppercase.
    """
    revsequence = sequence[::-1]  # Reverse the sequence
    return revsequence.upper()  # Convert to uppercase for consistency

# Function to compute the complement of a DNA sequence
def fcompliment(sequence):
    """
    Generate the complement of a DNA sequence.
    """
    compsequence = ""
    for i in range(len(sequence)):
        compsequence += nucliotidereplace(sequence[i], "d")  # DNA-specific complement
    return compsequence.upper()

# Function to transcribe DNA into RNA
def fRNA(sequence):
    """
    Convert a DNA sequence into RNA by replacing Thymine (T) with Uracil (U).
    """
    sequence = sequence.lower()  # Convert to lowercase for consistency
    rsequence = sequence.replace("t", "u")  # Replace T with U
    return rsequence.upper()

# Function to ensure input is only valid DNA
def Only_DNA(sequence):
    """
    Filter a sequence to allow only valid DNA bases (A, G, C, T).
    """
    sequences = ""
    for i in range(len(sequence)):
        sequences += nucliotideplace(sequence[i], "d")  # Validate each nucleotide
    return sequences.upper()

# Main function to handle user input and update GUI outputs
def runfolder():
    """
    Process input DNA sequence and display reverse, complement, reverse complement,
    RNA transcription, and reverse complement RNA in the GUI.
    """
    seq = inputseq.get()  # Get input sequence from the Entry widget
    sequence = Only_DNA(seq)  # Filter sequence to valid DNA
    compliments = fcompliment(sequence)  # Generate DNA complement
    compliment.delete('1.0', END)  # Clear the previous output
    compliment.insert(END, compliments)  # Display the result
    reverss = frevers(sequence)  # Generate reversed sequence
    revers.delete('1.0', END)
    revers.insert(END, reverss)
    revcompliments = fcompliment(frevers(sequence))  # Reverse complement
    revcompliment.delete('1.0', END)
    revcompliment.insert(END, revcompliments)
    rnas = fRNA(sequence)  # RNA transcription
    RNA.delete('1.0', END)
    RNA.insert(END, rnas)
    revcompRNAs = fRNA(fcompliment(frevers(sequence)))  # Reverse complement RNA
    revcompRNA.delete('1.0', END)
    revcompRNA.insert(END, revcompRNAs)

# Input validation callback for the Entry widget
vcmd = (root.register(Only_DNA), '%S')

# Widgets for the GUI
inputseqlable = Label(root, text="Insert sequence", font='David 12 bold')
reverslable = Label(root, text="Reverse", font='David 12 bold')
complimentlable = Label(root, text="Complement", font='David 12 bold')
revcomplimentlable = Label(root, text="Reverse Complement", font='David 12 bold')
RNAlable = Label(root, text="RNA", font='David 12 bold')
revcompRNAlable = Label(root, text="Reverse Complement RNA", font='David 12 bold')

# Input field for DNA sequence
inputseq = Entry(root, width=100, validate='focusout', vcmd=vcmd)

# Text boxes for displaying results
revers = Text(root, bd=3, bg="gray", height=1, width=70)
compliment = Text(root, bd=3, bg="gray", height=1, width=70)
revcompliment = Text(root, bd=3, bg="gray", height=1, width=70)
RNA = Text(root, bd=3, bg="gray", height=1, width=70)
revcompRNA = Text(root, bd=3, bg="gray", height=1, width=70)

# Button to execute sequence processing
runn = Button(root, text="Run", command=lambda: runfolder())

# Place widgets in the GUI grid
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

# Set window size and start the Tkinter main loop
size = "780x190"
root.geometry(size)
root.mainloop()
