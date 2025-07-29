#MODULO 3: PYTHON PROGRAMMING FUNDAMENTAL

print('\n1 - Conditions and branching')

print("Veamos como funciona la condicion 'igual a'")

print("Si declaramos la variable a=6 y le preguntamos si a es igual a 7, es decir, 'a==7', el resultado será False o True")

a=6

print(f"El resultado de a==7 es {a==7}")


print("Ahora declaramos la variable i=5 y le preguntamos si i es menor o igual a 7, es decir, 'i<=7'")

i=5

print(f"El resultado es: {i<=7}")

print(f"Veamos si i es distinto de 6, es decir i!=6. El resultado es {i!=6}")

print(f"Ahora vamos a hablar de 'if', con el ejemplo de un concierto. Construiremos un programa que nos dirá si el individuo puede asistir a un concierto o no dependiendo de su edad.")

print('Primero probaremos con la edad de 20 años')

age=20

if age>18:
   print('Puedes entrar al concierto de AC/DC')
elif age==18:
     print('No puedes entrar al concierto de AC/DC pero si al de Melendi')
else: 
     print('Con tu edad solo puedes asistir al concierto de Melendi si vas acompañado de un adulto.')

print('Que pase el siguiente')

print('Ahora probemos con 18 años')

age=18

if age>18:
   print('Puedes entrar al concierto de AC/DC')
elif age==18:
     print('No puedes entrar al concierto de AC/DC pero si al de Melendi')
else: 
     print('Con tu edad solo puedes asistir al concierto de Melendi si vas acompañado de un adulto.')

print('Que pase el siguiente')

print('Ahora probemos con 17 años')

age=17

if age>18:
   print('Puedes entrar al concierto de AC/DC')
elif age==18:
     print('No puedes entrar al concierto de AC/DC pero si al de Melendi')
else: 
     print('Con tu edad solo puedes asistir al concierto de Melendi si vas acompañado de un adulto.')

print('Que pase el siguiente')

print('Hagamos un ejemplo mas. Ahora queremos saber si un número dado entre el 1 y el 200 es mutiplo de 7')

numero=int(input('Introduce un numero del 1 al 200:'))

if numero<=200 and numero>=1:
   numero1=numero%7
   if numero1==0:
      print(f'El numero {numero} es multiplo de 7')
   else:
        print(f'El numero {numero} no es multiplo de 7')
else:
     print(f'El número {numero} no está entre 1 y 200')

print('\n2 - Loops')

print("En este apartado haremos algún bucle de ejemplo. En el primer bucle tenemos una cadena con 5 colores, y cambiaremos cada color al blanco. La cadena inicial es: colores=['rojo','azul','verde','amarillo','lila','plateado']")

colores=['rojo','azul','verde','amarillo','lila','plateado']

for i in range(0, 6):
    print(f"El color {i} es {colores[i]}")
    colores[i] = 'blanco'
    print(f"Despues del bucle el color {i} es {colores[i]}")

print("Ahora queremos hacer un bucle el cual, a partir de esta cadena de años: fechas=[1956,1968,1999,2003,2009,2012,2020,2022], imprima los años hasta el año 2009 y nos diga cuantas repeticiones hizo antes de salir del buble.")

fechas=[1956,1968,1999,2003,2009,2012,2020,2022]

i = 0
año = fechas[0]

while(año != 2009):    
    print(año)
    i = i + 1
    año = fechas[i]
print(f"Tomó {i} repeticiones salir del bucle")

print('\n3 - Funciones')

print("Ahora vamos a construir una función que aumente en una cifra el número que queramos")

def sumar1(a):
    """
    Suma 1 al número a
    """
    b = a + 1
    print(f"Si le sumas 1 a {a} es igual a {b}")
    return(b)

print(f"Si ahora ejecutamos nuestra función sumar1(8), veamos que resultado obtenemos:")

sumar1(8)

print(f"Si ponemos el comando help(sumar1) obtenemos la aclaración que nosotros le hayamos colocado a la función. En este caso:")

help(sumar1)

print(f"Ahora vamos a construir una función que multiplique a y b ")

def Mult(a, b):
    """
    Multiplica el número a por b
    """
    c = a * b
    print(f'El resultado es {a}*{b}={c}')
    return(c)
    
    
print(f"Si ahora ejecutamos nuestra función Mult(8,9), veamos que resultado obtenemos:")

Mult(8,9)

print('Ahora vamos a hablar de funciones predeterminadas de python')

print('Definamos la lista L=[10,8,9,7,7,9,9,9]')

L=[10,8,9,7,7,9,9,9]

print(f"La función len(L)={len(L)} nos dice el numero de elementos que hay en la lista")

print(f"La función sum(L)={sum(L)} suma todos los elementos de la lista")

print(f"La función L1=sorted(L) crea una nueva lista con los elementos ordenados")

L1=sorted(L)

print(f"La nueva lista obtenida es L1={L1}")

print(f'En cambio L.sort() ordena la lista L pero no crea una nueva.')

print("Ahora vamos a hacer una función utilizando if, de forma que si el numero es menor que 1 lo eleve al cuadrado pero si el numero es mayor que 1 le sume 4:")

def ecuacion(a):
    if a< 1:
        return (a*a)
    else:
        return (a+4)
    
print(f"Si tomamos a=0.5, obtenemos: {ecuacion(0.5)}")

print(f"Si tomamos a=1.5, obtenemos: {ecuacion(1.5)}")


print('\n3 - Objetos y clases')

print('Para comenzar vamos a crear una clase llamada circulo y meter en ella tres elementos ')

print('Primero definimos el constructor, en el que metemos los atributos de color y radio.')

print('Además también añadiremos dos métodos, uno para dibujar el círculo y otro para añadir una cantidad r al radio.')

import matplotlib.pyplot as plt

class Circle(object):
    
    # Constructor de la clase
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Metodo
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Metodo
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

print("Una vez definido, definiremos los siguientes círculos: C1=Circle(10,'red') y C2=Circle(radious=100) (Se sobreentiende que es azul porque pusimos azul por defecto al definir la clase)")

C1=Circle(10,'red')

C2=Circle(radius=100)

print(f"Veamos si esta bien definido: C1.radius={C1.radius}, C1.color={C1.color}, C2.radius={C2.radius} y C2.color={C2.color}")

print("Podemos cambiar un dato de la siguiente forma: C1.color='green'")

C1.color='green'

print(f"Por tanto ahora tenemos: C1.color={C1.color}")

print("También podemos aumentar el radio con C1.add_radius(10)")

C1.add_radius(10)

print(f"Ahora el radio de C1 es: {C1.radius}")

print("Dibujemos uno de los círculos con: C1.drawCircle()")

C1.drawCircle()











