# Pedido de datos para la Actualización de datos

import tkinter as tk

def actualizacionDatos():
    ventana1 = tk.Tk()
    ventana1.title('Actualización de Datos')
    # Caja de texto con el ticker a pedir
    label1 = tk.Label(ventana1, text="Ingrese ticker a pedir:")
    label1.grid(column=0, row=0)
    dato1 = tk.StringVar()
    entry1 = tk.Entry(ventana1, width=30, textvariable=dato1)
    entry1.grid(column=1, row=0)
    # Caja de texto fecha de inicio a pedir
    label2 = tk.Label(ventana1, text="Fecha inicio")
    label2.grid(column=0, row=1)
    dato2 = tk.StringVar()
    entry2 = tk.Entry(ventana1, width=30, textvariable=dato2)         #Ver en que formato debe ingresar la fecha
    entry2.grid(column=1, row=1)
    # Caja de texto fecha fin a pedir
    label3 = tk.Label(ventana1, text="Fecha fin")
    label3.grid(column=0, row=2)
    dato3 = tk.StringVar()
    entry3 = tk.Entry(ventana1, width=30, textvariable=dato3)         #Ver en que formato debe ingresar la fecha
    entry3.grid(column=1, row=2)

    # Función para ingresar los datos
    def boton():
        def cerrarVentana():
            ventana1.destroy()                #Funcion para cerrar la ventana
        ventana1.title("Pidiendo Datos...")
        ventana1.after(3000, cerrarVentana)          #Cerramos la ventana después de 3 segundos

    # Botón para envío de los datos
    boton1 = tk.Button(ventana1, text="Pedir datos", command=boton)
    boton1.grid(column=1, row=3)

    ventana1.mainloop()
    lista = [dato1.get(), dato2.get(), dato3.get()]
    return lista

datos = actualizacionDatos()
print(datos)