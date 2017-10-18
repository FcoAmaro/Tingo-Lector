from tkinter import *
from time import *
#from PIL import imagetk
import lector

def colorM():
	return color

root = Tk()
root.title('TINGO ID')
root.geometry("400x300+100+100")
root.minsize(420,320)

'''canvas = Canvas(width=600, height=600)
canvas.pack()
photoimage = ImageTk.PhotoImage(file="tingo.png")
canvas.create_image(430, 180, image=photoimage)'''

photo = PhotoImage(file="tingo.png")
photo_label = Label(image=photo)
photo_label.grid()             
photo_label.image = photo
photo_label.place(x=30,y=30)

cabecera = Label(text="Lector de\ncodigos",font=("FreeSans",28),fg="black").place(x=240,y=90)

texto = StringVar()
color = "black"
#texto.set("New Text!")

n = Label(textvariable=texto,font=("FreeSans",14),fg=color).place(x=30,y=220)

while root:
	cod = input()
	#cod = getpass()
	respuesta = lector.lector(cod)
	texto.set(respuesta[0])
	color = respuesta[1]

root.mainloop()