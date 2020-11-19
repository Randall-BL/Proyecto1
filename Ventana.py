import os
import threading
from threading import *
from tkinter import *
from tkinter import messagebox
import vlc
import time
from time import sleep
import random

player = vlc.MediaPlayer("fondo.mp3")

def enemigo():
    A=random.randint(1,4)
    if A==1:
        avatar = "Canibal.png"
    elif A==2:
        avatar="Arquero.png"
    elif A==3:
        avatar="Escudero.png"
    elif A==4:
        avatar="Leñador.png"
    return avatar

def posicion():
    B=random.randint(1,9)
    if B==1:
        spawn = 277
    elif B==2:
        spawn = 391
    elif B==3:
        spawn= 500
    elif B==4:
        spawn= 613
    elif B == 5:
        spawn = 726
    elif B == 6:
        spawn = 841
    elif B == 7:
        spawn = 951
    elif B == 8:
        spawn = 1068
    elif B == 9:
        spawn = 165
    return spawn

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
    C_principal.canibal = cargarImg(enemigo())
    canibal = C_principal.create_image(posicion(), 585, image=C_principal.canibal)

    def movimiento():
        global C_principal
        cancord = C_principal.coords(canibal)
        sleep(1)
        if (cancord[1] > 200):
            C_principal.coords(canibal, cancord[0], cancord[1] - 9.2)
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