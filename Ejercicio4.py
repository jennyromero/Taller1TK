"""Ejercicio4:"""

from os import pread
from tkinter import *
from tkinter import messagebox

#-------------------
#funciones de la app
#-------------------

def sumar ():
    z=int(x.get())*(int(x.get())+1)/2
    t_resultado.insert(INSERT, "Resultados:\n La suma de los primeros "+x.get()+" enteros positivos es : "+str(z)+"\n")

def borrar():
    messagebox.showinfo("N Enteros", "Los datos serán borrados...")
    x.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("N Enteros", "La App se cerrará...")
    ventana_principal.destroy()


ventana_principal= Tk()
#titulo de la ventana 
ventana_principal.title("Jenny Romero")

# establecer tamaño de la ventana 
ventana_principal.geometry("800x500")

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

#color de fondo de la ventana principal
ventana_principal.config(bg="DarkseaGreen2")

#--------------------
# variables globales
#--------------------

x=StringVar()
z=IntVar()

#-----------------
# frame entrada
#-----------------
frame_entrada = Frame(ventana_principal )
frame_entrada.config (bg="aquamarine3", width=780, height=170)
frame_entrada.place(x=10,y=10)

#Etiqueta para el titulo de la app
titulo= Label(frame_entrada, text="Colegio San Jose de Guanenta")
titulo.config(bg="yellow", fg="blue" , font=("Arial", 16))
titulo.place(x=350, y=10)

# Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada, text ="Especialidad en sistemas")
subtitulo.config(bg="yellow", fg="blue", font=("Arial", 12))
subtitulo.place(x=350, y=40)

#Etiqueta para el subtitulo2 de la app
subtitulo2 =Label(frame_entrada, text="Determinar la suma de los primeros N enteros positivos")
subtitulo.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=360, y=70)

# imagen - logo de la app 
logo = PhotoImage(file="sum4.png")
etiq_logo = Label (frame_entrada,image=logo)
etiq_logo.place(x=50, y=10)

#Etiqueta para valor X
etiq_x = Label(frame_entrada, text="valor N= ")
etiq_x.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_x.place(x=340, y=120)

#Entry para valor x
entry_x = Entry(frame_entrada,width=4, textvariable=x)
entry_x .config(font=("Arial", 20), justify=CENTER)
entry_x .focus_set()
entry_x.place(x=430, y=120)

#-----------------
# frame operaciones
#-----------------

frame_operaciones = Frame(ventana_principal )
frame_operaciones.config (bg="", width=760, height=150)
frame_operaciones.place(x=20,y=185)

bt_sum= PhotoImage(file="sumj.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=130, height=125, command=sumar)
bt_sumar.place(x=100, y=5)


bt_bor= PhotoImage(file="elimi.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=125, height=120, command=borrar)
bt_borrar.place(x=330, y=7)


bt_sal= PhotoImage(file="salif.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=125, height=120, command=salir)
bt_salir.place(x=585, y=7)

#-----------------
# frame resultados
#-----------------

frame_resultados= Frame(ventana_principal )
frame_resultados.config (bg="seashell3", width=740, height=100)
frame_resultados.place(x=30,y=340)

t_resultado=Text(frame_resultados, width=96, height=3)
t_resultado.config(bg="SkyBlue3", fg="white", font=("Arial", 20))
t_resultado.pack()


ventana_principal.mainloop()



