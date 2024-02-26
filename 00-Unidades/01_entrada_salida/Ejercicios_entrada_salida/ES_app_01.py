import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marcelo
apellido: Poloni
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        contador_masculino_IAIOT = 0
        contador_IA = 0
        contador_IOT = 0
        contador_RV_RA = 0
        seguir = True
        while seguir == True :
            nombre = prompt("m","ingrese nombre")
            
            edad = prompt ("m","ingrese edad")
            edad = int(edad)
            while edad < 18 :
                 edad = prompt ("error","reeingrese edad")
            edad = int(edad)


            genero = prompt ("m","ingrese genero")
            while genero != "masculino" and genero != "femenino" and genero != "otro":
                genero = prompt ("error","reeingrese genero")
            
            tecnologia = prompt ("m","ingrese tecnologia")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = prompt ("error","Reeingre tecnologia")
            
            #1) 
            if genero == "masculino" and (tecnologia == "IA" or tecnologia == "IOT") and edad >= 25 and edad <= 50:
                contador_masculino_IAIOT += 1
            # 2)
            if tecnologia == "IA":
                contador_IA += 1 
                
            elif tecnologia == "IOT" :
                contador_IOT += 1

            else:
                contador_RV_RA += 1
            
           
            


            


            seguir = question("mensaje" , "desea continuar?")
        
        if contador_IA > contador_RV_RA and contador_IA > contador_RV_RA:
            p

        print (f"la cantidad de personas de genero masculino que votaron por IA/IOT es {contador_masculino_IAIOT}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
