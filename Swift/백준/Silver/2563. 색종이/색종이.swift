//
//  main.swift
//  2563
//
//  Created by Seungeun Park on 5/6/25.
//

import Foundation

let N = Int(readLine()!)!
var board = Array(repeating: Array(repeating: 0, count: 100), count: 100) // 100 x 100 배열 만들기
var result = 0


for _ in 0 ..< N {
    let location = readLine()!.split(separator: " ").map { Int($0)! }
    var X = location[0]
    var Y = location[1]
    
    for i in X..<X+10 {
        for j in Y..<Y+10 {
            board[i][j] = 1
        }
    }
}

for i in 0..<100 {
    for j in 0..<100 {
        if board[i][j] == 1 {
            result += 1
        }
    }
}

print(result)

