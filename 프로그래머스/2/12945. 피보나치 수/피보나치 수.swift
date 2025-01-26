import Foundation

func solution(_ n: Int) -> Int {
    let mod = 1234567
    
    var a = 0
    var b = 1
    
    // a에 이전 피보나치 수 담기
    for _ in 2...n {
        let temp = (a + b) % mod
        a = b
        b = temp
    }
    
    return b
}

