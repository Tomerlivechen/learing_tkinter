# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:57:41 2023

@author: tomer
"""

import math
import random
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("TALE Construction")
root.geometry("660x520")

# varyables

catalist_poiner = 0
catalist_options = ["FokI", "FokI duplex", "DddA+UDG",
                    "Max10-TadA"]
catalist_type = IntVar()
NLS_options = ["SV40 NLS", "nucleoplasmin NLS"]
NLS_value1 = IntVar()
NLS_value2 = IntVar()
catalist_selection = ""
Talen_prot_sequence = ""
Talen_target_sequence = ""

# Segments

# Nucleotide binding

# HD->C NI->A NG->T NH->G

pHD = ["LTPDQVVAIASHDGGKQALETVQRLLPVLCQDHG", "LTPEQVVAIASHDGGKQALETVQRLLPVLCQAHG",
       "LTPDQVVAIASHDGGKQALETVQRLLPVLCQAHG", "LTPAQVVAIASHDGGKQALETVQRLLPVLCQDHG"]
pNI = ["LTPDQVVAIASNIGGKQALETVQRLLPVLCQDHG", "LTPEQVVAIASNIGGKQALETVQRLLPVLCQAHG",
       "LTPDQVVAIASNIGGKQALETVQRLLPVLCQAHG", "LTPAQVVAIASNIGGKQALETVQRLLPVLCQDHG"]
pNG = ["LTPDQVVAIASNGGGKQALETVQRLLPVLCQDHG", "LTPEQVVAIASNGGGKQALETVQRLLPVLCQAHG",
       "LTPDQVVAIASNGGGKQALETVQRLLPVLCQAHG", "LTPAQVVAIASNGGGKQALETVQRLLPVLCQDHG"]
pNH = ["LTPDQVVAIASNHGGKQALETVQRLLPVLCQDHG", "LTPEQVVAIASNHGGKQALETVQRLLPVLCQAHG",
       "LTPDQVVAIASNHGGKQALETVQRLLPVLCQAHG", "LTPAQVVAIASNHGGKQALETVQRLLPVLCQDHG"]

# Catalists
FokI = "QLVKSELEEKKSELRHKLKYVPHEYIELIEIARNSTQDRILEMKVMEFFMKVYGYRGKHLGGSRKPDGAIYTVGSPIDYGVIVDTKAYSGGYNLPIGQADEMQRYVEENQTRNKHINPNEWWKVYPSSVTEFKFLFVSGHFKGNYKAQLTRLNHITNCNGAVLSVEELLIGGEMIKAGTLTLEEVRRKFNNGEINFRS"
FokID = "SIVAQLSRPDPALAALTNDHLVALACLGGRPALDAVKKGLPHAPELIRRINRRIPERTSHRVALKQLVKSELEEKKSELRHKLKYVPHEYIELIEIARNSTQDRILEMKVMEFFMKVYGYRGKHLGGSRKPDGAIYTVGSPIDYGVIVDTKAYSGGYNLPIGQADEMQRYVEENQTRNKHINPNEWWKVYPSSVTEFKFLFVSGHFKGNYKAQLTRLNHITNCNGAVLSVEELLIGGEMIKAGTLTLEEVRRKFNNGEINFGSGSGSGSITRTTNPRNVVPKIYMSAGSIPLTTHITNSIQPTLWTIGSINGVAPLAKSIKLGIPVTGSAYTDQTTAMVRKKVSVFMGSGSGSGSSQLVKSELEEKKSELRHKLKYVPHEYIELIEIARNSTQDRILEMKVMEFFMKVYGYRGKHLGGSRKPDGAIYTVGSPIDYGVIVDTKAYSGGYNLPIGQADEMQRYVEENQTRNKHINPNEWWKVYPSSVTEFKFLFVSGHFKGNYKAQLTRLNHITNCNGAVLSVEELLIGGEMIKAGTLTLEEVRRKFNNGEINF"
DddA = "GSGSYALGPYQISAPQLPAYNGQTVGTFYYVNDAGGLESKVFSSGGPTPYPNYANAGHVEGQSALFMRDNGISEGLVFHNNPEGTCGFCVNMTETLLPENAKMTVVPPEGAIPVKRGATGETKVFTGNSNSPKSPTKGGCSGGSTNLSDIIEKETGKQLVIQESILMLPEEVEEVIGNKPESDILVHTAYDESTDENVMLLTSDAPEYKPWALVIQDSNGENKIKML"
Max10 = "SGGSSGGSSGSETPGTSESATPESSGGSSGGSSEVEFSHEYWMRHALTLAKRARDEREVPVGAVLVLNNRVIGEGWNRAIGLHDPTAHAEIMALRQGGLVMQNYRLIDATLYVTFEPCVMCAGAMIHSRIGRVVFGVRNSKRGAAGSLMNVLNYPGMNHRVEITEGILADECAALLCDFYRMPRQVFNAQKKAQSSIN"
catalist_sequences = [FokI, FokID, DddA, Max10]


# Functions

# Randomizer

def random_seq():
    random_number = random.randint(0, 3)
    return (random_number)

# Target sequence check


def is_valid_sequence(string):
    string = string.upper()
    if len(string) > 15:
        if (re.match('^[A,C,T,G]*$', string)):
            return True
        else:
            messagebox.showerror("Error", "Target is not DNA")
            return False
    else:
        messagebox.showerror("Error", "Target too short")
        return False

# seperate sequence and last nucleoteid


def sequence_brakedown(Talen_target_sequence):
    main_sequence_binding = Talen_target_sequence[0:len(
        Talen_target_sequence)-1]
    print(main_sequence_binding)
    last_nucliotide_binding = Talen_target_sequence[len(
        Talen_target_sequence)-1]
    print(last_nucliotide_binding)

    main_protein_binding_sequence = sequence_construction(
        main_sequence_binding)
    print(main_protein_binding_sequence)
    last_nucliotide_binding_sequence = last_nucliotide(last_nucliotide_binding)
    binding_sequence = main_protein_binding_sequence + last_nucliotide_binding_sequence
    return binding_sequence

# construct the sequence binding regon


def sequence_construction(main_sequence):
    # Necletide binding
    # HD->C NI->A NG->T NH->G
    pHD = ["LTPDQVVAIASHDGGKQALETVQRLLPVLCQDHG", "LTPEQVVAIASHDGGKQALETVQRLLPVLCQAHG",
           "LTPDQVVAIASHDGGKQALETVQRLLPVLCQAHG", "LTPAQVVAIASHDGGKQALETVQRLLPVLCQDHG"]
    pNI = ["LTPDQVVAIASNIGGKQALETVQRLLPVLCQDHG", "LTPEQVVAIASNIGGKQALETVQRLLPVLCQAHG",
           "LTPDQVVAIASNIGGKQALETVQRLLPVLCQAHG", "LTPAQVVAIASNIGGKQALETVQRLLPVLCQDHG"]
    pNG = ["LTPDQVVAIASNGGGKQALETVQRLLPVLCQDHG", "LTPEQVVAIASNGGGKQALETVQRLLPVLCQAHG",
           "LTPDQVVAIASNGGGKQALETVQRLLPVLCQAHG", "LTPAQVVAIASNGGGKQALETVQRLLPVLCQDHG"]
    pNH = ["LTPDQVVAIASNHGGKQALETVQRLLPVLCQDHG", "LTPEQVVAIASNHGGKQALETVQRLLPVLCQAHG",
           "LTPDQVVAIASNHGGKQALETVQRLLPVLCQAHG", "LTPAQVVAIASNHGGKQALETVQRLLPVLCQDHG"]
    Talen_partial_sequence = ""

    for char in main_sequence:
        randomize = random_seq()
        if char == "A":
            Talen_partial_sequence = Talen_partial_sequence+pNI[randomize]
        if last_nucliotide == "C":
            Talen_partial_sequence = Talen_partial_sequence+pHD[randomize]
        if last_nucliotide == "T":
            Talen_partial_sequence = Talen_partial_sequence+pNG[randomize]
        if last_nucliotide == "G":
            Talen_partial_sequence = Talen_partial_sequence+pNH[randomize]
    return Talen_partial_sequence

# Last Necletide binding sequence


def last_nucliotide(last_nucliotide):
    # Last Necletide binding
    # HD->C NI->A NG->T NH->G
    pLHD = "TPEQVVAIASHDGGRPALE"
    pLNI = "TPEQVVAIASNIGGRPALE"
    pLNG = "TPEQVVAIASNGGGRPALE"
    pLNH = "TPEQVVAIASNHGGRPALE"
    if last_nucliotide == "A":
        return pLNI
    if last_nucliotide == "C":
        return pLHD
    if last_nucliotide == "T":
        return pLNG
    if last_nucliotide == "G":
        return pLNH


def Tale_assembler(DNA_binding, catalist):
    global Talen_prot_sequence
    global catalist_sequences
    global NLS_value1
    global NLS_value2
    # TALEN structural scaffolds

    TALEN_N_scaffold = "MYPYDVPDYAGYPYDVPDYAGYPYDVPDYAMAPKKKRKVGIHGVPAAVDLRTLGYSQQQQEKIKPKVRSTVAQHHEALVGHGFTHAHIVALSQHPAALGTVAVKYQDMIAALPEATHEAIVGVGKQWSGARALEALLTVAGELRGPPLQLDTGQLLKIAKRGGVTAVEAVHAWRNALTGAPLK"
    TALEN_C_scaffold = "SIVAQLSRPDPALAALTNDHLVALACLGGRPALDAVKKGLPHAPALIKRTNRRIPERTSHRVAGS"

    TALEN_N_scaffold_NLS = "MAPKKKRKVYPYDVPDYAGYPYDVPDYAGYPYDVPDYAMAPKKKRKVGIHGVPAAVDLRTLGYSQQQQEKIKPKVRSTVAQHHEALVGHGFTHAHIVALSQHPAALGTVAVKYQDMIAALPEATHEAIVGVGKQWSGARALEALLTVAGELRGPPLQLDTGQLLKIAKRGGVTAVEAVHAWRNALTGAPLK"
    TALEN_C_scaffold_NLS = "SIVAQLSRPDPALAALTNDHLVALACLGGRPALDAVKKGLPHAPALIKRTNRRIPERTSHRVAGSKRPAATKKAGQAKKKK"

    TALEN_N = [TALEN_N_scaffold, TALEN_N_scaffold_NLS]
    TALEN_C = [TALEN_C_scaffold, TALEN_C_scaffold_NLS]

    catalist_sequence = catalist_sequences[catalist]

    Talen_prot_sequence = TALEN_N[NLS_value1.get()] + \
        DNA_binding+TALEN_C[NLS_value2.get()]+catalist_sequence


# Start Fuction


def start():
    global catalist_selection
    global Talen_target_sequence
    global catalist_type
    global Talen_prot_sequence
    target_test = is_valid_sequence(talen_target.get())
    if target_test:
        catalist_selection = int(catalist_type.get())
        Talen_target_sequence = str(talen_target.get())
        print(catalist_selection)
        print(Talen_target_sequence)
        DNA_binding_locus = sequence_brakedown(Talen_target_sequence.upper())
        Tale_assembler(DNA_binding_locus, catalist_selection)
        talen_sequence.delete('1.0', END)
        talen_sequence.insert(END, Talen_prot_sequence)


# Wigets
# Lables
toplable = Label(root, text="TALE Construction tool", font='David 18 bold')
sequence_input_lable = Label(
    root, text="Insert TALEN target sequence", font='David 12 bold')
catalyst_input_lable = Label(
    root, text="Choose catalyst:", font='David 12 bold')
talen_sequene = Label(
    root, text="Construct sequence", font='David 12 bold')
NLS_selection = Label(
    root, text="Choose NLS:", font='David 12 bold')
# Button
generate_button = Button(root, text="Generate", command=lambda: start())
# Text boxes
talen_target = Entry(root, width=50)
talen_sequence = Text(root, borderwidth=5, bd=3,
                      bg="gray", width=80, height=10)

# Placment
counter = 0
toplable.grid(row=counter, column=0, columnspan=2)
counter += 1
sequence_input_lable.grid(row=counter, column=0)
talen_target.grid(row=counter, column=1, columnspan=1)
root.grid_rowconfigure(counter, minsize=50)
counter += 1
catalyst_input_lable.grid(row=counter, column=1, sticky="w")
counter += 1
for i in catalist_options:

    Radiobutton(root, text=i, variable=catalist_type, value=catalist_options.index(i), font='courier 12 bold').grid(
        row=counter, column=1, sticky="w")
    counter += 1
counter -= len(catalist_options)+1
NLS_selection.grid(row=counter, column=2, sticky="w")
counter += 1
Checkbutton(root, text=NLS_options[0], variable=NLS_value1, onvalue=1, offvalue=0).grid(
    row=counter, column=2, sticky="w")
counter += 1
Checkbutton(root, text=NLS_options[1], variable=NLS_value2, onvalue=1, offvalue=0).grid(
    row=counter, column=2, sticky="w")
counter += 1

talen_sequene.grid(row=8+counter, column=0)
talen_sequence.grid(row=11+counter, column=0, columnspan=3)

generate_button.grid(row=12+counter, column=0, columnspan=2, sticky="e")

# Run system
root.mainloop()
