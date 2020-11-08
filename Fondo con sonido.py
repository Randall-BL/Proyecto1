from tkinter import *
import playsound
import os
def cargarImg(archivo):
    ruta= os.path.join('img',   archivo)
    imagen=PhotoImage(file=ruta)
    return imagen
def reproducir():
    playsound('Sonido/fondo.mp3')
    return reproducir()
reproducir()
ventana=Tk()
ventana.title("Avatars vs rooks")
ventana.minsize(1200, 700)
ventana.resizable(width=NO, height=NO)
#Crear imagen de fondo
C_principal=Canvas(ventana, width=1200, height=700, bg='black')
C_principal.place(x=0, y=0)
C_principal.fondo=cargarImg('Tablero1.png')
imgCanvas= C_principal.create_image(0,0, anchor=NW, image= C_principal.fondo)
ventana.mainloop()