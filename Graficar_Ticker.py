######     Ventana para pedir datos al usuario - Gráfico de Ticker    ######
import tkinter as tk

def graficarTicker():
    ventana1 = tk.Tk()
    ventana1.title('Grafico de ticker')
    # Caja de texto con el ticker a pedir
    label1 = tk.Label(ventana1, text="Ingrese ticker a graficar:")
    label1.grid(column=0, row=0)
    dato1 = tk.StringVar()
    entry1 = tk.Entry(ventana1, width=30, textvariable=dato1)
    entry1.grid(column=1, row=0)

    # Función para ingresar los datos y cerrar ventana
    def boton():
        def cerrarVentana():
            ventana1.destroy()
        ventana1.title("Graficando...")       # Instanciar con programa de graficar
        ventana1.after(3000, cerrarVentana)   #Cerramos la ventana después de 3 segundos
    
    # Botón para envío de los datos
    boton1 = tk.Button(ventana1, text="Graficar", command=boton)     
    boton1.grid(column=1, row=3)

    ventana1.mainloop()
    return (dato1.get())


# Prueba si se devuelve el dato solicitado
# datos = graficarTicker()
# print(datos)