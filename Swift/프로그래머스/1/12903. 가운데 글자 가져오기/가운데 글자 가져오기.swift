import Foundation

func solution(_ s:String) -> String {
    let length = s.count
    let mid = length / 2
    
    if length % 2 == 0 {
        return String(s[mid - 1]) + String(s[mid])
    } else {
        return String(s[mid])
    }
}

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}