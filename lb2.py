import numpy as np
import math

#Варіант 303

def matrix(x1, x2, x3, x4, x5, x6, x7, x8, x9):
    m = x1 * x5 * x9 - x1 * x6 * x8 - x2 * x4 * x9 + x2 * x6 * x7 + x3 * x4 * x8 - x3 * x5 * x7
    return m
N=3
ymax = (30 - N) * 10
ymin = (20 - N) * 10

x1max = 30
x1min = -20
x2max = 40
x2min = -20

m = 5
n = 3

M = np.random.randint(low=-1, high=2, size=6).reshape(3, 2)
print(' x1','  x2')
print(M)

T = np.random.randint(low=ymin, high=ymax, size=15).reshape(3, 5)

print("Матриця планування:\n")
print('X1',' X2',' Y1',' Y2',' Y3',' Y4',' Y5' )
for i in range(3):
    print("{0} {1} {2} {3} {4} {5} {6}".format(M[i][0], M[i][1], T[i][0], T[i][1], T[i][2], T[i][3], T[i][4]))

#дисперсія  по рядкам
sFunc = [(T[i][0] + T[i][1] + T[i][2] + T[i][3] + T[i][4]) / 5 for i in range(3)]
disp = [((T[i][0] - sFunc[i]) ** 2 + (T[i][1] - sFunc[i]) ** 2 + (T[i][2] - sFunc[i]) ** 2 + (
        T[i][3] - sFunc[i]) ** 2 + (T[i][4] - sFunc[i]) ** 2) / 5 for i in range(3)]
#осн відхилення
dispe = math.sqrt((2 * (2 * m - 2)) / (m * (m - 4)))
if disp==0:
    print("")

F = []
if disp[0] > disp[1]:
    F.append(disp[0] / disp[1])
else:
    F.append(disp[1] / disp[0])

if disp[2] > disp[0]:
    F.append(disp[2] / disp[0])
else:
    F.append(disp[0] / disp[2])

if disp[2] > disp[1]:
    F.append(disp[2] / disp[1])
else:
    F.append(disp[1] / disp[2])

Teta = [(m - 2 / m) * F[i] for i in range(3)]
R = [math.fabs(Teta[i] - 1) / dispe for i in range(3)]


#нормованих  коеф  рівняння
mx1 = (M[0][0] + M[1][0] + M[2][0]) / 3
mx2 = (M[0][1] + M[1][1] + M[2][1]) / 3
my = (sFunc[0] + sFunc[1] + sFunc[2]) / 3
a1 = (M[0][0] ** 2 + M[1][0] ** 2 + M[2][0] ** 2) / 3
a2 = (M[0][0] * M[0][1] + M[1][0] * M[1][1] + M[2][0] * M[2][1]) / 3
a3 = (M[0][1] ** 2 + M[1][1] ** 2 + M[2][1] ** 2) / 3
a11 = (M[0][0] * sFunc[0] + M[1][0] * sFunc[1] + M[2][0] * sFunc[2]) / 3
a22 = (M[0][1] * sFunc[0] + M[1][1] * sFunc[1] + M[2][1] * sFunc[2]) / 3

b0 = matrix(my, mx1, mx2, a11, a1, a2, a22, a2, a3) / matrix(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b1 = matrix(1, my, mx2, mx1, a11, a2, mx2, a22, a3) / matrix(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b2 = matrix(1, mx1, my, mx1, a1, a11, mx2, a2, a22) / matrix(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)

y = [(b0 + b1 * M[i][0] + b2 * M[i][1]) for i in range(3)]
print('Нормоване рівняння регресії')
print(f"\ny={b0}+{b1}*x1+{b2}*x2\n")
print(f"""b0={y[0]}\nb1={y[1]}\nb2={y[2]}""")

# натурал коеф.
dx1 = math.fabs(x1max - x1min) / 2
dx2 = math.fabs(x2max - x2min) / 2
x10 = (x1max + x1min) / 2
x20 = (x2max + x2min) / 2

a0 = b0 - b1 * x10 / dx1 - b2 * x20 / dx2
a1 = b1 / dx1
a2 = b2 / dx2

y = [(a0 + a1 * M[i][0] + a2 * M[i][1]) for i in range(3)]
print('Нутуралізоване рівняння регресії')
print(f"\ny={a0}+{a1}*x1+{a2}*x2\n")
print(f"""b0={y[0]}\nb1={y[1]}\nb2={y[2]}""")