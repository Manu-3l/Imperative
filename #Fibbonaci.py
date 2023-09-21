#Fibbonaci

# f0 = 0
# f1 = 1
# f2 = 1
# f3 = 2
# f4 = 3
# f5 = 5

def fibonacci(n):
    if n < 0 : return None
    
    if n < 3: return 1

    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    print(fibonacci(6))

def fun(a):
    if a > 100:
        return 5
    else:
        return a + fun(a + 25)

