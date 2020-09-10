
def giaithua(a):
    if a==1:
        return 1
    else: return (a*giaithua(a-1))
print(giaithua(3))
