from tkinter import Tk, Button, Label, StringVar, PhotoImage
from random import choice  # Importamos la función choice del módulo random
import logica  # tu archivo de lógica

ventana=Tk()
ventana.title("Piedra, papel, tijera")
ventana.geometry("440x300")
ventana.configure(bg="#470d4e")
ventana.resizable(0,0)


#---------imagenes------------
imagen_piedra = PhotoImage(file="piedra.png")
imagen_papel = PhotoImage(file="papel.png")
imagen_tijera = PhotoImage(file="tijera.png")

#---------boton piedra
btn_piedra = Button(ventana, image=imagen_piedra, command=lambda: logica.elegir_piedra(texto_usuario, texto_pc, texto_resultado))
btn_piedra.grid(row=2, column=1, pady=5, padx=0)

#---------boton papel------
btn_papel = Button(ventana, image=imagen_papel, command=lambda: logica.elegir_papel(texto_usuario, texto_pc, texto_resultado))
btn_papel.grid(row=2, column=2, pady=5, padx=25)

#---------boton tijera------
btn_tijera = Button(ventana, image=imagen_tijera, command=lambda: logica.elegir_tijera(texto_usuario, texto_pc, texto_resultado))
btn_tijera.grid(row=2, column=3, pady=5, padx=25)

# ------------------ VARIABLES --------------------
texto_usuario = StringVar(ventana)
texto_usuario.set("Piedra")  # Valor por defecto
texto_pc = StringVar(ventana)
texto_pc.set("Piedra")  # Valor por defecto
texto_resultado = StringVar(ventana)
texto_resultado.set("")  # Empieza vacío

# ------------------ TITULO--------------------
titulo=Label(ventana, text="PIEDRA - PAPEL - TIJERA", bg="#d1acd6", font=("Courier", 16, "bold", "italic", "underline"), fg="#551166")
titulo.grid(row=0, column=0, columnspan=4, pady=5, padx=5)

# ------------------ LABEL USUARIO --------------------
eleccion_usuario = Label(ventana, text="Tu eleccion:", bg="#602d7e", font=("Courier", 12, "bold", "italic"), fg="#f4e2fc")
eleccion_usuario.grid(row=8, column=1, padx=20, pady=10)

# ------------------ LABEL PC --------------------
eleccion_pc=Label(ventana, text="Eleccion PC:", bg="#602d7e", font=("Courier", 12, "bold", "italic"), fg="#f4e2fc")
eleccion_pc.grid(row=9, column=1, padx=20, pady=10)

#-------------------LABEL ELECCION USUARIO --------------------
opcion_usuario = Label(ventana, textvariable=texto_usuario, bg="#f5f5f5", font=("Arial", 12), fg="#333333", bd=3, relief="sunken")
opcion_usuario.grid(row=8, column=2, columnspan=2, padx=1, pady=10, ipadx=25, ipady=1)
#-------------------LABEL ELECCION PC --------------------
opcion_pc = Label(ventana, textvariable=texto_pc, bg="#f5f5f5", font=("Arial", 12), fg="#333333", bd=3, relief="sunken")
opcion_pc.grid(row=9, column=2, padx=1, columnspan=2, pady=10, ipadx=25, ipady=1)
#------------------- RESULTADO --------------------
resultado = Label(ventana, textvariable=texto_resultado, bg="#f08edf", font=("Arial", 12), fg="#333333", bd=3, relief="sunken")
resultado.grid(row=12, column=2, padx=10, pady=10, ipadx=45, ipady=1, columnspan=2)

ventana.mainloop()