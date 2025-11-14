from collections import deque

def round_robin():
    n = int(input("Enter number of processes: "))
    arrival = []
    burst = []
    remaining = []
    completion = [0] * n
    waiting = [0] * n
    turnaround = [0] * n
    response = [-1] * n


    for i in range(n):
            at = int(input(f"Enter arrival time of P{i}: "))
            bt = int(input(f"Enter burst time of P{i}: "))
            arrival.append(at)
            burst.append(bt)
            remaining.append(bt)

    timeQuantum = int(input("Enter time quantum: "))

    currentTime = 0
    q = deque()
    inQueue = [False] * n
    completedProcesses = 0

    
    for i in range(n):
        if arrival[i] <= currentTime:
            q.append(i)
            inQueue[i] = True

    while completedProcesses < n:
        if not q:
            currentTime += 1
            for i in range(n):
                if not inQueue[i] and arrival[i] <= currentTime and remaining[i] > 0:
                    q.append(i)
                    inQueue[i] = True
            continue

        idx = q.popleft() 

        if response[idx] == -1:
            response[idx] = currentTime - arrival[idx]

        if remaining[idx] <= timeQuantum:
            currentTime += remaining[idx]
            remaining[idx] = 0
            completion[idx] = currentTime
            turnaround[idx] = completion[idx] - arrival[idx]
            waiting[idx] = turnaround[idx] - burst[idx]
            completedProcesses += 1
        else:
            currentTime += timeQuantum
            remaining[idx] -= timeQuantum

        
        for i in range(n):
            if not inQueue[i] and arrival[i] <= currentTime and remaining[i] > 0:
                q.append(i)
                inQueue[i] = True

        
        if remaining[idx] > 0:
            q.append(idx)

    print("\n| Process | Completion Time | Waiting Time | Turnaround Time | Response Time |")
    totalWaiting = totalTurnaround = totalCompletion = 0
    for i in range(n):
        print(f"| P{i:<6} | {completion[i]:<15} | {waiting[i]:<12} | {turnaround[i]:<15} | {response[i]:<13} |")
        totalWaiting += waiting[i]
        totalTurnaround += turnaround[i]
        totalCompletion += completion[i]

    print(f"\nAverage Completion Time: {totalCompletion / n:.2f}")
    print(f"Average Waiting Time: {totalWaiting / n:.2f}")
    print(f"Average Turnaround Time: {totalTurnaround / n:.2f}")

if __name__ == "__main__":
    round_robin()
