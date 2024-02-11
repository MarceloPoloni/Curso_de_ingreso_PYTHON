import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marcelo 
apellido:Poloni
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
       nombre_1 = prompt ("1","ingrese su nombre")
       nombre_2 = prompt ("2","ingrese su nombre")
       edad_1 = int (prompt ("1" , "ingrese su edad"))
       edad_2 = int(prompt ("2" , "ingrese su edad"))
       peso_1 = float(prompt ("1" , "ingrese su peso"))
       peso_2 = float(prompt ("2" , "ingrese su peso"))
      
       suma_de_pesos = peso_1 + peso_2
       promedio_edades = (edad_1 + edad_2) / 2
       PRECIO = suma_de_pesos * 1000
       alert ("viaje", "Hola {0} y {1},sus pesos son {2} kilos y {3} kilos respectivamente,sumados da {4},el promedio de edad es {5} y su viaje vale {6} pesos".format(nombre_1,nombre_2,peso_1,peso_2,suma_de_pesos,promedio_edades,PRECIO))
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()