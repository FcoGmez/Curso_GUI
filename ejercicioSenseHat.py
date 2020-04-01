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
        #self.i=0
        #self.imax=100
        self.play=1
        self.ventana=tk.Tk()
        style = ThemedStyle(self.ventana)
        style.set_theme("ubuntu")
        self.ventana.title("Práctica GUI SenseHat")
        self.cuaderno = ttk.Notebook(self.ventana)

        self.pagina1 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina1, text='Monitorización')
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text='Control')
        self.labelframe1.pack(expand=False)
        self.control()

        self.labelframe2=ttk.LabelFrame(self.pagina1, text='Medidas')
        self.labelframe2.pack(fill='both',expand=False)
        self.medidas()

        self.labelframe3=ttk.LabelFrame(self.pagina1, text='Histórico')
        self.labelframe3.pack(fill='both',expand=True)
        self.historico()




        self.pagina2 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina2, text='Grafica')
        

        self.cuaderno.pack(fill='both',expand=True)
        self.ventana.geometry('600x600')
        #self.ventana.minsize(height=600, width=400)

    
    
        #self.cuaderno.grid(column=0, row=0, sticky='WE')
        self.ventana.after(1000,self.obtenervalor2)
        self.ventana.mainloop()
        
        
    def control(self):
        self.label1=ttk.Label(self.labelframe1, text="Start o Stop")
        self.label1.grid(column=0, row=0, sticky='WE')

        self.boton1=ttk.Button(self.labelframe1, text="Start/Stop", command=self.obtenervalor)
        self.boton1.grid(column=0, row=2)

    def medidas(self):
        self.label2=ttk.Label(self.labelframe2, text="Valor del sensor: ")
        self.label2.grid(column=0, row=0)

        self.lectura=ttk.Label(self.labelframe2)
        self.lectura.configure(foreground='blue')
        self.lectura.grid(column=1, row=0, columnspan=4)

        self.seleccion=tk.IntVar()
        self.seleccion.set(3)
        self.radio1=ttk.Radiobutton(self.labelframe2,text="Temperatura",variable=self.seleccion, value=1)
        self.radio1.grid(column=0,row=3)
        self.radio2=ttk.Radiobutton(self.labelframe2,text="Presion",variable=self.seleccion, value=2)
        self.radio2.grid(column=1,row=3)
        self.radio3=ttk.Radiobutton(self.labelframe2,text="Humedad",variable=self.seleccion, value=3)
        self.radio3.grid(column=2,row=3) 

        

    def historico(self):
        self.label3=ttk.Label(self.labelframe3, text="Aqui se implementará un historico de los datos")
        self.label3.grid(column=0, row=0, sticky='WE')


    def obtenervalor(self):
        
        self.play=self.play + 1 
    

    def obtenervalor2(self):
        self.ventana.after(1000,self.obtenervalor2)
        self.lecturasensor()


    def lecturasensor(self):
        if self.play%2 == 0:    
            if self.seleccion.get() == 1:
                valor = sense.temp
                self.lectura.configure(text=str(valor)+' ºC')
                
            elif self.seleccion.get() == 2:
                valor = sense.pressure
                self.lectura.configure(text=str(valor)+' mbar')
                
            elif self.seleccion.get() == 3:
                valor = sense.humidity
                self.lectura.configure(text=str(valor)+' %')
            else:
                valor = 0
                self.lectura.configure(text=str(valor))    
        
        


aplicacion=Aplicacion()









#while self.i < self.imax : 
#    pinta=str(self.i)
#    print(pinta)
#    self.lecturasensor()
#    self.i=self.i + 1
#    time.sleep(1)



#temp= sense.temp
#pre = sense.pressure
#hum= sense.humidity