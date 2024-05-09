###Author Faizan Mirza ###########
##Simulatin Of watch for Demostration Perpose###### 




from tkinter import *
from PIL import image,imageaTk
root = Tk()
#gui logic here
#geometry for gui
root.geometry("712x260") #width and height resp
#min size
root.minsize(200,100)
#max size
root.maxsize(1200,900)
#lable
image= image.open("backgroung.png")
background = imageTk.PhotoImage(image)
heading=Label(image=background)
heading.pack()# rule for tkinter to take into consideration



root.mainloop()
