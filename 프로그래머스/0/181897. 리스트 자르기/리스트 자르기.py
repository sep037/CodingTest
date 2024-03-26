#items[start:stop]   리스트의 start 인덱스에서 stop-1 인덱스까지 슬라이싱
#items[start:]       리스트의 start 인덱스에서 리스트의 마지막까지 슬라이싱
#items[:stop]        리스트의 처음부터 stop-1 인덱스까지 슬라이싱
#items[:]            리스트 전체 아이템들 반환(복사본)


def solution(n, slicer, num_list):
    answer = []
    if n==1:
        answer.append(num_list[:slicer[1]+1])
    elif n==2:
        answer.append(num_list[slicer[0]:])
    elif n==3:
        answer.append(num_list[slicer[0]:slicer[1]+1])
    else:
        answer.append(num_list[slicer[0]:slicer[1]+1:slicer[2]])
    return answer[0]