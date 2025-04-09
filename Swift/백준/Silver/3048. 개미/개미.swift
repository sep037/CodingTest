import Foundation

struct Ant {
    var name: Character
    var direction: Character
}

let parts = readLine()!.split(separator: " ").map { Int($0)! }
let rightDirectionAnt = readLine()!
let leftDirectionAnt = readLine()!
let time = Int(readLine()!)!

func jumpAnt(n1: Int, n2: Int, rightDirection: String, leftDirection: String, time: Int) -> String {
    var ants: [Ant] = []

    for rightAnt in rightDirection.reversed() {
        ants.append(Ant(name: rightAnt, direction: "R"))
    }

    for leftAnt in leftDirection {
        ants.append(Ant(name: leftAnt, direction: "L"))
    }

    for _ in 0..<time {
        var i = 0
        var newAnts = ants // 복사본 이용

        while i < ants.count - 1 {
            if ants[i].direction == "R" && ants[i + 1].direction == "L" {
                // 위치만 바꿈, 방향은 그대로
                newAnts[i] = ants[i + 1]
                newAnts[i + 1] = ants[i]
                i += 2
            } else {
                i += 1
            }
        }

        ants = newAnts
    }

    return ants.map { String($0.name) }.joined()
}

let result = jumpAnt(n1: parts[0], n2: parts[1], rightDirection: rightDirectionAnt, leftDirection: leftDirectionAnt, time: time)
print(result)
