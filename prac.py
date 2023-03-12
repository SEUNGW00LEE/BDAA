# 260000
# 4
# 20000 5
# 30000 2
# 10000 6
# 5000 8

total = int(input())
t = int(input())
sum = 0
for _ in range(t):
  price, quantity = map(int, input().split())
  sum += price * quantity

if total == sum  :
  print("Yes")
else :
  print("No")