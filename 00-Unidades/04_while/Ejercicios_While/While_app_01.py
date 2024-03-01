import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: while_01
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        ventas = True
        contador_celular = 0
        contador_computadora = 0
        contador_ventilador = 0
        contador_productos = 0
        bandera_primer_ingreso = True
        nombre_producto_mas_caro = None
        precio_producto_mas_caro = 0
        precio_producto_mas_barato = 0
        nombre_producto_mas_barato = 0
        contador_de_error = 0
        while ventas :
            nombre_producto = prompt("m", "ingrese nombre del producto")

            tipo_de_producto = prompt("m" , "ingrese el tipo del producto")
            while tipo_de_producto != "celular" and tipo_de_producto != "computadora" and tipo_de_producto != "ventilador":
                tipo_de_producto = prompt("m" , "No existen esos productos")
                contador_de_error += 1
            
            precio_producto = prompt("m" , "ingrese precio")
            precio_producto = int(precio_producto)
            while precio_producto < 1000 :
                precio_producto = prompt("m","El precio del producto no puede ser menor a 1000")
                precio_producto = int(precio_producto)
                contador_de_error += 1

            dia_de_semana = prompt("m" , "ingrese dia")
            while dia_de_semana == "sabado" or dia_de_semana == "domingo" :
                dia_de_semana =prompt("m" , "solo se trabaja de lunes a viernes")
                contador_de_error += 1
            
            match tipo_de_producto:
                case "celular" :
                    contador_celular += 1
                
                case "computadora" :
                    contador_computadora += 1
                     

                case "ventilador" :
                    contador_ventilador += 1
             
            contador_productos += 1
            
        
            if bandera_primer_ingreso == True or precio_producto > precio_producto_mas_caro:
                precio_producto_mas_caro = precio_producto
                nombre_producto_mas_caro = nombre_producto
            
            if dia_de_semana == "viernes" and ( precio_producto < precio_producto_mas_barato or bandera_primer_ingreso == True):
                precio_producto_mas_barato = precio_producto
                nombre_producto_mas_barato = nombre_producto
                bandera_primer_ingreso = False
        
            if question("m" , "desea añadir otro producto") == False:
                break

                    

        #a)
        porcentaje_celular = contador_celular * 100 / contador_productos
        porcentaje_ventilador = contador_ventilador * 100 / contador_productos
        porcentaje_computadora = contador_computadora * 100 / contador_productos

        #d)
        promedio_computadoras = contador_computadora / contador_productos 

        promedio_errores = contador_de_error / contador_productos

        mensaje = (f"El porcentaje de computadoras es {porcentaje_computadora} \n" + 
                   f"El porcentaje de celulares es {porcentaje_celular} \n" + 
                   f"El porcentaje de ventiladores  es {porcentaje_ventilador} \n" + 
                   f"El producto mas caro vendido es {nombre_producto_mas_caro}\n" +
                   f"El producto mas barato vendido el viernes es {nombre_producto_mas_barato}\n" + 
                   f"el promedio de computadoras vendidas es {promedio_computadoras}\n" + 
                   f"El promedio de los errores es {promedio_errores}")
        alert ("m" , mensaje)




#         Nos piden diseñar un sistema de control de ventas para una empresa de electrodomésticos. 
# (Teniendo en cuenta que no sabemos cuantas ventas hubo en total y que todos los datos deben ser ingresados por prompt y mostrados en un solo alert)

# Para ello los empleados deben ingresar:

# -Nombre del producto.

# -Tipo de producto (Celular o Computadora o Ventilador)

# -Precio del producto (No puede ser menor a $1000)

# -Día de la semana en el que se realizó la venta (La empresa no trabaja sábados ni domingos)

# En base a la información ingresada se debe informar:

# +El porcentaje de productos que se vendieron por tipo.

# +El nombre del producto más caro vendido.

# +El nombre del producto mas barato vendido un viernes.

# +Promedio de computadoras vendidas.

# +Promedio de errores que ocurrieron durante la carga de datos (Ya sea al ingresar el tipo, el precio o el día de la venta, esto para controlar la eficiencia de los empleados al cargar las ventas)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()