def run():
    # for i in range(1000):
    #     if i % 11 != 0:
    #         continue
    #     print(i)

    # for i in range(10000):
    #     print(i)
    #     if i == 2000:
    #         break

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()