import tkinter as tk
from Actualizacion_Datos import actualizacionDatos       #Función (ventana) opción 'Actualizacion de datos'
from Graficar_Ticker import graficarTicker               #Función (ventana) opción 'Grafico de Ticker'

# Se debe llamar a la función que muestra el resumen
def acciona():
    texto.configure(text='Llamar programa Resumen de visualización de datos')

#################  Menu Principal  ###################

# creamos la ventana principal
ventana = tk.Tk()
ventana.title('Nombre del programa')          # Ver que nombre le ponemos
ventana.geometry('500x400')

# creamos una barra de menús y la añadimos a la ventana principal
# cada ventana solo puede tener una barra de menús
barra_menus = tk.Menu(ventana)
ventana.config(menu=barra_menus)

# creamos un menú cuyo contenedor será la barra de menús
menu = tk.Menu(barra_menus, tearoff=False)

# añadimos opciones al menú indicando su nombre y acción asociado
menu.add_command(label='Actualizacioón de datos', command=actualizacionDatos)

# creamos submenú de las opciones de visualización de datos 
submenu = tk.Menu(menu, tearoff=False)
submenu.add_command(label='Resumen', command=acciona)
submenu.add_command(label='Gráfico de ticker', command=graficarTicker)

# añadimos el submenú al menú principal
menu.add_cascade(label='Visualización de datos', menu=submenu)

# añadimos una línea separadora y la opción de salir
menu.add_separator()
menu.add_command(label='Salir', command=ventana.destroy)

# finalmente añadimos el menú a la barra de menús
barra_menus.add_cascade(label="Menú", menu=menu)

# añadimos una etiqueta
texto = tk.Label(ventana, text='¡Bienvenido/a!')
texto.place(x=200, y=150)


if __name__ == '__main__':
    ventana.mainloop()  # ejecutamos la ventana principal