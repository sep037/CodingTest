//
//  main.swift
//  1713
//
//  Created by Seungeun Park on 5/13/25.
//

import Foundation

let picturelimit = Int(readLine()!)!
let recommendCount = Int(readLine()!)!

struct Candidate {
    var num : Int
    var votes : Int
    var time : Int = 0
}

var time = 0

var candidateArray : [Candidate] = []
let recommendations = readLine()!.split(separator: " ").map { Int($0)! }

for candidateNum in recommendations {
    time += 1 // 일단 시간은 흘러가니까 ..
    
    /*
     if 후보에 올라가있지 않으면 {
         if 사진틀이 비어있으면 or 자리가 있으면 {
             // 그냥 올리기
         } else {
             // 가장 적게 추천받은 사람 제거하고 새 후보 올리기
         }
     } else {
         // 이미 올라가 있으면 투표 수만 올리기
     }
     */
    
    if let index = candidateArray.firstIndex(where: {$0.num == candidateNum}) { // 해당 후보 번호가 있는 인덱스 확인
        candidateArray[index].votes += 1 // 이미 올라가 있으면 수만 올리기
    } else { // 올라가있지 않으면
        if candidateArray.count < picturelimit { // 자리 있으면 그냥 추가
            candidateArray.append(Candidate(num: candidateNum, votes: 1, time: time))
        } else { // 자리가 없으면 비교해주기
            candidateArray.sort { // 추천 수 같으면
                if $0.votes == $1.votes {
                    return $0.time < $1.time // 시간으로 비교
                }
                return $0.votes < $1.votes // 아니면 추천 수로 비교
                }
            candidateArray.removeFirst()
            candidateArray.append(Candidate(num: candidateNum, votes: 1, time: time))
            }
            
        }
        
    }
    
let result = candidateArray.map { $0.num }.sorted() // 후보 번호 오름차순 !
print(result.map { String($0) }.joined(separator: " "))
    
