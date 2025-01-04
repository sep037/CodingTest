import Foundation

func solution(_ n: Int) -> Int {
    // 정수를 문자열로 변환하여 각 자리 숫자를 배열로 만듦
    let digits = String(n).compactMap { $0.wholeNumberValue }

    let result = digits.reduce(0, +)
    return result
}
