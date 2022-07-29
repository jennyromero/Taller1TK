"""Ejercicio1:
Dado el valor de venta de producto, calcular su IVA y el precio final de venta."""

from tkinter import *
from tkinter import messagebox

#-------------------
#funciones de la app
#-------------------

def sumar ():
    i=int(x.get())*0.19
    z=int(x.get())+i
    t_resultado.insert(INSERT, "Resultados:\n El valor del Iva(0.19) de este producto es "+str(i)+"$.\n El valor total del producto es "+str(z)+"\n")

def borrar():
    messagebox.showinfo("Iva", "Los datos serán borrados...")
    x.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Iva", "La App se cerrará...")
    ventana_principal.destroy()



ventana_principal=Tk()
#titulo de la ventana 
ventana_principal.title("Jenny Romero")

# establecer tamaño de la ventana 
ventana_principal.geometry("800x500")

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

#color de fondo de la ventana principal
ventana_principal.config(bg="SteelBlue1")


#--------------------
# variables globales
#--------------------

x= StringVar()
i= DoubleVar()
z= IntVar()

#-----------------
# frame entrada
#-----------------
frame_entrada = Frame(ventana_principal )
frame_entrada.config (bg="aquamarine", width=780, height=240)
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
subtitulo2 =Label(frame_entrada, text="calcular IVA y el precio final de venta")
subtitulo.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=350, y=70)

# imagen - logo de la app 
logo = PhotoImage(file="logo.png")
etiq_logo = Label (frame_entrada,image=logo)
etiq_logo.place(x=10, y=10)

#Etiqueta para valor X
etiq_x = Label(frame_entrada, text="Valor = ")
etiq_x.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_x.place(x=350, y=160)

#Entry para valor x
entry_z = Entry(frame_entrada)
entry_z .config(font=("Arial", 20),width=4, textvariable=x)
entry_z .config(font=("Arial", 20))
entry_z.place(x=430, y=150)


#-----------------
# frame operaciones
#-----------------

frame_operaciones = Frame(ventana_principal )
frame_operaciones.config (bg="azure3", width=760, height=150)
frame_operaciones.place(x=10,y=220)

bt_sum= PhotoImage(file="ivao.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=120, height=125, command=sumar)
bt_sumar.place(x=100, y=5)


bt_bor= PhotoImage(file="borrar.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=125, height=120, command=borrar)
bt_borrar.place(x=330, y=7)


bt_sal= PhotoImage(file="salir.iva.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=125, height=120, command=salir)
bt_salir.place(x=585, y=7)

#---------------------
# Frame Resultados
#---------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="mediumpurple3", width=780, height=100)
frame_resultados.place(x=10,y=400)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="cadetblue1", fg="black", font=("Courier", 12))
t_resultado.pack()


ventana_principal.mainloop()