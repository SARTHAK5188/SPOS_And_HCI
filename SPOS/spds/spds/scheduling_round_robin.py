'''Write a program to simulate CPU Scheduling Algorithms:  Round Robin 
(Preemptive). '''
def round_robin():
    n = int(input("Enter number of processes: "))
    arrival_time = []
    burst_time = []
    remaining_time = []
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    response_time = [-1] * n
    execution_log = []

    for i in range(n):
        a = int(input(f"Enter arrival time of Process {i}: "))
        b = int(input(f"Enter burst time of Process {i}: "))
        arrival_time.append(a)
        burst_time.append(b)
        remaining_time.append(b)

    time_quantum = int(input("Enter time quantum: "))
    current_time = 0
    queue = []
    completed = 0
    in_queue = [False] * n

    for i in range(n):
        if arrival_time[i] <= current_time:
            queue.append(i)
            in_queue[i] = True

    while completed < n:
        if not queue:
            execution_log.append("IDLE")
            current_time += 1
            for i in range(n):
                if not in_queue[i] and arrival_time[i] <= current_time and remaining_time[i] > 0:
                    queue.append(i)
                    in_queue[i] = True
            continue

        process = queue.pop(0)

        if response_time[process] == -1:
            response_time[process] = current_time - arrival_time[process]

        run_time = min(time_quantum, remaining_time[process])
        for _ in range(run_time):
            execution_log.append(f"P{process}")
        current_time += run_time
        remaining_time[process] -= run_time

        if remaining_time[process] == 0:
            completion_time[process] = current_time
            turnaround_time[process] = completion_time[process] - arrival_time[process]
            waiting_time[process] = turnaround_time[process] - burst_time[process]
            completed += 1

        for i in range(n):
            if not in_queue[i] and arrival_time[i] <= current_time and remaining_time[i] > 0:
                queue.append(i)
                in_queue[i] = True

        if remaining_time[process] > 0:
            queue.append(process)

    print("\n| Process ID | Completion Time | Waiting Time | Turnaround Time | Response Time |")
    for i in range(n):
        print(f"| P{i:<10} | {completion_time[i]:<15} | {waiting_time[i]:<13} | {turnaround_time[i]:<15} | {response_time[i]:<13} |")

    print(f"\nAverage Completion Time: {sum(completion_time)/n:.2f}")
    print(f"Average Waiting Time   : {sum(waiting_time)/n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time)/n:.2f}")

    # Gantt Chart
    print("\nGantt Chart:")
    parts = []
    times = []
    current = execution_log[0]
    start = 0
    for t in range(1, len(execution_log)):
        if execution_log[t] != current:
            parts.append(current)
            times.append(start)
            current = execution_log[t]
            start = t
    parts.append(current)
    times.append(start)
    times.append(len(execution_log))

    print(" | ".join(parts))
    print("  ".join(str(t) for t in times))
    print("\n")   # prevents weird repeated output in some terminals


def main():
    while True:
        print("\n===== CPU Scheduling Simulator =====")
        print("1. Round Robin Scheduling")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            round_robin()
        elif choice == '2':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
