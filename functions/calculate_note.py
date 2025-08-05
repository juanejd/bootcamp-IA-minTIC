def calculate_note(note_1, note_2, note_3):
    if note_1 >= 0 and note_2 >= 0 and note_3 >= 0:
        percentage_1 = 0.3
        percentage_2 = 0.3
        percentage_3 = 0.4

        note_1_total = note_1 * percentage_1
        note_2_total = note_2 * percentage_2
        note_3_total = note_3 * percentage_3

        note = note_1_total + note_2_total + note_3_total

        return round(note, 2)
    raise ValueError("Una de las notas es menor a 0")


note_1 = float(input("Ingrese la 1ra nota: "))
note_2 = float(input("Ingrese la 2da nota: "))
note_3 = float(input("Ingrese la 3ra nota: "))

note = calculate_note(note_1, note_2, note_3)
print(note)
