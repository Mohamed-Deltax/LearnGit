def factorial(n):
    
    """
    Return the factorial of n, an exact integer >= 0.

    """

    import math
    # I added this
    # second change
    # third change
    # fourth change
    # fifth change
    # another change 
    # changes in sameer_br1  commit_br_1
    # changes in sameer_br1  commit_br_1
    # changes in sameer_br1  commit_br_1
    
    # master changes after two branches , three commits for each branch commit 14  
    # master changes after two branches , three commits for each branch commit 15
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:         # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


# this commit after linking with two github account
# AAA