import math

x = 3
y = -13.0
z = float('nan') # NaN or nan can work

# floating absolute | 12.5 |
print(math.fabs(y))
# up from 3.33 to 4 ปัดขึ้น
print(math.ceil(x))
# down from 3.33 to 3 ปัดลง
print(math.floor(x))
# removing the fractional part of the number without rounding.
print(math.trunc(x))
# removing the fractional part of the number without rounding.
print(math.trunc(y))
# modulus
print(math.fmod(y,x))
# bruh get mantissa and exponent
print(math.frexp(x))
# check is not a number??
print(math.isnan(x))
print(math.isnan(z))

print(x*z)
# square root
print(math.sqrt(x))
# square root return as integer so no decimals
print(math.isqrt(x))

print(math.pow(y,x)) #  y^x

print(math.pi)

print(math.pi * math.pow(x,2))