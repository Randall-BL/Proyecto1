"""******************************************************************************
                                   Instituto Tecnológico de Costa Rica
                                         Ingeniería en Computadores
Lenguaje: Python 3.8.5
Profesor: Milton Villegas Lemus
Autor: Randall Bryan Bolaños López
Versión: 1.0
Fecha Última Modificación: Noviembre 28 2020
*****************************************************************************"""
import os
import tkinter
import tkinter.messagebox
import vlc
from tkinter import *
import random
import json
import time
import csv
import threading
name=[]
shots=[]
spawndificultad=0

def auto_doc():
    """******************************************************************************
                                       Instituto Tecnológico de Costa Rica
                                             Ingeniería en Computadores
    Lenguaje: Python 3.8.5
    Profesor: Milton Villegas Lemus
    Autor: Randall Bryan Bolaños López
    Versión: 1.0
    Fecha Última Modificación: Noviembre 28 2020
    *****************************************************************************"""
    print (auto_doc.__doc__)

def cargarImg(archivo): #Define la función que permitira cargar la imagen para posteriormente crearla
    ruta= os.path.join('img',   archivo)
    imagen=PhotoImage(file=ruta)
    return imagen




def enemigo():#Random que luego va a servir para escoger al tipo de enemigo que se va a cargar
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



def posicion():#Random responsable de la posición en x de los enemigos
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

def musica():#Funcion que permite la reproducción de musica en bucle
    global player
    player.play()
    time.sleep(16)
    player.stop()
    return musica()



def mute():#Funcion que pausa la musica
    global player
    player.pause()


hiloFondo = threading.Thread(target=musica)
hiloFondo.start()

class Tablero(threading.Thread): #Clase encagarda del tablero del juego
    global random
    def __init__(self): #Variables que se uitilizaran despues en el codigo
        self.enemigo=[]
        self.balas=[]
        self.C_principal=None
        self.ventanajuego=None
        self.contadormoneda = 0
        self.sizebalas=0
        self.size=0
        self.listadetorres = []
        self.coin = 0
        print(self.enemigo)
        print(self.balas)

    def __cargarImagen(self,nombre):#Funcion que permite cargar la imagen dentro de la clase creada, dada por el tutor José Morales
        global random
        if isinstance(nombre, str):
            imagen = PhotoImage(file=nombre)
            return imagen


    def dibujar(self):#Función encargada de cargar las imagenes del tablero, la creación de la ventana del juego y la ventana del cronometro
        global random
        self.ventanajuego=Tk()
        self.ventanajuego.title("GAME")
        self.ventanajuego.geometry("1200x700+390+240")
        self.ventanajuego.resizable(width=NO, height=NO)
        self.C_principal= Canvas(self.ventanajuego, width= 1200, height = 700, bg="white")
        self.C_principal.place(x=0,y=0)
        img= self.__cargarImagen("Tablero1.png")
        self.imgArena = self.__cargarImagen("arena.png")
        self.imgFuego = self.__cargarImagen("fuego.png")
        self.imgRoca = self.__cargarImagen("rocas.png")
        self.imgAgua = self.__cargarImagen("agua.png")
        self.C_principal.create_image(600,350, image = img)
        BotonPausaMusica = Button(self.C_principal, width=8, height=4, text="Pausa/Play", command=mute).place(x=600, y=600)
        self.imgsand = self.__cargarImagen("Sand_Rook.png")
        self.imgsand1 = self.C_principal.create_image(323, 49, image=self.imgsand)
        self.imgRock = self.__cargarImagen("Rock_Rook.png")
        self.imgRock1 = self.C_principal.create_image(463, 49, image=self.imgRock)
        self.imgFire = self.__cargarImagen("Fire_Rook.png")
        self.imgFire1 = self.C_principal.create_image(830, 49, image=self.imgFire)
        self.imgWater = self.__cargarImagen("Water_Rook.png")
        self.imgWater1 = self.C_principal.create_image(1034, 49, image=self.imgWater)
        self.moneda50 = self.__cargarImagen("50.png")
        self.moneda25 = self.__cargarImagen("25.png")
        self.moneda100 = self.__cargarImagen("100.png")
        self.monedas = [self.moneda50, self.moneda25, self.moneda100]
        self.labelcoi = Label(self.C_principal, text="Coins= " + str(self.coin))
        self.labelcoi.place(x=620, y=30)
        self.root = Tk()
        self.root.title('Cronometro')

        self.time = Label(self.root, fg='red', width=20, font=("", "18"))
        self.time.pack()
        self.empezarJuego()
        self.C_principal.bind("<ButtonPress-1>", self.mouseevent)
        self.C_principal.bind("<ButtonRelease-1>", self.colocar_torre)
        self.ventanajuego.mainloop()

    def mouseevent(self, event):#Funcion que toma las coordenadas x y y del mouse para luego colocar las torres
        global labelcoi
        global coin
        global imgmoneda
        global moneda100
        global moneda25
        global moneda5
        rango = self.C_principal.bbox(self.imgsand1)
        rang = self.C_principal.bbox(self.imgRock1)
        rang1 = self.C_principal.bbox(self.imgFire1)
        rang2 = self.C_principal.bbox(self.imgWater1)
        rang3 = self.C_principal.bbox(imgmoneda)
        if event.x >= rango[0] and event.x < (rango[2]):
            if event.y >= rango[1] and event.y < (rango[3]):
                self.contadormoneda = 1
                self.coin = self.coin - 50
                self.labelcoi.config(text="Coins" + str(self.coin))

        if event.x >= rang[0] and event.x < (rang[2]):
            if event.y >= rang[1] and event.y < (rang[3]):
                self.contadormoneda = 2
                self.coin = self.coin - 100
                self.labelcoi.config(text="Coins" + str(self.coin))

        if event.x >= rang1[0] and event.x < (rang1[2]):
            if event.y >= rang1[1] and event.y < (rang1[3]):
                self.contadormoneda = 3
                self.coin = self.coin - 150
                self.labelcoi.config(text="Coins" + str(self.coin))

        if event.x >= rang2[0] and event.x < (rang2[2]):
            if event.y >= rang2[1] and event.y < (rang2[3]):
                self.contadormoneda = 4
                self.coin = self.coin - 200
                self.labelcoi.config(text="Coins" + str(self.coin))

        if event.x >= rang3[0] and event.x < (rang3[2]):
            if event.y >= rang3[1] and event.y < (rang3[3]):
                if str(self.monedas[0]) == str(self.moneda50):
                    self.coin = self.coin + 50
                    self.labelcoi.config(text="Coins" + str(self.coin))
                    self.contadormoneda = 5
                if str(self.monedas[0]) == str(self.moneda25):
                    self.coin = self.coin + 25
                    self.labelcoi.config(text="Coins" + str(self.coin))
                    self.contadormoneda = 5
                if str(self.monedas[0]) == str(self.moneda100):
                    self.coin = self.coin + 100
                    self.labelcoi.config(text="Coins" + str(self.coin))
                    self.contadormoneda = 5

    def colocar_torre(self, event):  #Función que toma las coordenadas del mouse para crear las torres donde se le indica
        if self.contadormoneda == 1:
            self.C_principal.create_image(event.x, event.y, anchor=CENTER, image=self.imgsand)
            self.spawnArena(event.x,event.y)
            #self.movementflecha()
            self.listadetorres.append(self.C_principal.create_image(event.x, event.y, anchor=CENTER, image=self.imgsand))
            self.C_principal.update()
            self.contadormoneda = 0
        if self.contadormoneda == 2:
            self.img2 = self.C_principal.create_image(event.x, event.y, anchor=CENTER, image=self.imgRock)
            self.spawnRoca(event.x, event.y)
            self.C_principal.update()
            self.contadormoneda = 0
        if self.contadormoneda == 3:
            self.img3 = self.C_principal.create_image(event.x, event.y, anchor=CENTER, image=self.imgFire)
            self.spawnFuego(event.x, event.y)
            self.C_principal.update()
            self.contadormoneda = 0
        if self.contadormoneda == 4:
            self.img4 = self.C_principal.create_image(event.x, event.y, anchor=CENTER, image=self.imgWater)
            self.spawnAgua(event.x, event.y)
            self.C_principal.update()
            self.contadormoneda = 0
        if self.contadormoneda==5:
            self.C_principal.delete(imgmoneda)
            self.C_principal.update()
            self.contadormoneda=0


    def spawnArena(self,x,y):#Funcion encargada de spawnear el proyectil de la torre indicada
        self.balas.append(random.randrange(4))
        tag1 = "g" + str(self.sizebalas)
        print(self.balas)
        self.C_principal.create_image(x, y, image=self.imgArena, tags=tag1)
        self.sizebalas += 1
    def spawnRoca(self,x,y):#Funcion encargada de spawnear el proyectil de la torre indicada
        self.balas.append(random.randrange(4))
        tag1 = "g" + str(self.sizebalas)
        print(self.balas)
        self.C_principal.create_image(x, y, image=self.imgRoca, tags=tag1)
        self.sizebalas += 1
    def spawnAgua(self,x,y):#Funcion encargada de spawnear el proyectil de la torre indicada
        self.balas.append(random.randrange(4))
        tag1 = "g" + str(self.sizebalas)
        print(self.balas)
        self.C_principal.create_image(x, y, image=self.imgAgua, tags=tag1)
        self.sizebalas += 1
    def spawnFuego(self,x,y):#Funcion encargada de spawnear el proyectil de la torre indicada
        self.balas.append(random.randrange(4))
        tag1 = "g" + str(self.sizebalas)
        print(self.balas)
        self.C_principal.create_image(x, y, image=self.imgFuego, tags=tag1)
        self.sizebalas += 1



    def movementflecha(self):#Funcion encargada de mover el proyectil de la torre indicada
        j=random.randrange(self.sizebalas)
        self.balas[j].move(0,0)
        tag="f"+str(j)
        self.posybala=92
        self.C_principal.move(tag,self.balas[j].posx,self.balas[j].posybala)
        self.C_principal.after(10,self.movement)

    def SpawnEnemigo(self):#Funcion encargada de spawnear el a los enemigos
        self.enemigo.append(Enemigo(random.randrange(4)))#Este nos crea un enemigo
        tag="f"+str(self.size)
        print(self.enemigo)
        self.C_principal.create_image(posicion(),585,image=self.enemigo[self.size].imagen,tags=tag)
        self.size+=1
        if self.size==20:
            return print("Finalizó el spawn")
        self.C_principal.after(spawndificultad,self.SpawnEnemigo)

    def empezarJuego(self):#Funcion con mas funciones para poder empezar el juego al momento de crear la ventana
        self.SpawnEnemigo()
        self.movement()
        self.iniciar()
        self.crearmoneda()


    def movement(self):#Funcion encargada del movimiento de los enemigos
        j=random.randrange(self.size)
        self.enemigo[j].move(0,0)
        tag="f"+str(j)
        self.C_principal.move(tag,self.enemigo[j].posx,self.enemigo[j].posy)
        self.C_principal.after(1,self.movement)

    def crearmoneda(self):#Funcion encargada de la creación de las monedas
        global random
        global moneda25
        global moneda25
        global moneda100
        global monedas
        global imgmoneda
        random.shuffle(self.monedas)
        imgmoneda = self.C_principal.create_image(random.randint(100, 600), random.randint(300, 600), anchor=CENTER, image=self.monedas[0],tags=str(self.monedas[0]))
        self.C_principal.after(6000,self.crearmoneda)

    def iniciar(self, h=0, m=0, s=0):#Funcion encargada del cronometro
        if s >= 60:
            s = 0
            m = m + 1
            if m >= 60:# Verificamos si los segundos y los minutos son mayores a 60 y Verificamos si las horas son mayores a 24
                m = 0
                h = h + 1
                if h >= 24:
                    h = 0
        self.time['text'] = str(h) + ":" + str(m) + ":" + str(s)#Muestra el cronometro en pantalla
        self.proceso = self.time.after(1000, self.iniciar, (h), (m), (s + 1))#Inicia cuenta regresiva


#-------------------------------------------------Scores----------------------------------------------------------------
    """def imprimirscore():

        with open('puntajes.json') as file:  # abre el doc de puntajes
            scores = json.load(file)
        self.C_principal.create_text(self.C_principal.winfo_width() / 2, 320,
                                     text=str(scores["Nombres"][0]) + " " + str(scores["Scores"][0]), fill="yellow",
                                     font=Fuente2)  # crea un texto con el jugador con el punteje mas alto
        self.C_principal.create_text(self.C_principal.winfo_width() / 2, 350,
                                     text=str(scores["Nombres"][1]) + " " + str(scores["Scores"][1]), fill="yellow",
                                     font=Fuente2)  # segundo puntaje mas alto
        self.C_principal.create_text(self.C_principal.winfo_width() / 2, 380,
                                     text=str(scores["Nombres"][2]) + " " + str(scores["Scores"][2]), fill="yellow",
                                     font=Fuente2)  # tercer puntaje mas alto
        self.C_principal.create_text(self.C_principal.winfo_width() / 2, 410,
                                     text=str(scores["Nombres"][3]) + " " + str(scores["Scores"][3]), fill="yellow",
                                     font=Fuente2)  # cuarto mas alto
        self.C_principal.create_text(self.C_principal.winfo_width() / 2, 440,
                                     text=str(scores["Nombres"][4]) + " " + str(scores["Scores"][4]), fill="yellow",
                                     font=Fuente2)  # quinto mas alto"""
#-----------------------------------------------Class Enemigo------------------------------------------------------------
class Enemigo:#Clase encargada de los enemigos
    def __init__(self, tipo):#Escoger el tipo de enemigo, dada por el tutor José Morales
        if (tipo == 0):
            self.tipo = "escudero"
            self.imagen = self.__cargarImagen("escudero.png")
            self.posx = posicion()
            self.posy = -0.0092
        if (tipo == 1):
            self.tipo = "canibal"
            self.imagen = self.__cargarImagen("canibal.png")
            self.posx = posicion()
            self.posy = -0.00671
        if (tipo == 2):
            self.tipo = "leñador"
            self.imagen = self.__cargarImagen("leñador.png")
            self.posx = posicion()
            self.posy = -0.00723
        if (tipo == 3):
            self.tipo = "arquero"
            self.imagen = self.__cargarImagen("arquero.png")
            self.posx = posicion()
            self.posy = -0.0092

    def move(self, x, y):#X y Y de los enemigos
        self.posx = x
        self.posy += y


    def __cargarImagen(self, nombre):#Cargar imagen de la clase
        if isinstance(nombre, str):
            imagen = PhotoImage(file=nombre)
            return imagen





#----------------------------------------------------Highscore--------------------------------------------------------------
"""def highscore(): #funcion que comprueba si se deben guardar
    with open("puntajes.json") as file: #abre el doc
        puntajes = json.load(file)

    if Score>puntajes['Scores'][0]: #si el puntaje es mayor al mas alto lo guarda y corre todos un espacio sacando al quinto

        puntajes['Scores'] = [Score] + puntajes['Scores'][:-1]
        puntajes["Nombres"] = [name] + puntajes["Nombres"][:-1]
        with open('puntajes.json','w') as file:
            json.dump(puntajes,file)
    elif Score == puntajes['Scores'][0]: #si es igual no lo guarda
        pass

    elif Score>puntajes['Scores'][1]: #si es mayor al segundo deja al primero y corre los demas un espacio

        puntajes['Scores'] = puntajes['Scores'][0:1] + [Score] + puntajes['Scores'][1:-1]
        puntajes["Nombres"] = puntajes["Nombres"][0:1] + [name] + puntajes["Nombres"][1:-1]
        with open('puntajes.json','w') as file:
            json.dump(puntajes,file)
    elif Score == puntajes['Scores'][1]: #si es igual no lo guarda
        pass

    elif Score>puntajes['Scores'][2]: #si es mayor al tercero deja el 1 y 2 y corre los demas un espacio

        puntajes['Scores'] = puntajes['Scores'][0:2] + [Score] + puntajes['Scores'][2:-1]
        puntajes["Nombres"] = puntajes["Nombres"][0:2] + [name] + puntajes["Nombres"][2:-1]
        with open('puntajes.json','w') as file:
            json.dump(puntajes,file)
    elif Score == puntajes['Scores'][2]: #si es igual no lo guarda
        pass

    elif Score>puntajes['Scores'][3]: #si es mayor al cuarto deja los primeros y corre un espacio

        puntajes['Scores'] = puntajes['Scores'][0:3] + [Score] + puntajes['Scores'][3:-1]
        puntajes["Nombres"] = puntajes["Nombres"][0:3] + [name] + puntajes["Nombres"][3:-1]
        with open('puntajes.json','w') as file:
            json.dump(puntajes,file)
    elif Score == puntajes['Scores'][3]: #si es igual no lo guarda
        pass

    elif Score>puntajes['Scores'][4]: #si es mayor al ultimo lo reemplaza

        puntajes['Scores'] = puntajes['Scores'][0:4] + [Score]
        puntajes["Nombres"] = puntajes["Nombres"][0:4] + [name]
        with open('puntajes.json','w') as file:
            json.dump(puntajes,file)
    elif Score == puntajes['Scores'][4]:#si es igual no se guarda
        pass"""

#-------------------------------------------------------ventanainicial-------------------------------------------------


def about():#Funcion para la ventana creditos
    ventanabout.deiconify()

def ayuda():#Funcion para la ventana ayuda
    ventanayuda.deiconify()
def dificultad():#Funcion para la ventana dificultad
    ventanadificultad.deiconify()

def dificultadfacil():#Funcion para escoger la dificultad en facil
    global spawndificultad
    spawndificultad=4000
    ventanadificultad.destroy()

def dificultadmedio():#Funcion para escoger la dificultad en medio
    global spawndificultad
    spawndificultad=2800
    ventanadificultad.destroy()

def dificultaddificil():#Funcion para escoger la dificultad en dificil
    global spawndificultad
    spawndificultad=1600
    ventanadificultad.destroy()

def prejuego():#Funcion encargada en verificar el login y la dificultad, para así poder iniciar el juego
    global spawndificultad
    if len(name) > 0:
        lectura()
        if spawndificultad==0:
            tkinter.messagebox.showinfo("Dificultad","Seleccione la dificultad primero")
            return
        ventana.destroy()
    else:
        tkinter.messagebox.showinfo(message="Name must have at least 1 character") #si no hay un nombre establecido no se puede jugar

#-----------------------lee-el-csv-----------------------------------------------------------#
def comprobar_user(name,documento2,i): #funcion que comprueba si el usuario ya se encuentra en el doc
#se utiliza un programa de recursion realizado en practicas anteriores
    if i == len(documento2): # si no lo encuentra lo guarda
        with open("Usuarios.csv","a", newline = '') as doc_Usuarioscsv:
            csv_data = csv.writer(doc_Usuarioscsv)
            csv_data.writerows([[name]])
        doc_Usuarioscsv.close()
    elif [name] == documento2[i]:
        pass #si se encuentra el usuario no lo guarda pero igual se utiliza para el puntaje
    else:
        comprobar_user(name,documento2,i+1) #recursion

def lectura(): #funcion que lee el documento para la revision del usuario
    global name
    doc = open("Usuarios.csv","r") #se abre el doc
    documento = csv.reader(doc) #se lee
    documento2=list(documento)
    doc.close()# se cierra el doc
    comprobar_user(name,documento2,0)#se llama a la funcion comprobar




ventana=Tk()
ventana.title("Avatars vs rooks")
ventana.geometry("1200x700+390+240")
ventana.resizable(width=NO, height=NO)
#Crear imagen de fondo
C_menu=Canvas(ventana, width=1200, height=700, bg='black')
C_menu.place(x=0, y=0)
C_menu.fondo=cargarImg('menu.png')
imgCanvas= C_menu.create_image(0,0, anchor=NW, image= C_menu.fondo)

def usuario():  # funcion que obtiene el usuario y lo garda en una variable
    global name
    global texto
    name = data.get()


data = StringVar()  # se define que es de tipo str<
textField = Entry(C_menu, textvariable=data)  # entry para insertar el usuario y poscicion
textField.place(x=320, y=450)
savename = Button(C_menu, text="Set Nick Name", command=usuario)  # boton para guardar el usuario y poscicion
savename.place(x=450, y=450)
playbut = Button(C_menu, text=" Play ", font=21, command=prejuego)  # boton para iniciar el juego
playbut.place(x=350, y=480)

ventanabout=Toplevel(ventana)#Ventanda de creditos
ventanabout.title("About")
ventanabout.geometry("500x600+760+300")
ventanabout.resizable(width= NO, height=NO)
C_about=Canvas(ventanabout,width=500, height=650,bg="white")
C_about.place(x=0, y=0)
C_about.fondo=cargarImg("About.png")
imgAbout=C_about.create_image(0,0, anchor=NW, image=C_about.fondo)
ventanabout.withdraw()

PlayAbout=Button(C_menu,width=8,height=4,text="Crèditos",command=about).place(x=1100, y=600)

ventanayuda=Toplevel(ventana)#ventana de ayuda
ventanayuda.title("About")
ventanayuda.geometry("500x600+760+300")
ventanayuda.resizable(width= NO, height=NO)
C_ayuda=Canvas(ventanayuda,width=500, height=650,bg="white")
C_ayuda.place(x=0, y=0)
C_ayuda.fondo=cargarImg("ayuda.png")
imgAyuda=C_ayuda.create_image(0,0, anchor=NW, image=C_ayuda.fondo)
ventanayuda.withdraw()

PlayAyuda=Button(C_menu,width=8,height=4,text="Ayuda",command=ayuda).place(x=1000, y=600)

ventanadificultad=Toplevel(ventana)#ventana de dificultad
ventanadificultad.title("Seleccione dificultad")
ventanadificultad.geometry("500x600+760+300")
ventanadificultad.resizable(width=NO,height=NO)
C_dificultad=Canvas(ventanadificultad,width=500,height=650,bg="white")
C_dificultad.place(x=0,y=0)
ventanadificultad.withdraw()

selecdificultad=Button(C_menu,width=8,height=4,text="dificultad",command=dificultad).place(x=800,y=600)
facil=Button(ventanadificultad,width=10, height=6,text="Facil",command=dificultadfacil).place(x=200,y=100)
medio=Button(ventanadificultad,width=10, height=6,text="medio",command=dificultadmedio).place(x=200,y=200)
dificil=Button(ventanadificultad,width=10, height=6,text="dificil",command=dificultaddificil).place(x=200,y=300)
auto_doc()
ventana.mainloop()


t=Tablero()
t.dibujar()#Dibuja el tablero
