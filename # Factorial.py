# Factorial

# # factorial
# def factorial(n):

#     if n < 0: return None
#     if n < 2: return 1
#     else:
#         return n*factorial(n-1)
    
# if __name__ == '__main__':
#     print(factorial(5))

def factorial(n):

    if n < 0: return None

    if n < 2: return 1 
    else:
        return n*factorial(n-1)


if __name__ == '__main__':
   print(factorial(5))
