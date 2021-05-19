import os
from Modulos import *


class principal:

    def __init__(self, root):

        root.geometry("1080x620")
        root.minsize(width=200, height=256)

        self.frame = Frame(root,bg="#03A9F4",width=10080, height=1080)
        self.frame.place(x=0, y=0)

        self.imagen = PhotoImage(file="iconos e imagenes\hacia atras.png")
        self.imagen2 = PhotoImage(file="iconos e imagenes\hacia adelante.png")
        self.imagen3 = PhotoImage(file="iconos e imagenes\salir.png")
        self.imagen4 = PhotoImage(file="iconos e imagenes\Facturacion.png")

        self.boton_adelante = Button(root, image=self.imagen2, command=self.cambiar)
        self.boton_adelante.place(rely=0.5,relx=0.9, x=16)
        self.boton_adelante.place_configure(bordermode=OUTSIDE, anchor=SE)


        self.boton_atras = Button(root, image=self.imagen, command=root.destroy)
        self.boton_atras.place(rely=0.8,relx=0.9, x=16)
        self.boton_atras.place_configure(bordermode=OUTSIDE, anchor=SE)

        self.boton_opcion_salir = Button(root, image=self.imagen3, bg="#0040FF", activebackground="#0040FF", command=root.destroy)
        self.boton_opcion_facturacion = Button(root, image=self.imagen4, bg="#0040FF", activebackground="#0040FF")

        menu = Menu(root)
        root.config(menu=menu)

        sub_menu = Menu(menu, tearoff=0)
        sub_menu.add_separator()
        sub_menu.add_command(label="salir", command=root.quit)

        Menu(menu)
        menu.add_cascade(label="opciones", menu=sub_menu)

    def cambiar(self):

        self.boton_atras.place_forget()
        self.boton_adelante.place_forget()
        self.boton_opcion_salir.place(rely=0.8,relx=0.9, x=16)
        self.boton_opcion_salir.place_configure(bordermode=OUTSIDE, anchor=SE)

        try:

            self.boton_opcion_facturacion.place(rely=0.2,relx=0.001, x=16)
            self.boton_opcion_facturacion.place_configure(bordermode=OUTSIDE, anchor=NO)

        except tkinter.TclError:
            pass

root0 = Tk()
principal(root0)
root0.mainloop()
