import math 

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def division(a,b):
    if b != 0:
        return a/b 
    else:
        return "No se puede dividir entre cero"

def multiplicacion(a,b):
    return a * b

def exponente(numero):
    return math.exp(numero)

def raiz_cuadrada(numero):
    return math.sqrt(numero)

def potenciacion(numero,potencia):
    return math.pow(numero,potencia)

def porcentaje(numero,porcentaje):
    return (porcentaje/100)* numero

def logaritmo(numero):
    return math.log10(numero)

def coseno(numero):
    return math.cos(numero)

def menu():
    print("1)Suma")
    print("2)Resta")
    print("3)Division")
    print("4)Multiplicacion")
    print("5)Exponente")
    print("6)Raiz cuadrada")
    print("7)Potenciacion")
    print("8)Porcentaje")
    print("9)Logaritmo")
    print("10)Coseno")
    print("11)SALIR")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opcion: ")

        if opcion == '11':
            print("ADIOS")
            break

        if opcion in ('1','2','3','4'):
            try:
                num1 = float(input("Ingrese el primer valor: "))
                num2 = float(input("Ingrese el segundo valor: "))
            except ValueError:
                print("Opcion invalida")
                continue 

            if opcion == '1':
                print("Resultado: ", suma(num1,num2))
            elif opcion == '2':
                print("Resultado: ",resta(num1,num2))
            elif opcion == '3':
                print("Resultado: ",division(num1,num2))
            elif opcion == '4':
                print("Resultado: ",multiplicacion(num1,num2))

        if opcion in ('5','9','10'):
            try:
                num = float(input("Ingrese el valor: "))
            except ValueError:
                print("Opcion invalida")
                continue 

            if opcion == '5':
                print("Resultado: ", exponente(num))
            elif opcion == '9':
                print("Resultado: ",logaritmo(num))
            elif opcion == '10':
                print("Resultado: ",coseno(num))

        elif opcion == '6':
            try:
                num = float(input("Ingrese el valor: "))

                if num < 0:
                    print("Math Error")
                    continue 
                print("Resultado: ",raiz_cuadrada(num))
            except ValueError:
                print("Ingrese un valor valido")

        elif opcion == '7':
            try:
                num = float(input("Ingrese el valor a  potenciar: "))
                pot = float(input("Ingrese la potencia: "))
                
                print("Resultado: ",potenciacion(num,pot))
            except ValueError:
                print("Ingrese un valor valido")

        elif opcion == '8':
            try:
                num = float(input("Ingrese el valor: "))
                porc = float(input("Ingrese el porcentaje: "))
                
                print("Resultado: ",porcentaje(num,porc))
            except ValueError:
                print("Ingrese un valor valido")

        else:
            print("Opcion no valida, por favor selecciona una opcion del menu")


if __name__ == "__main__":
    main()
   
                         









    

