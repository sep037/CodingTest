from collections import Counter
import math

def min_sets_needed(room_number):
    # 방 번호에서 각 숫자의 빈도를 세기
    count = Counter(room_number)
    
    # 6과 9는 같은 숫자로 취급
    six_nine_count = count.get('6', 0) + count.get('9', 0)
    
    # 6과 9를 합친 후 반올림하여 필요한 개수 계산
    count['6'] = math.ceil(six_nine_count / 2)
    
    # 더 이상 9는 따로 필요하지 않으므로 삭제
    if '9' in count:
        del count['9']
    
    # 최댓값이 필요한 세트의 개수
    return max(count.values())

room_number = input()
print(min_sets_needed(room_number))
