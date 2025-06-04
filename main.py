from pprint import pp

def e(x):
    sum = 0
    current_factorial = 1
    for i in range(50):
        if i > 0:
            current_factorial *= i
        term = (x ** i) / current_factorial
        sum += term
    return sum

def atanpi(x):   
  return  (x - x**3 / 3 + x**5 / 5 - x**7 / 7 + x**9 / 9 -
              x**11 / 11 + x**13 / 13 - x**15 / 15 +
              x**17 / 17 - x**19 / 19 + x**21 / 21)


pi = 4 * (4 * atanpi(1/5) - atanpi(1/239))

def abs(x):
  if x < 0:
    return -x
  return x

def sqrt(x):
  return x**0.5

def sin(theta):
    theta = theta % (2 * pi)  
    
    result = 0
    for n in range(20):
        factorial = 1
        for i in range(1, 2 * n + 2):
            factorial *= i
        term = ((-1) ** n) * (theta ** (2 * n + 1)) / factorial
        result += term
    
    return result

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

def derivative(func, x, h=1e-8):
  return (func(x + h) - func(x)) / h

def euler_method(func, x0, y0, h, n):
  x = x0
  y = y0
  b = n / h
  for i in range(int(b)):
    y += h * derivative(func, x)
    x += h
  return y

def riemann_sum(func, a, b, step_size, mode):
  sum = 0
  if (mode == "left"):
      while a < b - step_size * 0.001:
        width = min(step_size, b - a)
        sum += func(a) * width
        a += width
  elif (mode == "right"):
      a += step_size
      while a <= b - step_size * 0.001:
        width = min(step_size, b - a)
        sum += func(a) * width
        a += width
  elif (mode == "middle"):
      while a < b - step_size * 0.001:
        width = min(step_size, b - a)
        sum += func(a + width / 2) * width
        a += width
  elif (mode == "trap"):
      while a < b - step_size * 0.001:
        width = min(step_size, b - a)
        sum += (func(a) + func(a+width))/2 * width
        a += width
  else:
      raise ValueError("Invalid mode")
  return sum


def ln(x):
  if x == 0:
    return(1)
  if x < 0:
    raise ValueError("Log of negative number DNE")
  return 1e+7*(x**(1e-7))-1e+7

def logb(b, x):
  return (ln(x)/ln(b))

def integral(func, a, b, step_size=1e-5):
  return riemann_sum(func, a, b, step_size, "left")

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
  return  integral((lambda x: 1/(1+x**2)), 0, x)

def newtons_method(func, x0, low_bound, upper_bound, accuracy, max_iter=100):
  x = x0
  for i in range(max_iter):
    if derivative(func, x) == 0:
      print("Derivative is zero, can't use Newton's method")
      break
    if x > upper_bound or x < low_bound:
      print("There are no zeros on the interval or entered interval wrong")
      break
    x_new = x - func(x) / derivative(func, x)
    if abs(x_new - x) < accuracy:
      return x_new
    x = x_new

def intersections(func_one, func_two, guess, a=-100, b=100):
  x = newtons_method((lambda x : func_one(x) - func_two(x)), guess, a, b, 0.001)
  return [x, func_one(x)]






if __name__ == "__main__":
  pp(integral((lambda x : 2*x**2), 0, 10))
  pp(derivative((lambda x : 3*x+5), 2))
  pp(ln(1000))
