def contar_lineas(texto):
    return len(texto.split('\n'))
 
def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)
 
def contar_caracteres(texto):
    return len(texto)
 
def contar_palabra_especifica(texto, palabra):
    palabras = texto.split()
    return palabras.count(palabra)
 
def procesar_archivo(input_file_name, output_file_name, palabra):
    with open(input_file_name, 'r', encoding='utf-8') as file:
        texto = file.read()
 
    num_lineas = contar_lineas(texto)
    num_palabras = contar_palabras(texto)
    num_caracteres = contar_caracteres(texto)
    num_palabra_especifica = contar_palabra_especifica(texto, palabra)
 
    with open(output_file_name, 'w', encoding='utf-8') as file:
        file.write(f"Total de líneas: {num_lineas}\n")
        file.write(f"Total de palabras: {num_palabras}\n")
        file.write(f"Total de caracteres: {num_caracteres}\n")
        file.write(f"Frecuencia de la palabra '{palabra}': {num_palabra_especifica}\n")

# Ejemplo de uso
input_file_name = 'archivo_entrada.txt'
output_file_name = 'archivo_salida.txt'
palabra_a_buscar = 'ejemplo'

procesar_archivo(input_file_name, output_file_name, palabra_a_buscar)
