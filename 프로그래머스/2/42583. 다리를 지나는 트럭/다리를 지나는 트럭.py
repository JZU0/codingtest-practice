from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    curr = 0
    while bridge:
        time += 1
        curr -= bridge.popleft()
        if(truck): 
            if(curr + truck[0] <= weight):
                truckin = truck.popleft()
                bridge.append(truckin)
                curr += truckin
            else:
                bridge.append(0)       
    return time