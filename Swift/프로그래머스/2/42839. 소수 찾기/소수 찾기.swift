import Foundation

func isPrime(_ n: Int) -> Bool {
    if n < 2 { return false }
    if n == 2 { return true }

    let limit = Int(Double(n).squareRoot())
    if limit < 2 { return true }

    for i in 2...limit {
        if n % i == 0 { return false }
    }
    return true
}

func solution(_ numbers:String) -> Int {
    let digits = Array(numbers)
    var visited = Array(repeating: false, count: digits.count)
    var madeNumbers = Set<Int>()

    func dfs(_ current: String) {
        if !current.isEmpty {
            madeNumbers.insert(Int(current)!)
        }

        for i in 0..<digits.count {
            if visited[i] { continue }

            visited[i] = true
            dfs(current + String(digits[i]))
            visited[i] = false
        }
    }

    dfs("")

    return madeNumbers.filter { isPrime($0) }.count
}