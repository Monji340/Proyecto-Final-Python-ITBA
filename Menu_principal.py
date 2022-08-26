import tkinter as tk

# definimos las acciones asociadas a las opciones de los menús
def accion1():
    texto.configure(text='Reemplazar/llamar programa de actualización de datos')


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
menu.add_command(label='Actualizacioón de datos', command=accion1)

# creamos un submenú
submenu = tk.Menu(menu, tearoff=False)
submenu.add_command(label='Resumen', command=acciona)
submenu.add_command(label='Gráfico de ticker', command=accionb)

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