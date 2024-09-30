import sys

# 점수 같은 건 매핑하면 편함 1
grade_map = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}

def calculate_gpa(lessons):
    total_score = 0  # 학점이랑 평점 곱한 거
    total_credits = 0  # 학점 총합

    for lesson in lessons:
        data = lesson.split() 
        # course_name = data[0] 이건 쓸모 없지만 ~ ..
        credits = float(data[1])
        grade = data[2]

        # P는 계산에서 제외
        if grade == 'P':
            continue

        # 학점이랑 평점 곱한 거
        total_score += credits * grade_map[grade]
        # 학점의 총합 계산
        total_credits += credits
    if total_credits == 0:
        return 0
    return total_score / total_credits

input_lines = sys.stdin.readlines()

gpa = calculate_gpa(input_lines)
print(gpa)
