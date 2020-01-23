def circle_length(radius):
    return p * radius * 2


def circle_area(radius):
    return p * radius ** 2


def main():
    radius = float(input())
    print(circle_length(radius), circle_area(radius))


p = 3.14159
