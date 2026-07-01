  
def validar_nombre(nombre):

  return len(nombre.strip()) > 0



def validar_edad(edad_str):

  if edad_str.isdigit():

    return int(edad_str) >= 0

  return False



def validar_nota(nota_str):

  try:

    nota= float(nota_str)

    return nota > 0

  except ValueError:

    return False


   


def mostrar_menu():

   print("\n========== MENÚ PRINCIPAL ==========")

   print("1. Agregar estudiante")

   print("2. Buscar estudiante")

   print("3. Eliminar estudiante")

   print("4. Actualizar estados")

   print("5. Mostrar estudiantes")

   print("6. Salir")

   print("=====================================")



def leer_opcion():

  opcion = input("Seleccione una opción(1-6): ")

  return opcion



def agregar_estudiante(lista_estudiante):

  nombre = input("Ingrese el nombre del estudiante: ")

  edad_ = input("Ingrese la edad del estudiante: ")

  nota_  = input("Ingrese la nota del estudiante : ")



  if not validar_nombre(nombre):

    print("Error: El nombre no puede estar vacío ni ser solo espacios en blanco.")

    return



  if not validar_edad(edad_):

    print("Error: la nota debe ser un número entero mayor o igual que uno.")

    return



  if not validar_nota(nota_):

    print("Error: la nota debe ser un número decimal entre 1.0 y 7.0.")

    return


def buscar_estudiante(nombre,lista):
 for posicion in lista(posicion):
   

 
 
 
def eliminar_estudiante():
  
 


def actualizar_estados():
  



def mostrar_estudiantes():
  


def salir():
  
 print("Gracias por usar el sistema. Vuelva Pronto")
 exit
  
  