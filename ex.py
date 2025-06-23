n = input()
m = input()
s = {}
s1 = {}
for i in range(len(n)):
    s[n[i]] = s.get(n[i],0)+1
for i in range(len(m)):
    s1[m[i]] = s1.get(m[i],0)+1
if s == s1:
    print('YES')
else:
    print('NO')
