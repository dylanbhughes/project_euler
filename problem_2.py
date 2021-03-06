"""
Project Euler: Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fibonacciEvenSum(mx):
    allFib = [1,2]
    sumEven = 0
    while sum(allFib[-2:]) < mx:
        allFib.append(sum(allFib[-2:]))    
    for n in allFib:
        if n % 2 == 0:
            sumEven+=n
    return sumEven
