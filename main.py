import matplotlib.pyplot as plt
import sympy as sp
from math import sqrt

# define my points
A = [5, 1]
B = [1, 4]

# draw A & B points
plt.plot(A, B, 'o')

# define my constants
x = sp.Symbol('x')
t = sp.Symbol('t')
z = 1
S = 1000
z_point = 0

m = 70.0             # mass of the object in kg
V = 0.25             # volume of the object in m^3
h = 0.25             # depth in water in meters
g = 9.81             # gravity in m/s^2
rho_water = 1000     # density of water in kg/m^3
k = 0.25             # viscosity

while z <= 5:

    if z == B[0]:    # skip this to avoid dividing by zero
        z += 0.1
        continue

    # draw all possible paths
    plt.plot(z, 3, 'o')
    # plt.plot([A[0], z], [A[1], 3], '-o')
    # plt.plot([B[0], z], [B[1], 3], '-o')

    # the function of each path between B and z
    x_BZ = lambda t: B[0] + (z - B[0]) * t
    y_BZ = lambda t: B[1] + (3 - B[1]) * t

    # the function of all path between z and A
    x_AZ = lambda t: z + (A[0] - z) * t
    y_AZ = lambda t: 3 + (A[1] - 3) * t

    # the velocity Bz
    dx_dtB = (z - B[0])
    dy_dtB = 3 - B[1]
    vB = sqrt(dx_dtB  2 + dy_dtB  2)

    # the velocity Az
    dx_dtA = A[0] - z
    dy_dtA = A[1] - 3
    vA = sqrt(dx_dtA  2 + dy_dtA  2)

    # the distance of each path on water
    d = ((z - A[0])2 + (3 - A[1])2)**0.5

    # kinetic energy in the land
    Ec1 = 0.5 * m * vB ** 2

    # kinetic energy in the water
    Ec2 = 0.5 * m * vA ** 2 - k * vA * d

    # total kinetic energy
    Ec = Ec1 + Ec2

    # total potential energy
    Ep_land = 0
    Ep_water = g * h * (m - rho_water * V)
    Ep = Ep_land + Ep_water

    # calculate s
    s = Ec - Ep

    if s < S:
        S = s
        z_point = z

    z += 0.1

    # show s graph in function of z
    # plt.scatter(z, s, color='blue', label='Data points')

print(f"the best path is with s = {S} & z = {z_point}")

# draw the best path
plt.plot(z_point, 3, 'o')
plt.plot([A[0], z_point], [A[1], 3], '--o')
plt.plot([B[0], z_point], [B[1], 3], '--o')

plt.grid(True)
plt.show()
