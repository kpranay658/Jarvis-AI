import threading
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from Scripts.Listen import Listen
from Scripts.Say import Say
from Chats.Chats import ReplyToQuery
from Body.Brain import ActionToQuery

def MainExecution():
    while True:
        Query = Listen()
        if Query and "none" not in Query:
            Reply = ReplyToQuery(Query)
            if Reply: Say(Reply)
            else: ActionToQuery(Query)

def play_gif(root, label):
    img = Image.open("UI/Gui.gif")
    for frame in ImageSequence.Iterator(img):
        lbl_img = ImageTk.PhotoImage(frame)
        label.config(image=lbl_img)
        label.image = lbl_img
        root.update()
    root.after(10, lambda: play_gif(root, label))

root = Tk()
root.geometry("1040x576")
lbl = Label(root)
lbl.pack()
threading.Thread(target=MainExecution, daemon=True).start()
root.after(0, lambda: play_gif(root, lbl))
root.mainloop()
