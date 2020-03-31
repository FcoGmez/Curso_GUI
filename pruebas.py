from sense_emu import SenseHat # pip3 install sense_emu
sense= SenseHat()
import time 
import tkinter as tk 
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from tkinter.messagebox import showinfo
from tkinter import messagebox as mb

valor=0

class Aplicacion:
    def __init__(self):
        self.i=0
        self.imax=100
        self.ventana=tk.Tk()
        style = ThemedStyle(self.ventana)
        style.set_theme("ubuntu")
        self.ventana.title("Práctica GUI SenseHat")

        self.lectura=ttk.Label(self.ventana)
        self.lectura.configure(foreground='blue')
        self.lectura.grid(column=1, row=2)

        self.seleccion=tk.IntVar()
        self.seleccion.set(3)
        self.radio1=ttk.Radiobutton(self.ventana,text="Temperatura",variable=self.seleccion, value=1)
        self.radio1.grid(column=0,row=3)
        self.radio2=ttk.Radiobutton(self.ventana,text="Presion",variable=self.seleccion, value=2)
        self.radio2.grid(column=1,row=3)
        self.radio3=ttk.Radiobutton(self.ventana,text="Humedad",variable=self.seleccion, value=3)
        self.radio3.grid(column=2,row=3) 

        self.lecturasensor()

        self.ventana.mainloop()

    def lecturasensor(self):
        
        if self.seleccion.get() == 1:
            valor = sense.temp
            self.lectura.configure(text=str(valor))
            
        elif self.seleccion.get() ==2:
            valor = sense.pressure
            self.lectura.configure(text=str(valor))
            
        elif self.seleccion.get() ==3:
            valor = sense.humidity
            self.lectura.configure(text=str(valor))
        else:
            valor=0
            self.lectura.configure(text=str(valor))    
        

aplicacion=Aplicacion()