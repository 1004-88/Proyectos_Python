#Menu de calculadora
    #Funciones def
    #Ciclo de repetición menu
    #Validaciones con try except
import time

#Paso 01 - creación de funciones

#Las variables num1 y num2 que se encuentran dentro de los parentisis,
#Son los argumentos que recibe desde afuera la función sumar
def sumar(num1,num2):
    #Proceso de suma
    resultado_suma = num1 + num2
    #Devuelve la variable resultado_suma
    return (resultado_suma)

def restar(num1,num2):
    resultado_resta = num1 - num2
    return (resultado_resta)

def division(num1,num2):
    try:
        resultado_division = num1 / num2
        return (resultado_division)
    except ZeroDivisionError:
        print('Error, no se puede dividir por cero.\n')
        time.sleep(3)
def multiplicar(num1,num2):
    resultado_multiplicacion = num1 * num2
    return (resultado_multiplicacion)

def mostrar_menu():
    print('========================================')
    print('Menu de calculadoraen python')
    print('========================================')
    print('1.- Sumar.')
    print('2.- Restar.')
    print('3.- Dividir.')
    print('4.- Multiplicar.')
    print('5.- Salir.')
#Funcion def que no recibe argumentos pero si retorna datos
def obtener_numeros():
    while True:
        try:
            num1 = int(input('Ingrese el primer numero a operar:'))
            num2 = int(input('Ingrese el segundo numero a operar:'))
            return (num1,num2)
        except ValueError:
            print('Error,se ah ingrsado un número no valido.')
            time.sleep(3)

def main():
    while True:
        #Llamar a la funcion mostrar menu
        mostrar_menu()

        #Validar que la opcion ingresada sea numerica 
        try:
            op = int(input('Ingrese una opción de 1 a 5:'))
        except ValueError:
            print('Error, ingrese un número valido.')
            time.sleep(3)

        #Validar que la opcion ingresada este entre 1 y 5
        if op < 1 or op > 5:
            print('Error, ah ingresado una opcion no valida.')
            time.sleep(3)

        #Cuando la opcion ingresada sea entre las 4 opciones de la lista
        #Ingresa el codigo interno del if
        if op in [1,2,3,4]:
            #Guardar en las variables num1 y num2, lo que me edsta retornando
            #la funcion obtener numeros()
            num1, num2 = obtener_numeros()

            if op == 1:
                resultado = sumar(num1, num2)
                print(f'El resultado de la suma es: {resultado}\n')
                time.sleep(2)
            if op == 2:
                resultado = restar(num1, num2)
                print(f'El resultado de la resta es: {resultado}\n')
                time.sleep(2)
            if op == 3:
                resultado = division(num1, num2)
                print(f'El resultado de la división es: {resultado}\n')
                time.sleep(2)
            if op == 4:
                resultado = multiplicar(num1, num2)
                print(f'El resultado de la multiplicaión es: {resultado}\n')
                time.sleep(2)
        if op == 5:
            print('Muchas gracias por utilizar el programa.')
            exit()

main()




           
