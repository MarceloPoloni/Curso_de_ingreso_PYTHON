import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marcelo
apellido:Poloni
---
Ejercicio: if_01
---
Enunciado:
Al presionar el botón 'Mostrar', se deberá obtener el contenido de la caja de texto txt_edad,
transformarlo en número, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años” utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

    
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_de_votos_femeninos = 0
        total_edad_femenino = 0
        bandera_primer_ingreso = True
        votante_mas_viejo = None
        participante_mas_votado = None
        bandera_primer_ingreso = False
        edad_del_mas_joven = 100
        contador_giovanni = 0
        contador_gianni = 0 
        contador_esteban = 0
        votante_de_gianni = None
        edad_del_mas_viejo = 0
        votante_mas_joven = None
        total_votantes = 0
        promedio_femenino = 0
        while True:
            nombre_del_votante = prompt("Ingrese","nombre del votante")
            
            
            edad_del_votante = prompt("ingrese" , "ingrese edad")
            edad_del_votante = int(edad_del_votante)
            print (edad_del_votante)
            while edad_del_votante < 13 :
                edad_del_votante = prompt("error" , "el votante tiene que ser mayor a 13 años")
                edad_del_votante = int(edad_del_votante)
                
            
            genero_del_votante = prompt("ingrese" , "ingrese genero")
            while genero_del_votante != "masculino" and genero_del_votante != "femenino" and genero_del_votante != "otro": 
                genero_del_votante=prompt("error" , "reingrese genero")

            nombre_participante = prompt ("ingrese" , "A quien votas para que salga?")
            while nombre_participante != "giovanni" and nombre_participante != "gianni" and nombre_participante != "esteban":
                nombre_participante = prompt("error" , "tiene que ingresar participante que este en placa")
            total_votantes += 1

            #a)
            if genero_del_votante == "femenino":
                contador_de_votos_femeninos += 1 
                total_edad_femenino += edad_del_votante

            #b)
            if bandera_primer_ingreso == True or edad_del_votante > edad_del_mas_viejo:
                votante_mas_viejo = nombre_del_votante
                edad_del_mas_viejo = edad_del_votante
               
            #c
            if nombre_participante == "gianni" and (edad_del_votante < edad_del_mas_joven or  bandera_primer_ingreso == True):
                edad_del_mas_joven = edad_del_votante
                votante_de_gianni = nombre_del_votante
                bandera_primer_ingreso = False
            #D)
            match nombre_participante:
                case "esteban":
                    contador_esteban += 1
                    
                case "gianni":
                    contador_gianni += 1
                    
                case "giovanni":
                    contador_giovanni += 1
                    
            
            if question("mensaje" , "Desea ingresar otro?") == False:
                break
    
          
                
            


        porcentaje_esteban = contador_esteban * 100 / total_votantes
        porcentaje_gianni = contador_gianni * 100 / total_votantes
        porcentaje_giovanni = 100 - porcentaje_gianni - porcentaje_esteban

        if contador_de_votos_femeninos != 0:
            promedio_femenino = total_edad_femenino / contador_de_votos_femeninos
       
        
        if contador_gianni > contador_esteban and  contador_gianni > contador_giovanni:
            participante_mas_votado = "gianni"
        elif contador_esteban > contador_gianni and contador_esteban > contador_giovanni:
            participante_mas_votado = "esteban"
        else:
            participante_mas_votado = "giovanni"




        resultado = (f"El promedio de edad de mujeres votantes es {promedio_femenino}\n" + 
                      f"El votante mas viejo es {votante_mas_viejo} \n"+
                      f"El votante mas joven que voto a Gianni es {votante_de_gianni}\n"+
                      f" participante gianni = {porcentaje_gianni}% \n" + 
                      f"participante esteban = {porcentaje_esteban}% \n" + 
                      f"participan giovanni = {porcentaje_giovanni}\n"
                      f"La persona que deja la casa es {participante_mas_votado}")
        alert ("ATENCION" , resultado)
            






#         Simulacro Turno Mañana

# Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.

# Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.

# Cada televidente que vota deberá ingresar:

# Nombre del votante

# Edad del votante (debe ser mayor a 13)

# Género del votante (Masculino, Femenino, Otro)

# El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

# No se sabe cuántos votos entrarán durante la gala.

         # Se debe informar al usuario:

# El promedio de edad de las votantes de género Femenino 

# Del votante más viejo, su nombre.

# Nombre del votante más joven qué votó a Gianni.

# Nombre de cada participante y porcentaje de los votos qué recibió.

# El nombre del participante que debe dejar la casa (El que tiene más votos)
         
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()