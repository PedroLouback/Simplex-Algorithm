import numpy as np

# Read file and separated variables used in Simplex
def read_file(file):
    with open(file, 'r') as f:
        rows = f.readlines()
        
    n, m = map(int, rows[0].strip().split())
    c = list(map(float, rows[1].strip().split()))
    A = []
    b = []

    for row in rows[2:2+m]:
        coefficients = list(map(float, row.strip().split()))
        A.append(coefficients[:-1])
        b.append(coefficients[-1]) # takes the values ​​resulting from the restrictions

    return n, m, c, A, b

def main():
    import sys
    file = sys.argv[1]
    n, m, c, A, b = read_file(file)