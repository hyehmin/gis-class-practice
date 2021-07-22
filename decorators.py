"""
def decorator(func):
    def decorated():
        print('함수시작!')
        func()
        print('함수 끝!')
    return decorated


@decorator
def hello_world():
    print('hello_world')


hello_world()
"""


def decorator(area_func):
    def decorated(x, y):
        if x >= 0 and y >= 0:
            return area_func(x,y)
        else:
            raise ValueError("Input must be positive value")
    return decorated


@decorator

def square_area(x, y):
    return x * y


@decorator
def triangle_are(x, y):
    return (x * y) * 0.5


a = int(input(" a : "))
b = int(input(" b : "))

print(square_area(a,b))
print(triangle_are(a,b))

