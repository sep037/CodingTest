//
//  main.swift
//  5525
//
//  Created by Seungeun Park on 5/7/25.
//

import Foundation

let N = Int(readLine()!)!
let _ = Int(readLine()!)! // 문자열 길이는 필요 없음
let S = Array(readLine()!) // 문자열을 배열로 바꿔 인덱싱하기 쉽게

var i = 0
var match = 0
var count = 0

while i < S.count - 2 {
    if S[i] == "I" && S[i+1] == "O" && S[i+2] == "I" {
        match += 1
        if match == N {
            count += 1
            match -= 1 // 중첩 가능한 패턴 고려
        }
        i += 2 // IOI 다음은 'I'부터 다시 검사
    } else {
        match = 0
        i += 1
    }
}

print(count)
