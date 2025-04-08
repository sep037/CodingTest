import Foundation

func solution(_ schedules:[Int], _ timelogs:[[Int]], _ startday:Int) -> Int {
    
    // 일단 출근 인정 시각 계산하기
    func add10Minutes(time: Int) -> Int {
        var hour = time / 100
        var minutes = time % 100
        minutes += 10
        
        if minutes >= 60 {
            hour += 1
            minutes -= 60
        }
        return hour*100 + minutes
    }
    
    
    // startday 까다로워요 생각이 잘 안 났어요 ..
    var weekdays : [Int] = []
    for i in 0 ..< 7 {
        let day = (startday + i - 1) % 7 + 1
        if day != 6 && day != 7 { // 평일만 추가 !
            weekdays.append(i)
        }
    }
    
    var giftCount = 0
    
    for i in 0 ..< schedules.count {
        let hopeTime = schedules[i]
        let limitTime = add10Minutes(time: hopeTime)
        let logs = timelogs[i]
        
        var suitableDay = true
        
        for weekday in weekdays {
            if logs[weekday] > limitTime {
                suitableDay = false
                break
            }
        }
        
        if suitableDay {
            giftCount += 1
        }
    }
    return giftCount
}