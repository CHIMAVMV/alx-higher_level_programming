import sys

# Import the functions from the calculator_1 module
from calculator_1 import add, subtract, multiply, divide

def main():
  # Check that there are exactly 3 arguments
  if len(sys.argv) != 4:
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    sys.exit(1)

  # Get the arguments
  a = int(sys.argv[1])
  operator = sys.argv[2]
  b = int(sys.argv[3])

  # Perform the requested operation
  if operator == '+':
    result = add(a, b)
  elif operator == '-':
    result = subtract(a, b)
  elif operator == '*':
    result = multiply(a, b)
  elif operator == '/':
    result = divide(a, b)
  else:
    print(f'Error: Unknown operator {operator}')
    sys.exit(1)

  # Print the result in the required format
  print(f'{a} {operator} {b} = {result}')
  print()

if __name__ == '__main__':
  main()
