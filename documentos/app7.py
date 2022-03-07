try:
    numero = int(input("digite um numero: "))
    print(numero)
except ZeroDivisionError:
    print("divisão por 0 não é possível")
except ValueError:
    print("digite um valor válido")
except:
    print("erro inesperado")
finally:
    print("sempre executa")