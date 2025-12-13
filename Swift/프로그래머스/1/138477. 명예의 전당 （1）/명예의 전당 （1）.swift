import Foundation

func solution(_ k:Int, _ score:[Int]) -> [Int] {
    var hall = [Int]()
    var result = [Int]()
    
    for s in score {
        hall.append(s)
        hall.sort(by: >) // 내림차순 정렬
        
        if hall.count > k {
            hall.removeLast()
        }
        
        result.append(hall.last!)
    }
    return result
}