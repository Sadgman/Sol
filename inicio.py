from Modulos import *

root = Tk()

root.iconbitmap('iconos e imagenes\icono.ico')

root.title("Iniciar de sesion")

root.resizable(0, 0)

root.config(width=500, height=300)

so = ""
z = False

def cosito1():

    global so

    carlitos = str(root.focus_get())

    try:

        if carlitos[7] == "2":

            Nombre.menu.post(so.x_root, so.y_root)

        elif carlitos[7] == "3":

            fight.menu.post(so.x_root, so.y_root)

    except:

        if carlitos[6] == "y":

            Company.menu.post(so.x_root, so.y_root)

def cosito(eventico):

    global so

    so = eventico

    carlitos = str(root.focus_get())

    try:
        if carlitos[7] == "2":
            Nombre.menu.post(eventico.x_root, eventico.y_root)

        elif carlitos[7] == "3":
            fight.menu.post(eventico.x_root, eventico.y_root)

    except:

        if carlitos[6] == "y":
            Company.menu.post(eventico.x_root, eventico.y_root)


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

def ejecucion():
    global z
    k = 0

    nanombre = sqlite3.connect("Data_base.db")

    cursor = nanombre.cursor()

    cursor.execute("SELECT EXISTS (SELECT 1 FROM PERSONA WHERE NOMBRE = ? LIMIT 1)", (name.get(),))

    personas = cursor.fetchone()

    if personas[0] == 1:

        k += 1


    else:

        messagebox.showinfo("", "El usuario que a introducido es incorrecto")

    nanombre.commit()

    nanombre.close()

    nanombre = sqlite3.connect("Data_base.db")

    cursor = nanombre.cursor()

    cursor.execute("SELECT EXISTS (SELECT 1 FROM PERSONA WHERE CONTRASEÑA = ? LIMIT 1)", (password.get(),))

    personas = cursor.fetchone()

    if personas[0] == 1:

        k += 1

    else:

        messagebox.showinfo("", "La contraseña que a introducido es incorrecta")

    nanombre.commit()

    nanombre.close()

    if k == 2:
        root.destroy()
        z = True

def enviar_abrir():
    if z:
        return True

def comprobacion1():

    if chequeo.get() == 1:

        fight.config(show="")

    else:

        fight.config(show="*")


def info():

    variable = name.get()

    v = password.get()

    s = compañia.get()

    if variable == "" and v == "":

        contraseña_vacia.place_forget()

        nombre_vacio.place_forget()

        Ambos_vacios.place(x=320, y=137)

    elif variable == "":

        contraseña_vacia.place_forget()

        Ambos_vacios.place_forget()

        nombre_vacio.place(x=320, y=137)

    elif v == "":

        nombre_vacio.place_forget()

        Ambos_vacios.place_forget()

        contraseña_vacia.place(x=320, y=137)


    else:

        if s == "":
            cuestion = messagebox.askyesno("", "Su compañia no tiene nombre desea continuar asi?")

            if cuestion:
                ejecucion()

        else:
            s = compañia.get()
            w = 0

            try:

                actual = os.getcwd()

                os.chdir(s)

                os.chdir(variable)

                os.chdir(actual)

                w += 1

            except:

                messagebox.showinfo("", "La compañia que introdujo no existe")

            if w == 1:

                ejecucion()


compañia = StringVar()

name = StringVar()

chequeo = IntVar()

password = StringVar()

fuent = fuente.Font(family="Lucida Grande", size=20)
fuente = fuente.Font(family="Lucida Grande", size=15)
###########################Negocio################################

ttk.Label(root, text="Negocio :", font=fuent).place(relx=.0, rely=.2)

Company = ttk.Entry(root, font=fuente, textvariable=compañia)
Company.place(x=125, y=68, width=168, height=30)

Company.menu = Menu(tearoff=False)
Company.menu.add_command(label="Copiar", command=copiar)
Company.menu.add_separator()
Company.menu.add_command(label="Pegar", command=pegar)
Company.bind("<Button-3>",cosito)

##########################Nombre################################

ttk.Label(root, text="Nombre :", font=fuent).place(relx=.0, rely=.4)

Nombre = ttk.Entry(root, font=fuente, textvariable=name)
Nombre.place(x=122, y=126, width=168, height=30)

Nombre.menu = Menu(tearoff=False)
Nombre.menu.add_command(label="Copiar", command=copiar)
Nombre.menu.add_separator()
Nombre.menu.add_command(label="Pegar", command=pegar)
Nombre.bind("<Button-3>",cosito)
##########################Contraseña##############################

ttk.Label(root, text="Contraseña :", font=fuent).place(relx=.0, rely=.6)

fight = ttk.Entry(root, font=fuente, textvariable=password)
fight.config(show="*")
fight.place(x=170, y=186, width=168, height=30)

fight.menu = Menu(tearoff=False)
fight.menu.add_command(label="Copiar", command=copiar)
fight.menu.add_separator()
fight.menu.add_command(label="Pegar", command=pegar)
fight.bind("<Button-3>",cosito)
##################################################################

ttk.Checkbutton(root, text="Mostrar contraseña", variable=chequeo, onvalue=1, offvalue=0, command=comprobacion1).place(x=339, y=196)

boton = Button(root, text="Iniciar", width=20, command=info)
boton.place(x=100, y=270)

boton1 = Button(root, text="Continuar", width=20)
boton1.place(x=260, y=270)

lapiz = tkinter.font.Font(weight="bold", size=7)

style = ttk.Style()
style.configure("BW.TLabel", foreground="red")

Ambos_vacios = ttk.Label(text="Los campos estan vacios", font=lapiz, style="BW.TLabel")

nombre_vacio = ttk.Label(text="El campo nombre esta vacio", font=lapiz, style="BW.TLabel")

contraseña_vacia = ttk.Label(text="El campo contraseña esta vacio", font=lapiz, style="BW.TLabel")

root.bind("<Return>", saltar)

claves = {
    "<menu>": cosito1
}

L = keyboard.GlobalHotKeys(claves)
L.start()

root.mainloop()
