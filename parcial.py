import random
import string

def generar_contraseña():
  caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
  letras_mayusculas = string.ascii_uppercase
  letras_minusculas = string.ascii_lowercase
  numeros = string.digits

  todos_caracteres = caracteres_especiales + letras_mayusculas + letras_minusculas + numeros

  while True:
   contraseña = ''.join(random.choice(todos_caracteres) for _ in range(8))
   if (any(char in letras_mayusculas for char in contraseña) and
            any(char in letras_minusculas for char in contraseña) and
            any(char in numeros for char in contraseña) and
            any(char in caracteres_especiales for char in contraseña) and
            ' ' not in contraseña):
            break
   

  print("Contraseña generada:", contraseña)
 
  with open("contraseña.txt", "w") as archivo:
        archivo.write(contraseña)
generar_contraseña()