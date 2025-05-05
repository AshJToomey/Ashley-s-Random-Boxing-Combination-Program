# Ashley's Random Boxing Combination Program

import random

punches = [
    "Jab",
    "Cross",
    "Lead Hook",
    "Rear hook",
    "Lead Uppercut",
    "Rear Uppercut",
    "Overhand",
]

defensive_moves = [
    "Slip",
    "Roll",
    "Catch"
    ]

# Combine punches and defensive moves together
all_moves = punches + defensive_moves

# Number of punches in combo (between 2 and 5)
num_moves = random.randint(3, 5)

# Create a random combination
combo = random.choices(all_moves, k=num_moves)

# Build the numbered combo
numbered_combo = []
punch_number = 1 # Start numbering punches from 1

for move in combo: 
    if move in punches: 
        numbered_combo.append(f"{punch_number}. {move}")
        punch_number += 1
    else:
        numbered_combo.append(move) # defensive move, no number
        
# Join them nicely with an arrow
print(" -> ".join(numbered_combo))
