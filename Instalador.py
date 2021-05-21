import wget
from Modulos import *

root = Tk()
root.title("Instalar")
root.iconbitmap('iconos e imagenes\icono.ico')
root.geometry("500x345")
root.resizable(width=False, height=False)

def cancelar():

    mas = messagebox.askyesno("cancelar la instalacion", "seguro que desea cancelar la instalacion")
    if mas:
        root.destroy()

root.protocol("WM_DELETE_WINDOW", cancelar)

def operacion():
    frome.place_forget()
    n.place_forget()
    o.place_forget()
    v.place_forget()
    w.place_forget()
    a.place_forget()
    y.place_forget()
    x.place_forget()
    m.place_forget()
    casa.place_forget()
    mesa.place_forget()
    comando1()


def operaciones2():
    fram.place_forget()
    ropa.place_forget()
    labanda.place_forget()
    luis.place_forget()
    l.place_forget()
    ro.place_forget()
    ber.place_forget()
    lo.place_forget()
    barra.place_forget()
    barra1.place_forget()
    frome.place(x=0, y=0)
    n.place(x=170, y=39)
    o.place(x=170, y=69)
    v.place(x=170, y=110)
    w.place(x=170, y=138)
    y.place(x=170, y=155)
    a.place(x=170, y=195)
    m.place(x=170, y=215)
    x.place(x=20, y=39)
    casa.place(x=310, y=310)
    mesa.place(x=400, y=310)


frome = Frame(root, width=570, height=299, bg="white", borderwidth=1)
frome.config(relief="raised")
frome.place(x=0, y=0)

fuento = tkinter.font.Font(family="Calibri", size=19)

fuent = tkinter.font.Font(family="artic", size=8)

n = Label(text="Bienvenido al asistente de", bg="white", font=fuento)
n.place(x=170, y=39)

o = Label(text="Instalacion de este programa", bg="white", font=fuento)
o.place(x=170, y=69)

v = Label(text="Este programa instalara este programa 1.0 en su sistema", bg="white", font=fuent)
v.place(x=170, y=110)

w = Label(text="Se recomienda cerrear todas las ventanas antes de", bg="white", font=fuent)
w.place(x=170, y=138)

y = Label(text="continuar.", bg="white", font=fuent)
y.place(x=170, y=155)

a = Label(text="Haga clic en Siguiente para continuar o en Cancelar para salir", bg="white", font=fuent)
a.place(x=170, y=195)

m = Label(text="de la instalacion.", bg="white", font=fuent)
m.place(x=170, y=215)

imagen = PhotoImage(file="iconos e imagenes\landra.png")

x = Label(frome, image=imagen)
x.place(x=20, y=39)

casa = Button(text="Siguiente", width=10, relief="groove", bd=1, command=operacion)
casa.place(x=310, y=310)

mesa = Button(text="Cancelar", width=10, relief="groove", bd=1, command=cancelar)
mesa.place(x=400, y=310)


def commando():
    fram.place_forget()
    ropa.place_forget()
    labanda.place_forget()
    luis.place_forget()
    l.place_forget()
    ro.place_forget()
    ber.place_forget()
    lo.place_forget()
    barra.place_forget()
    barra1.place_forget()


def comando1():
    fram.place(x=0, y=0)
    ropa.place(x=19, y=1)
    labanda.place(x=39, y=20)
    luis.place(x=40, y=59)
    l.place(x=244, y=310)
    ro.place(x=319, y=310)
    ber.place(x=419, y=310)
    lo.place(x=50, y=89)
    barra.place(x=445, y=89, height=198)
    barra1.place(x=47, y=289, width=400)

def lugar():
    Angel.place_forget()
    ropita.place_forget()
    suafan.place_forget()
    nando.place_forget()
    saya.place_forget()
    nome.place_forget()
    medi.place_forget()
    sape.place_forget()
    chupa.place_forget()
    perro.place_forget()
    diga.place_forget()


def lolos():
    Angel.place_forget()
    ropita.place_forget()
    suafan.place_forget()
    nando.place_forget()
    saya.place_forget()
    nome.place_forget()
    medi.place_forget()
    sape.place_forget()
    chupa.place_forget()
    perro.place_forget()
    diga.place_forget()
    fram.place(x=0, y=0)
    ropa.place(x=19, y=1)
    labanda.place(x=39, y=20)
    luis.place(x=40, y=59)
    l.place(x=244, y=310)
    ro.place(x=319, y=310)
    ber.place(x=419, y=310)
    lo.place(x=50, y=89)
    barra.place(x=445, y=89, height=198)
    barra1.place(x=47, y=289, width=400)

def sevolin():
    fram.place_forget()
    ropa.place_forget()
    labanda.place_forget()
    luis.place_forget()
    l.place_forget()
    ro.place_forget()
    ber.place_forget()
    lo.place_forget()
    barra.place_forget()
    barra1.place_forget()
    Angel.place(x=0, y=0)
    ropita.place(x=19, y=1)
    suafan.place(x=39, y=158, width=360, height=20)
    chupa.place(x=9, y=99)
    nando.place(x=9, y=117)
    perro.place(x=119, y=69)
    saya.place(x=49, y=20)
    nome.place(x=244, y=310)
    diga.place(x=319, y=310)
    medi.place(x=419, y=310)
    sape.place(x=410, y=158)


def ubicacion():
    fram.place_forget()
    ropa.place_forget()
    labanda.place_forget()
    luis.place_forget()
    l.place_forget()
    ro.place_forget()
    ber.place_forget()
    lo.place_forget()
    barra.place_forget()


fram = Frame(root, bg="white", width=570, height=53, borderwidth=1)
fram.place(x=0, y=0)

fuente = tkinter.font.Font(size=9, weight="bold")
fuent = fuente.Font(family="Calibri", size=5)

ropa = Label(text="Informacion", bg="white", font=fuente)
ropa.place(x=19, y=1)

labanda = Label(text="Es importante que lea la siguiente informacion antes de continuar", bg="white", font=fuent)
labanda.place(x=39, y=20)

luis = Label(text="Cuando este listo para continuar con la instalacion, haga clic en Siguiente.")
luis.place(x=40, y=59)

l = Button(root, text="< Atras", width=9, relief="groove", bd=1, command=operaciones2)
l.place(x=244, y=310)

ro = Button(root, text="Siguiente >", width=9, relief="groove", bd=1, command=sevolin)
ro.place(x=319, y=310)

ber = Button(root, text="Cancelar", width=9, relief="groove", bd=1, command=cancelar)
ber.place(x=419, y=310)

lo = Text(root, width=49, height=12, bd=2, wrap="none")
lo.place(x=50, y=89)

barra = Scrollbar(root, command=lo.yview)
lo.config(yscrollcommand=barra.set)
barra.place(x=445, y=89, height=198)

barra1 = Scrollbar(root, command=lo.xview, orient=HORIZONTAL)
lo.config(xscrollcommand=barra1.set)
barra1.place(x=47, y=289, width=400)

licensia = open("LICENSE","r")

licensia1 = licensia.read()

lo.insert(1.0, licensia1)

lo["state"] = "disable"

commando()

Angel = Frame(root, bg="white", width=570, height=53, borderwidth=1)
Angel.place(x=0, y=0)

file = "C:\Program Files"

def abrir():
    global file

    file = FileDialog.askdirectory(initialdir="C:\Program Files", title="Abrir")


    if len(file) > 0:
        sufall.set("")
        sufall.set(file)


def archivo():

    os.chdir(file)

    try:
        os.mkdir("contabilidad")
    except:
        propuesta = messagebox.askyesno("","Desea volver a instalar este programa en su sistema?")
        if propuesta:
            shutil.rmtree("contabilidad")
            os.mkdir("contabilidad")

    os.chdir("contabilidad")

    url = "https://download1335.mediafire.com/s8l98i405pqg/3368ata1bfvye0x/inicio.py"
    url2 = "https://download1591.mediafire.com/ksxta53h625g/rkmro9kl3qb8li3/Modulos.py"
    url3 = "https://download1652.mediafire.com/oug0gt4edlsg/d2q1tu6k4akhqee/principal.py"
    url4 = "https://download1080.mediafire.com/uui3rnr6vuug/trvrhqa68celyk7/user.py"

    wget.download(url)
    wget.download(url2)
    wget.download(url3)
    wget.download(url4)

    os.mkdir("iconos e imagenes")
    os.chdir("iconos e imagenes")

    hacia_atras = "https://download1474.mediafire.com/f338e7q2f3ug/5t6lkd91ik61g1q/hacia+atras.png"
    hacia_adelante = "https://download1327.mediafire.com/4r64hyfvh70g/s8ricyyrxmkxtn1/hacia+adelante.png"
    landra = "https://download1638.mediafire.com/38egairmkt3g/cmtu33zj7dj8air/landra.png"
    salir = "https://download1475.mediafire.com/72dfx9kkt4ug/jmo5i8omfli4t5u/salir.png"

    wget.download(hacia_atras)
    wget.download(hacia_adelante)
    wget.download(landra)
    wget.download(salir)


# angel luis propiedad
sufall = StringVar()

sufall.set("C:\Program Files")

puca = tkinter.font.Font(size=8, weight="bold")
fd = tkinter.font.Font(family="Calibri", size=10)
font = tkinter.font.Font(size=8)

ropita = Label(text="Selecciona la carpeta de Destino", bg="white", font=fd)


suafan = Entry(root, font=puca, textvariable=sufall)
suafan.config(bd=2)
suafan.place(x=39, y=158, width=360, height=20)

chupa = Label(text="para continuar, haga clic en Siguiente. si desea seleccionar una  carpeta diferente, haga",font=puca)

nando = Label(text="haga clic en examinar.", font=puca)

perro = Label(text="El programa instalara en la siguiente carpeta.", font=fd)

saya = Label(text="¿Donde debe instalarse?", bg="white", font=fd)
saya.place(x=49, y=20)

nome = Button(root, text="< Atras", width=9, relief="groove", bd=1, command=lolos)
nome.place(x=244, y=310)

diga = Button(root, text="Siguiente >", width=9, relief="groove", bd=1, command=archivo)
diga.place(x=319, y=310)

medi = Button(root, text="Cancelar", width=9, relief="groove", bd=1, command=cancelar)
medi.place(x=419, y=310)

sape = Button(text="examinar...", command=abrir)
sape.place(x=410, y=158)

lugar()

root.mainloop()
