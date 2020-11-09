import os
import threading
from tkinter import *
import vlc
import time

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

ventana.mainloop()


