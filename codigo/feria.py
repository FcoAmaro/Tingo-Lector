from tkinter import *
from time import *
#from PIL import imagetk
import lector


root = Tk()
root.title('TINGO ID')
root.geometry("800x600+100+100")
root.minsize(800,600)

photo = PhotoImage(file="tingo.png")
photo_label = Label(image=photo)
photo_label.grid()             
photo_label.image = photo
photo_label.place(x=360,y=30)

cabecera = Label(text="Lector de\ncodigos",font=("FreeSans",42),fg="black").place(x=90,y=90)

texto = StringVar()
escan = StringVar()
entrada = Entry(root, text=escan)
entrada.pack(side=BOTTOM, fill=X)
#texto.set("New Text!")

def Enter(event):
    codigo = entrada.get()
    print (codigo)
    ret = lector.feria(codigo)
    #print (tupla)
    #texto.set(tupla[0])
    texto.set(ret)
	entrada = Entry(root, text="")
   

entrada.bind("<Return>", Enter)

salida = Label(textvariable=texto,font=("FreeSans",20), fg="green").place(x=30,y=300)

root.mainloop()