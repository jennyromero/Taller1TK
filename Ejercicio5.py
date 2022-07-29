from tkinter import *
from tkinter import messagebox
import math
#-------------------
#funciones de la app
#-------------------

def sumar ():
    area=math.pi*int(rad.get())*int(rad.get())
    per=2*int(rad.get())*math.pi
    t_resultado.insert(INSERT, "Resultados:\n El valor del Radio es: "+rad.get()+"\n El valor del Área es: "+str(area)+"\n El valor del perímetro es "+str(per)+"\n")

def borrar():
    messagebox.showinfo("Circulo", "Los datos serán borrados...")
    rad.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Círculo", "La App se cerrará...")
    ventana_principal.destroy()

ventana_principal=Tk()
#titulo de la ventana 
ventana_principal.title("Jenny Romero")

# establecer tamaño de la ventana 
ventana_principal.geometry("800x500")

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

#color de fondo de la ventana principal
ventana_principal.config(bg="wheat3")

#--------------------
# variables globales
#--------------------
rad=StringVar()
area=DoubleVar()
per=DoubleVar()

#-----------------
# frame entrada
#-----------------
frame_entrada = Frame(ventana_principal )
frame_entrada.config (bg="burlywood2", width=780, height=240)
frame_entrada.place(x=10,y=10)

#Etiqueta para el titulo de la app
titulo= Label(frame_entrada, text="Calcular el area y el perimetro de un circulo")
titulo.config(bg="yellow", fg="blue" , font=("Arial", 16))
titulo.place(x=350, y=10)

# Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada, text ="Jenny Romero")
subtitulo.config(bg="yellow", fg="blue", font=("Arial", 12))
subtitulo.place(x=350, y=40)

# imagen - logo de la app 
logo = PhotoImage(file="circupj.png")
etiq_logo = Label (frame_entrada,image=logo)
etiq_logo.place(x=60, y=5)

#Etiqueta para valor 
etiq_x = Label(frame_entrada, text="valor = ")
etiq_x.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_x.place(x=350, y=160)

#Entry para valor rad
entry_rad = Entry(frame_entrada)
entry_rad .config(font=("Arial", 20),width=4, textvariable=rad)
entry_rad .config(font=("Arial", 20))
entry_rad.place(x=430, y=150)

#-----------------
# frame operaciones
#-----------------

frame_operaciones = Frame(ventana_principal )
frame_operaciones.config (bg="azure3", width=760, height=150)
frame_operaciones.place(x=10,y=230)

bt_sum= PhotoImage(file="halla.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=120, height=125, command=sumar)
bt_sumar.place(x=100, y=5)

bt_bor= PhotoImage(file="borra3.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=108, height=108, command=borrar)
bt_borrar.place(x=330, y=7)

bt_sal= PhotoImage(file="salir3.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=125, height=120, command=salir)
bt_salir.place(x=585, y=7)

#---------------------
# Frame Resultados
#---------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="burlywood1", width=780, height=100)
frame_resultados.place(x=10,y=400)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="cadetblue1", fg="black", font=("Courier", 12))
t_resultado.pack()

ventana_principal.mainloop()