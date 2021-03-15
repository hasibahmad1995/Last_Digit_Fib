# My implementation to find the last digit of the corresponding fibonacci number of a given index.
#Fast Algorithm
fib_list = []

fib_list.append(0)
fib_list.append(1)


for i in range(2,60):
  fib_list.append(fib_list[i-1]+fib_list[i-2])

def last_dig(n):
  for i in range(len(n)):
    print(str(fib_list[n[i]%60])[-1])



m = [int(i) for i in input().split()]



last_dig(m)

# starter code from bohubrihi course
# Naive Algorithm
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
