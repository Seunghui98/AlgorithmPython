final = 0
max_people = 0

for _ in range(4):
    off, on = map(int, input().split())
    final -= off
    final += on
    max_people = max(max_people, final)

print(max_people)
