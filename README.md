# rubik-ai

Problema:
Consiste de un cubo de 3x3 con colores desordenados. La meta es obtener cada cara del cubo de un solo color.

Solución: Para solucionar este problema, proponemos utilizar un método de búsqueda estudiado en clase.

Descripción del ambiente: 
-Totalmente observable
-Determinista
-Secuencial
-Estático
-Discreto
-Agente único

Representación concreta del estado del juego: Un arreglo de 6 matrices de 3x3, una para cada cara del cubo. Al cambiar de estado, cambian los valores dentro de cada matriz.

Descripción de las acciones que puede tomar el agente: Se toma como base una cara concreta del cubo, y en esta se pueden llevar a cabo las siguientes acciones: Up, Down, Right, Left, Front y Back, cuyo objetivo es girar la zona objetivo en el sentido de las agujas del reloj. Todas son acciones discretas.

Representación concreta de las acciones, representada por una estructura de datos: Cada acción está representada por un número: Up, Down, Right, Left, Front, CenterH y CenterV están representadas por 0, 1, 2, 3, 4, 5, 6 y las mismas acciones pero en sentido contrario por 7, 8, 9, 10, 11, 12, 13
