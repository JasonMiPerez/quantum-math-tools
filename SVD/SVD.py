import numpy as np

rows = int(input("Enter in number of rows for matrix:"))
columns = int(input("Enter in number of columns for matrix:"))

M = []
for i in range(rows):
    row = []
    for j in range(columns):
        element = float(input(f"Enter element [{i}{j}]: "))
        row.append(element)
    M.append(row)

U, S, VT = np.linalg.svd(M)

print("M:")
print(M)
print("U:")
print(U)
print("S:")
print(S)
print("VT:")
print(VT)