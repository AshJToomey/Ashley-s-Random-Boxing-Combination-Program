# Ashley's Random Boxing Combination Program

import tkinter as tk
from tkinter import scrolledtext
import random

# Define move lists
punches = [
    "Jab",
    "Cross",
    "Lead Hook",
    "Rear Hook",
    "Lead Uppercut",
    "Rear Uppercut",
    "Overhand",
]

defensive_moves = [
    "Slip",
    "Roll",
    "Catch"
]

all_moves = punches + defensive_moves

def generate_combo():
    # Random number of total moves (between 3 and 5)
    num_moves = random.randint(3, 5)
    combo = random.choices(all_moves, k=num_moves)

    # Format combo with numbering for punches
    numbered_combo = []
    punch_number = 1
    for move in combo:
        if move in punches:
            numbered_combo.append(f"{punch_number}. {move}")
            punch_number += 1
        else:
            numbered_combo.append(move)

    result = " -> ".join(numbered_combo)
    output_text.config(state='normal')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state='disabled')

# GUI setup
root = tk.Tk()
root.title("Random Boxing Combo Generator")
root.geometry("500x300")
root.resizable(False, False)

# Title
tk.Label(root, text="Ashley’s Boxing Combo Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

# Generate Button
tk.Button(root, text="Generate Combo", command=generate_combo, font=("Helvetica", 12), bg="red", fg="white").pack(pady=10)

# Output Box
output_text = scrolledtext.ScrolledText(root, height=5, width=50, font=("Courier", 12), wrap=tk.WORD, state='disabled')
output_text.pack(padx=10, pady=10)

root.mainloop()