#MODULO 4: WORKING WITH DATA IN PYTHON

print('\n1 - Working with data in Python')

print('Primero vamos a descargar un archivo de texto llamado example1.txt desde una URL en internet.')

# Importamos el módulo urllib.request, que permite trabajar con URLs y descargar contenido de internet
import urllib.request

# Esto descarga el archivo desde la URL y lo guarda con el nombre Example1.txt en el directorio actual.

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

print(f"Descarga completada. El archivo se guardó como", {filename})

print('Ahora vamos a utilizar algunos comandos útiles para textos: ')

#Vamos a abrir el archivo Example1.txt
Example1 = "Example1.txt"
print("Primero vamos a abrir el archivo con el comando 'open'")
file1 = open(Example1, "r")

print(f"El nombre del archivo es: file1.name={file1.name}")

print(f"El modo de apertura es: file1.mode={file1.mode}")

# Vamos a leer el archivo
FileContent = file1.read()

print(f"Contenido del archivo lo leemos con el comando: file1.read():")

print(f"{FileContent}")

print(f"Tipo del contenido del archivo es: type(FileContent)={type(FileContent)}")

print("Es muy importante cerrar el documento siempre al terminar con el comando 'close'")
file1.close()

print("Hay otra forma de abrir archivos y es mucho mas segura ya que cierra el archivo automáticamente. El comando es 'with'")

print("En 'with' hay tres modos, 'w' para escritura, 'r' para leer y 'a' para anexar.")

print("Con el comando: file1.read(), vamos a leer los digitos que queramos, en este caso primero leemos 4, luego 4, luego 7 y finalmente 15:")


with open(Example1, "r") as file1:
     print(file1.read(4))
     print(file1.read(4))
     print(file1.read(7))
     print(file1.read(15))

print(f"Comprobemos si with cerró el documento: file1.closed={file1.closed}")

print("También podemos leer una línea entera con el comando 'file1.readline()'")

with open(Example1, "r") as file1:
    print(f"La primera línea es: {file1.readline()}")
    print(f"La segunda línea es: {file1.readline()}")


print("Además podemos crear un bucle para imprimir cada línea. El resultado sería:")

with open(Example1,"r") as file1:
        i = 0;
        for line in file1:
            print(f"Iteración {str(i)}: {line}")
            i = i + 1
print(f"También podemos guardar las líneas como una lista con el comando: 'FileasList = file1.readlines()'")

with open(Example1, "r") as file1:
    FileasList = file1.readlines()
    print(f"El primer objeto de la lista seria: FileasList[0]={FileasList[0]}")
    print(f"El segundo objeto de la lista seria: FileasList[1]={FileasList[1]}")
    print(f"El tercer objeto de la lista seria: FileasList[2]={FileasList[2]}")

print('\n2 - Escritura de archivos con open()\n')

print("Para comenzar vamos a escribir dos líneas iniciales en 'Example2.txt' con el modo 'w'")
with open('Example2.txt', 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

print("Vamos a verificar que están escritas: ")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

print("Ahora vamos a escribir con un bucle los elementos de esta lista: Lines = ['This is line A', 'This is line B', 'This is line C']")
for line in Lines:
    print(line.strip())


print("Reescribimos el archivo con las líneas de la lista.")
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        writefile.write(line)

print("Ahora verificamos:")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

print("Si volvemos a escribir en el mismo archivo con el modo 'w', se reescribe:")
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite the file\n")

print("Contenido final del archivo tras sobrescribir:")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

print("Añadimos las líneas C, D y E al archivo 'Example2.txt' con el modo 'a'")
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

print("Contenido actualizado de 'Example2.txt':")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

print("\n Nota: En 'with' puedes usar modos adicionales:\n")
print(" - 'w+': Escritura y lectura (borra el contenido si ya existe)")
print(" - 'r+': Lectura y escritura (NO borra el contenido)")
print(" - 'a+': Añadir y lectura (crea el archivo si no existe)\n")

# Probando el modo 'a+' y las funciones tell() y seek()
print(" Ahora vamos a trabajar con el archivo 'Example2.txt' en modo 'a+'\n")
with open('Example2.txt', 'a+') as testwritefile: 
    print(f"Mostramos la posición inicial del cursor con el comando testwritefile.tell()={testwritefile.tell()}")

    print("Vamos a intentar leer desde la posición actual, es decir, el final del archivo: ")
    data = testwritefile.read()
    if not data:
        print("No se leyó nada (el cursor está al final).")
    else: 
        print(f"Contenido leído desde el final:\n {data}")

    print("Movemos el cursor al principio del archivo con el comando testwrite.seek(0,0)")
    testwritefile.seek(0, 0)
    print(f"Nueva posición del cursor tras seek(0, 0): {testwritefile.tell()}")

    print("Vamos a intentar leer desde el principio ahora: ")

    data = testwritefile.read()
    if not data:
        print("No se leyó nada desde el principio.")
    else: 
        print(f"Contenido leído desde el principio:\n {data}")

    print("Posición final del cursor tras leer:", testwritefile.tell())

print("Ahora vamos a conservar la primera linea del archivo, escribir encima de lo demás y eliminar lo sobrante con truncate()")

with open('Example2.txt', 'r+') as testwritefile:
    
    print("Primero, leemos el archivo original:")

    lines = testwritefile.readlines()

    for line in lines:
        print(line)
     
    
    print("Volvemos al principio con testwrite.seek(0,0) para reescribir")
    testwritefile.seek(0, 0)
    
    print('Conservamos la primera línea y escribimos las siguientes:')

    print()
    if lines:
        testwritefile.write(lines[0])  # conserva la primera línea original
    else:
        testwritefile.write("Line 0\n")  # si el archivo está vacío, la creamos

    testwritefile.write("Line 1\n")
    testwritefile.write("Line 2\n")
    testwritefile.write("Line 3\n")
    testwritefile.write("finished\n")

    print("Borramos todo lo demás con .truncate()")
    testwritefile.truncate()

    print("Ahora volvemos al principio y leemos el archivo:")
    testwritefile.seek(0)
    print(testwritefile.read())

print('\n3 - Loading Data with Pandas\n')

print(f"Primero, importamos la librería pandas para trabajar con estructuras de datos como DataFrames")

import pandas as pd 

print("A continuación, definimos la ruta del archivo CSV. ")

csv_path = "file1.csv"

print("Leemos el archivo CSV y lo almacenamos en un DataFrame. Además, mostramos las primeras 5 filas del archivo con .head()")
try:
    df = pd.read_csv(csv_path)
    print("Contenido de 'file1.csv':")
    print(df.head())
except FileNotFoundError:
    print(f"El archivo '{csv_path}' no fue encontrado.")

print("Ahora en vez de importar un archivo, creamos un diccionario con los datos llamado diccionario1.")
diccionario1 = {
    "Name": ["Ana", "Luis", "Marta", "Carlos", "Lucía", "Javier", "Sofía", "Andrés", "Laura", "Diego", "Elena", "Pablo", "Teresa", "Raúl", "Isabel"],
    "Age": [30, 25, 21, 40, 40, 33, 26, 38, 30, 31, 25, 27, 21, 32, 30],
    "City": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Zaragoza", "Granada", "Málaga", "Santander", "Oviedo", "Toledo", "Cádiz", "León", "Logroño", "Almería"],
    "Profession": ["Engineer", "Teacher", "Doctor", "Lawyer", "Designer", "Architect", "Pharmacist", "Accountant", "Analyst", "Developer", "Nurse", "Economist", "Writer", "Artist", "Engineer"]
}

print("Convertimos el diccionario en un DataFrame con el nombre: diccionario1_frame")
diccionario1_frame = pd.DataFrame(diccionario1)

print(f"Ahora vamos a leer solo los 10 primeros elementos de la columna de nombres con el comando: diccionario1_frame[['Name']]")

# Seleccionamos solo la columna 'Name'
x = diccionario1_frame[['Name']]
print("\nColumna 'Name':")
print(x.head(10))

print(f"Ahora vamos a leer solo los 6 primeros elementos de la columna de nombres y la de ciudades con el comando: diccionario1_frame[['Name','City']]")

# Seleccionamos las columnas 'Name' y 'City'
y = diccionario1_frame[['Name', 'City']]
print("\nColumnas 'Name' y 'City':")
print(y.head(6))

print("Accedemos a celdas específicas usando iloc (por posición)")

print("\nAcceso a celdas con iloc:")

print(f"Fila 0, Columna 0 (Name): diccionario1_frame.iloc[0, 0]={diccionario1_frame.iloc[0, 0]}")
print(f"Fila 1, Columna 0 (Name): diccionario1_frame.iloc[1, 0]={diccionario1_frame.iloc[1, 0]}")
print(f"Fila 0, Columna 2 (City): diccionario1_frame.iloc[0, 2]={diccionario1_frame.iloc[0, 2]}")

# Accedemos a una celda específica usando loc (por etiqueta)
print("\nAcceso a celda con loc:")
print(f"Edad de la persona en la fila 9: diccionario1_frame.loc[9, 'Age']={diccionario1_frame.loc[0, 'Age']}")


print('\n4 - Loading Data with Pandas\n')

print(f"Primero mostramos todos los valores de la columna 'Age' con diccionario1_frame[['Age']]: ")

print(diccionario1_frame[['Age']])

print("Ahora los valores únicos que aparecen en la columna 'Age'con: diccionario1_frame['Age'].unique()")

print(diccionario1_frame['Age'].unique())

print("¿Quien tiene 30 años o más? Lo haremos con el comando: diccionario1_frame['Age'] >= 30 ")
print("Esto nos dará como resultado 'True' o 'False'")

print(diccionario1_frame['Age'] >= 30)

print("Finalmente, filtramos el DataFrame para quedarnos solo con las personas cuya edad es mayor o igual a 30")
dc_30 = diccionario1_frame[diccionario1_frame['Age'] >= 30]

print("\nPersonas con edad mayor o igual a 30:")
print(dc_30)










