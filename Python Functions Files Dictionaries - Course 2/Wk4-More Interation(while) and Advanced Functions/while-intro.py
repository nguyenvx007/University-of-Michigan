def sumto(abound):
    """Add sum 1+2+3...n"""
    #sum so far
    current_sum=0
    #count so far
    anumber = 0
    while anumber <= abound:
        current_sum=current_sum+anumber
        anumber = anumber+1
    return current_sum
abound = 4
print(sumto(abound))
