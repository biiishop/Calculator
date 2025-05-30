e = (1 + 1/99999) ** 99999

def abs(x):
  if x < 0:
    return -x
  return x

def sqrt(x):
  return x**0.5

def sin(theta):
  if theta > 0:
    theta %= 2 * pi
  else:
    theta %= -2 * pi
  return (theta - theta**3 / 6 + theta**5 / 120 - theta**7 / 5040 +
          theta**9 / 362880 - theta**11 / 39916800 + theta**13 / 6227020800 -
          theta**15 / 1307674368000 + theta**17 / 355687428096000 -
          theta**19 / 121645100408832000 + theta**21 / 51090942171709440000)

def cos(theta):
  return sin(pi / 2 - theta)

def tan(theta):
  return sin(theta) / cos(theta)

def sec(theta):
  return 1 / cos(theta)

def csc(theta):
  return 1 / sin(theta)

def cot(theta):
  return 1 / tan(theta)

def asin(x):
  if x < -1 or x > 1:
    raise ValueError("asin: input must be in the range [-1, 1]")
  if x == -1:
    return -pi / 2
  if x == 1:
    return pi / 2
  return x + (x**3 / 6 + x**5 / 120 + x**7 / 5040 + x**9 / 362880 +
              x**11 / 39916800 + x**13 / 6227020800 + x**15 / 1307674368000 +
              x**17 / 355687428096000 + x**19 / 121645100408832000 +
              x**21 / 51090942171709440000)

def acos(x):
  if x < -1 or x > 1:
    raise ValueError("acos: input must be in the range [-1, 1]")
  if x == -1:
    return pi
  if x == 1:
    return 0
  return pi / 2 - asin(x)

def atan(x):
  if x == 0:
    return 0
  if x < 0:
    return -atan(-x)
  if x == 1:
    return pi / 4
  if x == float('inf'):
    return pi / 2
  if x == float('-inf'):
    return -pi / 2
  return  (x - x**3 / 3 + x**5 / 5 - x**7 / 7 + x**9 / 9 -
              x**11 / 11 + x**13 / 13 - x**15 / 15 +
              x**17 / 17 - x**19 / 19 + x**21 / 21)

def asec(x):
  if x < 1 and x > -1:
    raise ValueError("asec: input must be outside the range [-1, 1]")
  if x == 1:
    return 0
  if x == -1:
    return pi
  return acos(1 / x)

def acsc(x):
  if x < -1 or x > 1:
    raise ValueError("acsc: input must be in the range [-1, 1]")
  if x == -1:
    return -pi / 2
  if x == 1:
    return pi / 2
  return asin(1 / x)

def acot(x):
  if x == 0:
    return pi / 2
  if x < 0:
    return pi - atan(-x)
  if x == float('inf'):
    return 0
  if x == float('-inf'):
    return pi
  return pi / 2 - atan(x)

pi = 4 * (4 * atan(1/5) - atan(1/239))
print(pi)