import Foundation

func solution(_ new_id:String) -> String {
    var id = new_id
    
    // 1단계 : 소문자로 치환하기
    id = id.lowercased()
    
    // 2단계 : 허용하는 문자만 남기고 필터링하기
    let allowed = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    id = id.filter { allowed.contains($0) }
    
    // 3단계 : 두 번의 ..을 .으로 치환하기
    while id.contains("..") {
        id = id.replacingOccurrences(of: "..", with: ".")
    }
    
    // 4단계 : 앞 뒤의 . 삭제하기
    if id.hasPrefix(".") { id.removeFirst() }
    if id.hasSuffix(".") { id.removeLast() }
    
    // 5단계 : 문자열이 비어있으면 a 대입하기
    if id.isEmpty { id = "a" }
    
    // 6단계 : 15자로 제한
    if id.count >= 16 {
        id = String(id.prefix(15))
        if id.hasSuffix(".") { id.removeLast() }
    }
    
    // 7단계 : 3자보다 작으면 마지막 글자 반복
    while id.count < 3 {
        id.append(id.last!)
    }
    
    return id
}