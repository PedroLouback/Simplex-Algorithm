import numpy as np
import time

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

def simplex(c, A, b):
    start_time = time.time()
    num_vars = len(c)
    num_constraints = len(b)

    table = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))
    
    # Populate the simplex table
    table[:-1, :num_vars] = A
    table[:-1, num_vars:num_vars + num_constraints] = np.eye(num_constraints)
    table[:-1, -1] = b
    table[-1, :num_vars] = np.array(c)

    iteration = 0
    while True:
        # Check if the optimal solution
        if all(table[-1, :-1] >= 0):
            break

        # Find the most negative coefficient
        pivot_col = np.argmin(table[-1, :-1])

        # Handle potential infeasibility
        ratios = np.array([table[i, -1] / table[i, pivot_col] if table[i, pivot_col] > 0 else np.inf for i in range(num_constraints)])
        # Find leaving variable
        pivot_row = np.argmin(ratios)
        if ratios[pivot_row] == np.inf:
            raise ValueError("Problema ilimitado")
        
        # Perform pivot operation
        pivot_element = table[pivot_row, pivot_col]
        table[pivot_row, :] /= pivot_element

        for i in range(num_constraints + 1):
            if i != pivot_row:
                table[i, :] -= table[i, pivot_col] * table[pivot_row, :]

        iteration += 1
        print(f"Iteração: {iteration}")
        print(f"Tempo(s): {time.time() - start_time:.4f}")
        print(f"Objetivo: {-table[-1, -1]:.4f}\n")

    print(f"Solução ótima encontrada em {time.time() - start_time:.4f} segundos!")
    print(f"Função objetivo é {-table[-1, -1]:.4f}.\n")
    
    solution = np.zeros(num_vars)
    for i in range(num_vars):
        col = table[:-1, i]
        if np.count_nonzero(col) == 1 and np.isclose(col.sum(), 1):
            row = np.where(col == 1)[0][0]
            solution[i] = table[row, -1]
    
    print("Solução:")
    for i in range(num_vars):
        print(f"x[{i+1}] = {solution[i]:.4f}")

    return solution

if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    n, m, c, A, b = read_file(file)
    simplex(c, A, b)
