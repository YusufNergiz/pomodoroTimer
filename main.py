import winsound
from tkinter import *
from PIL import ImageTk, Image
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
marks = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    global marks
    window.after_cancel(timer)
    text_on_top.config(text="Timer")
    reps = 1
    tick_1.config(text="")
    canvas.itemconfig(timer_text, text="00:00")




# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        text_on_top.config(text="Long Break")
    if reps % 2 == 0:
        count_down(short_break_sec)
        text_on_top.config(text="Short Break")
    else:
        count_down(work_sec)
        text_on_top.config(text="Work")
        winsound.Beep(1000, 1000)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    for num in range(1, 10):
        if count_sec == num:
            count_sec = f"0{num}"

    if count == 0:
        reps += 1
        print(reps)


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        global marks
        start_timer()
        marks = ""
        mark_session = math.floor(reps/2)
        for _ in range(mark_session):
            marks += "✓"
        tick_1.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodore")
window.config(padx=100, pady=112, bg=PINK)

start_button = Button()
start_button.config(text="START", font=("Arial", 20, "bold"), bg=PINK, fg=GREEN, command=start_timer)
start_button.grid(column=1, row=2)

reset_button = Button()
reset_button.config(text="RESET", font=("Arial", 20, "bold"), bg=PINK, fg=GREEN, command=reset)
reset_button.grid(column=3, row=2)

text_on_top = Label(text="Timer")
text_on_top.config(font=("Arial", 35, "bold"), fg=GREEN, bg=PINK)
text_on_top.grid(column=2, row=0)

tick_1 = Label()
tick_1.config(bg=PINK, fg="green", font=("Arial", 20, "bold"))
tick_1.grid(column=2, row=3)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_image = ImageTk.PhotoImage(Image.open(r"C:\Users\yusuf\Desktop\pomodoro-start\tomato.png"))
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)


window.mainloop()