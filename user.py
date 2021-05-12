import os

from Modulos import *

root = Tk()
root.resizable(0, 0)
root.title("")
root.iconbitmap('iconos e imagenes\icono.ico')
root.config(width=500, height=299)


def cosito(eventico):

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


def comprobacion1():
    if chequeo.get() == 1:

        fight.config(show="")

    else:

        fight.config(show="*")


def comprobacion():
    s = compañia.get()

    variable = name.get()

    l = int(len(name.get()))

    v = int(len(password.get()))

    if l > 20:

        messagebox.showwarning("", "Demaciado largo")

    elif v < 5:

        m = messagebox.askyesno("", "La contraseña es poco segura, Quieres continuar?")

        if m:

            if s == "":

                extensions()

            else:

                try:
                    ruta = os.getcwd()
                    os.mkdir(s)
                    os.chdir(s)
                    os.mkdir(variable)
                    os.chdir(ruta)

                except:

                    ruta = os.getcwd()
                    os.chdir(s)
                    os.mkdir(variable)
                    os.chdir(ruta)

                extensions()
    else:

        if s == "":
            extensions()

        else:

            try:
                ruta = os.getcwd()
                os.mkdir(s)
                os.chdir(s)
                os.mkdir(variable)
                os.chdir(ruta)

            except:

                ruta = os.getcwd()
                os.chdir(s)
                os.mkdir(variable)
                os.chdir(ruta)

            extensions()


def info():
    # -----------------------------------
    s = compañia.get()

    variable = name.get()

    v = password.get()
    # -----------------------------------

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

            cuestion = messagebox.askyesno("", "Seguro que quieres continuar sin una compañia?")

            if cuestion:
                comprobacion2()

        else:

            comprobacion2()


def comprobacion2():
    s = compañia.get()
    t = name.get()
    to = password.get()
    robles = 0

    while True:

        if "," in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break
        elif "." in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break
        elif "@" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break
        elif "#" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "=" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "[" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        if "]" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "}" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break
        elif "{" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "!" in t and "¡" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "°" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "$" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "%" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "&" in t and "¬" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "/" in t and "~" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "(" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif ")" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "-" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "_" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif ":" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif ";" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "´" in t and "¨" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "*" in t and "+" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "|" in t and "/" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "?" in t and "¿" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "^" in t and "´" in t:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break
        #######################################CONTRASEÑA######################
        #
        if "," in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "." in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "@" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "#" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "=" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "[" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        if "]" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "}" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "{" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "!" in to and "¡" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "°" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "$" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "%" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "&" in to and "¬" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "/" in to and "~" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "(" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif ")" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "-" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "_" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif ":" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif ";" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "´" in to and "¨" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "*" in to and "+" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "|" in to and "/" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "?" in to and "¿" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
            #
        elif "^" in to and "´" in to:  #
            messagebox.showwarning("", "No se permiten caracteres extraños")  #
            break  #
        #######################################################################

        if "," in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break
        elif "." in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break
        elif "@" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break
        elif "#" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "=" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "[" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        if "]" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "}" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break
        elif "{" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "!" in s and "¡" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "°" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break
        elif "$" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "%" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "&" in s and "¬" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "/" in s and "~" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "(" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif ")" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "-" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "_" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif ":" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif ";" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "´" in s and "¨" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "*" in s and "+" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "|" in s and "/" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "?" in s and "¿" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        elif "^" in s and "´" in s:
            messagebox.showwarning("", "No se permiten caracteres extraños")
            break

        else:
            robles += 1
            break

    if robles == 1:
        comprobacion()


def extensions():
    s = compañia.get()

    l = str(name.get())

    v = password.get()

    lista = [
        (s, l, v)
    ]

    try:
        nanombre = sqlite3.connect("users.db")

        cursor = nanombre.cursor()

        cursor.executemany("INSERT INTO PERSONA VALUES(?,?,?)", lista)

        nanombre.commit()

        nanombre.close()

        root.quit()


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