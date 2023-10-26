#CMC

def harris_benedict_equation(gender, height, weight, age):
    if gender == "M" or gender == "MASCULINO":
        mcb = (13.75 * weight) + (5 * height) - (6.76 * age) + 66
        print (f"La cantidad minima de calorías es: {mcb}" )
    elif gender == "F" or gender == "FEMENINO":
        mcb = (9.56 * weight) + (1.85 * height) - (4.68* age) + 655
        print (f"La cantidad minima de calorías es: {mcb}" )
    else:
        print ("error vuelvalo a intentar, genero no reconocido")


if __name__ == "__main__":
    gen = input("Digite su género: ").upper()
    wei = float(input("Digite su peso en kilogramos: "))
    hei = float(input("Digite su peso en centimetros: "))
    ag = float(input("Digite su edad: "))
    harris_benedict_equation(gen, hei, wei, ag)

