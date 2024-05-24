import heapq
import random
from pyscript import window, document
from pyscript.js_modules import code

canvas = document.getElementById("boardCanvas")
ctx = canvas.getContext("2d")

# 도로 그래프 생성
graph = {}
for i in range(0, 11):
  for j in range(0, 11):
    node = f'{i},{j}'
    neighbors = {}
    # 각 칸마다 상하좌우로 이동 가능하며 이동하는데 걸리는 시간은 1분
    if i > 1:
      neighbors[f'{i-1},{j}'] = 1
    if i < 10:
      neighbors[f'{i+1},{j}'] = 1
    if j > 1:
      neighbors[f'{i},{j-1}'] = 1
    if j < 10:
      neighbors[f'{i},{j+1}'] = 1
    graph[node] = neighbors

# 횡단보도와 신호등 변수 설정
crosswalk_prob = 0.1  # 횡단보도가 있는 확률
traffic_light_prob = 0.1  # 신호등이 있는 확률

# 각 도로에 횡단보도와 신호등 설정
for i in range(0, 11):
  for j in range(0, 11):
    node = f'{i},{j}'
    for neighbor in graph[node]:
      print(graph[node][neighbor])
      if random.random() < crosswalk_prob:
        graph[node][neighbor] += 1
        code.drawDot(ctx, 54 * i, 54 * (10 - j), 5, "rgb(0, 255, 0)")
      if random.random() < traffic_light_prob:
        graph[node][neighbor] += 1
        code.drawDot(ctx, 54 * i, 54 * (10 - j), 5, "rgb(0, 255, 0)")
      print(graph[node][neighbor])


sran1 = random.randint(0, 1)
sran2 = random.randint(0, 1)
wran1 = random.randint(3, 7)
wran2 = random.randint(3, 7)
eran1 = random.randint(5, 10)
eran2 = random.randint(5, 10)
# 출발점, 경유지, 도착점 설정
start_point = f"{sran1},{sran2}"
waypoint = f"{wran1},{wran2}"
end_point = f"{eran1},{eran2}"

code.drawDot(ctx, 54 * sran1, 54 * (10 - sran2), 5, "rgb(0, 0, 0)")
code.drawDot(ctx, 54 * wran1, 54 * (10 - wran2), 5, "rgb(255, 0, 0)")
code.drawDot(ctx, 54 * eran1, 54 * (10 - eran2), 5, "rgb(0, 0, 255)")

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
    for neighbor, time in graph[current_vertex].items():
      total_time = current_time + time
      # 더 짧은 시간을 발견한 경우 업데이트
      if total_time < times[neighbor]:
        times[neighbor] = total_time
        #print(neighbor.split(",")[0])
        heapq.heappush(priority_queue, (total_time, neighbor))
        #code.drawArrow(ctx, 54 * int(current_vertex.split(",")[0]), 54 * (10 - int(current_vertex.split(",")[1])), 54 * int(neighbor.split(",")[0]), 54 * (10 - int(neighbor.split(",")[1])), "red")

  # 목적지까지의 최단 시간 반환
  return times[end]

# 최단 시간 경로 계산
shortest_time = dijkstra(graph, start_point, waypoint) + dijkstra(graph, waypoint, end_point)
print(dijkstra(graph, start_point, waypoint))
print(dijkstra(graph, waypoint, end_point))
print(f"({start_point})에서 ({waypoint})를 거쳐 ({end_point})까지의 최단 시간은 {shortest_time}분입니다.")