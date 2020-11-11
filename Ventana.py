import os
import threading
from threading import *
from tkinter import *
from tkinter import messagebox
import vlc
import time
from time import sleep

player = vlc.MediaPlayer("fondo.mp3")

def cargarImg(archivo):
    ruta= os.path.join('img',   archivo)
    imagen=PhotoImage(file=ruta)
    return imagen


def juego():
    global C_principal
    ventana.withdraw()
    ventana1 = Toplevel()
    ventana1.title("Avatars vs rooks")
    ventana1.minsize(1200, 700)
    ventana1.resizable(width=NO, height=NO)
    #Crear imagen de fondo
    C_principal=Canvas(ventana1, width=1200, height=700, bg='black')
    C_principal.place(x=0, y=0)
    C_principal.fondo=cargarImg('Tablero1.png')
    imgCanvas1 = C_principal.create_image(0, 0, anchor=NW, image=C_principal.fondo)
    C_principal.canibal = cargarImg("canibal.png")
    canibal = C_principal.create_image(165, 585, image=C_principal.canibal)

    def movimiento():
        global C_principal
        cancord = C_principal.coords(canibal)
        sleep(0.5)
        if (cancord[1] > 200):
            C_principal.coords(canibal, cancord[0], cancord[1] - 92)
        else:
            return messagebox.showwarning("MALA SUERTE!!", "HAS PERDIDO! ")
        Thread(target=movimiento, args=()).start()

    Thread(target=movimiento, args=()).start()

    def musica():
        global player
        player.play()
        time.sleep(16)
        player.stop()
        return musica()

    hiloFondo = threading.Thread(target=musica)
    hiloFondo.start()


    def mute():
        global player
        player.pause()

    BotonPausa = Button(C_principal, width=8, height=4, text="Pausa/Play", command=mute).place(x=600,y=600)

    ventana1.mainloop()



ventana=Tk()
ventana.title("Avatars vs rooks")
ventana.minsize(1200, 700)
ventana.resizable(width=NO, height=NO)
#Crear imagen de fondo
C_menu=Canvas(ventana, width=1200, height=700, bg='black')
C_menu.place(x=0, y=0)
C_menu.fondo=cargarImg('menu.png')
imgCanvas= C_menu.create_image(0,0, anchor=NW, image= C_menu.fondo)

Playjuego=Button(C_menu,width=8,height=4,text="Inicio",command=juego).place(x=600, y=600)



ventana.mainloop()