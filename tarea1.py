import tkinter as tk
from tkinter.messagebox import showinfo

class Aplicacion:
    def __init__(self):
        self.valor=1
        self.ventana=tk.Tk()

        self.label1=tk.Label(self.ventana, text=self.valor)
        self.label1.configure(foreground="blue")
        self.label1.pack()

        self.boton1=tk.Button(self.ventana, text="Incrementar",command=self.incrementar)
        self.boton1.pack()

        self.boton2=tk.Button(self.ventana, text="Decrementar",command=self.decrementar)
        self.boton2.pack()
        
        self.ventana.mainloop()

    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)
        self.color()

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)
        self.color()

    def color(self):
        if self.valor > 0:
            self.label1.configure(foreground="blue")
        else:
            self.label1.configure(foreground="red")



aplicacion1=Aplicacion()
