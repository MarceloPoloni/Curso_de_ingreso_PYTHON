import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: while_02
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números DESCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        casino = True
        bandera_primer_ingreso = True
        nombre_mas_gano = None
        genero_mas_gano = None
        importe_que_mas_gano = 0
        contador_poker = 0
        contador_ruleta = 0
        contador_tragamoneda = 0
        dinero_total = 0
        

        while casino :
            nombre = prompt ("ingrese" ,"ingrese su nombre")

            importe_ganado = prompt("m " ,"ingrese importe")
            importe_ganado= int(importe_ganado)
            while importe_ganado < 999 :
                importe_ganado = prompt("m", "el importe debe ser mayor o igual a 1000") 
                importe_ganado =int(importe_ganado)
            print (importe_ganado)

            genero = prompt("m" , "ingrese genero")
            while genero != "F" and genero != "M" and genero != "O" :
                genero = prompt ("m" , "el genero ingresado se tiene que escribir con M , F , O")
        
            print (genero)

            juego = prompt("m", "ingrese juego")
            while juego != "ruleta" and juego != "poker" and juego != "tragamonedas":
                juego = prompt("m" , "juego incorrecto")
            print (juego)
            
            dinero_total += importe_ganado

            match juego:
                case "poker":
                    contador_poker +=1
                    
                case "ruleta" :
                    contador_ruleta += 1

                case "tragamonedas" :
                    contador_tragamoneda += 1

            
            
            
            
            
            
            if bandera_primer_ingreso == True or importe_ganado > importe_que_mas_gano :
                nombre_mas_gano = nombre
                genero_mas_gano = genero
                importe_que_mas_gano = importe_ganado   
            print (nombre_mas_gano)

            if question ("m", "otro?") == False:
                break  

        promedio_ganado_ruleta =  dinero_total / contador_ruleta  
        print (promedio_ganado_ruleta)     




# Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:
# Nombre
# -Importe ganado (mayor o igual $1000)
# -Género (“Femenino”, “Masculino”, “Otro”)
# -Juego (Ruleta, Poker, Tragamonedas)

# Necesitamos saber:
# A) Nombre y género de la persona que más ganó.
# B) Promedio de dinero ganado en Ruleta.
# C) Porcentaje de personas que jugaron en el Tragamonedas.
# D) Cuál es el juego menos elegido por los ganadores.
# E) Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
# F) Porcentaje de dinero en función de cada juego.

        
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()