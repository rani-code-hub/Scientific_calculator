import tkinter as tk
from calculator import calculate
import math

# --- Global Modes ---
is_degree = False
is_dark = True

# --- Functions ---
def on_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def toggle_mode():
    global is_degree
    is_degree = not is_degree
    mode_btn.config(text="DEG" if is_degree else "RAD")

def toggle_theme():
    global is_dark
    is_dark = not is_dark

    if is_dark:
        root.configure(bg="#1e1e1e")
        entry.config(bg="#2d2d2d", fg="white")
        history.config(bg="#121212", fg="white")
        theme_btn.config(text="🌙 Dark")

        for btn in all_buttons:
            btn.config(bg=btn.default_bg, fg="white")

    else:
        root.configure(bg="#f5f5f5")
        entry.config(bg="white", fg="black")
        history.config(bg="#e0e0e0", fg="black")
        theme_btn.config(text="☀ Light")

        for btn in all_buttons:
            btn.config(bg="white", fg="black")

def evaluate():
    expr = entry.get()

    try:
        if is_degree:
            expr = expr.replace("sin(", "math.sin(math.radians(")
            expr = expr.replace("cos(", "math.cos(math.radians(")
            expr = expr.replace("tan(", "math.tan(math.radians(")

        result = calculate(expr)

        history.insert(tk.END, f"{entry.get()} = {result}\n")

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# --- Keyboard ---
def key_event(event):
    if event.char in "0123456789+-*/().":
        on_click(event.char)
    elif event.keysym == "Return":
        evaluate()
    elif event.keysym == "BackSpace":
        backspace()

# --- Hover ---
def on_enter(e):
    e.widget['bg'] = "#00adb5"

def on_leave(e, color):
    if is_dark:
        e.widget['bg'] = color
    else:
        e.widget['bg'] = "white"

# --- Window ---
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("420x650")
root.configure(bg="#1e1e1e")

root.bind("<Key>", key_event)

# --- Display ---
entry = tk.Entry(root, font=("Arial", 20),
                 bg="#2d2d2d", fg="white",
                 bd=0, insertbackground="white",
                 justify="right")
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# --- Top Buttons Frame ---
top_frame = tk.Frame(root, bg=root["bg"])
top_frame.pack()

mode_btn = tk.Button(top_frame, text="RAD", command=toggle_mode,
                     bg="#ff9800", fg="white", bd=0)
mode_btn.grid(row=0, column=0, padx=10)

theme_btn = tk.Button(top_frame, text="🌙 Dark", command=toggle_theme,
                      bg="#607d8b", fg="white", bd=0)
theme_btn.grid(row=0, column=1, padx=10)

# --- Main Frame ---
main_frame = tk.Frame(root, bg=root["bg"])
main_frame.pack()

# --- Buttons ---
buttons = [
    ['7','8','9','/','sqrt'],
    ['4','5','6','*','log'],
    ['1','2','3','-','sin'],
    ['0','.','=','+','cos'],
    ['(',')','^','C','⌫']
]

btn_style = {"font": ("Arial", 12), "bd": 0, "width": 5, "height": 2}

all_buttons = []

for r, row in enumerate(buttons):
    for c, btn in enumerate(row):

        if btn == '=':
            action = evaluate
            color = "#00adb5"
        elif btn == 'C':
            action = clear
            color = "#ff5722"
        elif btn == '⌫':
            action = backspace
            color = "#9c27b0"
        elif btn in ['sin','cos','tan','log','sqrt']:
            action = lambda x=btn: on_click(x + "(")
            color = "#393e46"
        else:
            action = lambda x=btn: on_click(x)
            color = "#222831"

        b = tk.Button(main_frame, text=btn, command=action,
                      bg=color, fg="white", activebackground="#00adb5",
                      **btn_style)

        b.grid(row=r, column=c, padx=5, pady=5)

        b.default_bg = color
        all_buttons.append(b)

        b.bind("<Enter>", on_enter)
        b.bind("<Leave>", lambda e, col=color: on_leave(e, col))

# --- History ---
history = tk.Text(root, height=8,
                  bg="#121212", fg="white", bd=0)
history.pack(fill="both", padx=10, pady=10)

# --- Run ---
root.mainloop()