from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(background=YELLOW, padx=100, pady=50)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
title_label.grid(column=1, row=1)

canvas = Canvas(width=200, height=224)
canvas.config(bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 33, "bold"))
# canvas.create_text(100, 50, text="Timer", fill=GREEN, font=("Courier", 50, "normal"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0)
start_button.config(width=7)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.config(width=7)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()