while True:
    num = input().strip()
    
    if num == "0":
        break
    
    # 뒤집어서 팰린드롬인지 확인
    if num == num[::-1]:
        print("yes")
    else:
        print("no")
