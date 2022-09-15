# Apocalipsis zombie

## TechSummit Idealista
Planteamiento del reto para el TechSummit

---
## Introducción
Es el año 2222 y lo que parecía de ciencia ficción y propio de videojuegos o la serie Walking Dead se ha vuelto realidad: **el apocalipsis zombie ha comenzado!** En esta nueva normalidad es común tener que enfrentarse a zombies a diario para ir a comprar el pan y digamos que programar ya no es una de tus prioridades. En realidad no has tenido más remedio que volverte un guerrero y utilizar cualquier cosa que parezca un arma para abrirte camino entre los muertos vivientes.

En este mundo infectado solo tenemos una opción: sobrevivir! 

## Reto
Dada la descripción de un escenario (mapa, supervivientes, zombies, equipamiento, etc...) y las acciones que tienen lugar en él (mover, atacar, equipar, etc), indica cual es el estado final de ese escenario. 

## Descripción del problema 

Cada escenario está definido por
- Mapa
  - un mapa sobre el que se sitúan supervivientes, zombies y equipación 
  - el mapa siempre tiene forma cuadrada, por ejemplo 5 celdas de largo por 5 celdas de ancho
  - ni los supervivientes ni los zombies pueden salir de los limites del mapa 
  - *Nota*: La coordenada 0 0 es la esquina superior izquierda del mapa

- Supervivientes
  - tienen un nombre único
  - tienen un valor inicial de vida
  - tienen un valor inicial de experiencia
  - pueden llevar con ellos hasta 5 elementos de equipación, uno en cada mano y el resto en la mochila
  - se encuentran siempre en alguna coordenada del mapa

- Zombies
  - tienen un nombre único
  - tienen solo un punto de vida, si son atacados con éxito mueren inmediatamente
  - se encuentran siempre en alguna coordenada del mapa

- Equipamiento
  - sirven para atacar a los zombies
  - los hay tanto de corto como largo alcance
  - solo puede haber un objeto de cada tipo en el escenario, no se repiten
  - algunos afortunados supervivientes tendrán la suerte de estar equipados en el momento de inicio del escenario
  - para los menos afortunados, también hay equipamiento distribuido por el mapa

Los supervivientes pueden atacar a los zombies con diferentes armas. Aun así, como no todos somos guerreros por naturaleza, a veces esos ataques no son exitosos. Si el ataque no es exitoso, el zombie no muere. 

Por otro lado, los zombies aun cuando no son muy ágiles y no pueden usar armas no perderán nunca una oportunidad para llevarte a su club. Así que si hay algún zombie cerca de un superviviente siempre lo intentará morder. 

Consideramos que hemos ganado la batalla si ya no hay zombies vivos en el escenario. De lo contrario, si al final del escenario ya no hay supervivientes, hemos perdido. 

## Formato de fichero de entrada
El fichero que define cada escenario se porporciona en un archivo de texto plano. El
archivo sólo contiene caracteres ASCII y las líneas terminan con un único carácter
"\n" (también llamado final de línea "estilo UNIX"). Cuando hay varios números
en una línea, se separan con un solo espacio entre cada dos números. 

El archivo de entrada tendrá el siguiente formato:
```
# Definición general de los elementos del escenario (bloques de información)
# Definición de supervivientes
# Definición de zombies
# Definición de items en el mapa
# Definición de instrucciones a ejecutar
```

#### Definición general de los elementos del escenario

La primera línea del fichero contiene cinco números que describen de forma general el escenario (numero de zombies, tamaño del mapa, etc)
```
S Z I M C

# S = Número de supervivientes
# Z = Número de zombies
# I = Número de items presentes en el mapa 
# M = Tamaño del lado del mapa (cuadrado)
# C = Número de instrucciones a ejecutar

```

#### Definición de supervivientes

Después, siguiente bloque define a los supervivientes y el equipo que cargan. 

Los supervivientes están definidos por 
- una primera línea obligatoria que define el nombre, la vida inicial, el nivel de experiencia, etc.
- si el superviviente tiene items equipados, habrá una línea más por cada item que tenga el superviviente. 

*Si el superviviente tiene dos items equipados habrá una primera linea que lo define y luego dos lineas más que especifican los items.*

```
V Ex Eq X Y N

# V = Vida inicial
# Ex = Puntos de experiencia iniciales
# Eq = Número de items equipados iniciales
# X = Coordenada X
# Y = Coordenada Y
# N = Nombre
```

```
I S

# I = Nombre del item
# S = Hueco en el que el superviviente tiene el Item
```

#### Definición de zombie
Después, el fichero contiene Z lineas con el siguiente formato que definen a cada zombie:
```
N X Y

# N = Nombre de zombi
# X = Coordenada X
# Y = Coordenada Y
```

#### Definición de item
Después, el fichero contiene I lineas  con el siguiente formato que definen a los items distribuidos por el mapa:
```
N X Y

# N = Nombre item
# X = Coordenada X
# Y = Coordenada Y
```


#### Ejemplo de fichero de entrada
```
3 1 3 6 1            	# S=3 supervivientes, Z=1 zombie, I=3 item, M=mapa de lado 6 y C=1 instrucciones
2 0 1 0 1 Bart       	# Superviviente N=Bart, V=2 de vida, Ex=0 experiencia, Eq=1 items equipados y está en la coordenada (X=0, Y=1)
RubberDuck RightHand 	# Item de Bart, I=RubberDuck equipado en S=mano derecha
2 0 1 5 2 Lisa       	# Superviviente N=Lisa, V=2 de vida, Ex=0 experiencia, Eq=1 item equipados y está en la coordenada (X=5, Y=2)
BaseballBat LeftHand 	# Item de Lisa, I=BaseballBat equipado en S=mano izquierda
2 0 1 0 5 Burns       # Superviviente N=Burns, V=5 de vida, Ex=0 experiencia, Eq=0 item equipados y está en la coordenada (X=0, Y=5)
Zombicillo 2 0       	# Zombie N=Zombicillo, está en la coordenada (X=2, Y=0)
ZombiLoco 1 4       	# Zombie N=ZombiLoco, está en la coordenada (X=1, Y=4)
ZombiVaquero 4 3      # Zombie N=ZombiVaquero, está en la coordenada (X=4, Y=3)
Knife 2 2            	# Item N=Knife en el suelo en la coordenada (X=2, Y=2)
Molotov 0 3           # Item N=Molotov en el suelo en la coordenada (X=0, Y=3)
Flamethrower 4 1      # Item N=Flamethrower en el suelo en la coordenada (X=4, Y=1)
M Bart Up            	# Instrucción a ejecutar
```

La última línea de este ejemplo contiene una instrucción de [Movimiento](###Movimiento) descrita más adelante.

El archivo representa este escenario:
![Ejemplo](Images/example.png)

*Se trata solo de una representación del escenario. La implementación gráfica no tiene porque ser igual a esta.*
### Salida del software: estado final del escenario
El software debe generar un log que describa el estado final del escenario tras ejecutar todos los comandos del fichero de entrada.

Este archivo debe tener el siguiente formato:
```
# (1) Definición general de los elementos del escenario (bloques de información) 
# (2) Definición de supervivientes
# (3) Definición de zombies
# (4) Definición de items en el mapa
# (5) Definición de instrucciones ejecutadas (eliminando cualquier instrucción que no tuviese efecto)
# (6) Resultado de la partida
```

Cada uno de los bloques 1 - 5 tiene la misma estructura interna que la del fichero de entrada. El bloque 6 se define a continuación.

#### Resultado de la partida
El resultado de la partida viene definido por una línea con el siguiente formato:
```
R

R=Resultado puede ser W (won), L (lost) o R (running)

```

#### Ejemplo log del estado final del escenario

```
# Entrada:
2 0 1 3 2     
2 0 0 0 1 Bart 
Knife Backpack
2 0 1 0 0 Lisa
BaseballBat LeftHand
A Bart Zombicillo Knife 1
A Lisa Zombicillo BaseballBat 1
```

```
# Log:
2 0 1 3 2     
2 0 0 0 1 Bart 
Knife Backpack
2 0 1 0 0 Lisa
BaseballBat LeftHand
A Lisa Zombicillo BaseballBat 1
W 
```


*Nota*: La coordenada 0 0 es la esquina superior izquierda del mapa.



## Definición de instrucciones
### Movimiento
Todos los personajes, tanto supervivientes como zombies, pueden moverse una casilla con esta instrucción. 

La instrucción está definida por una línea con el siguiente formato:
```
M P D  

# M = movimiento
# P = Personaje
# D = Dirección
```

**Ejemplo de entrada:** 
```
2 1 0 3 2     
2 0 0 0 1 Bart 
2 0 0 0 0 Lisa
Zombicillo 2 0
M Bart Up
M Lisa Right
M Zombicillo Left
```

### Recoger equipamiento
Los supervivientes pueden recoger un item siguiendo las siguientes reglas:
- Pueden llevar items en los siguientes "huecos": `LeftHand`, `RightHand` y `Backpack`
- La mochila puede llevar 3 items
- Si el superviviente recoge algo para la mochila y esta está llena, la instrucción no tiene efecto.
- *Bola extra:* Si el superviviente recoge algo con una mano y ya tiene algo en esa mano, lo que está sosteniendo actualmente pasa a la mochila si es posible. Si no, la instrucción no tiene efecto

La instrucción está definida por una línea con el siguiente formato:
```
P S I Sl 

# P = Recoger
# S = Superviviente
# I = Item
# Sl = Hueco
```

**Ejemplo de entrada:**
```
2 1 1 3 2     
2 0 0 0 1 Bart 
2 0 0 0 0 Lisa
Zombicillo 2 0
BaseballBat 0 0
P Lisa BaseballBat LeftHand 
```


## Mover Equipamiento
Los supervivientes pueden cambiar donde llevan guardado su equipamiento o incluso soltarlo siguiendo las siguientes reglas:
- Los destinos válidos son "huecos" (`LeftHand`, `RightHand`, `Backpack`) o el suelo (`Floor`)
- El superviviente tiene que tener ese item, si no, la instrucción no tiene efecto
- El destino debe tener capacidad para el objeto (esto es, no tener ya ningún objeto en caso de `LeftHand` y `RightHand` o tener menos de 3 objetos en el caso de `Backpack`) En caso contrario, la instrucción no tiene efecto 
- Los items siempre pueden moverse a `Floor` (independientemente de que ya haya algo)

La instrucción está definida por una línea con el siguiente formato:
```
R S I T 

# R = Mover equipamiento
# S = Superviviente
# I = item
# T = Destino del equipamiento
```

**Ejemplo de entrada:**
```
2 1 0 3 2     
2 0 0 0 1 Bart 
2 0 1 0 0 Lisa
BaseballBat LeftHand
Zombicillo 2 0
R Lisa BaseballBat Backpack
```

## Atacar
Todos los personajes tienen la capacidad de atacar siguiendo las siguientes reglas:
- Las armas usadas por los supervivientes pueden ser los items: `BaseballBat`, `RubberDuck`, `Katana`, `Knife`, `Handgun`, `Molotov`, `Flamethrower`, `Machete` o `Bow`
- El arma usada por los zombies siempre es `Bite`
- Los supervivientes pueden atacar con las siguientes armas si están en la misma casilla que el zombie objetivo: `BaseballBat`, `Katana`, `Knife`, `Machete`, `RubberDuck`
- `RubberDuck` no hace daño al zombie pero hace un ruido gracioso 
- Los supervivientes pueden atacar desde 1 casilla de distancia usando el arma `Handgun` y `RubberDuck` 
- Los supervivientes pueden atacar desde 2 casillas de distancia usando el arma `Molotov`
- Los supervivientes pueden atacar desde 3 casillas de distancia usando el arma `Bow`
- Las armas `Handgun`, `Molotov`, `Flamethrower` y `Bow` no pueden usarse para atacar a zombies en la misma casilla que el superviviente, en caso de hacerlo, la instrucción no tiene efecto
- Los supervivientes tienen que tener el arma en una de las manos para poder atacar con la misma, si no la instrucción no tiene efecto 
- Cada zombi muerto aumenta en 1 la experiencia
- Cuando un superviviente recibe un ataque, pierde 1 punto de vida
- Si la vida del superviviente es 0, muere y todas las instrucciones que le afecten, no tienen efecto. Además el superviviente no pierde su equipo y este no pasa al suelo, por lo que no puede ser recogido por otros supervivientes que estén en la misma casilla.
- *Bola Extra*: Algunas armas se destruyen tras un número de usos, tras ese número de ataques se eliminan del equipamiento del jugador: 
	- `BaseballBat` 1
	- `Knife` 2
	- `Katana` 3
	
La instrucción está definida por una línea con el siguiente formato:
```
A P1 P2 W R 


# A = Atacar
# P1 = Personaje que realiza el ataque
# P2 = Personaje que recibe el ataque
# W = arma usada
# R = Si el ataque surte efecto o no
```

**Ejemplo de entrada de ataque en misma casilla:**
```
2 1 0 3 2     
2 0 0 0 1 Bart 
2 0 1 0 0 Lisa
BaseballBat LeftHand
Zombicillo 0 0
A Lisa Zombicillo BaseballBat 1
```

**Ejemplo de entrada de ataque a distancia:**
```
2 1 0 3 2     
2 0 0 0 1 Bart 
2 0 1 0 0 Lisa
Handgun LeftHand
Zombicillo 1 0
A Lisa Zombicillo Handgun 1
```

**Ejemplo de entrada de ataque de zombie**
```
2 1 0 3 2     
2 0 0 0 1 Bart 
2 0 1 0 0 Lisa
Zombicillo 0 0
A Zombicillo Lisa Bite 1
```

## Ganar y perder la partida
Si todos los zombies han muerto, los supervivientes ganan la partida inmediatamente. Si todos los supervivientes han muerto, los supervivientes pierden la partida.

**Ejemplo de entrada de partida ganada**: 
```
2 1 0 3 2     
2 0 0 0 1 Bart 
2 0 1 0 0 Lisa
BaseballBat LeftHand
Zombicillo 0 0
A Lisa Zombicillo BaseballBat 1
```

**Ejemplo de entrada de partida perdida**: 
```
1 1 0 3 2     
1 0 1 0 0 Lisa
Zombicillo 0 0
A Zombicillo Lisa Bite 1
```

## Assets
- Zombie free icons designed by Smashicons https://www.flaticon.com/free-icon/zombie_3636891 a través de @flaticon 
- Survivors free icon designed by Freepik https://www.flaticon.com/free-icon/shopkeeper_3194579?term=shopkeeper a través de @flaticon 
- Equipment free icons designed by smalllikeart https://www.flaticon.com/free-icon/baseball-bat_1256792 a través de @flaticon 
- Tiles images have been designed using images from Freepik.com https://www.freepik.com/free-vector/textures-stone-floor-wall-with-green-moss-game-background-vector-cartoon-seamless-patterns-top-view-pavement-with-grass-cobblestones-granite-blocks_23592761.htm#query=ground%20tile&position=41&from_view=search 
