import Foundation

let input = readLine()!.components(separatedBy: " ").map { Int($0)! }
let (n, m) = (input[0], input[1])

for _ in 0..<m {
    print(String(repeating: "*", count: n))
}
