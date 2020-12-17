from sympy.abc import x
from sympy import expand, simplify

coord = [(1, 0), (3, 6), (4, 24), (5, 60)]
deltas = [[] for _ in range(len(coord) - 1)]

for i in range (len(coord) - 1):
  deltas[0].append((coord[i + 1][1] - coord[i][1])/(coord[i + 1][0] - coord[i][0]))

for k in range(len(deltas) - 1):
  for i in range(len(deltas[k]) - 1):
    deltas[k + 1].append((deltas[k][i + 1] - deltas[k][i])/(coord[i + 2 + k][0] - coord[i][0]))

firstItem = [item[0] for item in deltas]
firstItem.insert(0, coord[0][1])

print("deltas:", deltas)
print(firstItem)

factors = []

for i in range(len(coord) - 1):
  factors.append('(x - {})'.format(coord[i][0]))
  
print(factors)


