func solution(_ x: Int) -> Bool {
    let digitSum = String(x).map { Int(String($0))! }.reduce(0, +)
    return x % digitSum == 0
}