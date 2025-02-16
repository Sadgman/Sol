import os
import sqlite3

from Modulos import *

corchete = False

root = Tk()
root.resizable(0, 0)
root.title("Crear un usuario")
root.iconbitmap('iconos e imagenes\\icono.ico')
root.config(width=500, height=299)

def cosito(eventico):

    carlitos = str(root.focus_get())

    try:
        if carlitos[7] == "2":
            Nombre.menu.post(eventico.x_root, eventico.y_root)

        elif carlitos[7] == "3":
            fight.menu.post(eventico.x_root, eventico.y_root)

    except:
        try:

            if carlitos[6] == "y":
                Company.menu.post(eventico.x_root, eventico.y_root)
        except:
            pass
def copiar():

    carlitos = str(root.focus_get())

    try:

        if carlitos[7] == "2":
            Nombre.event_generate("<<Copy>>")

        elif carlitos[7] == "3":
            fight.event_generate("<<Copy>>")

    except:

        if carlitos[6] == "y":
            Company.event_generate("<<Copy>>")

def pegar():
    carlitos = str(root.focus_get())

    try:
        if carlitos[7] == "2":
            Nombre.event_generate("<<Paste>>")

        elif carlitos[7] == "3":
            fight.event_generate("<<Paste>>")

    except:

        if carlitos[6] == "y":
            Company.event_generate("<<Paste>>")


def saltar(evento):
    carlos = str(root.focus_get())

    try:

        if carlos[7] == "2":

            fight.focus_set()

        elif carlos[7] == "3":

            info()

            Company.focus_set()

    except:

        if carlos[6] == "y":
            Nombre.focus_set()


def comprobacion1():
    if chequeo.get() == 1:

        fight.config(show="")

    else:

        fight.config(show="*")


def comprobacion():
    
    ccompa = (compañia.get() + name.get()).lower()
    p = int(len(password.get()))
    s = compañia.get()

    if(re.fullmatch(r'^[a-záéíóúñ0-9 ]+$', ccompa) is None):
        messagebox.showwarning("", "No se permiten caracteres extraños")
        return

    elif len(name.get()) > 100: messagebox.showwarning("", "Demaciado largo"); return

    elif p < 4: messagebox.showwarning("", "Contraseña muy corta"); return
    
    elif not s: os.makedirs(os.path.join(os.getcwd(), s, name.get()), exist_ok=True)

    extensions()


def info():
    # -----------------------------------
    s = compañia.get()

    variable = name.get()

    v = password.get()
    # -----------------------------------
    if not variable and not v:

        contraseña_vacia.place_forget()

        nombre_vacio.place_forget()

        Ambos_vacios.place(x=320, y=137)

    elif not variable:

        contraseña_vacia.place_forget()

        Ambos_vacios.place_forget()

        nombre_vacio.place(x=320, y=137)

    elif not v:

        nombre_vacio.place_forget()

        Ambos_vacios.place_forget()

        contraseña_vacia.place(x=320, y=137)

    else:

        if not s:

            cuestion = messagebox.askyesno("", "Seguro que quieres continuar sin una compañia?")

            if cuestion:
                comprobacion()

        else:

            comprobacion()


def extensions():
    global corchete
    s = str(compañia.get())

    l = str(name.get())

    v = password.get()

    lista = [
        (l, v, s)
    ]

    try:
        nanombre = sqlite3.connect("./db/NDB.db")

        cursor = nanombre.cursor()

        cursor.executemany("INSERT INTO PERSONA (NOMBRE, CONTRASEÑA, COMPAÑIA) VALUES(?,?,?)", lista)

        nanombre.commit()

        nanombre.close()

        root.destroy()
        corchete = True

    except:

        messagebox.showinfo("", "El usuario ya existe")

name = StringVar()

compañia = StringVar()

chequeo = IntVar()

password = StringVar()

fuent = fuente.Font(family="Lucida Grande", size=20)
fuente = tkinter.font.Font(family="Lucida Grande", size=15)

###########################Compañia###############################
ttk.Label(root, text="Negocio :", font=fuent).place(relx=.0, rely=.2)

Company = ttk.Entry(root, font=fuente, textvariable=compañia)
Company.place(x=125, y=68, width=168, height=30)

Company.menu = Menu(tearoff=False)
Company.menu.add_command(label="Copiar", command=copiar)
Company.menu.add_separator()
Company.menu.add_command(label="Pegar", command=pegar)
Company.bind("<Button-3>", cosito)
#########################Nombre################################
ttk.Label(root, text="Nombre :", font=fuent).place(relx=.0, rely=.4)

Nombre = ttk.Entry(root, font=fuente, textvariable=name)
Nombre.place(x=122, y=126, width=168, height=30)

Nombre.menu = Menu(tearoff=False)
Nombre.menu.add_command(label="Copiar", command=copiar)
Nombre.menu.add_separator()
Nombre.menu.add_command(label="Pegar", command=pegar)
Nombre.bind("<Button-3>", cosito)
#######################Contraseña#################################
ttk.Label(root, text="Contraseña :", font=fuent).place(relx=.0, rely=.6)

fight = ttk.Entry(root, font=fuente, textvariable=password)
fight.config(show="*")
fight.place(x=170, y=186, width=168, height=30)

fight.menu = Menu(tearoff=False)
fight.menu.add_command(label="Copiar", command=copiar)
fight.menu.add_separator()
fight.menu.add_command(label="Pegar", command=pegar)
fight.bind("<Button-3>", cosito)
####################################################################

ttk.Checkbutton(root, text="Mostrar contraseña", variable=chequeo, onvalue=1, offvalue=0, command=comprobacion1).place(
    x=339, y=196)

boton = Button(root, text="Crear", width=20, command=info)
boton.place(x=100, y=270)

boton1 = Button(root, text="Continuar", width=20)
boton1.place(x=260, y=270)

root.bind("<Return>", saltar)

lapiz = tkinter.font.Font(weight="bold", size=7)

style = ttk.Style()
style.configure("BW.TLabel", foreground="red")

Ambos_vacios = ttk.Label(text="Los campos estan vacios", font=lapiz, style="BW.TLabel")

nombre_vacio = ttk.Label(text="El campo nombre esta vacio", font=lapiz, style="BW.TLabel")

contraseña_vacia = ttk.Label(text="El campo contraseña esta vacio", font=lapiz, style="BW.TLabel")

Company.menu = Menu(tearoff=False)
Company.menu.add_command(label="Copiar", command=copiar)
Company.menu.add_separator()
Company.menu.add_command(label="Pegar", command=pegar)
Company.bind("<Button-3>", cosito)

Nombre.menu = Menu(tearoff=False)
Nombre.menu.add_command(label="Copiar", command=copiar)
Nombre.menu.add_separator()
Nombre.menu.add_command(label="Pegar", command=pegar)
Nombre.bind("<Button-3>", cosito)

fight.menu = Menu(tearoff=False)
fight.menu.add_command(label="Copiar", command=copiar)
fight.menu.add_separator()
fight.menu.add_command(label="Pegar", command=pegar)
fight.bind("<Button-3>", cosito)

root.mainloop()

def soplamocos():
    if corchete:

        return True
