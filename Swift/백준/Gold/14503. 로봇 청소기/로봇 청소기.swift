//
//  main.swift
//  14503
//
//  Created by Seungeun Park on 5/19/25.
//

import Foundation

// 방향을 나타내는 상수: 북(0), 동(1), 남(2), 서(3)
// 각각의 방향에 대한 이동 좌표 변화량 (dy, dx)
let dy = [-1, 0, 1, 0] // 북, 동, 남, 서
let dx = [0, 1, 0, -1]

let size = readLine()!.split(separator: " ").map { Int($0)! }
let N = size[0], M = size[1]

let robotInit = readLine()!.split(separator: " ").map { Int($0)! }
var r = robotInit[0], c = robotInit[1], d = robotInit[2] // 로봇의 초기 위치와 방향

// 방의 상태 저장: 0은 청소 가능, 1은 벽
var map: [[Int]] = []
for _ in 0..<N {
    map.append(readLine()!.split(separator: " ").map { Int($0)! })
}

// 방문 여부 확인용 배열 (청소했는지 여부)
var cleaned = Array(repeating: Array(repeating: false, count: M), count: N)
var cleanedCount = 0 // 청소한 칸 개수

while true {
    // 1. 현재 위치가 청소되지 않았으면 청소
    if !cleaned[r][c] {
        cleaned[r][c] = true
        cleanedCount += 1
    }

    var moved = false // 4방향 중 이동했는지 여부

    // 2. 반시계 방향으로 4번까지 탐색
    for _ in 0..<4 {
        // 왼쪽 방향으로 회전
        d = (d + 3) % 4 // 북(0) → 서(3) → 남(2) → 동(1) 순서

        let nr = r + dy[d]
        let nc = c + dx[d]

        // 이동할 칸이 청소 안 된 빈 칸이면 이동
        if map[nr][nc] == 0 && !cleaned[nr][nc] {
            r = nr
            c = nc
            moved = true
            break // 전진했으므로 다시 1번부터 시작
        }
    }

    // 3. 네 방향 모두 청소 못하면 → 후진
    if !moved {
        let back = (d + 2) % 4 // 현재 방향의 반대 방향
        let br = r + dy[back]
        let bc = c + dx[back]

        // 뒤가 벽이면 종료
        if map[br][bc] == 1 {
            break
        } else {
            // 후진은 방향 그대로 유지하면서 위치만 이동
            r = br
            c = bc
        }
    }
}

// 결과 출력
print(cleanedCount)

