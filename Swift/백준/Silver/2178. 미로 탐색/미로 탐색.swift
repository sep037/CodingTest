import Foundation

let moveX = [-1, 1, 0, 0]
let moveY = [0, 0, -1, 1] // 상 하 좌 우

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0]
let m = input[1]

var miro: [[Int]] = []
for _ in 0..<n {
    let line = readLine()!
    var row: [Int] = []
    for char in line {
        let number = Int(String(char))!
        row.append(number)
    }
    miro.append(row)
}

// 방문 기록
var visited: [[Bool]] = []
for _ in 0..<n {
    visited.append(Array(repeating: false, count: m))
}

func bfs(startRow: Int, startColumn: Int) -> Int {
    // 현재 위치와 이동 거리 표시하기
    var queue: [(row: Int, col: Int, steps: Int)] = [(startRow, startColumn, 1)]
    visited[startRow][startColumn] = true

    while !queue.isEmpty { // 큐는 탐색해야할 다음 위치를 담고 이씀
        let current = queue.removeFirst()

        // 다음 위치가 도착지라면 이동 거리 반환
        if current.row == n - 1 && current.col == m - 1 {
            return current.steps
        }

        // 이동
        for direction in 0..<4 { // 순서대로 상 하 좌 우
            let nextRow = current.row + moveX[direction]
            let nextColumn = current.col + moveY[direction]
               
            // 크기가 제한적이니 이동 반경 제한하기 ! + 다음칸 이동 가능한지 확인하기
            if nextRow >= 0 && nextRow < n && nextColumn >= 0 && nextColumn < m {
                if miro[nextRow][nextColumn] == 1 && !visited[nextRow][nextColumn] { // 숫자가 1이고 방문하지 않았으면 방문하기
                    visited[nextRow][nextColumn] = true
                    queue.append((nextRow, nextColumn, current.steps + 1))
                }
            }
        }
    }

    // 도착할 수 없을 때
    return -1
}

let result = bfs(startRow: 0, startColumn: 0) // 시작점 !
print(result)
