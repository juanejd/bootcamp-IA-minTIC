from string import digits, ascii_letters


def type_of_input(char):
    if char not in ascii_letters:
        raise TypeError("el input no es una letra")

    vowels = "aeiouAEIOU"

    if char in vowels:
        return "vocal"
    if char in digits:
        return "numero"
    if char not in vowels and char not in digits:
        return "consonante"


char = input("ingrese un caracter: ")

result = type_of_input(char)

print(f"el caracter {char} es {result}")
