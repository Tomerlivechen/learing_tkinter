# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:20:30 2023

@author: tomer
"""

from tkinter import *

root = Tk()
root.title("Ribozyme Maker")
root.geometry("700x500")

Extended_Hammerhead_Sequence = ""
Pistol_Sequence = ""
Pistol_II_Sequence = ""
Theophylline_Aptazyme_Sequence = ""
Minimal_Hammerhead_Sequence = ""


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
            return (sequence[index-12:index+6])
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
            return (sequence[index-16:index+6])
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
            return (sequence[index-12:index+17])
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
            return (sequence[index-13:index+18])
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
            return (sequence[index-13:index+21])
        else:
            if index >= 0:
                index += 1
            else:
                forget_buttons(Theophylline_Aptazyme_button)
                return False


def Pistol_construct(sequence):
    # nnnnnnNNNNNNGUNNNN
    # fedcba987654..3210
    # CGUGGUUAGGGCCACGUUAAAUAGNNNNUUAAGCCCUAAGCGNNNNNNnnnnnn
    # ((((.[[[[[[.))))........0123.....]]]]]]...456789abcdef
    Ribozyme_Fold = "((((.[[[[[[.))))........((((.....]]]]]]...(((((((((((("
    RNA_Fold = "))))))))))))..))))"
    Psequence0 = sequence[len(sequence)-4:len(sequence)]
    Psequence1 = sequence[0:12]
    part0 = convert_to_RNA(make_compliment(revers_order(Psequence0), "r"))
    part1 = convert_to_RNA(make_compliment(revers_order(Psequence1), "r"))
    P_full_sequence = "CGUGGUUAGGGCCACGUUAAAUAG"+part0+"UUAAGCCCUAAGCG"+part1
    report = "Minimal_Hammerhead Ribozyme \n" + P_full_sequence + "\n Ribozyme_Fold \n" + \
        Ribozyme_Fold + "\n Substrate sequence  \n" + \
        sequence + "\n Substrate Fold \n" + RNA_Fold+"\n"
    print_report(report)
    print(P_full_sequence)


def Pistol_II_construct(sequence):
    # nnnnnnNNNNNNNNNNGUNNNN
    # jihgfedcba987654..3210
    # CGUGGUUAGGGCCACGUUAAAUAGNNNNUUAAGCCCUAAGCGNNNNNNNNNNnnnnnn
    # ((((.[[[[[[.))))........0123.....]]]]]]...456789abcdefghij
    Ribozyme_Fold = "((((.[[[[[[.))))........((((.....]]]]]]...(((((((((((((((("
    RNA_Fold = "))))))))))))))))..))))"
    P2sequence0 = sequence[len(sequence)-4:len(sequence)]
    P2sequence1 = sequence[0:16]
    part0 = convert_to_RNA(make_compliment(revers_order(P2sequence0), "r"))
    part1 = convert_to_RNA(make_compliment(revers_order(P2sequence1), "r"))
    P_2_full_sequence = "CGUGGUUAGGGCCACGUUAAAUAG"+part0+"UUAAGCCCUAAGCG"+part1
    report = "Minimal_Hammerhead Ribozyme \n" + P_2_full_sequence + "\n Ribozyme_Fold \n" + \
        Ribozyme_Fold + "\n Substrate sequence  \n" + \
        sequence + "\n Substrate Fold \n" + RNA_Fold+"\n"
    print_report(report)
    print(P_2_full_sequence)


def Minimal_Hammerhead_construct(sequence):
    # nnnnnnnnnnNNGUCNNNNnnnnnnnnnn
    # rqponmlkjihgfe.dcba9876543210
    # nnnnnnnnnnNNNNCUGANGAGNNNNNNNNNNCGAAACNNnnnnnnnnnn
    # nnnnnnnnnnNNNNCUGANGAGGUCAAAUGACCGAAACNNnnnnnnnnnn
    # 0123456789abcd.......((((....))))...efghijklmnopqr
    Ribozyme_Fold = "((((((((((((((.......((((....))))...(((((((((((((("
    RNA_Fold = ")))))))))))))).))))))))))))))"
    MHHsequence0 = sequence[len(sequence)-14:len(sequence)]
    MHHsequence1 = sequence[0:14]
    part0 = convert_to_RNA(make_compliment(revers_order(MHHsequence0), "r"))
    part1 = convert_to_RNA(make_compliment(revers_order(MHHsequence1), "r"))
    MHH_full_sequence = part0+"CUGANGAGGUCAAAUGACCGAA"+part1
    report = "Minimal_Hammerhead Ribozyme \n" + MHH_full_sequence + "\n Ribozyme_Fold \n" + \
        Ribozyme_Fold + "\n Substrate sequence  \n" + \
        sequence + "\n Substrate Fold \n" + RNA_Fold+"\n"
    print_report(report)
    print(MHH_full_sequence)


def Extended_Hammerhead_construct(sequence):
    # nnnnnnnnnnNNNGUCNNNNNNNnnnnnnnn
    # tsrqponmlkjihgf.edcba9876543210
    # nnnnnnnnNNAAUNNNNNCUGAUGAGUCGCUGAAAUGCGACGAAACNNNnnnnnnnnnn
    # 0123456789...abcde.......(((((......)))))...fghijklmnopqrst
    Ribozyme_Fold = "((((((((((...(((((.......(((((......)))))...(((((((((((((((("
    RNA_Fold = "))))))))))))))).)))))))))))))))"
    HHsequence0 = sequence[len(sequence)-10:len(sequence)]
    HHsequence1 = sequence[len(sequence)-15:len(sequence)-10]
    HHsequence2 = sequence[0:15]
    part0 = convert_to_RNA(make_compliment(revers_order(HHsequence0), "r"))
    part1 = convert_to_RNA(make_compliment(revers_order(HHsequence1), "r"))
    part2 = convert_to_RNA(make_compliment(revers_order(HHsequence2), "r"))
    HH_full_sequence = part0+"AAU"+part1+"CUGAUGAGUCGCUGAAAUGCGACGAA"+part2
    report = "Minimal_Hammerhead Ribozyme \n" + HH_full_sequence + "\n Ribozyme_Fold \n" + \
        Ribozyme_Fold + "\n Substrate sequence  \n" + \
        sequence + "\n Substrate Fold \n" + RNA_Fold+"\n"
    print_report(report)
    print(HH_full_sequence)


def Theophylline_Aptazyme_construct(sequence):
    # nnnnnnnnnnNNNGUCNNNNNNnnnnnnnnnnnn
    # wvutsrqponmlkji.hgfedcba9876543210
    # nnnnnnnnnnnnNNNNNNCUGAUGAGCCUGGAUACCAGCCGAAAGGCCCUUGGCAGUUAGACGAAACNNNnnnnnnnnnn
    # 0123456789abcdefgh.......(.((((...((.(((....)))....))...)))).)...ijklmnopqrstuvw
    Ribozyme_Fold = "((((((((((((((((((.......(.((((...((.(((....)))....))...)))).)...((((((((((((((("
    RNA_Fold = "))))))))))))))).))))))))))))))))))"
    TAsequence0 = sequence[len(sequence)-18:len(sequence)]
    TAsequence1 = sequence[0:15]
    part0 = convert_to_RNA(make_compliment(revers_order(TAsequence0), "r"))
    part1 = convert_to_RNA(make_compliment(revers_order(TAsequence1), "r"))
    TA_full_sequence = part0 + "CUGAUGAGCCUGGAUACCAGCCGAAAGGCCCUUGGCAGUUAGACGAA"+part1
    report = "Minimal_Hammerhead Ribozyme \n" + TA_full_sequence + "\n Ribozyme_Fold \n" + \
        Ribozyme_Fold + "\n Substrate sequence  \n" + \
        sequence + "\n Substrate Fold \n" + RNA_Fold + "\n"
    print_report(report)
    print(TA_full_sequence)


def print_report(report):
    report_text.insert(END, report)


def nucliotid_Compliment(nuc, ntype):
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
    elif nuc.lower() == "u" and ntype == "r":
        ret = "a"
    return ret


def revers_order(sequence):
    revsequence = sequence[::-1]
    return revsequence.upper()


def make_compliment(sequence, DorR):
    compsequence = ""
    for i in range(len(sequence)):
        compsequence += nucliotid_Compliment(sequence[i], DorR)
    return compsequence.upper()


def convert_to_RNA(sequence):
    sequence = sequence.lower()
    rsequence = sequence.replace("t", "u")
    return rsequence.upper()


def set_buttons(button_name, grid_position):
    button_name.grid(row=grid_position[0], column=grid_position[1], sticky="w")


def forget_buttons(button_name):
    button_name.grid_forget()


def on_scroll(*args):
    report_text.yview(*args)


def check():
    report_text.delete('1.0', END)
    global Extended_Hammerhead_Sequence
    global Pistol_Sequence
    global Pistol_II_Sequence
    global Theophylline_Aptazyme_Sequence
    global Minimal_Hammerhead_Sequence
    potential_sequence = convert_to_RNA(binding_site.get()).upper()
    Pistol_Sequence = pistol_check(potential_sequence)
    Pistol_II_Sequence = pistol_II_check(potential_sequence)
    Minimal_Hammerhead_Sequence = Minimal_Hammerhead_check(potential_sequence)
    Extended_Hammerhead_Sequence = Extended_Hammerhead_check(
        potential_sequence)
    Theophylline_Aptazyme_Sequence = Theophylline_Aptazyme_check(
        potential_sequence)


# widget
label_binding_site = Label(root, text="Enter a potential Ribozyme")

check_compatibelity = Button(
    root, text="Check Compatibility", command=lambda: check())

binding_site = Entry(root, width=100)

report_text = Text(root, borderwidth=5, bd=3,
                   bg="gray", width=80, height=20)
scrollbar = Scrollbar(root, command=on_scroll)
report_text.config(yscrollcommand=scrollbar.set)
pistol_button = Button(root, text="Pistol Ribozyme",
                       command=lambda: Pistol_construct(Pistol_Sequence))
pistol_II_button = Button(
    root, text="PistolII Ribozyme", command=lambda: Pistol_II_construct(Pistol_II_Sequence))
Minimal_Hammerhead_button = Button(
    root, text="Minimal Hammerhead Ribozyme", command=lambda: Minimal_Hammerhead_construct(Minimal_Hammerhead_Sequence))
Extended_Hammerhead_button = Button(
    root, text="Extended Hammerhead Ribozyme", command=lambda: Extended_Hammerhead_construct(Extended_Hammerhead_Sequence))
Theophylline_Aptazyme_button = Button(
    root, text="Theophylline Aptazyme Ribozyme", command=lambda: Theophylline_Aptazyme_construct(Theophylline_Aptazyme_Sequence))


# placment

counter = 0
label_binding_site.grid(row=counter, column=1, columnspan=4)
counter += 1
binding_site.grid(row=counter, column=1, columnspan=4, sticky="e")
counter += 1
check_compatibelity.grid(row=counter, column=1, columnspan=4, sticky="e")
report_text.grid(row=8+counter, column=0, columnspan=3)
scrollbar.grid(row=8 + counter, column=3, sticky="ns")

# Run system
root.mainloop()
