# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:01:16 2023

@author: tomer
"""

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext  # Added for scrolled text widget


def count_miRNA_targets(dna_input, miRNA_targets):
    result = {}
    total_occurrences = 0  # Added for sum total

    for target in miRNA_targets:
        count = dna_input.count(target)
        if count > 0:
            result[target] = count
            total_occurrences += count  # Update total occurrences

    return result, total_occurrences


def check_targets():
    dna_input = dna_input_entry.get().upper()
    miRNA_results, total_occurrences = count_miRNA_targets(
        dna_input, miRNA_targets)

    result_text.delete(1.0, tk.END)
    if not miRNA_results:
        result_text.insert(tk.END, "No miRNA targets found.")
    else:
        result_text.insert(tk.END, "miRNA Target Occurrences:\n")
        for target, count in miRNA_results.items():
            result_text.insert(tk.END, f"{target}: {count} occurrences\n")
        # Display total occurrences
        result_text.insert(tk.END, f"Total Occurrences: {total_occurrences}\n")


# List of miRNA targets
miRNA_targets = ["CGAGGAA", "ATGCTGCA", "TTGAAAA", "GGAGCTGA", "GAGGAGG", "TATTCAGA", "TCTACGA", "AATGGAG",
                 "ATAACCT", "TGTGTGA", "ATGCTGC", "ATGTAGC", "TCATCTC", "TCCAGCC", "GGCAGTG", "CTCAGTG",
                 "GAGCCTG", "AAGGCAT", "CTTTATA", "TTCCGTT", "AACTCCA", "TGTTTAC", "TACACAT", "AATGAAT",
                 "GGTACGAA", "TCTCTCC", "AAGTCCA", "GGACCAA", "TAGGTCA", "AAGAGGA", "GTGGCTGA", "AGGAGGA",
                 "TGCTGGA", "GTGCCTT", "CCCAGAG", "ATGAAGG", "TCTTGCC", "ACACTACA", "TGAATGT", "AAGCCAT",
                 "AACTGAC", "GGTGCAT", "TGGACTG", "CAACTGT", "TTGGGAG", "GAGCTGA", "CAGCTTT", "GAGACGG",
                 "AGGGCCA", "TCCCCGA", "CCTGCTG", "GGCTCGG", "GGGTCAG", "GGCAGCT", "GTACAGG", "ACCAAAG",
                 "CTATGCA", "GGAAGAAG", "GGAAGAG", "GAGCTGG", "CTGCTGAA", "AATGTTAA", "ACTCCTGA", "GTCGATC",
                 "GGATCCG", "CATTTCA", "AGACACG", "ACAGGGT", "AAAGGGA", "GTAACCT", "GGCACTT", "GTGCAAT",
                 "TACGGGT", "AAGGGCG", "GGGCATT", "CAGGACG", "TCTGATA", "GGCGCTC", "ACTACCT", "TGAGCGT",
                 "TGACTTG", "AGTACTG", "ATACTGT", "GAGCCAG", "AGTCTTA", "CAGTATT", "TGGAGGA", "GAGGAGA",
                 "CAACCTCA", "AGCCCCA", "GACTGAGA", "ATGAAGGA", "CAGTGTT", "CTTGCAT", "GGTTCAA", "GTCTACC",
                 "AGTCGAG", "GGCCAGT", "GCCCCGC", "AACTGGA", "GTGACTT", "CTCAGGG", "GCTCTTG", "GTGTCAT",
                 "ACTGTAG", "AACCACT", "CCTCCAT", "ACCGAGC", "CGCTGCT", "AATGTGA", "TCGCAAA", "GCATAGTA",
                 "AGTCCAG", "CGTCTTA", "TCATCAG", "TGCTGCA", "CCCTCC", "GAGCCCC", "AGGAGCA", "ACAGAAG",
                 "GGCAGTGA", "TCGACCG", "TCTATGA", "ACTTTAT", "CTACCTC", "GGGATGC", "TCTATGT", "AAGGGAT",
                 "GGCTTCC", "GCACTTT", "TGCACTG", "CAGGTGA", "CAAGGAT", "ATACCTCA", "ATTCTTT", "CGATCTA",
                 "CTCCTCGA", "ACATATC", "ACTGTGA", "TGCTTTG", "GTACCAA", "AAAAGCT", "GGCGCATA", "AGAGGAA",
                 "TGGCTGA", "CACCAGA", "CACTGAA", "ACCAATCA", "CTGTTAC", "AAGCACA", "CTTGTAT", "ATGCTGG",
                 "CAATGCA", "GCGCCAT", "GTGTGAG", "GCACTTA", "AAGACCCA", "TTTGCAC", "TCTACCT", "ACCTCCA",
                 "TATTATA", "ACGCACA", "TGGTGCT", "TACTTGA", "TTTGTGA", "CTGAGCC", "AATAATA", "AACGGTT",
                 "ACTGAGT", "TGATATC", "CACCAGC", "ATCCAGCA", "GCAGACA", "TAGCCCC", "AGAAGAA", "TGAGGAAA",
                 "TTGCCAAA", "GTCTTCC", "CACTGTG", "AATCCCT", "GTCTACT", "AGTTCTC", "TGCTGCT", "GCACCTT",
                 "ATAAGCT", "TTGCACT", "CGTCTCC", "GGTGTGT", "CCCGCGT", "GACAGGG", "CCAGGGG", "TGTTATG",
                 "ACTACTG", "GTACTGT", "ACACTGG", "CCAGGTT", "AGCATTA", "ACATTCC", "ATCTAGT", "AGCTCCT"]

# Create the GUI window
root = tk.Tk()
root.title("miRNA Target Checker")

# Create widgets
input_label = tk.Label(root, text="Enter DNA Sequence:")
dna_input_entry = tk.Entry(root, width=50)
check_button = tk.Button(root, text="Check Targets", command=check_targets)

# Create a scrolled text widget for displaying results
result_text = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, height=10, width=50)

# Place widgets in the window
input_label.pack()
dna_input_entry.pack()
check_button.pack()
result_text.pack()

# Start the GUI event loop
root.mainloop()
