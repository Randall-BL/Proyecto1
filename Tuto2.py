from tkinter import *
from tkinter import messagebox
import os
#import tkinter.scrolledtext as scrolledtext
import random
import math
from threading import *
from threading import Thread
import time


class Tablero:
    def __init__(self):
        self.enemigo=[]
        self.__fondo=None
        self.__ventana=None
        self.size=0
        print(self.enemigo)

    #***************Cargar Imagenes***********************
    #Entrada: Nombre de la imagen
    #Restricciones: el nombre de la imagen debe ser formato str
    #Salida: Genera la imagen
    def __cargarImagen(self,nombre):
        if isinstance(nombre, str):
            #path = os.path.join('Img',nombre)
            imagen = PhotoImage(file=nombre)
            return imagen


    def dibujar(self):
        self.__ventana = Toplevel()
        self.__ventana.title("GAME")
        self.__ventana.minsize(800,600)
        self.__ventana.resizable(width=NO, height=NO)
        self.__ventana.configure(background="white")                
        self.__fondo= Canvas(self.__ventana, width= 2000, height = 2000, bg="#d3c692")#d3c692
        self.__fondo.place(x=0,y=0)                
        img= self.__cargarImagen("tablero1.png")
        self.__fondo.create_image(425,320, image = img)               
        self.__r = Text(self.__ventana,width=1,height=1,bg="#d3c692",fg="black",font=("Helvetica",15))#self.__ventana de texto
        self.__r.place(x=500,y=25)
        botonMover = Button(self.__ventana, text="Mover enemigo", command=self.movement,bg="#144214",fg="white",font=("Helvetica",15)).place(x=100,y=20)
        botonInsertarEnemigo= Button(self.__ventana, text="InsertarEnemigo", command=self.__insertarEnemigo,bg="#096654",fg="white",font=("Helvetica",15)).place(x=400,y=20)
        self.__ventana.mainloop()

    def __insertarEnemigo(self):
        self.enemigo.append(Enemigo(random.randrange(3)))#Este nos crea un enemigo de tipo mario
        tag="f"+str(self.size)
        print(self.enemigo)
        self.__fondo.create_image(0,0,image=self.enemigo[self.size].imagen,tags=tag)
        self.size+=1



    def movement(self):
        j=random.randrange(self.size)
        self.enemigo[j].move(15,0)
        tag="f"+str(j)
        self.__fondo.move(tag,self.enemigo[j].posx,self.enemigo[j].posy)
        self.__fondo.after(100,self.movement)


    def __mover(self):
        j=random.randrange(self.size)
        self.enemigo[j].move(15,0)
        tag="f"+str(j)
        self.__fondo.move(tag,self.enemigo[j].posx,self.enemigo[j].posy)
        

    def threadMain(self):
        hilo=Thread(target=self.threadAux,args=(0,15,0))
        hilo.setDaemon(True)
        hilo.start()
        

    def threadAux(self,i,x,y):
        if(i==len(self.enemigo)):
            i=0
            x+=10
            y+=0
        else:
            for x in range(10):
                self.enemigo[i].move(x,0)
                tag="f"+str(i)
                self.__fondo.move(tag,self.enemigo[i].posx,self.enemigo[i].posy)
            return self.threadAux(i+1,x,y)

        









class Enemigo:
    def __init__(self,tipo):
        if (tipo==0):
            self.tipo="escudero"
            self.imagen=self.__cargarImagen("escudero.png")
            self.posx=0
            self.posy=10
        if (tipo==1):
            self.tipo="canibal"
            self.imagen=self.__cargarImagen("escudero.png")
            self.posx=0
            self.posy=40
        if (tipo==2):
            self.tipo="leñador"
            self.imagen=self.__cargarImagen("escudero.png")
            self.posx=0
            self.posy=70
        
     

    def move(self,x,y):
        self.posx+=x
        self.posy+=y




    def __cargarImagen(self,nombre):
        if isinstance(nombre, str):
            #path = os.path.join('Img',nombre)
            imagen = PhotoImage(file=nombre)
            return imagen
        
x=Tablero()
x.dibujar()
