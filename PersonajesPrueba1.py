from tkinter import *
from playsound import playsound
import os
def cargarImg(archivo):
    ruta= os.path.join('img',   archivo)
    imagen=PhotoImage(file=ruta)
    return imagen

playsound('Sonido\sonido_fondo.mp3')
ventana=Tk()
ventana.title("Avatars vs rooks")
ventana.minsize(1200, 700)
ventana.resizable(width=NO, height=NO)
#Crear imagen de fondo
C_principal=Canvas(ventana, width=1200, height=700, bg='black')
C_principal.place(x=0, y=0)
C_principal.fondo=cargarImg('Tablero1.png')
imgCanvas= C_principal.create_image(0,0, anchor=NW, image= C_principal.fondo)

def personaje(archivo):
    ruta= os.path.join('Avatars',   archivo)
    imagen=PhotoImage(file=ruta)
    return imagen
Avatars=Canvas(ventana,width=300, height=300, )
Avatars.place(x=20, y=20)
Avatars.Canibal=personaje('Canibal.png')
imgCanvas=Avatars.create_image(20,20, anchor=NW, image=Avatars.Canibal)



ventana.mainloop()