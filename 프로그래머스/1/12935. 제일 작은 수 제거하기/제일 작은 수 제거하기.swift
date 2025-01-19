func solution(_ arr: [Int]) -> [Int] {
    // 배열이 비어있거나 원소가 1개인 경우
    guard arr.count > 1 else { // 가드문
        return [-1] 
    }
    // 옵셔널 강제 추출
    let minValue = arr.min()!

    return arr.filter { $0 != minValue }
}