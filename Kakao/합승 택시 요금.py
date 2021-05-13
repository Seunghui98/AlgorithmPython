# 프로그래머스 2021 Kakao BLIND RECRUITMENT 합승 택시 요금 => 다익스트라(최단거리) 
import heapq
def dijkstra(start, graph, n):
    INF = int(1e9)
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for i in fares:
        x, y, cost = i
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    first_distance = dijkstra(s, graph, n)

    min_dis = first_distance[a] + first_distance[b]
    max_value = max(first_distance[a], first_distance[b])


    dist_dict = []
    for i in range(1, n + 1):
        dist_dict.append((first_distance[i], i))
    dist_dict.sort()

    for i in dist_dict:
        dist, start = i[0], i[1]
        if dist > max_value:
            print(dist)
            break
        dist_list = dijkstra(start, graph, n)
        min_dis = min(min_dis, (dist_list[a] + dist_list[b] + dist))

    answer = min_dis
    return answer
