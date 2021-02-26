from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)

  return right_index - left_index

# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
revesed_array = [[] for _ in range(10001)]
def solution(words, queries):
  answer = []
  for word in words:
    array[len(word)].append(word)
    revesed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입
  
  # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
  # 정렬 O(NlogN)
  for i in range(10001):
    array[i].sort()
    reversed[i].sort()
  
  # 쿼리를 하나씩 확인하며 처리
  # 탐색 O(N * logM)
  for q in queries:
    if q[0] != '?' # 접미사에 와일드 카드가 붙은 경우
      res = count_by_range(array[len(q)], q.replace('?', a), q.replace('?','z'))
    else: # 접두사에 와일드카드가 붙은 겨우
      res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', a), q[::-1].replace('?', z))
    # 검색된 단어의 개수를 저장
    answer.append(res)
  return answer
  
