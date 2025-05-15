//
//  main.swift
//  1063
//
//  Created by Seungeun Park on 5/15/25.
//

import Foundation

// 위치 문자열을 숫자 좌표로 바꾸는 함수
func chessToTuple(pos: String) -> (Int, Int) {
    let col = Int(pos.first!.asciiValue! - Character("A").asciiValue!) // A~H → 0~7
    let row = Int(String(pos.last!))! - 1                              // 1~8 → 0~7
    return (row, col)
}

// 숫자 좌표를 체스 문자열로 바꾸는 함수
func tupleToChess(_ row: Int, _ col: Int) -> String {
    let colChar = String(UnicodeScalar(col + Int(Character("A").asciiValue!))!)
    let rowStr = String(row + 1)
    return colChar + rowStr
}

// 입력 처리
let location = readLine()!.split(separator: " ")
let kingLocation = String(location[0])
let stoneLocation = String(location[1])
let N = Int(location[2])!

// 위치를 숫자 튜플로 변환
var king = chessToTuple(pos: kingLocation)     // (row, col)
var stone = chessToTuple(pos: stoneLocation)   // (row, col)

let directionMap: [String: (Int, Int)] = [
    "R": (0, 1),
    "L": (0, -1),
    "B": (-1, 0),
    "T": (1, 0),
    "RT": (1, 1),
    "LT": (1, -1),
    "RB": (-1, 1),
    "LB": (-1, -1)
]

for _ in 0..<N {
    let command = readLine()!
    let (dy, dx) = directionMap[command]!  // 이동 방향

    let newKing = (king.0 + dy, king.1 + dx)

    if (0..<8).contains(newKing.0) && (0..<8).contains(newKing.1) { // 이 문법은 구글링함 !
        if newKing == stone { // 왕이랑 돌이랑 위치가 같으면
            // 돌도 같은 방향으로 이동
            let newStone = (stone.0 + dy, stone.1 + dx)
            // 돌도 이동 가능한지 확인
            if (0..<8).contains(newStone.0) && (0..<8).contains(newStone.1) {
                king = newKing
                stone = newStone
            }
            // 돌이 벗어나면 킹도 못 감
        } else {
            // 돌이 없으니 킹만 이동
            king = newKing
        }
    }
}

print(tupleToChess(king.0, king.1))
print(tupleToChess(stone.0, stone.1))

