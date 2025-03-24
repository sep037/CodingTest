import Foundation

func solution(_ dots: [[Int]]) -> Int {
    func slope(_ p1: [Int], _ p2: [Int]) -> Double {
        return Double(p2[1] - p1[1]) / Double(p2[0] - p1[0])
    }
    
    let cases = [
        (dots[0], dots[1], dots[2], dots[3]), 
        (dots[0], dots[2], dots[1], dots[3]),
        (dots[0], dots[3], dots[1], dots[2])  
    ]
    
    for (p1, p2, p3, p4) in cases {
        if slope(p1, p2) == slope(p3, p4) {
            return 1
        }
    }
    
    return 0
}
