# Combinatorial Solution
import math
cnt = 0
max = 13
for a in range(1, max+1):
    for b in range(a + 1, max+1):
        for c in range(b + 1, max+3):
            if abs(b - c) < a and b + c > a:
                cnt = cnt + 1
print("total number of triangles : "+str(cnt))
print("Probability : "+str(cnt/math.comb(max,3)))