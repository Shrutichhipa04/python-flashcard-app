from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card ={}
to_learn={}
try:
    data=pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data= pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
def next_card():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_img,image=card_front_img)
    canvas.itemconfig(card_title,text="French",fill="Black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="Black")
    
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(canvas_img,image= card_back_img)
    canvas.itemconfig(card_title,text="English",fill="White")
    canvas.itemconfig(card_word,text=current_card["English"],fill="White")

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv",index=False)
    next_card()
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,flip_card)

canvas = Canvas(height=526,width=800)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img=canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,260,text="", font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

cross_img = PhotoImage(file="/images/wrong.png")
cross_button = Button(image=cross_img,highlightthickness=0,command=next_card)
cross_button.grid(row=1,column=0)
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

next_card()

window.mainloop()
