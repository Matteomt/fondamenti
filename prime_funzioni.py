def h(n,i):  "divisore di n più piccolo maggiore di i
    if n%(i+1) == 0:
        return i+1
    else:
        return h(n,i+1)
        
def prime(n):  "test primalità
    if h(n,1) == n:
        return 1
    else:
        return 0

def primeh(n,i=1):  "prime e h unite
    if n==i+1 or n==1:
        return 1
    elif n%(i+1) == 0:
        return 0
    else:
        return primeh(n,i+1)

def np(x):  "primo primo > x
    if primeh(x+1) == 1:
        return x+1
    else:
        return np(x+1)

def mc(x):  "cifra più significativa
    if x < 10:
        return x
    else:
        return mc(x/10)

def nc(x):  "numero cifre
    if x < 10:
        return 1
    else:
        return 1+nc(x/10)
