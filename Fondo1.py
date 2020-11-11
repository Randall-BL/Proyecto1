import os
import threading
from threading import *
from tkinter import *
from tkinter import messagebox

import vlc
import time
from time import sleep


def musica():
    player = vlc.MediaPlayer("fondo.mp3")
    player.play()
    time.sleep(16)
    return musica()

hiloFondo=threading.Thread(target=musica)
hiloFondo.start()

def cargarImg(archivo):
    ruta = os.path.join('img', archivo)
    imagen = PhotoImage(file=ruta)
    return imagen

ventana = Tk()
ventana.title("Avatars vs rooks")
ventana.minsize(1200, 700)
ventana.resizable(width=NO, height=NO)
C_principal = Canvas(ventana, width=1200, height=700, bg='black')
C_principal.place(x=0, y=0)
C_principal.fondo = cargarImg('Tablero1.png')
imgCanvas = C_principal.create_image(0, 0, anchor=NW, image=C_principal.fondo)

C_principal.canibal= cargarImg("canibal.png")
canibal= C_principal.create_image(165,585,image=C_principal.canibal)

def movimiento():
    global C_principal
    cancord= C_principal.coords(canibal)
    sleep(0.5)
    if(cancord[1] > 200):
        C_principal.coords(canibal,cancord[0],cancord[1]-92 )
    else:
        return messagebox.showwarning("MALA SUERTE!!", "HAS PERDIDO! ")
    Thread(target=movimiento, args=()).start()

Thread(target=movimiento, args=()).start()





ventana.mainloop()


