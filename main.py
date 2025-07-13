import tkinter as tk
import random
import csv

# Path to your CSV file
filename = r"E:\My Portfolio\Python\Day 31\flash-card-project-start\data\french_words.csv"

# Load words from CSV
def load_words(filename):
    word_dict = {}
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            english = row['English'].strip()
            french = row['French'].strip()
            word_dict[french] = english  # Key = French, Value = English
    return word_dict

# Select a random French word
def pick_random_word():
    global current_french
    current_french = random.choice(list(words.keys()))
    show_french_word()

# Show the French word in the canvas
def show_french_word():
    canvas.itemconfig(word_text, text=current_french)

# Show the English translation
def show_english_word():
    english = words[current_french]
    canvas.itemconfig(word_text, text=english)

# Load word list from CSV
words = load_words(filename)
current_french = ""

# Tkinter setup
root = tk.Tk()
root.title("Flashcard App")

CANVAS_WIDTH = 850
CANVAS_HEIGHT = 600
PADDING = 50
BACKGROUND_COLOR = "#B1DDC6"

# Create canvas
canvas = tk.Canvas(
    root,
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
    bg=BACKGROUND_COLOR,
    highlightthickness=0
)
canvas.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# White inner rectangle
canvas.create_rectangle(
    PADDING, PADDING,
    CANVAS_WIDTH - PADDING,
    CANVAS_HEIGHT - PADDING,
    fill="white",
    outline="blue",
    width=2
)

# Word text in center
word_text = canvas.create_text(
    CANVAS_WIDTH / 2,
    CANVAS_HEIGHT / 2,
    text="",
    font=("Arial", 40, "bold"),
    fill="black"
)

# Buttons
show_english_btn = tk.Button(root, text="✅ Show English", command=show_english_word)
show_english_btn.grid(row=1, column=0, pady=10, padx=20)

next_word_btn = tk.Button(root, text="🔁 Next Word", command=pick_random_word)
next_word_btn.grid(row=1, column=1, pady=10, padx=20)

# Show the first French word
pick_random_word()

# Start the GUI loop
root.mainloop()
