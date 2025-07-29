#MODULO 2: PYTHON DATA STRUCTURES
print('\n1 - Listas y tuplas')
print('Las duplas y las listas son ordenadas, a diferencia de que las tupas son inmutables pero las listas se pueden modificar.')
print('Comenzaremos hablando de las tuplas')

print("Definimos una tupla de la siguiente forma: Tuple=('disco',10,1.2)")

Tuple=('disco',10,1.2)
print(f'El primer elemento de la tupla es:Tuple[0]={Tuple[0]}' )
print(f'Otra forma de calcularlo con indice negativo:Tuple[-3]={Tuple[-3]}')

print(f'El segundo elemento de la tupla es:Tuple[1]={Tuple[1]}' )
print(f'Otra forma de calcularlo con indice negativo:Tuple[-2]={Tuple[-2]}')

print(f'El tercer elemento de la tupla es:Tuple[2]={Tuple[2]}' )
print(f'Otra forma de calcularlo con indice negativo:Tuple[-1]={Tuple[-1]}')

print("Para concatenar una tupla usamos +: Tuple2=Tuple+('metal',10)")

Tuple2=Tuple+('metal',10) 

print(f'Por tanto hemos definido la tupla: Tuple2={Tuple2}')

print('Recordemos que las tuplas son inmutables, por tanto si queremos modificar una solo podemos crear una nueva')

print(f'Para calcular los 3 primeros elementos de una tupla Tuple2[0:3]={Tuple2[0:3]}')

print(f'Para calcular los restantes Tuple2[3:]={Tuple2[3:]}')

print(f'Definimos una tupla cin cifras: Ratings=(10,9,6,5,10,8,9,6,2)')
Ratings=(10,9,6,5,10,8,9,6,2)

print('Para ordenarla usamos el comando sorted ')

Ratings2=sorted(Ratings)
print(f'La lista rodenada obtenida es: Ratings2={Ratings2}')

print('Ahora vamos a definir una tupla conteniendo otras tuplas, a esto se le llama anidamiento')

NT=(1,2,('metal','pop'),(3,4),('disco',(1,2)))

print(f'La dupla definida es: NT={NT}')

print(f'Hallemos el elemento 3 de la tupla NT: NT[2]={NT[2]}')

print(f'Hallemos el elemento 1 del elemento 3 de la tupla NT: NT[2][0]={NT[2][0]}')

print(f'Hallemos el elemento 3 del elemento 1 del elemento 3 de la tupla NT: NT[2][0][2]={NT[2][0][2]}')


print('Continuaremos hablando sobre las listas')

print("Definimos una lista de la siguiente forma: Lista=['tomate',1090,4]")

Lista=['tomate',1090,4]

print(f'El primer elemento de la lista es:Lista[0]={Lista[0]}' )
print(f'Otra forma de calcularlo con indice negativo:Lista[-3]={Lista[-3]}')

print(f'El segundo elemento de la lista es:Lista[1]={Lista[1]}' )
print(f'Otra forma de calcularlo con indice negativo:Lista[-2]={Lista[-2]}')

print(f'El tercer elemento de la lista es:Lista[2]={Lista[2]}' )
print(f'Otra forma de calcularlo con indice negativo:Lista[-1]={Lista[-1]}')

print("Para concatenar una lista usamos +: Lista2=Lista+['pop',1.8]")

Lista2=Lista+['pop',1.8] 

print(f'Por tanto hemos definido la lista: Lista2={Lista2}')

print('Recordemos que las listas se pueden modificar')

print(f"En este caso añadimos elementos a la lista original, no creamos una nueva: Lista.extend(['pop',1.8]")

Lista.extend(['pop',1.8])

print(f'El resultado obtenido es Lista={Lista}')

print(f"Para cambiar un elemento usamos el comando Lista[1]='rock'")

Lista[1]='rock'

print(f'El resultado obtenido es Lista={Lista}')

print(f'Para eliminar un elemento de una lista utilizamos el comando del(Lista[0])')

del(Lista[0])

print(f'El resultado obtenido es Lista={Lista}')

print(f"Para generar una lista a partir de una cadena escribimos: 'hard rock'.split(), cuyo resultado es {'hard rock'.split()}")

print(f"En caso de una cadena separada por comas, escribimos 'A,B,C,D'.split(','), cuyo resultado es: {'A,B,C,D'.split(',')}")

print(f'Vamos ahora a definir la lista A=[0,1,2]')

A=[0,1,2]

print('Si definimos la lista B en funcion de A, es decir, B=A, todo cambio que le apliques a A también le afectará a B')

B=A

print('Vamos a eliminar el primer elemento de A con el comando del(A[0])')
del(A[0])
print(f'Entonces tenemos que A={A} y B={B}')
print('Definimos A nuevamente como: A=[0,1,2] ')
A=[0,1,2]

print(f'Si en cambio definimos C de la siguiente forma: C=A[:], creamos una copia de A pero funcionan de manera independiente')

C=A[:]

print('Vamos a eliminar el primer elemento de A con el comando del(A[0]) y ver que sucede')
del(A[0])

print(f'Entonces tenemos que A={A} y C={C}')

print('\n2 - Sets')

print('Los sets son conjuntos no ordenados que se definen mediante llaves {}')
 
print("Definimos el set de la siguiente forma: Set1={'pop','rock','rock','disco','disco'}")

Set1={'pop','rock','rock','disco','disco'}

print(f"Vease que las listas tienen elementos únicos, los repetidos se omiten: Set1={Set1}")

print("Definimos la lista Lista=['pop', 10, 10, 322]" )
Lista=['pop', 10, 10, 322]

print(f'Podemos pasar la lista a un set con el comando set(Lista)={set(Lista)} (Vease que los elementos repetidos se omiten)')

print(f"Ahora vamos a añadir un elemento al set Set1 con el comando: Set1.add('soul')")

Set1.add('soul')

print(f'El resultado es Set1={Set1}')

print(f'Añadamos otra vez el mismo elemento para ver que no varia:')

Set1.add('soul')

print(f"El resultado de añadir dos veces 'soul' es: Set1={Set1}")

print(f"Para eliminar un elemento del set Set1 usamos el comando: Set1.remove('rock')")

Set1.remove('rock')

print(f"El resultado de eliminar 'rock' es: Set1={Set1}")

print(f"Para ver si un elemento está en una lista usamos el comando 'rock' in Set1={'rock' in Set1}")

print('Si el resultado es False, el elemento no está en el set, si es True, el elemento está en el set')

print("Ahora definimos los siguientes sets: Album_set1={'AC/DC','BACK IN BLACK','THRILLER'} y Album_set2={'AC/DC','BACK IN BLACK','NSYNC'}")

Album_set1={'AC/DC','BACK IN BLACK','THRILLER'}
Album_set2={'AC/DC','BACK IN BLACK','NSYNC'}

print(f"Para calcular su intersección usamos &: Album_set3=Album_set1 & Album_set2")

Album_set3=Album_set1 & Album_set2

print(f'El resultado es: Album_set3={Album_set3}')

print(f"Para calcular su unión usamos: Album_set4=Album_set1.union(Album_set2)")

Album_set4=Album_set1.union(Album_set2)

print(f'El resultado es Album_set4={Album_set4}')

print('Para ver si un set está dentro de otro usamos: Album_set3.issubset(Album_set1)')

Album_set3.issubset(Album_set1)

print(f'El resultado es: {Album_set3.issubset(Album_set1)}')

print('Para ver si un set contiene a otro usamos: Album_set3.issuperset(Album_set1)')

Album_set3.issuperset(Album_set1)

print(f'El resultado es: {Album_set3.issuperset(Album_set1)}')


print('\n3 - Dictionaries')
print('Una lista tiene índices y elementos, un diccionario tiene claves y valores.')

print('Para definirlos usamos llaves. Las claves son inmutables y únicas mientras que los valores pueden ser inmutables, mutables o duplicados.')

print("La forma de definir un diccionario es la siguiente: DIC={'THRILLER':1982,'BACK IN BLACK':1980, 'THE DARK SIDE OF THE MOON':1973,'THE BODYGUARD':1992, 'BAT OF HELL':1977}")

DIC={'THRILLER':1982,'BACK IN BLACK':1980, 'THE DARK SIDE OF THE MOON':1973,'THE BODYGUARD':1992, 'BAT OF HELL':1977}

print(f'El resultado es: DIC={DIC}')

print(f"Para encontrar un valor a partir de una clave escribimos DIC['THE BODYGUARD']={DIC['THE BODYGUARD']} ")

print(f"Para añadir una nueva entrada al diccionario: DIC['GRADUATION']='2007'")

DIC['GRADUATION']='2007'

print(f'El resultado es DIC={DIC}')

print(f"Para eliminar una entrada del diccionario: del(DIC['THRILLER'])")

nombre = input("Introduce tu nombre: ")
print("Hola,", nombre)

del(DIC['THRILLER'])

print(f'Ahora tenemos: DIC={DIC}')

print(f"Para saber todas las claves: DIC.keys()={DIC.keys()}")

print(f"Finalmente, para saber todos los valores: DIC.values()={DIC.values()}")






