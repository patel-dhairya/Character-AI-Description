from tkinter import Tk, ttk, messagebox
from Text.text_generator import Character


def submit_function():
    character_name = name.get()
    character_tropes = [trope.strip() for trope in tropes.get().split(",")]
    char = Character(character_name)
    char.add_character_tropes(character_tropes)
    print(char)
    clear_function()


def clear_function():
    name.delete(0, 'end')
    tropes.delete(0, 'end')


window = Tk()
window.title("Character Information")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

label_frame = ttk.Frame(window)
label_frame.pack(pady=10)

name_label = ttk.Label(label_frame, text="Character Name:")
name_label.pack(side="left", padx=5)

name = ttk.Entry(label_frame, width=30)
name.pack(side="left", padx=5)

tropes_label = ttk.Label(label_frame, text="Character Tropes:")
tropes_label.pack(side="left", padx=5)

tropes = ttk.Entry(label_frame, width=30)
tropes.pack(side="left", padx=5)

button_frame = ttk.Frame(window)
button_frame.pack(pady=10)

submit_button = ttk.Button(button_frame, text="Submit", command=submit_function)
submit_button.pack(side="left", padx=5)

cancel_button = ttk.Button(button_frame, text="Cancel", command=window.destroy)
cancel_button.pack(side="left", padx=5)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)


def run(test=False):
    if test:
        name.insert(0, "Chris Hansen")
        tropes.insert(0, "Investigative, Journalistic")
    window.mainloop()
