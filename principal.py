from Modulos import *


class principal:

    def __init__(self, root):

        self.root = root

        root.geometry("1080x640")
        root.minsize(width=200, height=256)

        self.frame = Frame(root,bg="#03A9F4",width=10080, height=1080)
        self.frame.place(x=0, y=0)

        self.frame_inventario = Frame(root,bg="white",width=500, height=500)

        self.frame_crear_producto = Frame(root, width=900, height=530, bg="#127271")

        fuente_inventario = font.Font(size=13, font="Arial")
        fuente_todos = font.Font(font="Arial")
        fuente_crear_producto = font.Font(size=14, family="Lucida Grande")
        fuente_numeros = font.Font(size=16)
        fuente_numeros1 = font.Font(size=10)
        fuente_categoria = font.Font(size=10)
        fuente_especial = font.Font(size=8)

        self.imagen = PhotoImage(file="iconos e imagenes\hacia atras.png")
        self.imagen2 = PhotoImage(file="iconos e imagenes\hacia adelante.png")
        self.imagen3 = PhotoImage(file="iconos e imagenes\salir.png")
        self.imagen4 = PhotoImage(file="iconos e imagenes\Facturacion.png")
        self.crear_producto_imagen = PhotoImage(file="iconos e imagenes\Crear.png")
        self.Inventario_imagen = PhotoImage(file="iconos e imagenes\Inventario.png")

        self.boton_adelante = Button(root, image=self.imagen2, command=self.cambiar)
        self.boton_adelante.place(rely=0.5,relx=0.9, x=16)
        self.boton_adelante.place_configure(bordermode=OUTSIDE, anchor=SE)


        self.boton_atras = Button(root, image=self.imagen, command=root.destroy)
        self.boton_atras.place(rely=0.8,relx=0.9, x=16)
        self.boton_atras.place_configure(bordermode=OUTSIDE, anchor=SE)

        self.boton_opcion_salir = Button(root, image=self.imagen3, bg="#0040FF", activebackground="#0040FF", command=root.destroy)
        self.boton_opcion_facturacion = Button(root, image=self.imagen4, bg="#0040FF", activebackground="#0040FF")
        self.boton_opcion_inventario = Button(root, image=self.Inventario_imagen, bg="#0040FF", activebackground="#0040FF", command=self.inventario)

        self.Label_codigo = Label(root, text="Codigo", bg="#848484", font=fuente_inventario, width=9)
        self.codigo_productos = Text(root, width=10, height=22, bd=1, wrap="none", font=fuente_todos)
        self.Label_Descripcion = Label(root, text="Descripcion", bg="#848484", font=fuente_inventario, width=14)
        self.Label_Precio = Label(root, text="Precio", bg="#848484", font=fuente_inventario, width=9)
        self.Descripcion_productos = Text(root, width=18, height=22, bd=1, wrap="none", font=fuente_inventario)
        self.Precio_productos = Text(root, width=10, height=22, bd=1, wrap="none", font=fuente_todos)
        self.Label_Tipo = Label(root, text="Tipo", bg="#848484", font=fuente_inventario, width=9)
        self.tipo_producto = Text(root, width=12, height=22, bd=1, wrap="none", font=fuente_todos)
        self.Label_unidades = Label(root, text="Unidades", bg="#848484", font=fuente_inventario, width=11)
        self.Unidades_producto = Text(root, width=13, height=22, bd=1, wrap="none", font=fuente_todos)
        self.Label_Medida = Label(root, text="Medida", bg="#848484", font=fuente_inventario, width=10)
        self.Medida_producto = Text(root, width=13, height=22, bd=1, wrap="none", font=fuente_todos)
        self.Label_Categoria = Label(root, text="Categoria", bg="#848484", font=fuente_inventario, width=10)
        self.Categoria_producto = Text(root, width=13, height=22, bd=1, wrap="none", font=fuente_todos)
        self.Label_estado = Label(root, text="Estado", bg="#848484", font=fuente_inventario, width=10)
        self.estado_producto = Text(root, width=13, height=22, bd=1, wrap="none", font=fuente_todos)
        self.Label_Venta = Label(root, text="Venta", bg="#848484", font=fuente_inventario, width=12)
        self.Venta_producto = Text(root, width=14, height=22, bd=1, wrap="none", font=fuente_todos)

        self.crear_productos = Button(root, image=self.crear_producto_imagen, command=self.crear_producto_1)

        self.label_codigo = Label(self.frame_crear_producto, text="Codigo", font=fuente_crear_producto, bg="#127271")
        self.entry_codigo = ttk.Entry(self.frame_crear_producto, width=35,validate='all', validatecommand=(root.register(self.activar_puestos), '%P'))
        self.Entry_Nombre_producto = ttk.Entry(self.frame_crear_producto, width=46)
        self.label_Nombre_producto = Label(self.frame_crear_producto, bg="#127271",text="Nombre del producto", font=fuente_crear_producto)

        self.label_precio_en_venta = Label(self.frame_crear_producto, text="Precio en compra.", font=fuente_crear_producto, bg="#127271")
        self.label_precio_Ganancias = Label(self.frame_crear_producto, text="Utilidad %", bg="#127271", font=fuente_crear_producto)
        self.label_coste_producto = Label(self.frame_crear_producto, text="Costo del producto", bg="#127271",font=fuente_crear_producto)
        self.label_calificacion_producto = Label(self.frame_crear_producto, text="Calificacion del producto",bg="#127271", font=fuente_crear_producto)

        self.label_numero1 = Label(self.frame_crear_producto, text="1.", bg="#127271", font=fuente_numeros)
        self.label_numero2 = Label(self.frame_crear_producto, text="2.", bg="#127271", font=fuente_numeros)
        self.label_numero3 = Label(self.frame_crear_producto, text="3.", bg="#127271", font=fuente_numeros)
        self.label_numero4 = Label(self.frame_crear_producto, text="4.", bg="#127271", font=fuente_numeros)

        self.label_por_unidad = Label(self.frame_crear_producto, text="Por unidad", bg="#127271", font=fuente_numeros1)
        self.label_en_us = Label(self.frame_crear_producto, text="En dolares", bg="#127271", font=fuente_numeros1)
        self.label_El_producto_es = Label(self.frame_crear_producto, text="El producto es", bg="#127271", font="Arial")
        self.label_cantidad_inicial = Label(self.frame_crear_producto, text="Cantidad inicial", bg="#127271", font="Arial")
        self.label_facturar_precio = Label(self.frame_crear_producto, text="Facturar con precio", bg="#127271", font="Arial")
        self.label_inpuesto = Label(self.frame_crear_producto, text="Impuesto", bg="#127271", font="Arial")
        self.label_inpuesto1 = Label(self.frame_crear_producto, text="Otro impto", bg="#127271", font="Arial")
        self.label_categoria = Label(self.frame_crear_producto, text="Categoria producto", bg="#127271", font=fuente_categoria)
        self.label_sub_categoria = Label(self.frame_crear_producto, text="Sub categoria", bg="#127271", font=fuente_categoria)
        self.label_asignado_bodega = Label(self.frame_crear_producto, text="Asignado a bodega", bg="#127271", font=fuente_categoria)
        self.label_ubicacion = Label(self.frame_crear_producto, text="Ubicacion fisica",bg="#127271", font=fuente_categoria)
        self.label_vende_por = Label(self.frame_crear_producto, text="Se vende por",bg="#127271", font=fuente_categoria)
        self.label_compra_por = Label(self.frame_crear_producto, text="Se vende por",bg="#127271", font=fuente_categoria)

        self.label_contiene = Label(self.frame_crear_producto, text="Y contiene",bg="#127271", font=fuente_categoria)
        self.label_cUnidades = Label(self.frame_crear_producto, text="Unidades",bg="#127271", font=fuente_especial)
        self.label_Aplicar_en = Label(self.frame_crear_producto, text="Aplicar en\nventas  compras",bg="#127271", font=fuente_especial)

        self.label_precio1 = Label(self.frame_crear_producto, text="Precio 1 impto",bg="#127271", font=fuente_categoria)
        self.label_precio2 = Label(self.frame_crear_producto, text="Precio 2 impto",bg="#127271", font=fuente_categoria)
        self.label_precio3 = Label(self.frame_crear_producto, text="Precio 3 impto",bg="#127271", font=fuente_categoria)
        self.label_precio4 = Label(self.frame_crear_producto, text="Precio 4 impto",bg="#127271", font=fuente_categoria)

        self.string_entry1 = StringVar()
        self.string_entry2 = StringVar()
        self.string_entry3 = StringVar()
        self.string_entry4 = StringVar()

        self.string_entry1.set("0.00")
        self.string_entry2.set("0.00")
        self.string_entry3.set("0.00")
        self.string_entry4.set("0.00")

        self.entry_numero1 = ttk.Entry(self.frame_crear_producto, textvariable=self.string_entry1)
        self.entry_numero2 = ttk.Entry(self.frame_crear_producto, textvariable=self.string_entry2)
        self.entry_numero3 = ttk.Entry(self.frame_crear_producto, textvariable=self.string_entry3)
        self.entry_numero4 = ttk.Entry(self.frame_crear_producto, textvariable=self.string_entry4)

        self.string_entry5 = StringVar()
        self.string_entry6 = StringVar()
        self.string_entry7 = StringVar()
        self.string_entry8 = StringVar()

        self.string_entry5.set("0.000")
        self.string_entry6.set("0.000")
        self.string_entry7.set("0.000")
        self.string_entry8.set("0.000")

        self.entry_numero5 = ttk.Entry(self.frame_crear_producto, justify="right", textvariable=self.string_entry5, validate='all', validatecommand=(root.register(self.calculo), '%P'))
        self.entry_numero6 = ttk.Entry(self.frame_crear_producto, justify="right", textvariable=self.string_entry6)
        self.entry_numero7 = ttk.Entry(self.frame_crear_producto, justify="right", textvariable=self.string_entry7)
        self.entry_numero8 = ttk.Entry(self.frame_crear_producto, justify="right", textvariable=self.string_entry8)

        self.Int_por_unidad = IntVar()
        self.Int_en_dolares = IntVar()

        self.Int_por_unidad.set("0.00")

        self.entry_por_unidad = ttk.Entry(self.frame_crear_producto, textvariable=self.Int_por_unidad,validate='all', validatecommand=(root.register(self.calculos), '%P'))
        self.entry_en_dolares = ttk.Entry(self.frame_crear_producto, state="readonly", textvariable=self.Int_en_dolares)
        self.entry_cantidad_inicial = ttk.Entry(self.frame_crear_producto)

        self.entry_ubicacion_fisica = ttk.Entry(self.frame_crear_producto, width=11)
        self.entry_numero14 = ttk.Entry(self.frame_crear_producto)
        self.entry_numero15 = ttk.Entry(self.frame_crear_producto)
        self.entry_numero16 = ttk.Entry(self.frame_crear_producto)
        self.entry_numero17 = ttk.Entry(self.frame_crear_producto)

        self.CN = Checkbutton(self.frame_crear_producto, text="El producto esta activo?", onvalue=1, offvalue=0, bg="#127271", activebackground="#127271")
        self.CN1 = Checkbutton(self.frame_crear_producto, onvalue=1, offvalue=0, bg="#127271", activebackground="#127271")
        self.CN2 = Checkbutton(self.frame_crear_producto, onvalue=1, offvalue=0, bg="#127271", activebackground="#127271")
        self.CN3 = Checkbutton(self.frame_crear_producto, onvalue=1, offvalue=0, bg="#127271", activebackground="#127271")
        self.CN4 = Checkbutton(self.frame_crear_producto, onvalue=1, offvalue=0, bg="#127271", activebackground="#127271")

        self.R1 = Radiobutton(root, text="Fisico", bg="#127271", activebackground="#127271")
        self.R2 = Radiobutton(root, text="Servicio", bg="#127271", activebackground="#127271")
        self.R3 = Radiobutton(root, text="Ocasional", bg="#127271", activebackground="#127271")

        self.S1 = Spinbox(self.frame_crear_producto, from_=0, to=10, width=3)

        self.cx_inpuesto = ttk.Combobox(root, width=12, values=("Tax", "Iva", "SIN"))
        self.cx0_otro_inpu = ttk.Combobox(root, width=12)
        self.cx1_categoria_producto = ttk.Combobox(self.frame_crear_producto, width=8)
        self.cx2_asignacion_bodega = ttk.Combobox(self.frame_crear_producto, width=8)
        self.cx3_asignado_bodega = ttk.Combobox(self.frame_crear_producto, width=6)
        self.cx4_se_vende_por = ttk.Combobox(self.frame_crear_producto, width=8, values=("Unidad", "Pieza", "Docena", "kilogramos", "Botella"))
        self.cx5_y_contiene = ttk.Combobox(self.frame_crear_producto, width=10)
        self.cx5_se_compra_por = ttk.Combobox(self.frame_crear_producto, width=10)

        self.n = 1
        self.n1 = 1

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

        self.boton_opcion_inventario.place(rely=0.8, relx=0.5, x=16)
        self.boton_opcion_inventario.place_configure(bordermode=OUTSIDE, anchor=CENTER)

        try:

            self.boton_opcion_facturacion.place(rely=0.2,relx=0.001, x=16)
            self.boton_opcion_facturacion.place_configure(bordermode=OUTSIDE, anchor=NO)

        except tkinter.TclError:
            pass

    def inventario(self):
        self.root.resizable(width=False, height=False)
        self.boton_opcion_salir.place_forget()
        self.boton_opcion_inventario.place_forget()
        self.boton_opcion_facturacion.place_forget()
        self.frame.place_forget()
        self.Label_codigo.place(x=59, y=107)
        self.codigo_productos.place(x=59, y=140)
        self.Label_Descripcion.place(x=151, y=107)
        self.Label_Precio.place(x=289, y=107)
        self.Descripcion_productos.place(x=143, y=140)
        self.Precio_productos.place(x=291, y=140)
        self.Label_Tipo.place(x=382, y=107)
        self.tipo_producto.place(x=375, y=140)
        self.Label_unidades.place(x=475, y=107)
        self.Unidades_producto.place(x=475, y=140)
        self.Label_Medida.place(x=588, y=107)
        self.Medida_producto.place(x=583, y=140)
        self.Label_Categoria.place(x=689, y=107)
        self.Categoria_producto.place(x=688, y=140)
        self.Label_estado.place(x=794, y=107)
        self.estado_producto.place(x=794, y=140)
        self.Label_Venta.place(x=899, y=107)
        self.Venta_producto.place(x=900, y=140)
        self.crear_productos.place(x=53, y=550)

    def crear_producto_1(self):
        self.Label_codigo.place_forget()
        self.codigo_productos.place_forget()
        self.Label_Descripcion.place_forget()
        self.Label_Precio.place_forget()
        self.Descripcion_productos.place_forget()
        self.Precio_productos.place_forget()
        self.Label_Tipo.place_forget()
        self.tipo_producto.place_forget()
        self.Label_unidades.place_forget()
        self.Unidades_producto.place_forget()
        self.Label_Medida.place_forget()
        self.Medida_producto.place_forget()
        self.Label_Categoria.place_forget()
        self.Categoria_producto.place_forget()
        self.Label_estado.place_forget()
        self.estado_producto.place_forget()
        self.Label_Venta.place_forget()
        self.Venta_producto.place_forget()
        self.crear_productos.place_forget()

        self.root.config(bg="#335DD9")

        self.label_codigo.place(x=42,y=12)
        self.entry_codigo.place(x=130, y=18, height=20)
        self.frame_crear_producto.place(x=90, y=40)
        self.Entry_Nombre_producto.place(x=600, y=18, height=20)

        self.label_Nombre_producto.place(x=400, y=12)
        self.label_precio_en_venta.place(x=40, y=90)
        self.label_precio_Ganancias.place(x=250, y=90)

        self.label_coste_producto.place(x=400, y=90)
        self.label_calificacion_producto.place(x=630, y=90)

        self.label_numero1.place(x=40, y=140)
        self.label_numero2.place(x=40, y=180)
        self.label_numero3.place(x=40, y=220)
        self.label_numero4.place(x=40, y=256)

        self.label_por_unidad.place(x=380, y=145)
        self.label_en_us.place(x=380, y=178)
        self.label_El_producto_es.place(x=40, y=320)
        self.label_cantidad_inicial.place(x=37, y=390)
        self.label_facturar_precio.place(x=330, y=390)

        self.label_inpuesto.place(x=39, y=440)
        self.label_inpuesto1.place(x=36, y=480)
        self.label_categoria.place(x=600, y=140)
        self.label_sub_categoria.place(x=600, y=180)

        self.label_asignado_bodega.place(x=600, y=220)
        self.label_ubicacion.place(x=600, y=260)

        self.label_vende_por.place(x=600, y=300)
        self.label_contiene.place(x=600, y=340)
        self.label_compra_por.place(x=600, y=374)
        self.label_cUnidades.place(x=800, y=345)
        self.label_Aplicar_en.place(x=290, y=419)

        self.label_precio1.place(x=600, y=410)
        self.label_precio2.place(x=600, y=440)
        self.label_precio3.place(x=600, y=470)
        self.label_precio4.place(x=600, y=500)

        self.entry_numero1.place(x=70, y=145)
        self.entry_numero2.place(x=70, y=186)
        self.entry_numero3.place(x=70, y=226)
        self.entry_numero4.place(x=70, y=260)

        self.entry_numero5.place(x=240, y=145)
        self.entry_numero6.place(x=240, y=186)
        self.entry_numero7.place(x=240, y=226)
        self.entry_numero8.place(x=240, y=260)

        self.entry_por_unidad.place(x=460, y=145)
        self.entry_en_dolares.place(x=460, y=179)
        self.entry_cantidad_inicial.place(x=189, y=392)

        self.entry_ubicacion_fisica.place(x=745, y=265)

        self.entry_numero14.place(x=700, y=413)
        self.entry_numero15.place(x=700, y=442)
        self.entry_numero16.place(x=700, y=472)
        self.entry_numero17.place(x=700, y=502)

        self.CN.place(x=410, y=230)
        self.CN1.place(x=300, y=450)
        self.CN2.place(x=300, y=483)
        self.CN3.place(x=340, y=450)
        self.CN4.place(x=340, y=483)

        self.R1.place(x=270, y=360)
        self.R2.place(x=340, y=362)
        self.R3.place(x=420, y=364)

        self.S1.place(x=516,y=394)

    def calculos(self, dominiga):

        if self.n == 1:

            self.entry_por_unidad.delete(0, END)

            self.n -= 1

        if str.isdigit(dominiga):

            Dominicanos = float(dominiga)

            dolares_entre_dominicanos = format(Dominicanos / 58, ".2f")

            self.Int_en_dolares.set(dolares_entre_dominicanos)

            return True

        else:

            return True

    def activar_puestos(self, dxs):

        en_numeros = len(dxs)

        if str.isdigit(dxs):

            if en_numeros > 2:

                self.cx4_se_vende_por.place(x=744, y=305)
                self.cx5_y_contiene .place(x=700, y=340)
                self.cx2_asignacion_bodega.place(x=744, y=180)
                self.cx1_categoria_producto.place(x=744, y=140)
                self.cx3_asignado_bodega.place(x=744, y=225)
                self.cx5_se_compra_por.place(x=700, y=374)

                self.cx_inpuesto.place(x=234, y=483)
                self.cx0_otro_inpu.place(x=234, y=523)

            else:
                self.cx4_se_vende_por.place_forget()
                self.cx5_y_contiene.place_forget()
                self.cx2_asignacion_bodega.place_forget()
                self.cx1_categoria_producto.place_forget()
                self.cx3_asignado_bodega.place_forget()
                self.cx_inpuesto.place_forget()
                self.cx0_otro_inpu.place_forget()
                self.cx5_se_compra_por.place_forget()

            return True

        else:

            self.cx4_se_vende_por.place_forget()
            self.cx5_y_contiene.place_forget()
            self.cx2_asignacion_bodega.place_forget()
            self.cx1_categoria_producto.place_forget()
            self.cx3_asignado_bodega.place_forget()
            self.cx_inpuesto.place_forget()
            self.cx0_otro_inpu.place_forget()
            self.cx5_se_compra_por.place_forget()

            return True

    def calculo(self, cel):

        nf = float(self.Int_por_unidad.get())

        if self.n1 == 1:

            self.entry_numero5.delete(0, END)

            self.n1 -= 1

        if str.isdigit(cel):

            fn = float(cel)

            fns = format(fn / nf, ".2f")

            self.string_entry1.set(fns)

            return True

        else:

            return True

root0 = Tk()
principal(root0)
root0.mainloop()
