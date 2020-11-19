import os
import threading
from tkinter import *
from tkinter import messagebox
import vlc
import time
import random






def cargarImg(archivo):
    ruta= os.path.join('img',   archivo)
    imagen=PhotoImage(file=ruta)
    return imagen



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


player = vlc.MediaPlayer("fondo.mp3")

def musica():
    global player
    player.play()
    time.sleep(16)
    player.stop()
    return musica()



def mute():
    global player
    player.pause()


hiloFondo = threading.Thread(target=musica)
hiloFondo.start()

class Tablero(threading.Thread):
    def __init__(self):
        self.enemigo=[]
        self.C_principal=None
        self.ventanajuego=None
        self.size=0
        print(self.enemigo)

    def __cargarImagen(self,nombre):
        if isinstance(nombre, str):
            #path = os.path.join('Img',nombre)
            imagen = PhotoImage(file=nombre)
            return imagen


    def dibujar(self):
        self.ventanajuego=Tk()
        self.ventanajuego.title("GAME")
        self.ventanajuego.geometry("1200x700+390+240")
        self.ventanajuego.resizable(width=NO, height=NO)
        self.C_principal= Canvas(self.ventanajuego, width= 1200, height = 700, bg="#d3c692")#d3c692
        self.C_principal.place(x=0,y=0)
        img= self.__cargarImagen("Tablero1.png")
        self.C_principal.create_image(600,350, image = img)
        #botonMover = Button(self.ventanajuego, text="Mover enemigo", command=self.movement,bg="#144214",fg="white",font=("Helvetica",15)).place(x=100,y=20)
        #botonInsertarEnemigo= Button(self.ventanajuego, text="InsertarEnemigo", command=self.SpawnEnemigo(),bg="#096654",fg="white",font=("Helvetica",15)).place(x=400,y=20)
        BotonPausa = Button(self.C_principal, width=8, height=4, text="Pausa/Play", command=mute).place(x=600, y=600)
        self.empezarJuego()
        self.ventanajuego.mainloop()

    def SpawnEnemigo(self):
        self.enemigo.append(Enemigo(random.randrange(4)))#Este nos crea un enemigo de tipo mario
        tag="f"+str(self.size)
        print(self.enemigo)
        self.C_principal.create_image(posicion(),585,image=self.enemigo[self.size].imagen,tags=tag)
        self.size+=1
        self.C_principal.after(5000,self.SpawnEnemigo)

    def empezarJuego(self):
        self.SpawnEnemigo()
        self.movement()


    def movement(self):
        j=random.randrange(self.size)
        self.enemigo[j].move(0,0)
        tag="f"+str(j)
        self.C_principal.move(tag,self.enemigo[j].posx,self.enemigo[j].posy)
        self.C_principal.after(100,self.movement)



class Enemigo:
    def __init__(self, tipo):
        if (tipo == 0):
            self.tipo = "escudero"
            self.imagen = self.__cargarImagen("escudero.png")
            self.posx = posicion()
            self.posy = -0.92
        if (tipo == 1):
            self.tipo = "canibal"
            self.imagen = self.__cargarImagen("canibal.png")
            self.posx = posicion()
            self.posy = -0.92
        if (tipo == 2):
            self.tipo = "leñador"
            self.imagen = self.__cargarImagen("leñador.png")
            self.posx = posicion()
            self.posy = -0.92
        if (tipo == 3):
            self.tipo = "arquero"
            self.imagen = self.__cargarImagen("arquero.png")
            self.posx = posicion()
            self.posy = -0.92

    def move(self, x, y):
        self.posx = x
        self.posy += y

    def __cargarImagen(self, nombre):
        if isinstance(nombre, str):
            # path = os.path.join('Img',nombre)
            imagen = PhotoImage(file=nombre)
            return imagen

#------------------------------------------------------------------------------------------------------------------



def about():
    ventanabout.deiconify()

def ayuda():
    ventanayuda.deiconify()
def prejuego():
    ventana.destroy()


ventana=Tk()
ventana.title("Avatars vs rooks")
ventana.geometry("1200x700+390+240")
ventana.resizable(width=NO, height=NO)
#Crear imagen de fondo
C_menu=Canvas(ventana, width=1200, height=700, bg='black')
C_menu.place(x=0, y=0)
C_menu.fondo=cargarImg('menu.png')
imgCanvas= C_menu.create_image(0,0, anchor=NW, image= C_menu.fondo)

Playjuego=Button(C_menu,width=8,height=4,text="Inicio",command=prejuego).place(x=600, y=600)

ventanabout=Toplevel(ventana)
ventanabout.title("About")
ventanabout.geometry("500x600+760+300")
ventanabout.resizable(width= NO, height=NO)
C_about=Canvas(ventanabout,width=500, height=650,bg="white")
C_about.place(x=0, y=0)
C_about.fondo=cargarImg("About.png")
imgAbout=C_about.create_image(0,0, anchor=NW, image=C_about.fondo)
ventanabout.withdraw()

PlayAbout=Button(C_menu,width=8,height=4,text="Crèditos",command=about).place(x=1100, y=600)

ventanayuda=Toplevel(ventana)
ventanayuda.title("About")
ventanayuda.geometry("500x600+760+300")
ventanayuda.resizable(width= NO, height=NO)
C_ayuda=Canvas(ventanayuda,width=500, height=650,bg="white")
C_ayuda.place(x=0, y=0)
C_ayuda.fondo=cargarImg("ayuda.png")
imgAyuda=C_ayuda.create_image(0,0, anchor=NW, image=C_ayuda.fondo)
ventanayuda.withdraw()

PlayAyuda=Button(C_menu,width=8,height=4,text="Ayuda",command=ayuda).place(x=1000, y=600)

ventana.mainloop()

t=Tablero()
t.dibujar()
