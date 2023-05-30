from tkinter import Tk, ttk, messagebox
from Text.text_generator import Character


def submit_function():
    character_name = name.get()
    character_tropes = [trope.strip() for trope in tropes.get().split(",")]
    character_voice = [voice.strip() for voice in voices.get().split(",")]
    character_narration = [narration.strip() for narration in narrations.get().split(",")]
    character_speech = [speech.strip() for speech in speeches.get().split(",")]
    char = Character(character_name)
    char.add_information("tropes", character_tropes)
    char.add_information("voice", character_voice)
    char.add_information("narration", character_narration)
    char.add_information("speech", character_speech)
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

# name of character - Start
name_label = ttk.Label(label_frame, text="Character Name:")
name_label.pack(side="left", padx=5)

name = ttk.Entry(label_frame, width=15)
name.pack(side="left", padx=5)
# name of character - End

# Character tropes - Start
tropes_label = ttk.Label(label_frame, text="Character Tropes:")
tropes_label.pack(side="left", padx=5)

tropes = ttk.Entry(label_frame, width=30)
tropes.pack(side="left", padx=5)
# Character tropes - End

# Character speaking style - Start
# Character Speaking Style
speaking_frame = ttk.Frame(window)
speaking_frame.pack(pady=10)

speaking_label = ttk.Label(speaking_frame, text="Speaking Style:")
speaking_label.grid(row=0, column=2, columnspan=2, pady=5)

voice_label = ttk.Label(speaking_frame, text="Voice:")
voice_label.grid(row=1, column=0, padx=5)

voices = ttk.Entry(speaking_frame, width=30)
voices.grid(row=1, column=1, padx=5)

speech_label = ttk.Label(speaking_frame, text="Speech:")
speech_label.grid(row=1, column=2, padx=5)

speeches = ttk.Entry(speaking_frame, width=30)
speeches.grid(row=1, column=3, padx=5)

narration_label = ttk.Label(speaking_frame, text="Narration:")
narration_label.grid(row=1, column=4, padx=5)

narrations = ttk.Entry(speaking_frame, width=30)
narrations.grid(row=1, column=5, padx=5)

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
        name.insert(0, "Seeley Booth")
        tropes.insert(0, "Investigative, Casual,Natural")
        voices.insert(0, "Deep, Resonant, Firm")
        speeches.insert(0, "Direct, Persuasive, Assertive")
        narrations.insert(0, "Objective, Precise, Focused")
    window.mainloop()
