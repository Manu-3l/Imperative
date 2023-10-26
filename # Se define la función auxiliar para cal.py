# Se define la función auxiliar para calcular la nota
def note_definitive(exam_1, exam_2, homew_1, homew_2, parti_1):
    return (exam_1*0.2
            + exam_2*0.4
            + homew_1*0.2
            + homew_2*0.2
            + parti_1/10)

# Función principal, clasifica el valor de la nota y retona un valor


def classification(signature, note_finally):
    if signature == "FUNDAMENTOS":
        if note_finally >= 0 and note_finally < 2.0:
            return "malo"
        elif note_finally >= 2 and note_finally < 3.0:
            return "Deficiente"
        elif note_finally >= 3 and note_finally < 3.8:
            return "regular"
        elif note_finally >= 3.8 and note_finally < 4.5:
            return "bueno"
        elif note_finally >= 4.5 and note_finally <= 5:
            return "Excelente"
        else:
            print("Nota No válida...")


if __name__ == '__main__':
    variable_c = "C"
    while variable_c == "C":  # Condición de parada. Ciclo para calcular a n cantidad de estudiante su nota
        try:  # captura el error para valores negativos
            name = input("Digite tu nombre:")
            signature = input("Digite el nombre la asignatura:").upper()
            exam_1 = float(input("Digite el valor del parcial I: "))
            exam_2 = float(input("Digite el valor del parcial Final: "))
            homew_1 = float(input("Digite el valor de la tarea I: "))
            homew_2 = float(input("Digite el valor de la tarea II: "))
            parti_1 = float(input("Digite el valor del participación: "))
            if exam_1 < 0:
                raise Exception("Negative")
        except Exception as neg:
            print("Error:", str(neg))
    # invoca la función note definitive
        else:
            note_finally = note_definitive(
                exam_1, exam_2, homew_1, homew_2, parti_1)
    # invoca la función classification
            result = classification(signature, note_finally)
            print(f"""Nombre del alumno: {name}, 
                Nombre de la asigntura: {signature}, 
                clasificación: {result} """)
            variable_c = input("Desea ingresar otro usuario, digite c, en caso contrario otra letra: ").upper(
            )  # se actualiza la variable
