import tkinter as tk

######     Ventana para pedir datos al usuario - Actualización de datos    ######
class ActualizacionDatos:
    
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title('Actualización de Datos')

        self.label1 = tk.Label(self.ventana1, text="Ingrese ticker a pedir:")
        self.label1.grid(column=0, row=0)
        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=30, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        self.label2 = tk.Label(self.ventana1, text="Fecha inicio")
        self.label2.grid(column=0, row=1)
        self.dato2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=30, textvariable=self.dato2)         #Ver en que formato debe ingresar la fecha
        self.entry2.grid(column=1, row=1)

        self.label3 = tk.Label(self.ventana1, text="Fecha fin")
        self.label3.grid(column=0, row=2)
        self.dato3 = tk.StringVar()
        self.entry3 = tk.Entry(self.ventana1, width=30, textvariable=self.dato3)         #Ver en que formato debe ingresar la fecha
        self.entry3.grid(column=1, row=2)

        self.boton1 = tk.Button(self.ventana1, text="Pedir datos", command=self.ingresar)    # Falta agregar que la ventana se cierre una vez enviado los datos
        self.boton1.grid(column=1, row=3)

        self.ventana1.mainloop()
    
    def cerrarVentana(self):
        self.ventana1.destroy() 

    def ingresar(self):
        self.ventana1.title("Pidiendo Datos...")     # Instanciar con programa de Actualizacion de datos.
        self.ventana1.after(3000, self.cerrarVentana)   #Cerramos la ventana después de 3 segundos
        

######     Ventana para pedir datos al usuario - Gráfico de Ticker    ######
class GraficarTicker:

    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title('Grafico de ticker')

        self.label1 = tk.Label(self.ventana1, text="Ingrese ticker a graficar:")
        self.label1.grid(column=0, row=0)
        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=30, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        self.boton1 = tk.Button(self.ventana1, text="Graficar", command=self.ingresar)      # Falta agregar que la ventana se cierre una vez enviado los datos
        self.boton1.grid(column=1, row=3)

        self.ventana1.mainloop()
    
    def cerrarVentana(self):
        self.ventana1.destroy() 
        
    def ingresar(self):
        self.ventana1.title("Graficando...")      # Instanciar con programa de graficar
        self.ventana1.after(3000, self.cerrarVentana)   #Cerramos la ventana después de 3 segundos



# definimos las acciones asociadas a las opciones de los menús
def accion1():
    texto.configure(text='Pedir datos a la API')


def acciona():
    texto.configure(text='Llamar programa Resumen de visualización de datos')


def accionb():
    texto.configure(text='Llamar programa Gráfico de ticker de visualización de datos')


# creamos la ventana principal
ventana = tk.Tk()
ventana.title('Nombre del programa')
ventana.geometry('400x400')

# creamos una barra de menús y la añadimos a la ventana principal
# cada ventana solo puede tener una barra de menús
barra_menus = tk.Menu(ventana)
ventana.config(menu=barra_menus)

# creamos un menú cuyo contenedor será la barra de menús
menu = tk.Menu(barra_menus, tearoff=False)

# añadimos opciones al menú indicando su nombre y acción asociado
menu.add_command(label='Actualizacioón de datos', command=ActualizacionDatos)

# creamos un submenú
submenu = tk.Menu(menu, tearoff=False)
submenu.add_command(label='Resumen', command=acciona)
submenu.add_command(label='Gráfico de ticker', command=GraficarTicker)

# añadimos un submenú al menú principal
menu.add_cascade(label='Visualización de datos', menu=submenu)

# añadimos una línea separadora y la opción de salir
menu.add_separator()
menu.add_command(label='Salir', command=ventana.destroy)

# finalmente añadimos el menú a la barra de menús
barra_menus.add_cascade(label="Menú", menu=menu)

# añadimos una etiqueta para ver el efecto de los botones del menú
texto = tk.Label(ventana, text='¡Bienvenido/a!')
texto.place(x=200, y=200)


if __name__ == '__main__':
    ventana.mainloop()  # ejecutamos la ventana principal