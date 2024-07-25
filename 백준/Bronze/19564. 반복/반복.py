n = input()
cnt = 1

for i in range(len(n)-1):
  if ord(n[i]) < ord(n[i+1]):
    continue
  else:
    cnt += 1

print(cnt)