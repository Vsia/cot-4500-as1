import math
import numpy as np


#Question 1
#Use double precision, calculate the resulting values (format to 5 decimal places) 
#convert binary to decimal 
binary= "0b010000000111111010111001"
decimalNumber =int(binary,2)

#format to five decimal places 
print("{:.5f}".format(decimalNumber))

#Question 2
#Three digit chopping 
decimalNumberTwo= decimalNumber
print("%.3f"%decimalNumberTwo)


#Question 3
#Three digit rounding
threeRounding= round(decimalNumber,3 )
print(threeRounding)

#Question 4
#Compute the absolute and relative error with the exact value from question 1 and its 3 digit rounding 
def absolute(threeRounding, decimalNumber):
  sub= decimalNumber - threeRounding
  absolute_error= abs(sub)
  print(absolute_error)

def relative(threeRounding, sub):
  relative_error= sub/decimalNumber
  print(relative_error)
  
#question 5 
#What is the minimum number of terms needed to computer f(1) with error < 10-4? 

def check_for_alternating(function_we_got: str):
    term_check = check_for_negative_1_exponent_term(function_we_got)
    return term_check
  
def check_for_decreasing(function_we_got: str, x: int):
    decreasing_check = True
    k = 1
    starting_val = abs(eval(function_we_got))
    for k in range(2, x):
        result = abs(eval(function_we_got))
        print(result)
        if starting_val <= result:
            decreasing_check = False
    return decreasing_check
  
def check_for_negative_1_exponent_term(function: str) -> bool:
    if "-1**k" in function:
        return True
    return False
def use_minimum_term_function(error_rate):
  count = 0
  while (  (1 + count) <= (10**(-1*(error_rate/3))) ):
    count += 1

  print(count, "\n")

function_a: str = "(-1**k) * (x**k) / (k**3)"
x: int = 1
check1: bool = check_for_alternating(function_a)
check2: bool = check_for_decreasing(function_a, x)
print(check1 and check2)
error_rate= 10e-4
if check1 and check2:
  use_minimum_term_function(error_rate)


#6 Determine the number of iterations necessary to solve f(x) = x3 + 4x2 – 10 = 0 with accuracy 10-4 using a = -4 and b = 7. 
  
def func(x):
  function =   "x**3 + (4*(x**2)) - 10"
  accuracy =10**(-4)
  left: int = -4
  right: int = 7
  bisection_option= bisection_method(left,right,function, accuracy)
  print(bisection_option)
  
def bisection_method(left,right,function,accuracy):
  diff: float = right-left
  
  iteration_counter = 0
  max_iterations: int = 20

  while (diff >= tol and iteration_counter<= max_iterations):
      iteration_counter += 1
      # get midpoint from class example
      midpoint = (left + right) / 2
      x = mid_point
      evaluated_midpoint = eval(given_function)

    #From class example
      first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
      second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0
      if first_conditional or second_conditional:
        right = mid_point
      else:
        left = mid_point
        diff = abs(right - left)
  print(iteration_counter,"\n")

 