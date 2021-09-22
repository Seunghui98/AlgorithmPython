# 파일 정리 - BOJ 20291
# 단순 구현 - 딕셔너리(해쉬맵), 리스트 활용
n = int(input())
file_dict = {}
file_list = []

for _ in range(n):
    file = input().split('.')
    if file[1] not in file_dict.keys():
        file_dict[file[1]] = 1
        file_list.append(file[1])
    else:
        file_dict[file[1]] += 1

for f in sorted(file_list):
    print(f, file_dict[f])

