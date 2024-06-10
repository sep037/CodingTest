def solution(phone_number):

    length = len(phone_number)

    masked_number = '*' * (length - 4) + phone_number[-4:]
    return masked_number
