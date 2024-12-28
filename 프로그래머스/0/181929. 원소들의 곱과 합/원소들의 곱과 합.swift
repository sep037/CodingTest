func solution(_ num_list: [Int]) -> Int {
    var sum = 0
    var mul = 1

    for num in num_list {
        sum += num
        mul *= num
        // 곱이 이미 합의 제곱보다 크면 바로 0 반환
        if mul > sum * sum {
            return 0
        }
    }

    return 1
}
