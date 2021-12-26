"""
def fac(n):
    return 1 if n<=1 else fac(n-1)*n
print(fac(int(input())))



def fibo(n):
    return n if n<=1 else fibo(n-1)+fibo(n-2)
print(fibo(int(input())))




from sys import stdout as so
def star(a,k):
    if k>3 and a//(k//3)==1:
        temp = star(a%(k//3),k//3)
        return temp+" "*(k//3)+temp
    elif k>3 and a//(k//3)!=1:
        return star(a%(k//3),k//3)*3
    else:
        return "* *" if a%3==1 else "***"
n = int(input())
for i in range(n):
    so.write(star(i,n)+"\n")


"""

def move(s,e,c):
    if c==1:
        print(s,e)
    else:
        move(s,6-s-e,c-1)
        move(s,e,1)
        move(6-s-e,e,c-1)
n=int(input())
print(2**n-1)
move(1,3,n)
