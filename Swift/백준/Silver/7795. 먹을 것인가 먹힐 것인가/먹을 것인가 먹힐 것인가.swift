//
//  main.swift
//  7795
//
//  Created by Seungeun Park on 5/5/25.
//

import Foundation


let N = Int(readLine()!)! // 테스트 케이스 수

for _ in 0 ..< N {
    let counts = readLine()!.split(separator: " ").map { Int($0)! }
    let countA = counts[0]
    let countB = counts[1]
    
    let Aarray = readLine()!.split(separator: " ").map { Int($0)! }
    let Barray = readLine()!.split(separator: " ").map { Int($0)! }

    print(comparison(A: Aarray, B: Barray))
}

//func comparison(A: [Int], B: [Int]) -> Int {
//    var count = 0
//    for a in A {
//        for b in B {
//            if a > b {
//                count += 1
//            }
//        }
//    }
//    return count
//}
// 시간 초과 ㅋㅋ

func comparison(A: [Int], B: [Int]) -> Int {
    let sortedA = A.sorted()
    let sortedB = B.sorted()
    var count = 0
    
    var j = 0

    for a in sortedA {
        while j < sortedB.count && sortedB[j] < a {
            j += 1
        }
        count += j
    }
    return count
}



