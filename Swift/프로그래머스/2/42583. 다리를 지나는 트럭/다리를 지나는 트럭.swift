import Foundation

func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    // 일단 다리 길이 큐를 생성한 후 초기화 해야 함
    // 다리 위에 트럭이 없으면 0, 있으면 해당 트럭의 무게
    // 시간이 지나면 시간은 +1이 되고 맨 앞에 있는 차량이 제거되고 무게가 갱신됨
    // 새 트럭을 올릴 수 있는지 판단하는 것은 모든 큐 값들을 다 더해서 weight보다 작으면 올리기 아니면 0을 추가
    var bridge = Array(repeating: 0, count: bridge_length)
    var trucks = truck_weights
    var time = 0
    var bridgeWeight = 0
    
    while !bridge.isEmpty {
        time += 1
        
        let out = bridge.removeFirst()
        bridgeWeight -= out
        
        if let next = trucks.first {
            if bridgeWeight + next <= weight {
                bridge.append(next)
                bridgeWeight += next
                trucks.removeFirst()
            } else {
                bridge.append(0)
            }
        } else {
            bridge.append(0)
        }
        
        if trucks.isEmpty && bridgeWeight == 0 {
            break
        }
    }
    
    return time
}