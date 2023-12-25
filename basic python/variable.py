_x = 5435
print(_x)
# Object Identity
'''
In Python, every created object identifies uniquely in Python. Python provides the guaranteed that no two objects will have the same identifier. The built-in id() function, is used to identify the object identifier. Consider the following example.
'''
a = 50
print(id(a))
print(id(534))
print(id(_x))

name = "A"
Name = "B"
naMe = "C"
NAME = "D"
n_a_m_e = "E"
_name = "F"
name_ = "G"
_name_ = "H"
na56me = "I"

print(name, Name, naMe, NAME, n_a_m_e, NAME,
      n_a_m_e, _name, name_, _name, na56me)

# Multiple Assignment
x = y = z = 56543
print(x, y, z)

x = 0b10100  # Binary Literals
y = 100  # Decimal Literal
z = 0o215  # Octal Literal
u = 0x12d  # Hexadecimal Literal

# Float Literal
float_1 = 100.5
float_2 = 1.5e2

# Complex Literal
a = 5+3.14j
print(x, y, z, u)
print(float_1, float_2)
print(a, a.imag, a.real)

x = 'rakib'
print(x[slice(0,1)])
