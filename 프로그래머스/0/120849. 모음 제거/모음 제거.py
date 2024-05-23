def solution(my_string):
    answer = ''
    arr = ['a', 'e', 'i', 'o', 'u']
    for i in arr:
        my_string = my_string.replace(i, "")
    return my_string