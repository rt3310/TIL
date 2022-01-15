def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = []
    on_bridge = []
    bridge_weight = 0

    time = 0
    while(True):
        time += 1
        
        if len(bridge) > 0: # 다리에 트럭이 있을 시
            if (time - on_bridge[0]) >= bridge_length: # 해당 트럭이 다리를 다 지났으면
                bridge_weight -= bridge[0]
                on_bridge.pop(0)
                bridge.pop(0)
                
        if len(truck_weights) > 0: # 대기 트럭이 있을 시
            if ((bridge_weight + truck_weights[0]) <= weight) and (len(bridge) < bridge_length): # 다리에 올라갈 수 있으면
                bridge_weight += truck_weights[0]
                on_bridge.append(time)
                bridge.append(truck_weights.pop(0))
        
        if len(bridge) == 0 and len(truck_weights) == 0: # 다리와 대기에 트럭이 없을 시
            answer = time
            break

    return answer