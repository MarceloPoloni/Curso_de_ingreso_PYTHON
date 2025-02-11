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

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        giovanni = None
        gianni = None
        esteban = None
        contador_de_votos_femeninos = 0
        total_edad_femenino = 0
        bandera_primer_ingreso = True
        votante_mas_viejo = None
        participante_mas_votado = None
        bandera_primer_ingreso = False
        maximo_de_votos = 0
        edad_del_mas_joven = 0
        votos_gianni = 0
        votante_de_gianni = None
        edad_del_mas_viejo = None
        votante_mas_joven = None
        while True:
            nombre_del_votante = prompt("Ingrese","nombre del votante")
            while nombre_del_votante == None or nombre_del_votante == "":
                nombre_del_votante = prompt ("error" , "ingrese un nombre")
            
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
            
            votos = prompt("ingrese" , "debera ingresar 1 para confirmar su voto")
            votos = int(votos)
            while votos != 1 :
                votos =prompt("error" ,"tiene que ingresar solo 1 para confirmar")
                votos = int(votos)


            #a)
            if genero_del_votante == "femenino":
                contador_de_votos_femeninos += 1 
                total_edad_femenino += contador_de_votos_femeninos

            #b)
            elif bandera_primer_ingreso == True:
                votante_mas_viejo = nombre_del_votante
                edad_del_mas_viejo = edad_del_votante
                edad_del_mas_joven = edad_del_votante
                votante_mas_joven = nombre_del_votante
                participante_mas_votado = nombre_participante
                maximo_de_votos = votos
                votos_gianni = votos
                votante_de_gianni = nombre_del_votante
                bandera_primer_ingreso = False
                edad_del_votante = int(edad_del_votante)
                edad_del_mas_viejo=int(edad_del_mas_viejo)
            elif edad_del_votante > edad_del_mas_viejo :
                edad_del_mas_viejo = edad_del_votante
                votante_mas_viejo = nombre_del_votante
                edad_del_mas_viejo = int(edad_del_mas_viejo)
             
            elif edad_del_votante < edad_del_mas_joven and nombre_participante == gianni and votos > votos_gianni :
                edad_del_mas_joven = edad_del_votante
                votos_gianni = votos
                votante_de_gianni = nombre_del_votante
            #e)
            elif votos > maximo_de_votos:
                participante_mas_votado = nombre_participante
            
            if question("mensaje" , "Desea ingresar otro?") == False:
                break
        
        promedio_femenino = total_edad_femenino / contador_de_votos_femeninos

        resultado = (f"El promedio de edad de mujeres votantes es {promedio_femenino}\n" + 
                     f"El votante mas viejo es {votante_mas_viejo} \n"+
                     f"El votante mas joven que voto a Gianni es {votante_de_gianni}\n"+
                     f"nombre de los participantes {gianni},{giovanni},{esteban}\n" + 
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