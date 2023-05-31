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

basic_info_label = ttk.Label(label_frame, text="Basic information about character:")
basic_info_label.grid(row=0, column=0, columnspan=4, pady=5)

# name of character - Start
name_label = ttk.Label(label_frame, text="Character Name:")
name_label.grid(row=1, column=0, padx=5)

name = ttk.Entry(label_frame, width=15)
name.grid(row=1, column=1, padx=5)
# name of character - End

# Character DOB - start
dob_label = ttk.Label(label_frame, text="Date of Birth(DD/MM/YYYY):")
dob_label.grid(row=1, column=2, padx=5)

dob = ttk.Entry(label_frame, width=18)
dob.grid(row=1, column=3, padx=5)
# Character DOB - end

# Character tropes - Start
tropes_label = ttk.Label(label_frame, text="Character Tropes:")
tropes_label.grid(row=3, column=0, padx=5, pady=10)

tropes = ttk.Entry(label_frame, width=30)
tropes.grid(row=3, column=1, padx=5, pady=10)
# Character tropes - End

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

# Character Physical Appearance
appearance_frame = ttk.Frame(window)
appearance_frame.pack(pady=10)

appearance_label = ttk.Label(appearance_frame, text="Physical Appearance:")
appearance_label.grid(row=2, column=4, columnspan=2, pady=5)

race_label = ttk.Label(appearance_frame, text="Race:")
race_label.grid(row=3, column=0, padx=5)

race = ttk.Entry(appearance_frame, width=10)
race.grid(row=3, column=1, padx=5)

sex_label = ttk.Label(appearance_frame, text="Sex:")
sex_label.grid(row=3, column=2, padx=5)

sex = ttk.Entry(appearance_frame, width=10)
sex.grid(row=3, column=3, padx=5)

height_label = ttk.Label(appearance_frame, text="Height(cm):")
height_label.grid(row=3, column=4, padx=5)

height = ttk.Entry(appearance_frame, width=18)
height.grid(row=3, column=5, padx=5)

weight_label = ttk.Label(appearance_frame, text="Weight(kg):")
weight_label.grid(row=3, column=6, padx=5)

weight = ttk.Entry(appearance_frame, width=18)
weight.grid(row=3, column=7, padx=5)

# Character Physical Appearance
face_frame = ttk.Frame(window)
face_frame.pack(pady=10)

face_label = ttk.Label(face_frame, text="Face:")
face_label.grid(row=2, column=4, columnspan=2, pady=5)

shape_label = ttk.Label(face_frame, text="Shape:")
shape_label.grid(row=3, column=0, padx=5)

shape = ttk.Entry(face_frame, width=10)
shape.grid(row=3, column=1, padx=5)

tone_label = ttk.Label(face_frame, text="Tone:")
tone_label.grid(row=3, column=2, padx=5)

tone = ttk.Entry(face_frame, width=10)
tone.grid(row=3, column=3, padx=5)

structure_label = ttk.Label(face_frame, text="Structure:")
structure_label.grid(row=3, column=4, padx=5)

structure = ttk.Entry(face_frame, width=18)
structure.grid(row=3, column=5, padx=5)

nose_label = ttk.Label(face_frame, text="Nose:")
nose_label.grid(row=3, column=6, padx=5)

nose = ttk.Entry(face_frame, width=18)
nose.grid(row=3, column=7, padx=5)

mouth_label = ttk.Label(face_frame, text="Mouth:")
mouth_label.grid(row=3, column=8, padx=5)

mouth = ttk.Entry(face_frame, width=18)
mouth.grid(row=3, column=9, padx=5)

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
