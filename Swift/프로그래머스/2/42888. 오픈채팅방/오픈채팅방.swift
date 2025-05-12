import Foundation

func solution(_ records: [String]) -> [String] {
    
    var nickName: [String: String] = [:] // 유저 아이디 : 닉네임 딕셔너리
    var notes: [(String, String)] = [] // 명령어와 닉네임 튜플 배열
    
    for record in records {
        let notifications = record.split(separator: " ").map { String($0) } // substring을 string으로 바꿔줌
        let command = notifications[0] // 명령어 담기
        let userId = notifications[1] // 유저 아이디 담기
        
        if command == "Enter" {
            nickName[userId] = notifications[2] // 기존 닉네임 값 담기 + 기존 닉네임과 달라지면 새로운 닉네임 넣기
            notes.append(("Enter", userId))
        } else if command == "Leave" {
            notes.append(("Leave", userId)) // 그냥 기록만 남기기
        } else if command == "Change" {
            nickName[userId] = notifications[2] // 변경된 닉네임 담기
        }
    }
    
    var result: [String] = []
    
    for (command, userId) in notes {
        let name = nickName[userId]! // nickName은 무조건 존재함 -> 강제추출
        let message = command == "Enter" ? "\(name)님이 들어왔습니다." : "\(name)님이 나갔습니다."
        result.append(message)
    }
    
    return result
}