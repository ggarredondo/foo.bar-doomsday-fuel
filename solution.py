import numpy as np
import fractions as f


def standard_form(matrix):
    rows, columns = matrix.shape
    swaps = 0
    to_swap = []

    for i in range(0, rows):
        if not np.any(matrix[i]):
            matrix = np.row_stack((matrix[i], matrix))
            matrix = np.delete(matrix, i+1, 0)
            swaps += 1
        else:
            to_swap.append(i)
            matrix[i] /= matrix[i].sum()

    aux = matrix.copy()
    counter = 0
    for i in to_swap:
        matrix = np.column_stack((matrix, aux[:, i]))
        matrix = np.delete(matrix, i-counter, 1)
        counter += 1

    for i in range(0, swaps):
        matrix[i, i] = 1
    return matrix, swaps


def solution(m):
    states, swaps = standard_form(np.matrix(m, dtype=float))
    FR = states
    if len(states) > 1:
        Q = states[swaps:, swaps:]
        I = np.diag(np.ones(len(Q)))
        R = states[swaps:, :swaps]
        F = (I-Q)**(-1)
        FR = F*R

    result = map(f.Fraction, FR[0].A1.tolist())
    numerators = []
    denominators = []
    for i in range(0, len(result)):
        result[i] = result[i].limit_denominator(100)
        denominators.append(result[i].denominator)
    lcm = np.lcm.reduce(denominators)
    for i in range(0, len(result)):
        numerators.append(result[i].numerator*lcm/result[i].denominator)
    numerators.append(lcm)

    return numerators