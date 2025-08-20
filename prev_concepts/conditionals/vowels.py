def is_vowel(char):
    vowels = "aeiouAEIOU"

    if char in vowels:
        return True
    else:
        return False


string = "loremimpusmab3c32s21"

for i in string:
    result = is_vowel(i)
    if result:
        print(f"la letra {i} es vocal")
    else:
        print(f"la letra {i} no vocal")
