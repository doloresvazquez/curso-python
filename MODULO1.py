# MODULO 1: PYTHON BASICS
print('\n1 - Mi primer programa')
# Escribimos Hello World con el comando print
print('Hello World')
print('Hello\nWorld')

print('\n2 - Tipos de datos\n')

# Mostramos el tipo de cada dato con mensaje claro
print(f'El tipo del número 11 es: {type(11)}')
print(f'El tipo del número 2.234 es: {type(2.234)}')
print(f'El tipo de la cadena "Hello" es: {type("Hello")}')

print('\nAhora convertimos el número 1 a booleano y luego volvemos a entero\n')

print(f'bool(1) = {bool(1)}')
print(f'int(True) = {int(True)}')

print('\n3 - Expresiones y variables\n')

print('Comenzamos con operaciones aritméticas:\n')

print(f'43 + 60 + 16 + 41 = {43 + 60 + 16 + 41}')
print(f'50 - 60 = {50 - 60}')
print(f'5 * 5 = {5 * 5}')
print(f'25 / 5 = {25 / 5}  # Resultado float')
print(f'25 / 6 = {25 / 6}  # Resultado float')
print(f'25 // 5 = {25 // 5}  # División entera')
print(f'25 // 6 = {25 // 6}  # División entera')
print(f'2 * 60 + 30 = {2 * 60 + 30}')
print(f'30 + 2 * 60 = {30 + 2 * 60}  # Primero multiplica')
print(f'(30 + 2) * 60 = {(30 + 2) * 60}  # Paréntesis primero\n')

print('Ahora continuamos con las variables:\n')

variable = 1
print(f'variable = {variable}')
variable = 10
print(f'variable = {variable}')
print(f'Ahora variable vale: {variable}  # Se reescribió el valor\n')

x = 43 + 60 + 16 + 41
print(f'x =43 + 60 + 16 + 41 = {x}')

y = x / 60
print(f'y =x/60= {y}')

print(f'El tipo de y es: {type(y)}')

print('\n4 - Operaciones con cadenas\n')

# Definimos el nombre
Name = 'Michael Jackson'
print('Utilizaremos de ejemplo Michael Jackson')

# Accedemos a caracteres individuales
print(f'El carácter en la posición 0 es: {Name[0]}')
print(f'El carácter en la posición 4 es: {Name[4]}')
print(f'El último carácter es: {Name[-1]}')

# Subcadenas 
print(f'Desde la posición 0 hasta antes de la 4: {Name[0:4]}')
print(f'Desde la posición 4 hasta antes de la 8: {Name[4:8]}')

#Encontrar caracteres
print(f'Encuentra los caracteres -el-:{Name.find('el')}')
print(f'Encuentra los caracteres -Jack-:{Name.find('Jack')}')
print(f'Encuentra los caracteres -8-:{Name.find('8')}')
print('Aclaración: si aparece -1 es que no encontró los caracteres')

# Saltos 
print(f'Caracteres saltando de 2 en 2: {Name[::2]}')
print(f'Caracteres del 0 al 4 saltando de 2 en 2: {Name[0:5:2]}')

# Longitud de la cadena
print(f'La longitud de la cadena es: {len(Name)}')

# Concatenación de cadenas
Name1 = Name + ' is the best'
print(f'Concatenación: {Name1}')
# Repetición de cadenas
print(f'\nRepetición de cadenas:')
print(2 * Name)  # Imprime el nombre dos veces

# Caracteres especiales
print(f'\nEjemplos con caracteres especiales:')
print('Michael Jackson\nis the best')    # Salto de línea
print('Michael Jackson\tis the best')    # Tabulación
print('Michael Jackson\\is the best')    # Barra invertida
print(r'Michael Jackson\is the best')    # Cadena raw (sin procesar caracteres especiales)

# Cadena original
A = 'Maths teacher'

# Convertimos a mayúsculas
B = A.upper()
print(f'Cadena original: {A}')
print(f'Cadena en mayúsculas: {B}')

# Reemplazo de palabras
C = A.replace('teacher', 'class')
print(f'Reemplazando "teacher" por "class": {C}')

# División en palabras (split)
D = A.split()
print(f'División en palabras con split(): {D}')

# Uso de expresiones regulares
import re



texto = 'The BodyGuard is the best album'
print(f'El texto es:{texto} ')

print(' Buscamos la palabra "Body" dentro del texto')
resultado = re.search('Body', texto)

if resultado:
    print('¡Patrón encontrado!')
else:
    print('Patrón no encontrado')

print('Encontremos si en la siguiente frase hay algun digito usando \d')
print('La frase es:Vivo en el numero 148 ')
s3 = 'Vivo en el numero 148'
resultado=re.search(r"\d", s3)
print('El resultado es:')
if resultado:
    print("Dígito encontrado")
else:
    print("Dígito no encontrado.")




