import tkinter as tk
from tkinter import messagebox
import time

root = tk.Tk()
root.title("Writing speed test")
root.geometry("800x300")
root.configure(background="SystemButtonFace")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

TIME_STARTED = False
START_TIME = 0


def click(key):
    global TIME_STARTED
    global START_TIME
    user_string = user_entry.get(1.0, "end-1c")

    if len(user_string) == 1 and not TIME_STARTED:
        TIME_STARTED = True
        START_TIME = time.time()
    elif len(user_string) == len(sample_text):
        total_time = time.time() - START_TIME
        check_result(total_time)
    else:
        pass


def check_result(time_spent):
    user_string_array = user_entry.get(1.0, "end-1c").split()
    missed_words = []
    correct_words = []
    counter = 0

    # Check how many words were missed
    for word in sample_text.split():
        try:
            if word == user_string_array[counter]:
                correct_words.append(word)
                counter += 1
            elif word != user_string_array[counter]:
                missed_words.append(f"Word was: '{word}', Input was: '{user_string_array[counter]}'")
                counter += 1
        except IndexError:
            print("Word wrong count")
            pass

    # Return type speed
    if correct_words:
        wpm = round(len(correct_words) / time_spent * 60)
        if missed_words:
            messagebox.showinfo("Results", f"Words per minute: {wpm}, missed: {str(missed_words)}")
        else:
            messagebox.showinfo("Results", f"Words per minute: {wpm}")
    else:
        messagebox.showinfo("Results", f"You missed every words. Try again.")


# sample_text = "This, is, a, test."

sample_text = "Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. " \
              "It is a gas giant with an average radius of about nine and a half times that of Earth. " \
              "It has only one-eighth the average density of Earth, but is over 95 times more massive."

tk.Label(text="Measure your typing speed. Type text bellow to begin.", font=('Arial', 16, 'bold'))\
        .grid(row=0, column=0, sticky="N", pady=50)
tk.Label(text=f"{sample_text}", font=('Arial', 12, ''), wraplength=500).grid(row=0, column=0)

user_entry = tk.Text(width=60, height=5)
user_entry.grid(row=0, column=0, pady=20, sticky="S")
user_entry.bind("<KeyRelease>", click)

root.mainloop()
