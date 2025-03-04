func solution(_ numbers: [Int]) -> Int {
    let totalSum = 45 // 0부터 9까지의 합 (0+1+2+...+9)
    var sum = 0

    for num in numbers { // numbers 배열 요소를 순회하며 합 구하기
        sum += num
    }

    return totalSum - sum // 전체 합에서 numbers 배열의 합을 빼기
}
