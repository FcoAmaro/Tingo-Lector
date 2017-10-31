from tkinter import *
from time import *
#from PIL import imagetk
import lector


root = Tk()
root.title('TINGO ID')
root.geometry("400x300+100+100")
root.minsize(420,320)

photo = PhotoImage(file="tingo.png")
photo_label = Label(image=photo)
photo_label.grid()             
photo_label.image = photo
photo_label.place(x=30,y=30)

cabecera = Label(text="Lector de\ncodigos",font=("FreeSans",28),fg="black").place(x=240,y=90)

texto = StringVar()
escan = StringVar()
entrada = Entry(root, text=escan)
entrada.pack(side=BOTTOM, fill=X)
#texto.set("New Text!")

def Enter(event):
    codigo = entrada.get()
    print (codigo)
    tupla = lector('TID12')
    print (tupla)
    #texto.set(tupla[0])
    texto.set(codigo)
    escan.set('')
    return "break"


entrada.bind("<Return>", Enter)
salida = Label(textvariable=texto,font=("FreeSans",14),fg="black").place(x=30,y=220)

root.mainloop()