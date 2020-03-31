import tkinter as tk 
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from tkinter.messagebox import showinfo
from tkinter import messagebox as mb

class Aplicacion:
    def __init__(self):
        self.valorconversion=0
        self.ventana=tk.Tk()
        style = ThemedStyle(self.ventana)
        style.set_theme("ubuntu")
        self.ventana.title("Conversor de Temperatura")

        self.labelframe1=ttk.LabelFrame(self.ventana, text="Datos de Entrada:")
        self.labelframe1.grid(column=0, row=0, sticky="WE")
        self.datosdeentrada()

        self.labelframe2=ttk.LabelFrame(self.ventana, text="Datos Conversion:")
        self.labelframe2.grid(column=0, row=1, sticky="WE")
        self.datosconversion()

        self.labelframe3=ttk.LabelFrame(self.ventana, text="Resultados:")
        self.labelframe3.grid(column=0, row=2, sticky="WE")
        self.resultados()

        self.ventana.mainloop()        

    def datosdeentrada(self):    
        self.label1=ttk.Label(self.labelframe1, text="Cantidad")
        self.label1.grid(column=0, row=0)
    
        self.dato=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1, width=10, textvariable=self.dato)
        self.entry1.grid(column=1, row=0)

        self.seleccion=tk.IntVar()
        self.seleccion.set(3)
        self.radio1=ttk.Radiobutton(self.labelframe1,text="Kelvin",variable=self.seleccion, value=1)
        self.radio1.grid(column=0,row=1)
        self.radio2=ttk.Radiobutton(self.labelframe1,text="Celsius",variable=self.seleccion, value=2)
        self.radio2.grid(column=1,row=1)
        self.radio3=ttk.Radiobutton(self.labelframe1,text="Fahrenheit",variable=self.seleccion, value=3)
        self.radio3.grid(column=2,row=1) 

    def datosconversion(self):
        #self.boton1=ttk.Button(self.labelframe2, text="Convertir a:", command=self.conversor_temperatura)
        #self.boton1.grid(column=1, row=2)

        self.seleccion1=tk.IntVar()
        self.check1=ttk.Checkbutton(self.labelframe2, text="Kelvin", variable=self.seleccion1)
        self.check1.grid(column=0, row=3)
        self.seleccion2=tk.IntVar()
        self.check1=ttk.Checkbutton(self.labelframe2, text="Celsius", variable=self.seleccion2)
        self.check1.grid(column=1, row=3)
        self.seleccion3=tk.IntVar()
        self.check1=ttk.Checkbutton(self.labelframe2, text="Fahrenheit", variable=self.seleccion3)
        self.check1.grid(column=2, row=3)

    def resultados(self):
        self.label2=ttk.Label(self.labelframe3, text="Kelvin:")
        self.label2.grid(column=0, row=4)
        self.label3=ttk.Label(self.labelframe3, text="Celsius:")
        self.label3.grid(column=0, row=5)
        self.label4=ttk.Label(self.labelframe3, text="Fahrenheit:")
        self.label4.grid(column=0, row=6)

        self.kelvin=ttk.Label(self.labelframe3, text=self.valorconversion)
        self.kelvin.configure(foreground="blue")
        self.kelvin.grid(column=1, row=4)       
        self.celsius=ttk.Label(self.labelframe3, text=self.valorconversion)
        self.celsius.configure(foreground="blue")
        self.celsius.grid(column=1, row=5)
        self.fahrenheit=ttk.Label(self.labelframe3, text=self.valorconversion)
        self.fahrenheit.configure(foreground="blue")
        self.fahrenheit.grid(column=1, row=6)



    #def conversor_temperatura(self):
        

aplicacion1=Aplicacion()