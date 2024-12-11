import Foundation

func solution(_ my_string: String, _ k: Int) -> String {
    var result = "" // 결과 문자열을 저장할 변수
    for _ in 1...k {
        result += my_string // 반복할 때마다 my_string을 추가
    }
    return result
}
