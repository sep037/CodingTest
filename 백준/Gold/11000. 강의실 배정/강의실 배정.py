import heapq
# 끝날 시간을 정렬할 필요는 없고 최소힙을 사용하여 강의실에서 가장 빨리 끝나는 수업의 종료 시간을 추적한다.

N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]

def min_classrooms(classes):
    # 시작 시간 기준으로 오름차순 정렬
    classes.sort(key=lambda x: x[0])
    
    # 최소 힙 생성 (끝나는 시간을 추적)
    heap = []
    
    # 첫 번째 수업의 끝나는 시간을 힙에 추가
    heapq.heappush(heap, classes[0][1])
    
    # 두 번째 수업부터 반복
    for i in range(1, len(classes)):
        # 가장 빨리 끝나는 수업의 종료 시간
        earliest_end = heap[0]
        
        # 현재 수업의 시작 시간과 비교
        if classes[i][0] >= earliest_end:
            # 현재 수업을 기존 강의실에 배정할 수 있음 (종료 시간 갱신)
            heapq.heappop(heap)
            heapq.heappush(heap, classes[i][1])
        else:
            # 새로운 강의실 필요
            heapq.heappush(heap, classes[i][1])
    
    # 힙의 크기가 필요한 최소 강의실 수
    return len(heap)

print(min_classrooms(classes))
