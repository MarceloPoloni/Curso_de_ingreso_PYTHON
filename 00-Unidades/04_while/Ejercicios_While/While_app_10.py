import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_positivo = 0
        acumulador_negativo = 0
        contador_positivos = 0
        contador_negativo = 0
        contador_0 = 0
        while True:
            numero_ingresado  =prompt("ingresar","ingresar numero")
            if numero_ingresado == None or numero_ingresado == "":
                break 
            else:
                numero_ingresado = int(numero_ingresado)
                if numero_ingresado > 0 :
                    acumulador_positivo += numero_ingresado
                    contador_positivos += 1
                elif numero_ingresado < 0:
                    acumulador_negativo += numero_ingresado
                    contador_negativo += 1
                elif numero_ingresado == 0:
                    contador_0 += 1
                
                
                diferencia = contador_positivos - contador_negativo
        mensaje = ("resultado \n suma acumulado de negativos {0} \n suma acumulada de positivos {1} \n cantidad de numeros positivos {2} \n cantidad de numeros negativos {3} \n cantidad de ceros {4} \n la diferencia es {5} ".format(acumulador_negativo,acumulador_positivo,contador_positivos,contador_negativo,contador_0,diferencia))
        alert ("mensaje",mensaje)
                 
            

        


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
