import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
      
        # sumatoria_votos = 0
        # contador_candidatos = 0
        # votos_maximos = 0
        # votos_minimos = 0 
        # candidato_mas_votado = None
        # sumatoria_de_edades = 0
        # edad_menos_votado = 0 
        # candidato_menos_votado = None
        # bandera_primer_ingreso = True

        # while True:
        #     nombre_candidato = prompt("ingrese","ingrese nombre")
        #     while nombre_candidato == None:
        #         prompt ("ERROR", "Reingrese nombre")

        #     edad = prompt("ingrese" , "ingrese edad")
        #     edad = int(edad)
        #     while edad < 25 :
        #         edad = prompt("error" , "Reingrese edad, debe ser mayor a 25")
        #         edad = int(edad)
            
        #     cantidad_de_votos = prompt("Ingrese","ingrese cantidad de votos") 
        #     cantidad_de_votos = int(cantidad_de_votos)

        #     while cantidad_de_votos <= 0 :
        #         cantidad_de_votos = prompt("Error" , "no tiene votos, Reingrese")
        #         cantidad_de_votos = int(cantidad_de_votos)

        #     if bandera_primer_ingreso == True:
        #         candidato_mas_votado = nombre_candidato
        #         votos_maximos = cantidad_de_votos
        #         votos_minimos = cantidad_de_votos
        #         edad_menos_votado = edad 
        #         bandera_primer_ingreso = False
        #    # a)
        #     if cantidad_de_votos > votos_maximos:
        #         votos_maximos = cantidad_de_votos
        #         candidato_mas_votado = nombre_candidato
        #     # b)
        #     if cantidad_de_votos < votos_minimos:
        #         votos_minimos = cantidad_de_votos
        #         candidato_menos_votado = nombre_candidato
        #         edad_menos_votado = edad
        #     # c)
        #     contador_candidatos += 1
        #     sumatoria_de_edades += edad
        #     # d)
        #     sumatoria_votos += cantidad_de_votos
           
        #     if question ("mensaje","desea ingresar otro?") == False:
        #         break
                
            
        # promedio_edades= sumatoria_de_edades / contador_candidatos
        # resultado = (f"el nombre del candidato mas votado es {candidato_mas_votado} \n" + 
        #              f"B: {candidato_menos_votado} , {edad_menos_votado}\n" + 
        #              f"c:{promedio_edades} \n" +
        #               f"d: {sumatoria_votos}\n" )
                    

        # alert ("datos", resultado )
                
           
        bandera_primer_ingreso = True
        candidato_mas_votado = None
        maximo_de_votos = 0
        minimo_de_votos = 0 
        edad_menos_votado = 0 
        contador_de_candidatos = 0 
        contador_de_edades = 0
        total = 0
  
        #valido
        while True:
            nombre_de_candidato = prompt("ingrese","ingrese nombre del candidato")
            while nombre_de_candidato == None or nombre_de_candidato == "":
                nombre_de_candidato = prompt("error","reingrese nombre")
            
            edad_candidato = prompt("x","ingrese edad")
            edad_candidato = int(edad_candidato)
            while edad_candidato < 25 :
                edad_candidato = prompt("error" , "la edad tiene que ser mayor a 25")
                edad_candidato = int(edad_candidato)
            
            cantidad_de_votos = prompt("x","ingrese cantidad de votos")
            cantidad_de_votos = int(cantidad_de_votos)
            while cantidad_de_votos <= 0 :
                cantidad_de_votos = prompt("error", "no tiene votos")
            
        #1)
            if bandera_primer_ingreso == True:
                maximo_de_votos = cantidad_de_votos
                minimo_de_votos = cantidad_de_votos
                candidato_mas_votado = nombre_de_candidato
                candidato_menos_votado = nombre_de_candidato
                edad_menos_votado = edad_candidato
                bandera_primer_ingreso = False
            else :
                if cantidad_de_votos > maximo_de_votos :
                    maximo_de_votos = cantidad_de_votos
                    candidato_mas_votado = nombre_de_candidato
                    #b
                elif cantidad_de_votos < minimo_de_votos:
                    candidato_menos_votado = nombre_de_candidato
                    edad_menos_votado = edad_candidato
            
            #c
            contador_de_candidatos += 1
            contador_de_edades += edad_candidato
            #d
            total += cantidad_de_votos
            if question ("mensaje","desea agregar uno mas?") == False:
                break
        promedio = contador_de_edades / contador_de_candidatos
        resultado = (f"el nombre del candidato mas votado es {candidato_mas_votado} \n" + 
                     f"el nombre del candidato con menos votos es {candidato_menos_votado} y la edad es {edad_menos_votado} \n" + 
                     f"el promedio de edades de los candidatos es {promedio} \n" + 
                     f"el total de votos emitidos es {total}")
        alert("Elecciones" , resultado)

  
  
  #De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
#nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
#Informar: 
# a. nombre del candidato con más votos
#. nombre y edad del candidato con menos votos
#c. el promedio de edades de los candidatos
#. total de votos emitidos.
#Todos los datos se ingresan por prompt y los resultados por alert
      

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
