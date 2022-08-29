# Pedido de datos para la Actualización de datos

import tkinter as tk

class ActualizacionDatos:
    
    def __init__(self):
        self.ventana1 = tk.Tk()

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

        self.boton1 = tk.Button(self.ventana1, text="Pedir datos", command=self.ingresar)
        self.boton1.grid(column=1, row=3)

        self.ventana1.mainloop()
    
    def ingresar(self):
        self.ventana1.title("Pidiendo Datos...")


aplicacion1=ActualizacionDatos()
