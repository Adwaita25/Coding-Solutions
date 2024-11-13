import math
 
n, m, a = map(int, input().split())
 
hight = math.ceil(n / a)
width = math.ceil(m / a)
total = hight * width
print(total)
