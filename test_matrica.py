matrica = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(matrica[1][2])

for row in matrica:
  for elem in row:
    print(elem, end=' ')
  print()


kvadrat_broja=[x**2 for x in range(10) if x % 2 == 0]
print(kvadrat_broja, end=' ')