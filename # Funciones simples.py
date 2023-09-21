# Funciones simples
# Triangle


def is_triangle(a,b,c):
    if a + b <= c or b + c <= a or a + c <= b:
        return False
    return True
    

def is_trianguleRect(a,b,c):
    if not is_triangle(a,b,c):
        return False
    if c > a and c > b:
        return c**2 == a**2 + b**2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
if __name__ == '__main__':
    print(is_triangle(1,1,1))
    print(is_triangle(1,1,3))