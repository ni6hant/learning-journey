# Original 2D list
sudoku = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. No copy (same object)
a = sudoku

# 2. Shallow copy of the outer list
b = sudoku[:]

# 3. Copy every row (independent 2D copy)
c = [row[:] for row in sudoku]

print("Initially")
print("sudoku =", sudoku)
print("a      =", a)
print("b      =", b)
print("c      =", c)

print("\nIdentity checks")
print("a is sudoku:", a is sudoku)
print("b is sudoku:", b is sudoku)
print("c is sudoku:", c is sudoku)

print("\nRow identity checks")
print("b[0] is sudoku[0]:", b[0] is sudoku[0])
print("c[0] is sudoku[0]:", c[0] is sudoku[0])

# Modify an element
print("\nChanging sudoku[0][0] = 99")
sudoku[0][0] = 99

print("sudoku =", sudoku)
print("a      =", a)
print("b      =", b)
print("c      =", c)

# Replace an entire row
print("\nReplacing sudoku[1] = [40, 50, 60]")
sudoku[1] = [40, 50, 60]

print("sudoku =", sudoku)
print("a      =", a)
print("b      =", b)
print("c      =", c)

# Modify b
print("\nChanging b[2][1] = 88")
b[2][1] = 88

print("sudoku =", sudoku)
print("a      =", a)
print("b      =", b)
print("c      =", c)

# Modify c
print("\nChanging c[0][2] = 777")
c[0][2] = 777

print("sudoku =", sudoku)
print("a      =", a)
print("b      =", b)
print("c      =", c)