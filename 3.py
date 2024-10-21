import numpy as np
import sys
from datetime import datetime

def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c

if __name__ == "__main__":
    # Check if size is provided, else use a default value
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    else:
        size = 1000  # Default value if no argument is passed

    # PythonSum
    start = datetime.now()
    c = pythonsum(size)
    delta = datetime.now() - start
    print("The last 2 elements of the sum:", c[-2:])
    print("PythonSum elapsed time in microseconds:", delta.microseconds)

    # NumPySum
    start = datetime.now()
    c = numpysum(size)
    delta = datetime.now() - start
    print("The last 2 elements of the sum:", c[-2:])
    print("NumPySum elapsed time in microseconds:", delta.microseconds)
