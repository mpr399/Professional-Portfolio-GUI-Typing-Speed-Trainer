from tkinter import messagebox

from sample_text import text
import random
import tkinter as tk

TIME_UP = False
STORY = ""
WORDS = []
INDEX = 0
THREAD_COUNTER = ""


def replace_curly_quotes(t):
    return t.replace('“', '"') \
        .replace('”', '"') \
        .replace("‘", "'") \
        .replace("’", "'")


def countdown(x):
    update_time_label(x)

    if x > 0:
        global THREAD_COUNTER
        THREAD_COUNTER = window.after(1000, countdown, x - 1)
    else:
        end_session()
        stop_countdown()


def stop_countdown():
    global THREAD_COUNTER
    window.after_cancel(THREAD_COUNTER)


def end_session():
    messagebox.showinfo("TIME UP", f"You typed {INDEX} words in a minute")
    refresh()


def update_time_label(time_left):
    l_time['text'] = f"Time Left: {time_left}"


def update_next_word():
    t_word.config(state=tk.NORMAL)
    t_word.delete(0, tk.END)
    t_word.insert(0, WORDS[INDEX])
    t_word.config(state=tk.DISABLED)

    t_typing.delete(0, tk.END)


def validate_typed(user_input):
    global INDEX
    if user_input.get() == WORDS[INDEX] + " ":
        INDEX += 1
        update_next_word()


def update_story():
    t_text.config(state=tk.NORMAL)
    t_text.delete('1.0', tk.END)
    t_text.insert(tk.INSERT, STORY)
    t_text.config(state=tk.DISABLED)


def refresh():
    global TIME_UP, STORY, WORDS, INDEX
    TIME_UP = False
    STORY = replace_curly_quotes(random.choice(text).strip())
    WORDS = STORY.split(" ")
    INDEX = 0


def start():
    refresh()
    update_story()
    update_next_word()
    try:
        stop_countdown()
    except:
        pass
    countdown(60)


# GUI ####################################################################
window = tk.Tk()
window.title("How many words can you type in a minute?")
window.config(padx=10, pady=10)

b_start = tk.Button(text="Click to Start", command=start)
b_start.grid(row=0, column=0)

l_story = tk.Label(text="Short Story")
l_story.grid(row=1, column=0)

t_text = tk.Text(wrap=tk.WORD)
t_text.grid(row=1, column=1, columnspan=2)

l_current = tk.Label(text="Current Word")
l_current.grid(row=2, column=0)

t_word = tk.Entry()
t_word.grid(row=2, column=1)

l_time = tk.Label(text="Time Left: ")
l_time.grid(row=2, column=2)

l_here = tk.Label(text="Type Here")
l_here.grid(row=3, column=0)

typed = tk.StringVar()
typed.trace("w", lambda name, index, mode, sv=typed: validate_typed(typed))
t_typing = tk.Entry(textvariable=typed)
t_typing.grid(row=3, column=1)

window.mainloop()
