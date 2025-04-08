func solution(_ files:[String]) -> [String] {
    struct FilePart {
        let head : String
        let number : Int
        let originalfile : String
    }
    
    var FileList : [FilePart] = []
    
    for file in files {
        var head = "" // head를 저장할 변수
        var number = "" // number을 저장할 변수
        var numberStarted = false // 숫자가 시작했는지 담는 변수
        
        for char in file {
            if char.isNumber { // 숫자가 시작되었는지 감별하기
                numberStarted = true
                if number.count < 5 { 
                    number.append(char) // 숫자 다섯자리 되기 전까지 number 변수에 담기
                }
                
            } else {
                if numberStarted { // numberStarted가 True인데 다시 문자가 나오면 break. number이 끝났다는 뜻 !
                    break; 
                } else {
                    head.append(char)
                }
            }
        }
        let num = Int(number)! // 저도 안전하게 guard문이나 if let을 자주 이용하는 습관을 길러볼게요 ,, 일단 강제 추출 !
            let lowercasedHead = head.lowercased()
            FileList.append(FilePart(head: lowercasedHead, number: num, originalfile: file))
    }
    
    let sortedList = FileList.sorted { // sorted { 조건 }는 배열을 순회하면서 정렬하는 함수
        if $0.head == $1.head {
            return $0.number < $1.number
        }
        else {
            return $0.head < $1.head
        }
    }
    
    return sortedList.map { $0.originalfile }
}