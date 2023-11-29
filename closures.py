# hola 3 -> HolaHolaHola
# Facundo 2 -> FacundoFacundo
# platzi 4 -> PlatziPlatziPlatziPlatzi

# def make_repeater_off(n):
#     def repeater(string):
#         assert type(string) == str, "Solo puedes usar cadenas"
#         return string * n
#     return repeater

# def run():
#     repeat_5 = make_repeater_off(5)
#     print(repeat_5("Hola"))
#     repeat_10 = make_repeater_off(10)
#     print(repeat_10("Platzi"))


# if __name__ == '__main__':
#     run()


def make_division_by(n) -> float:
    def divisor(x):
        assert n != 0, "No puedes divinir entre cero"
        return x / n
    return divisor


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    division_by_18 = make_division_by(18)
    print(division_by_18(54))

if __name__ == '__main__':
    run()