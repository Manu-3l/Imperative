# Integrante: Manuel Jesús Rosero Zuñiga - 202176007 3743

# Docente: Luis Germán Toro Pareja
# Número de grupo: 1
# Quiz 1


def SN(SB, bonus, adjustment):
    bonus = SB * bonus
    adjustment = SB * adjustment
    x = SB + bonus - adjustment
    print("Your salary is {}" .format(x))
    

def identification(name, CC, salary, date):
    print("Hi. {}" .format(name))
    print("Your CC is: {}" .format(CC))
    if date >= 1995 & salary >= 1200000:
        SN(salary, 0.06, 0.04)
        
    elif date == 1995 | salary <= 550000:
        SN(salary, 0.03, 0.04)
        
    else:
        SN(salary, 0.04, 0.04)
        
        


if __name__ == '__main__':
    name = input("Enter your name:").upper()
    cc = int(input("Enter your CC:"))
    salary = int(input("Enter your salary:"))
    date = int(input("Enter your year you started working:"))
    identification(name, cc, salary, date)
