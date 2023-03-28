# typecasting & inputs

# python days/2.py
# python3 days/2.py

# implicit typecasting

a = 10;
b = 6.9;

print(a + b);

# --------------------------------------------------

# explicit typecasting

c = "10";
d = "6";

print(int(c) + int(d));

#----------------------------------------------------

# implicit and explicit typecasting

e = "10";
f = "6.9";

print(int(e) + float(f));


# ----------------------------------------------------

# user inputs

g = input("fuck zodiacs, what's your favorite taylor swift album? \n >> ");

print("cool, i like the " + g + " album too!");


# typecasting with user inputs

h = input("enter your favorite number: ");

i = int(h);

print("your favorite number is: ", i);
