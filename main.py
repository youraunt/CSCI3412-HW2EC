from math import sqrt


def pi_approximation(n):
    approx_pi = 0
    edges_squared = 2
    edge_length = sqrt(edges_squared)
    sides = 4
    num_outside_triangles = 2
    for i in range(n):
        sides *= 2
        edges_squared = 2 - 2 * sqrt(1 - edges_squared / 4)
        edge_length = sqrt(edges_squared)
        approx_pi = (sides * edge_length / 2)
        print(i + 1, approx_pi)
        num_outside_triangles *= 2
        print(num_outside_triangles)
    return approx_pi


def area_circle(approx_pi):
    r = 1
    area = approx_pi * r ** 2
    return area


print("The approximate area of the unit circle is: ", area_circle(pi_approximation(5)))
