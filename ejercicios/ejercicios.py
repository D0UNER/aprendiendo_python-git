# Ejercicio 1:
# Declara una variable edad con un número entero y una variable precio con un número flotante.
# Mostralas por pantalla.

edad_1 = 20
precio_1 = 15.99

print('Ejercicio 1: ', edad_1, precio_1)

# Ejercicio 2
# Guardá tu nombre en una variable tipo string y mostrá:
# "Hola, mi nombre es <tu_nombre>".

minombre = 'Lucas'
mensaje = f'Hola, mi nombre es {minombre}'
print('Ejercicio 2: ', mensaje)

# Ejercicio 3
# Convertí una edad que está en texto

edad_2 = '19'
int(edad_2)

print('Ejercicio 3: ', edad_2)

# Ejercicio 4
# Crea una lista con 5 números.
# Mostrá el primer y el último.

lista = [40, 23, 70, 15, 37]
print('Ejercicio 4: ', lista[0], lista[4])

# Ejercicio 5
# Agregá un nuevo número a la lista anterior y eliminá el segundo.

lista.insert(3, 54)
lista.pop(1)
print('Ejercicio 5: ', lista)

# Ejercicio 6
# Crea una tupla con 3 colores.
# Mostrá el color del medio.

tupla = ('rojo', 'verde', 'azul')
print('Ejercicio 6: ', tupla[1])

# Ejercicio 7
# Creá tres variables: a = 3, b = 4, c = 5.
# Luego intercambiá los valores de a y b sin usar una variable temporal.

a = 3
b = 4
c = 5

a, b = b, a

print('Ejercicio 7: ', a, b)

# Ejercicio 8
# Crea una variable nombre, asignale un valor, reasignale otro distinto y mostrá ambos valores antes y después.

nombre_2 = 'manolo'
print('Ejercicio 8: ', nombre_2)
nombre_2 = 'julio'
print('Ejercicio 8: ', nombre_2)

# Ejercicio 9
# Pedile al usuario dos números (usar input) y mostrale:

# suma
# resta
# multiplicación
# división
# potencia (a ** b)

numero_1 = int(input('Escribe tu primer numero: '))
numero_2 = int(input('Escribe tu segundo numero: '))

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2
potencia = numero_1 ** numero_2

print('Ejercicio 9: ', suma, resta, multiplicacion, division, potencia)

# Ejercicio 10
# Con una variable radio = 7, calculá el área de un círculo:

radio = 7
area = 3.14159 * radio ** 2

print('Ejercicio 10:', area)

# Ejercicio 11
# Pedile al usuario su edad como número.
# Mostrá si es mayor o menor de edad usando ==, !=, <, >=.

edad_3 = int(input('Cual es tu edad: '))

if edad_3 >= 18:
    print('Ejercicio 11: Sos mayor de edad')
else:
    print('Ejercicio 11: Sos menor de edad')

# Ejercicio 12
# Dadas dos variables: x = 10 y = 20
# Mostrá:
# si son iguales
# si x es menor que y
# si y es distinto de 30

x = 10
y = 20

print('Ejercicio 12: ', x == y, x < y, y != 30)

# Ejercicio 13
# Pedile al usuario un número.
# Mostrá si está entre 1 y 10:

numero_3 = int(input('Escribe un numero aleatorio: '))

if 10 >= numero_3 >= 1:
    print('Ejercicio 13: ', 'Tu numero esta entre 1 y 10')
else:
    print('Ejercicio 13: ', 'Tu numero no esta dentro de 1 y 10')

# Ejercicio 14
# Dadas:
# llueve = True
# tengo_paraguas = False
# Mostrá si podés salir sin mojarte usando operadores and y or.

llueve = True
tengo_paraguas = True

if llueve == False:
    print('Ejercicio 14: No esta lloviendo')
elif llueve and tengo_paraguas:
    print('''Ejercicio 14:
    ¿Puedo salir sin mojarme?: si''')
else:
    print('''Ejercicio 14:
    No tienes paraguas''')

# Ejercicio 15
# Pedile al usuario una contraseña.
# Si la contraseña es "python123", mostrá “Acceso permitido”, si no “Acceso denegado”.

contraseña = input('Ingresa tu contraseña: ')
if contraseña == 'python123':
    print('Ejercicio 15: Acceso permitido')
else:
    print('Ejercicio 15: Acceso denegado')

# Ejercicio 16
# Pedile al usuario un número y mostrale si es positivo, negativo o cero.

numero_4 = int(input('Ingresa tu numero: '))

if numero_4 == 0:
    print('Tu numero es 0')
elif numero_4 >= 1:
    print('Tu numero es positivo')
else:
    print('Tu numero es negativo')

# Ejercicio 17
# Simulá un menú:

# 1 - Ver saldo
# 2 - Depositar
# 3 - Salir

# Si elige otra cosa, mostrar “Opción inválida”.

menu = int(input('''    MENU DEL BANCO.
                 
    1 - Ver saldo
    2 - Depositar
    3 - Salir
                 
    Ingrese el numero de opcion que desea:'''))

if menu == 1:
    print('Su saldo es de: $15')
elif menu == 2:
    print('El saldo minimo para deposito es de $100')
elif menu == 3:
    print('Gracias por contactar con el banco')
else:
    print('Opción inválida')