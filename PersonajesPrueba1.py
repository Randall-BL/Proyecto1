import os
from threading import Thread
from tkinter import *
import vlc
import time

player = vlc.MediaPlayer("fondo.mp3")

def cargarImg(archivo):
    ruta= os.path.join('img',   archivo)
    imagen=PhotoImage(file=ruta)
    return imagen


def juego():
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
    Imagen1 = cargarImg("Canibal.png")
    C_principal.image1 = Imagen1
    canibal = C_principal.create_image(81, 540, anchor=NW, image=C_principal.image1)

    def movimiento():
        cardcord=C_principal.coords(canibal)
        if (cardcord(0)<600):
            C_principal.coords(canibal,carcord(0)+20,cardcord(1))
        Tk().after(100,movimiento())

    Thread(target=movimiento(),args=()).start()



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

    sumadre = Button(C_principal, width=8, height=4, text="Pausa/Play", command=mute).place(x=600,y=600)

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
