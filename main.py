import heapq
import random
from pyscript import window, document

# 도로 그래프 생성
graph = {}
for i in range(1, 11):
    for j in range(1, 11):
        node = f'{i},{j}'
        neighbors = {}
        # 각 도로의 길이를 1로 설정하고 속도는 그대로 유지
        for k in range(1, 5):
            if i > 1:
                neighbors[f'{i-1},{j}'] = (1, 1)  # 거리는 1, 속도는 1 (정상)
            if i < 10:
                neighbors[f'{i+1},{j}'] = (1, 1)
            if j > 1:
                neighbors[f'{i},{j-1}'] = (1, 1)
            if j < 10:
                neighbors[f'{i},{j+1}'] = (1, 1)
        graph[node] = neighbors

# 횡단보도와 신호등 변수 설정
crosswalk_prob = 0.3  # 횡단보도가 있는 확률
traffic_light_prob = 0.4  # 신호등이 있는 확률

# 각 도로에 횡단보도와 신호등 설정
for i in range(1, 11):
    for j in range(1, 11):
        node = f'{i},{j}'
        for neighbor in graph[node]:
            if random.random() < crosswalk_prob:
                distance, speed = graph[node][neighbor]
                graph[node][neighbor] = (distance, speed + 1)  # 속도를 1 줄여서 시간을 지연
            if random.random() < traffic_light_prob:
                distance, speed = graph[node][neighbor]
                graph[node][neighbor] = (distance, speed + 1)  # 속도를 1 줄여서 시간을 지연

# 출발점, 경유지, 도착점 설정
start_point = "1,1"
waypoint = "5,5"
end_point = "10,10"

def dijkstra(graph, start, end):
    # 시작점에서 각 정점까지의 시간을 무한대로 초기화
    times = {vertex: float('infinity') for vertex in graph}
    # 시작점에서 시작점까지의 시간은 0으로 설정
    times[start] = 0
    
    # 우선순위 큐를 생성하고 시작점을 추가
    priority_queue = [(0, start)]
    
    while priority_queue:
        # 우선순위 큐에서 시간이 가장 짧은 정점을 꺼냄
        current_time, current_vertex = heapq.heappop(priority_queue)
        
        # 현재 정점까지의 시간이 이미 더 짧은 경우 무시
        if current_time > times[current_vertex]:
            continue
        
        # 현재 정점의 이웃 정점들을 순회
        for neighbor, (distance, speed) in graph[current_vertex].items():
            total_time = current_time + distance / speed
            # 더 짧은 시간을 발견한 경우 업데이트
            if total_time < times[neighbor]:
                times[neighbor] = total_time
                heapq.heappush(priority_queue, (total_time, neighbor))
    
    # 목적지까지의 최단 시간 반환
    return times[end]

# 최단 시간 경로 계산
shortest_time = dijkstra(graph, start_point, waypoint) + dijkstra(graph, waypoint, end_point)
print(f"{start_point}에서 {waypoint}를 거쳐 {end_point}까지의 최단 시간은 {shortest_time}입니다.")
