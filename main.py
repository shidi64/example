myset1 = set(map(int, input().split()))
myset2 = set(map(int, input().split()))
myset3 = set(map(int, input().split()))
all_grade = myset1 | myset2
result = myset3-all_grade
print(*sorted(result)[::-1])
