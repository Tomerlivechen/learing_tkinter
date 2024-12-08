# TALE Construction Tool

## Project Overview
This is a graphical user interface (GUI) tool designed for constructing TALEN (Transcription Activator-Like Effector Nuclease) sequences. The tool allows users to input a target DNA sequence, select a catalyst, and choose Nuclear Localization Signal (NLS) options to generate the corresponding TALEN protein sequence.

## Features
- **Input Target DNA Sequence**: The user can input a DNA sequence for TALEN targeting.
- **Select Catalyst**: The user can choose between different catalysts such as FokI, FokI duplex, DddA+UDG, and Max10-TadA.
- **NLS Selection**: Users can select between different Nuclear Localization Signals (SV40 NLS and nucleoplasmin NLS).
- **Sequence Generation**: Based on the user inputs, the tool generates the corresponding TALEN protein sequence.
- **GUI Interface**: The tool utilizes the Tkinter library to provide an interactive and user-friendly interface.

## Technologies Used
- **Python**: The main programming language.
- **Tkinter**: For building the graphical user interface.
- **Regular Expressions**: To validate the input DNA sequence.

## Requirements
- Python 3.x
- Tkinter (usually bundled with Python)
- Random and Math libraries

## How to Use
1. **Input Target Sequence**: Enter a valid DNA sequence in the input box.
2. **Select Catalyst**: Choose a catalyst from the options available.
3. **Choose NLS**: Select the appropriate Nuclear Localization Signal.
4. **Generate Sequence**: Click the "Generate" button to construct the TALEN protein sequence.

## Code Structure
- **Target Sequence Validation**: Ensures the input sequence is valid DNA (A, T, C, G) and is of sufficient length.
- **Sequence Breakdown**: Breaks the target sequence into parts for constructing the binding domain.
- **TALEN Construction**: Assembles the TALEN protein sequence by combining the appropriate scaffolds and selected catalyst.

