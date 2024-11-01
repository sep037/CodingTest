def solution(bandage, health, attacks):
    t, x, y = bandage  # 붕대 감기 시전 시간, 초당 회복량, 추가 회복량
    current_health = health
    success_time = 0  # 연속 붕대 감기 성공 시간
    current_time = 1  # 현재 시간
    attack_index = 0  # 공격 인덱스
    
    # 공격 리스트가 남아있는 동안 시간 경과 처리
    while current_time <= (attacks[-1][0] if attacks else 0):
        # 현재 시간에 공격이 있는 경우
        if attack_index < len(attacks) and attacks[attack_index][0] == current_time:
            # 현재 체력에서 공격 피해량을 빼기
            current_health -= attacks[attack_index][1]
            if current_health <= 0:
                return -1  # 체력이 0 이하가 되면 캐릭터가 죽음 ㅠㅠ
            
            # 공격이 있었다면 붕대 감기 실패로 간주
            success_time = 0
            attack_index += 1
        else:
            # 공격이 없는 경우 체력 회복
            current_health = min(current_health + x, health)  # 최대 체력을 초과하면 안됨
            success_time += 1
            
            # 붕대 감기 성공 시간이 t초 이상인 경우 추가 회복 적용
            if success_time == t:
                current_health = min(current_health + y, health)
                success_time = 0
        
        # 1초 경과
        current_time += 1

    return current_health
