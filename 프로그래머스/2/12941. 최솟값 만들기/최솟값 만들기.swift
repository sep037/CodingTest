import Foundation

func solution(_ A: [Int], _ B: [Int]) -> Int {
    // 배열 A는 오름차순, 배열 B는 내림차순으로 정렬
    let sortedA = A.sorted()
    let sortedB = B.sorted(by: >)
    
    var result = 0
    
    for i in 0..<A.count {
        result += sortedA[i] * sortedB[i]
    }
    
    return result
}
