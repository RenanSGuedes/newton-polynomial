coord = [(-1, 4), (0, 1), (2, -1)]

deltas = [[] for _ in range(len(coord) - 1)]

print("deltas:", deltas)

for i in range (len(coord) - 1):
  deltas[0].append((coord[i + 1][1] - coord[i][1])/(coord[i + 1][0] - coord[i][0]))
print("deltas:", deltas)



for k in range(len(deltas) - 1):
  for i in range(len(deltas[k]) - 1):
    deltas[k + 1].append((deltas[k][i + 1] - deltas[k][i])/(coord[i + 2 + k][0] - coord[i][0]))
  print("deltas:", deltas)


'''
for i in range(len(deltas[0]) - 1):
  deltas[0 + 1].append((deltas[0][i + 1] - deltas[0][i])/(coord[i + 2][0] - coord[i][0]))
print("deltas:", deltas)

for i in range(len(deltas[1]) - 1):
  deltas[0 + 2].append((deltas[1][i + 1] - deltas[1][i])/(coord[i + 3][0] - coord[i][0]))
print("deltas:", deltas)

for i in range(len(deltas[2]) - 1):
  deltas[0 + 3].append((deltas[2][i + 1] - deltas[2][i])/(coord[i + 4][0] - coord[i][0]))
print("deltas:", deltas)
'''