def divisors(num):
     divisors = []
     for i in range(1, num + 1):
        if num % i == 0:
             divisors.append(i)
     return divisors
    try:
        if num < 0:
            raise ValueError("Debes ingresar un número positvo")
        divisors =[i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        num = int(input('Ingresa un numero: '))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print('Debes ingresar un numero')


        


if __name__ == '__main__':
    run()