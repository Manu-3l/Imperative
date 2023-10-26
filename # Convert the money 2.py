# Convert the money

menu = """ Welcome to the convert the money🪙

1- Pesos Argentinos - Dollars
2- Pesos Colombianos - Dollars
3- Pesos Mexicanos - Dollars


"""

money = 0

country = int(input(menu))

def convert(type,currency):
    value = float(input("Enter the value money in {}:".format(type)))
    global money
    money = value/currency
    print("The values in dollars is: {}".format(money))


if country == 1:
    currency = 350
    convert("Argentinos",currency)
    
elif country == 2:
    currency = 3940
    convert("Colombianos",currency)
elif country == 3:
    currency = 17.13
    convert("Mexicanos",currency)
else:
    print("The options is not correct.")