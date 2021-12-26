"""
nums = input()
nums = nums.split(" ")
A = int(nums[0])
B = int(nums[1])
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
"""

"""
score = int(input())
grade = 'A' if score >= 90 else ('B' if score >= 80 else ('C' if score >= 70 else ('D' if score >= 60 else 'F')))
print(grade)

year = int(input())
print("1" if year%400==0 else ("0" if year%100==0 else ("1" if year%4==0 else "0")))


x = int(input())
y = int(input())
quadrant = abs((3 if y < 0 else -2) + (1 if x > 0 else 0))
print(quadrant)

"""

h, m = map(int, input().split())
m -= 45
if m < 0:
    h-=1
    m+=60
if h < 0:
    h+=24
print(h, m)
