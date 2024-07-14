import sys

input = sys.stdin.read
data = input().split()
    
N = int(data[0])  # 첫 번째 값은 회의의 개수
meetings = []
    
  # 각 회의의 시작 시간과 끝나는 시간을 튜플로 meetings 리스트에 추가
for i in range(1, len(data), 2):
  start = int(data[i])
  end = int(data[i+1])
  meetings.append((start, end))

def max_meetings(N, meetings):
    # 끝나는 시간을 기준으로 정렬, 끝나는 시간이 같으면 시작 시간을 기준으로 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    # 첫 번째 회의를 선택
    count = 1
    end_time = meetings[0][1]
    
    # 나머지 회의를 순회하며 선택 가능한 회의를 카운트
    for i in range(1, N):
        if meetings[i][0] >= end_time:
            count += 1
            end_time = meetings[i][1]
    
    return count

print(max_meetings(N, meetings))
