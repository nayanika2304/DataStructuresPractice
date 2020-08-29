'''
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
'''

def fib(n):
    if n < 1:
        raise ValueError('Must be positive Integer')
    elif n < 3:
        return 1
    elif n < 4:
        return 2
    else:
        a = 1
        b = 1
        c = 2
        d = 4

        for i in xrange(n - 4):
            a = b
            b = c
            c = d
            d = a + b + c

        return d


def fib_r(n):
    memo = {}
    return fib_r_helper(n, memo)


def fib_r_helper(n, memo):
    if n in memo:
        return memo[n]

    if n < 1:
        raise ValueError('Must be positive Integer')
    elif n < 3:
        return 1
    elif n < 4:
        return 2
    else:
        result = fib_r(n - 1) + fib_r(n - 2) + fib_r(n - 3)
        memo[n] = result
        return result
