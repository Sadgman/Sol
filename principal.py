import os
from Modulos import *


class principal:

    def __init__(self, root):

        self.frame = Frame(root, width=10080, height=1080)
        self.frame.config(bg="#03A9F4")
        self.frame.place(x=0, y=0)

        self.menu = Menu(root)
        root.config(menu=self.menu)

        self.sub_menu = Menu(self.menu, tearoff=0)
        self.sub_menu.add_separator()
        self.sub_menu.add_command(label="salir", command=root.quit)

        self.imagen = PhotoImage(file="iconos e imagenes\hacia atras.png")
        self.imagen2 = PhotoImage(file="iconos e imagenes\hacia adelante.png")

        self.boton_adelante = Button(root, image=self.imagen2, command=self.cambiar)
        self.boton_adelante.place(x=900, y=300)

        self.boton_atras = Button(root, image=self.imagen)
        self.boton_atras.place(x=900, y=500)

        self.second_menu = Menu(self.menu)
        self.menu.add_cascade(label="opciones", menu=self.sub_menu)

        self.imagen3 = PhotoImage(file="iconos e imagenes\salir.png")

        self.boton_opcion = Button(root, image=self.imagen3, command=root.destroy)

    def cambiar(self):

        self.boton_atras.place_forget()
        self.boton_adelante.place_forget()
        self.frame.place_forget()
        self.boton_opcion.place(x=900, y=600)


roto1 = Tk()
roto1.geometry("1080x620")
principal(roto1)
roto1.mainloop()