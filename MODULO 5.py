#Module 5 - Working with Numpy Arrays & Simple APIs
print('\n1 - Numpy 1D arrays')

print("En este apartado vamos a hablar de los arreglos en una dimensión, es decir, los vectores")

print("Podemos convertir una lista en un arreglo de Numpy. Generalmente son de tamaño fijo y todos los elementos son del mismo tipo.")

print("Primero importamos: 'import numpy as np'")

import numpy as np

print("Para convertir una lista en un arreglo definimos: 'a=np.array([0,1,2,3,4])'")

a=np.array([0,1,2,3,4])

print(f"El primer elemento de a es: a[0]={a[0]}")

print(f"El cuarto elemento de a es: a[3]={a[3]}")

print(f"Si queremos hallar los 3 primeros elementos: a[0:3]=a[:3]={a[0:3]}")

print(f"Para hallar los 2 últimos: a[3:5]=a[3:]={a[3:]}")

print(f"Si queremos los elementos del primero al tercero pero de dos en dos: a[0:3:2]={a[0:3:2]}")

print(f"Para saber de que tipo es a escribimos: type(a)={type(a)}")

print(f"Para saber el tipo de elementos de a escribimos: a.dtype={a.dtype}")

print(f"Para saber el tamaño de a: a.size={a.size}")

print(f"Para saber la dimensión/rango de a escribimos: a.ndim={a.ndim}")

print(f"Para saber el tamaño de a en cada dimensión escribimos: a.shape={a.shape}")

print("Ahora vamos a definir otro vector: b=np.array([3.1,11.02,6.2,213.4,5.2])}")

b=np.array([3.1,11.02,6.2,213.4,5.2])

print(f"Su tipo es: type(b)={type(b)}")

print(f"El tipo de elementos de b es: b.dtype={b.dtype}")

print("Ahora vamos a continuar con operaciones básicas.")

print("Sean los vectores: u=np.array([0,0,12]) y v=np.array([1,1,6])")

u=np.array([0,0,12])

v=np.array([1,1,6])

print(f"Para sumar los vectores podemos usar el comando: z=u+v={u+v}")

print(f"También podemos usar el comando: z=np.add(u,v)={np.add(u,v)}")

print(f"Para restar los vectores podemos usar el comando: z=u-v={u-v}")

print(f"También podemos usar el comando: z=np.subtract(u,v)={np.subtract(u,v)}")

print(f"Para multiplicar los vectores con el producto de Hadamard (elemento a elemento) podemos usar el comando: z=u*v={u*v}")

print(f"También podemos usar el comando: z=np.multiply(u,v)={np.multiply(u,v)}")

print(f"Para dividir los vectores elemento a elemento podemos usar el comando: z=u/v={u/v}")

print(f"También podemos usar el comando: z=np.divide(u,v)={np.divide(u,v)}")

print(f"Para hacer el producto escalar entre dos vectores usamos el comando: z=np.dot(u,v)={np.dot(u,v)}")

print(f"También podemos sumar una constante a cada elemento z=u+10={u+10}")

print(f"Continuemos con alguna función universal.")

print("Sea el vector c=np.array([1,1,0,-1,3])")

c=np.array([1,1,0,-1,3])

print(f"Calculamos su media con: c.mean()={c.mean()}")

print(f"Calculamos su desviación estandar con: c.std()={c.std()}")

print(f"El valor máximo de c es: c.max()={c.max()}")

print(f"El valor mínimo de c es: c.min()={c.min()}")

print(f"El valor de Pi se expresa como: np.pi={np.pi}")

print("Vamos a representar una función:")

print("Para el eje x, vamos a utilizar el comando np.linspace(a,b,num=c), que divide el intervalo [a,b] en c muestras distribuidas uniformemente.")

print("En este caso tomamos: x=np.linspace(0,2*np.pi,num=100)")

x=np.linspace(0,2*np.pi,num=100)

y=np.sin(x)

print(f"Para el eje y tomamos y=np.sin(x)={y}")

print("Importamos: import matplotlib.pyplot as plt y ejecutamos el comando plt.plot(x,y)")

import matplotlib.pyplot as plt

plt.plot(x,y)

plt.title("Gráfico de y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.show()

print("Finalmente vamos a graficar los vectores u=np.array([1,0]), v=np.array([0,1]) y z = np.add(u, v)  ")

u=np.array([1,0])
v=np.array([0,1])
z = np.add(u, v)

def dibujar_vectores(u, z, v):
    
    # Crear un sistema de ejes
    ax = plt.axes()

    # Dibujar el vector u en rojo con cabeza de flecha
    ax.arrow(0, 0, *u, head_width=0.05, head_length=0.1, color='r')
    plt.text(*(u + 0.1), 'u')  # Etiqueta "u" ligeramente desplazada

    # Dibujar el vector v en azul con cabeza de flecha
    ax.arrow(0, 0, *v, head_width=0.05, head_length=0.1, color='b')
    plt.text(*(v + 0.1), 'v')  # Etiqueta "v" ligeramente desplazada

    # Dibujar el vector z (color por defecto)
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')  # Etiqueta "z" ligeramente desplazada

    # Definir límites de los ejes
    plt.xlim(-0.5, 2)
    plt.ylim(-0.5, 2)

    # Mostrar el gráfico
    plt.title("Representación de vectores en el plano")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal')  # Escala igual en ambos ejes
    plt.show()

dibujar_vectores(u,z,v)

print('\n2 - Numpy 2D arrays')

print("En este apartado vamos a hablar de los arreglos en dos dimensiones, es decir, las matrices")

print("Primero importamos: 'import numpy as np'")

import numpy as np

print("Para convertir una lista en un arreglo, en este caso una matriz, definimos: 'A=np.array([[11,12,13],[21,22,23],[31,32,33]])'")

A=np.array([[11,12,13],[21,22,23],[31,32,33]])

print(f"El elemento de la primera colunma  y de la primera fila de A es: a[0,0]=A[0][0]={A[0,0]}")

print(f"El elemento de la segunda fila y la tercera columna de A es: A[1,2]=A[1][2]={A[1,2]}")

print(f"Si queremos hallar los 2 primeros elementos de la segunda fila: A[1,0:2]={A[1,0:2]}")

print(f"Para hallar los 2 últimos elementos de la tercera columna : A[1:3,2]={A[1:3,2]}")

print(f"Para saber de que tipo es A escribimos: type(A)={type(A)}")

print(f"Para saber el tipo de elementos de A escribimos: A.dtype={A.dtype}")

print(f"Para saber el tamaño de A: A.size={A.size}")

print(f"Para saber la dimensión/rango de A escribimos: A.ndim={A.ndim}")

print(f"Cabe destacar que aquí el rango de A no se refiere al número de columnas linealmente independientes de A, si no el número de listas anidadas, por eso en este caso es 2")

print(f"Para saber el tamaño de A en cada dimensión escribimos: A.shape={A.shape}")

print("Vamos a hacer un ejemplo de un arreglo de dimensión 3 para ver la diferencia: B=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])}")

B=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])

print(f"Su tipo es: type(B)={type(B)}")

print(f"El tamaño de B es: B.size={B.size}")

print(f"La dimensión/rango de B es: B.ndim={B.ndim}")

print(f"El tamaño de B en cada dimensión es: B.shape={B.shape}")

print("Ahora vamos a continuar con operaciones básicas.")

print("Sean las matrices: X=np.array([[1,0],[0,1]]) y Y=np.array([[2,1],[1,2]])")

X=np.array([[1,0],[0,1]])

Y=np.array([[2,1],[1,2]])

print("Usaremos .tolist() para que la matriz salga en la misma linea y no en dos.")

print(f"Para sumar las matrices usamos el comando: Z=(X+Y).tolist()={(X+Y).tolist()}")

print(f"Para restar las matrices usamos el comando: Z=(X-Y).tolist()=(X-Y).tolist()")

print(f"Para multiplicar las matrices con el producto de Hadamard (elemento a elemento) usamos el comando: Z=(X*Y).tolist()={(X*Y).tolist()}")

print(f"Para dividir los vectores elemento a elemento usamos el comando: Z=(X/Y).tolist()={(X/Y).tolist()}")

Z=np.dot(X,Y)

print(f"Para hacer el producto matricial usamos el comando: Z=np.dot(X,Y)={Z.tolist()}")

print("Cabe destacar que para poder multiplicar dos matrices, el número de columnas de la primera matriz debe de ser igual al número de filas de la segunda, es decir, se puede multiplicar una matriz 3x2 por una 2x4 (resultando una 3x4), pero no se puede multiplicar una matriz 2x4 por una 3x2")

print(f"También podemos sumar una constante a cada elemento Z=(X+10).tolist()={(X+10).tolist()}")

Z=Y.T

print(f"Para hallar ma matriz traspuesta de la martriz Y: Z=Y.T={Z.tolist()}")


print('\n3.1 - Simple APIs PARTE 1')

print("Los APIs son Interfaces de Programación de Aplicaciones")

import pandas as pd

print("Vamos a crear un diccionario y convertirlo a DataFrame, es decir, los datos del diccionario se pasan al API de pandas")

print("Nuestro diccionario es: dic_={'a':[11,21,31], 'b':[12,22,32]}")

dic_={'a':[11,21,31], 'b':[12,22,32]}

print("Ahora lo pasamos a DataFrame: df=pd.DataFrame(dic_)")

df=pd.DataFrame(dic_)

print("Cuando llamamos al método .head(), el DataFrame se comunica con la API y devuelve:")

print(df.head())

print("Del mismo modo, cuando llamamos a .mean(), la API calcula la media y devuelve: ")

print(df.mean())

print("Los REST APIs te permiten comunicarte a través de internet, sus siglas significan: REpresentational State Transfer.")

print("Por ejemplo, los datos deportivos siempre están cambiando. Esta es una excelente aplicación de una API ya que puede ser actualizada constantemente.")

print("Usaremos la API de la NBA de Swar Patel")

print("Tenemos que ejecutar: from nba_api.stats.static import teams. Si no tenemos el paquete necesario tendremos que instalarlo.")

from nba_api.stats.static import teams

print("Usamos el comando: nba_teams=teams.get_teams() que devuelve una lista de los diccionarios con los datos")

nba_teams=teams.get_teams()

print("Veamos sus 5 primeros elementos con nba_teams[:5]")

print(nba_teams[:5])

print("A continuación definiremos una función para convertir una lista de diccionarios en un único diccionario de listas llamada one_dict")

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key,value in dict_.items():
            out_dict[key].append(value)
    return out_dict

print("Definimos el diccionario a partir de la función: dict_nba_team=one_dict(nba_teams) y lo pasamos a DataFrame")

dict_nba_team=one_dict(nba_teams)

df_teams=pd.DataFrame(dict_nba_team)

print("Ahora mostramos los 5 primeros elementos con df_teams.head():")

print(df_teams.head())

print("Ahora cogemos solo los datos de los Warriors con df_warriors=df_teams[df_teams['nickname']=='Warriors']")

df_warriors=df_teams[df_teams['nickname']=='Warriors']

print(df_warriors)

print("Y de ahí sacamos su id que es único: id_warriors=df_warriors[['id']].values[0][0]")

id_warriors=df_warriors[['id']].values[0][0]

print(f"El ID de los warriors es id_warriors={id_warriors}")

print("Ahora tenemos que ejecutar: from nba_api.stats.endpoints import leaguegamefinder")

from nba_api.stats.endpoints import leaguegamefinder

print("Ahora utilizamos el comando gamefinder=leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors) y games=gamefinder.get_data_frames()[0]")

gamefinder=leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

games=gamefinder.get_data_frames()[0]

print("Finalmente, utilizamos head() y la ultima columna es el resultado de los partidos, es decir, si es negativo es la diferencia de puntos por los que han perdido y si es positivo la diferencia de puntos por los que han ganado.")

print(games.head())

print("Además, si pone vs. es que el partido fue en casa y si pone @ es que jugaron en el campo del equipo contrario. Esto no aparece con el head() porque solo muestra algunas colunmas ya que son demasiadas.")

print("Ahora voy a hacer una gráfica con los resultados en casa y fuera, y comprobaremos que los Warriors obtienen mejores resultados cuando juegan en casa.")

games_home=games[games['MATCHUP']=='GSW vs. TOR']

games_away=games[games['MATCHUP']=='GSW @ TOR']

import matplotlib.pyplot as plt

fig,ax=plt.subplots()

games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)

games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)

ax.legend(['away','home'])

plt.show()

print('\n3.2 - Simple APIs PARTE 2\n')

print("Hablaremos sobre APIs que utilizan algún tipo de inteligencia artificial.")
print("Transcribiremos un archivo de audio utilizando la API de Watson Speech to Text y luego traduciremos el texto a un nuevo idioma utilizando la API de Watson Language Translator.\n")
print("TODO ESTE APARTADO ESTA EN FORMA DE COMENTARIOS. Debido  que cada individuo debe registrarse y conseguir su propio url y su propia clave para poder utilizarlo.")

# Importamos las librerías necesarias de IBM Watson y autenticación
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# ***********************
# CONFIGURACIÓN - Rellena estos valores con tus datos personales de IBM Cloud
# ***********************

# URL y API key del servicio Speech to Text
#url_s2t = 'TU_URL_SPEECH_TO_TEXT'  # Ejemplo: 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/xxxxx'
#apikey_s2t = 'TU_API_KEY_SPEECH_TO_TEXT'

#print("IMPORTANTE: Cambia 'TU_URL_SPEECH_TO_TEXT' y 'TU_API_KEY_SPEECH_TO_TEXT' por tus credenciales reales.\n")

# Configuramos el autenticador para Speech to Text
#authenticator_s2t = IAMAuthenticator(apikey_s2t)
#s2t = SpeechToTextV1(authenticator=authenticator_s2t)
#s2t.set_service_url(url_s2t)

# Nombre del archivo de audio que vamos a transcribir (debe estar en la misma carpeta que este script)
#filename = 'hello_this_is_python.wav'

# Abrimos el archivo y hacemos la solicitud a la API para transcribir el audio
#with open(filename, mode='rb') as wav:
     #response = s2t.recognize(audio=wav, content_type='audio/wav')

# Obtenemos el texto reconocido del resultado
#recognized_text = response.result['results'][0]['alternatives'][0]['transcript']
#print("Texto reconocido del audio:\n", recognized_text, "\n")

# ***********************
# CONFIGURACIÓN - Rellena estos valores con tus datos personales del servicio Language Translator
# ***********************

#from ibm_watson.language_translator_v3 import LanguageTranslatorV3


# URL y API key del servicio Language Translator
#url_lt = 'TU_URL_LANGUAGE_TRANSLATOR'  # Ejemplo: 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/xxxxx'
#apikey_lt = 'TU_API_KEY_LANGUAGE_TRANSLATOR'

#print("IMPORTANTE: Cambia 'TU_URL_LANGUAGE_TRANSLATOR' y 'TU_API_KEY_LANGUAGE_TRANSLATOR' por tus credenciales reales.\n")

# Configuramos el autenticador para Language Translator
#authenticator_lt = IAMAuthenticator(apikey_lt)
#language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator_lt)
#language_translator.set_service_url(url_lt)

# Listamos los idiomas disponibles para traducción (opcional)
#print("Idiomas disponibles en el traductor:")
#print(language_translator.list_identifiable_languages().get_result(), "\n")

# Traducimos el texto reconocido del inglés al español
#translation_response = language_translator.translate(text=recognized_text,model_id='en-es')  # De inglés a español

# Obtenemos la traducción
#translation = translation_response.get_result()
#spanish_translation = translation['translations'][0]['translation']
#print("Traducción al español:\n", spanish_translation)







