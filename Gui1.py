from tkinter import *
from PIL import Image , ImageTk , ImageSequence
import time



root = Tk()
root.geometry("1040x576")

def play_gif(): 
    global img
    img = Image.open("C://Users//prati//Downloads//project work//project//Testing//UI//Gui.gif")

    lbl = Label(root)
    lbl.place(x=0,y=0)

    for img in ImageSequence.Iterator(img):

        
        img = ImageTk.PhotoImage(img)
        lbl.config(imag = img)
        root.update()
        time.sleep(0.01)
        
    root.after(0,play_gif)



def exit():
     root.destroy()





Button(root,text= "PLAY",command=play_gif).place(x= 500, y= 300)
Button(root,text= "EXIT",command=exit).place(x= 450, y= 300)

root.mainloop()

