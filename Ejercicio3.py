from tkinter import *
from tkinter import messagebox

#---------------------
# Funciones de la App
#---------------------

def sumar ():
    a=int(x.get())%10
    a1=int(x.get())//10
    a2=a*1000
    b=a1%10
    b1=a1//10
    b2=b*100
    c=b1%10
    c1=b1//10
    c2=c*10

    z=a2+b2+c2+c1

    t_resultado.insert(INSERT, "Resultados:\n El número "+x.get()+" a la inversa es "+str(z)+"\n")

def borrar():
    messagebox.showinfo("Inverso", "Los datos serán borrados...")
    x.set("")
    t_resultado.delete("Inverso", "end")

def salir():
    messagebox.showinfo("Inverso", "La App se cerrará...")
    ventana_principal.destroy()


#---------------------
# Ventana Principal
#---------------------

ventana_principal=Tk()

ventana_principal.title("Jenny Romero")

ventana_principal.geometry("800x500")


ventana_principal.resizable(0,0)

ventana_principal.config(bg="honeydew3")

#---------------------
# Variables Globales
#---------------------  
x=StringVar()
a=IntVar()
a1=IntVar()
a2=IntVar()

b=IntVar()
b1=IntVar()
b2=IntVar()

c=IntVar()
c1=IntVar()
c2=IntVar()
z=IntVar()

#---------------------
# Frame Entrada
#---------------------

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="snow3", width=780, height=240)
frame_entrada.place(x=10,y=10)

titulo= Label(frame_entrada, text="Jenny Romero")
titulo.config(bg="cadetblue3", fg="maroon")
titulo.place(x=240, y=10)

subtitulo2= Label(frame_entrada, text="Devolver número de 4 digitos inverso\n")
subtitulo2.config(bg="lemon chiffon", fg="blue", anchor=CENTER)
subtitulo2.place(x=240, y=70)

logo= PhotoImage(file="numeros3.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.config(bg="seashell3")
etiq_logo.place(x=10,y=10)

etiq_a=Label(frame_entrada, text="Número de 4 dígitos = ")
etiq_a.config(bg="mediumorchid", fg="lightyellow", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=280, y=120)

entry_a=Entry(frame_entrada, width=7, textvariable=x)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=490,y=115)


#---------------------
# Frame Operaciones
#---------------------

frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="bisque3", width=780, height=135)
frame_operaciones.place(x=10,y=260)


bt_sum= PhotoImage(file="inversoi.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=120, height=125, command=sumar)
bt_sumar.place(x=100, y=5)

bt_bor= PhotoImage(file="borra3.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=125, height=120, command=borrar)
bt_borrar.place(x=330, y=7)

bt_sal= PhotoImage(file="salir3.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=125, height=120, command=salir)
bt_salir.place(x=585, y=7)

#---------------------
# Frame Resultados
#---------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="gainsboro", width=780, height=100)
frame_resultados.place(x=10,y=400)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="chocolate1", fg="grey9", font=("Courier", 12))
t_resultado.pack()


ventana_principal.mainloop()