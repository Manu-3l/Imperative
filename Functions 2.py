#Functions 2

def age_from():
    if age >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")


def identification(name, gender, age):
    print("Hi. {}" .format(name))
    if gender == "M":
        print("Confirmado, eres genero Masculino")
        age_from(age)
    elif gender == "F":
        print("Confirmado, eres genero Femenino")
        age_from(age)
    elif gender == "NB":
        print("Confirmado, eres genero no binario")
        age_from(age)
    else:
        print ("Prefiere no confirmarlo")
        age_from(age)


if __name__ == '__main__':
    name = input("Enter your name:").upper()
    gender = input("Enter your gender:").upper()
    age = input("Enter your age:").upper()
    identification(name, gender, age)

