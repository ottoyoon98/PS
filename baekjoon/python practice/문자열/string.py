"""
print(ord(input()))


input();print(sum(map(int,input())))
    


ls =[-1]*26
w=input()
for i in range(len(w)):
    if ls[ord(w[i])-97]==-1:
        ls[ord(w[i])-97] = i
print(" ".join(map(str,ls)))


for case in range(int(input())):
    line = input().split()
    print("".join(c*int(line[0]) for c in line[1]))



"""

"""
word=input().upper()
cnt = [0]*26
for c in word:
    cnt[ord(c)-65]+=1
answer = [i for i in range(26) if cnt[i] == max(cnt)]
print("?" if len(answer)>1 else chr(answer[0]+65))
"""

#print(len(input().strip().split()))

"""
a,b = map(int,input()[::-1].split())
print(a if a>b else b)
"""

#print(sum((((ord(i)-(65 if i <='R' else (66 if i<='Y' else 67)))//3+3)) for i in input()))


"""
w=input()
print(len(w)-(w.count('c=')+w.count('c-')+w.count('d-')+w.count('lj')+w.count('nj')+w.count('s=')+w.count('z=')+w.count('dz=')))
"""


cnt=0
for i in range(int(input())):
    al = [0]*26
    pre=0
    cnt+=1
    for j in input():
        if al[ord(j)-97]==1 and j != pre:
            cnt-=1
            break
        else:
            al[ord(j)-97]=1
        pre = j
print(cnt)
