import os
import threading
from threading import *
from tkinter import *
import vlc
import time
from time import sleep

ventana=Tk()
ventana.title("Avatars vs rooks")
ventana.minsize(1200, 700)
ventana.resizable(width=NO, height=NO)
#Crear imagen de fondo
C_menu=Canvas(ventana, width=1200, height=700, bg='black')
C_menu.place(x=0, y=0)
C_menu.fondo=cargarImg('menu.png')
imgCanvas= C_menu.create_image(0,0, anchor=NW, image= C_menu.fondo)

Playjuego=Button(C_menu,width=8,height=4,text="Inicio",command=).place(x=600, y=600)



ventana.mainloop()
