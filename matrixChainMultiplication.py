import sys
def matrixChainMultiplication(dims, i, j):
    if j <= i + 1:
        return 0
    min = sys.maxsize
    for k in range(i + 1, j):
        cost = matrixChainMultiplication(dims, i, k)
        cost = cost + matrixChainMultiplication(dims, k, j)
        cost = cost + ( dims[i] * dims[k] * dims[j] )
        if cost < min:
            min = cost
    return min

if __name__ == '__main__':
    dimens = [1,3,8,4]
    print('The minimum cost is', matrixChainMultiplication(dimens, 0, len(dimens) - 1))
