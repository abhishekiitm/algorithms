# PROBLEM STATEMENT: Count the number of 2s between 0 and n
# Example: For n=22, a total of 6 2s appear as digits from 0 to 22 - (2, 12, 20, 21, 22);

def calc_twos_brute(n):
    cnt = 0
    for i in range(n+1):
        l = [int(x) for x in str(i)]
        cnt=cnt+l.count(2)
    return cnt