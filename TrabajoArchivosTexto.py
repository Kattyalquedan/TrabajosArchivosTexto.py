TrabajoArchivosTexto.py
# Trabajo con Archivos de Texto en Python
# Autor: [Tu nombre]
# Descripción: Este programa escribe y lee un archivo de texto llamado "my_notes.txt"

# --- ESCRITURA DE ARCHIVO ---
# Abrimos (o creamos si no existe) el archivo en modo escritura ('w')
# Si ya existía, se sobrescribirá su contenido
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales
archivo.write("1. Siempre aprender algo nuevo cada día.\n")
archivo.write("2. La práctica constante mejora las habilidades.\n")
archivo.write("3. El esfuerzo y la perseverancia construyen el éxito.\n")

# Cerramos el archivo después de escribir
archivo.close()

# --- LECTURA DE ARCHIVO ---
# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos línea por línea y mostramos en consola
print("Contenido del archivo 'my_notes.txt':\n")
linea = archivo.readline()
while linea:
    print(linea.strip())  # strip() elimina los saltos de línea extras
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()

print("\nArchivo leído y cerrado correctamente.")
