//
//  main.swift
//  1758
//
//  Created by Seungeun Park on 5/5/25.
//

import Foundation

let N = Int(readLine()!)!

var tip : [Int] = []
var sum : Int = 0

for _ in 0 ..< N {
    tip.append(Int(readLine()!)!)
}

tip.sort { $0 > $1 } // 내림차순

for i in 0 ..< N {
    if tip[i] - i < 0 {
        sum += 0
    } else {
        sum += tip[i] - i
    }
}

print(sum)


