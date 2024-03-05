import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marcelo
apellido:Poloni
---
Ejercicio: entrada_salida_04
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un nombre utilizando el Dialog Prompt 
y luego mostrarlo en la caja de texto txt_nombre (.delete / .insert )
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

       
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_clientes_1_dia = 0
        contador_clientes_3_dia = 0
        contador_clientes_5_dia = 0
        contador_de_personas = 0
        acumulador_kilos_PM = 0
        altura_cliente_mas_alto = None
        nombre_cliente_mas_alto = None
        edad_cliente_mas_alto = 0
        gimansio = True
        bandera_primer_ingreso = True
        cantidad_de_dias_elegidos = 0
        edad_mas_joven = 0
        peso_muerto_mas_joven = 0
        nombre_mas_joven = None
        
        while gimansio:
            nombre = prompt("m","ingrese su nombre")
             
            print(nombre)
            
            edad = prompt("m", "ingrese su edad")
            edad = int(edad)
            while edad < 13 :
                edad = prompt ("m","la edad debe ser mayor a 12")
                edad =int(edad)
            print (edad)

            altura = prompt("m","ingrese altura")
            altura = float(altura)
            while altura <= 0 :
                altura = prompt("m","La altura tiene que ser positiva")
                altura = float(altura)
            print(altura)

            dias_que_asiste = prompt("m","ingrese la cantidad de dias que asiste")
            dias_que_asiste = int(dias_que_asiste)
            while dias_que_asiste != 1 and dias_que_asiste !=3 and dias_que_asiste != 5:
                dias_que_asiste = prompt("m", "ingrese si es 1 , 3 o 5")
                dias_que_asiste = int(dias_que_asiste)
            print(dias_que_asiste)

            kilos_pesomuerto = prompt("m","ingrese la cantidad de kilos que levanta en PM")
            kilos_pesomuerto = float(kilos_pesomuerto)
            
            while kilos_pesomuerto <= 0 :
                kilos_pesomuerto = prompt("m","tiene que ser mayor a 0")
                kilos_pesomuerto = float(kilos_pesomuerto)
            print (kilos_pesomuerto)

            acumulador_kilos_PM += kilos_pesomuerto
            
            contador_de_personas += 1


            
            #a y b)
            match dias_que_asiste :
                case 1 :
                    contador_clientes_1_dia += 1
                    

                case 3 :
                    contador_clientes_3_dia += 1
                    


                case 5 :
                    contador_clientes_5_dia += 1

            #c)
            if bandera_primer_ingreso == True or altura > altura_cliente_mas_alto :
                nombre_cliente_mas_alto = nombre
                altura_cliente_mas_alto = altura
                edad_cliente_mas_alto = edad

            if dias_que_asiste == 5 and (edad < edad_mas_joven or bandera_primer_ingreso == True ):
                edad_mas_joven = edad
                peso_muerto_mas_joven = kilos_pesomuerto
                nombre_mas_joven = nombre
                bandera_primer_ingreso = False
            
            
            if question ("m", "Queres ingresar otro?") == False:
                break
            
        #d)
        if contador_clientes_1_dia > contador_clientes_3_dia and contador_clientes_1_dia > contador_clientes_5_dia:
            cantidad_de_dias_elegidos = 1
        elif contador_clientes_3_dia > contador_clientes_1_dia and contador_clientes_3_dia > contador_clientes_5_dia:
            cantidad_de_dias_elegidos = 3
        else :
            cantidad_de_dias_elegidos = 5

        #ayb)
        porcentaje_dia_1= contador_clientes_1_dia * 100 / contador_de_personas
        print(porcentaje_dia_1)
        
        promedio_kilos_3_dias =  acumulador_kilos_PM / contador_clientes_3_dia
        print (promedio_kilos_3_dias)


        mensaje = (f"El promedio de kilos que levantan las personas que asisten 3 dias es {promedio_kilos_3_dias}\n"+
                   f"El porcentaje de las personas que van solo 1 dia es {porcentaje_dia_1}\n" + 
                   f"El nombre del cliente mas alto es {nombre_cliente_mas_alto} y la altura es {altura_cliente_mas_alto} y tiene {edad_cliente_mas_alto} \n" + 
                   f"los clientes eligen ir {cantidad_de_dias_elegidos} dia/s \n" +
                    f"El levantador mas joven que asiste los 5 dias es {nombre_mas_joven} y levanta {peso_muerto_mas_joven} kilos" )
        
        alert ("GYM" , mensaje)

# Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

# -Nombre
# -Edad (debe ser mayor a 12)
# -Altura (no debe ser negativa)
# -Días que asiste a la semana (1, 3, 5)
# -Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

# No sabemos cuántos clientes serán consultados.
# Se debe informar al usuario:
# A) El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
# B) El porcentaje de clientes que asiste solo 1 día a la semana.
# C) Nombre y edad del cliente con más altura.
# D) Determinar si los clientes eligen más ir 1, 3 o 5 días
# E) Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()