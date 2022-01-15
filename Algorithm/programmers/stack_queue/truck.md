# 트럭


## 문제

### 설명
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

|경과 시간|다리를 지난 트럭|다리를 건너는 트럭|대기 트럭|
|---|---|---|---|
|0|[]|[]|[7,4,5,6]|
|1~2|[]|[7]|[4,5,6]|
|3|[7]|[4]|[5,6]|
|4|[7]|[4,5]|[6]|
|5|[7,4]|[5]|[6]|
|6~7|[7,4,5]|[6]|[]|
|8|[7,4,5,6]|[]|[]|
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

### 입력
- 다리에 올라갈 수 있는 트럭 수 bridge_length
- 다리가 견딜 수 있는 무게 weight
- 트럭 별 무게 truck_weights

### 출력
- 모든 트럭이 다리를 건너는데 걸리는 시간(초)

### 제한사항
- bridge_length는 1 이상 10,000 이하
- weight는 1 이상 10,000 이하
- truck_weights의 길이는 1 이상 10,000 이하
- 모든 트럭의 무게는 1 이상 weight 이하


## 해결방안
- 시간 변수를 놓아 전체적인 시간을 증가시켜 측정하고, 다리에 올라가 있는 트럭이 해당 시간에 도달하면 나가도록 하였다.
- 문서 위치는 `(location + len(priorities) - 1) % len(priorities) ` 를 통해 해당 배열에서 순환시키도록 하였다.


## 코드 분석
```python3
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
```
- 작성한 코드는 O(n)의 시간복잡도를 가진다.
