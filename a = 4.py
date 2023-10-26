def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True

def is_trianguleRect(a,b,c):
    if not is_triangle(a,b,c):
        return False
    if c > a and c > b:
        return c**2 == a**2 + b**2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2 
    

if __name__ == '__main__':
    # print(is_triangle(1,1,1))
    # print(is_triangle(1,1,3))
    # print(is_triangle(1,1,2))
    # print(is_triangle(2,1,2))
    print(is_trianguleRect(5,3,4))
    print(is_trianguleRect(1,3,4))