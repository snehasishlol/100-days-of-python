# strings

# python days/3.py
# python days/3.py


# strings --------------------------

a = "this is a string (?)"

print(a)

# -----------------------------------

b = """
this
is 
a
multi
line
string 
(?)
"""

print(b)

# -----------------------------------

c = "first string"

d = "plus"

e = "third string"

print(c, d, e) # with space

print(c + d + e) # without space

# -------------------------------------

f = "this is another string (?)"

print(f[0]) # first character: index 0
print(f[1]) # second character: index 1

# ---------------------------------------

g = "first, second, third"

print(g[0:5])

print(g[7:13])

# ---------------------------------------

h = "how long is this string ?"

i = len(h)

print(i)

print(h[0:-1]) # also: print(h[0 : i - 1]) | subtracts from len(h), i.e. i

print(h[-10:-5]) # also: print(h[i - 10 : i - 5]) | subtracts from len(h), i.e. i
