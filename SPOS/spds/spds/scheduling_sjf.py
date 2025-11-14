"""
Simple menu-driven Preemptive SJF (Shortest Job First)
Includes a simple Gantt-like timeline style:
  P0 | P1 | IDLE | P2
  0  2   5      6
"""

def get_input():
    try:
        n = int(input("Enter number of processes: ").strip())
        if n <= 0:
            print("Number of processes must be positive.")
            return None, 0
    except ValueError:
        print("Please enter a valid integer.")
        return None, 0

    processes = []
    for i in range(n):
        while True:
            try:
                a = int(input(f"Arrival time for P{i}: ").strip())
                b = int(input(f"Burst time for P{i}: ").strip())
                if a < 0 or b <= 0:
                    print("Arrival must be >= 0 and Burst must be > 0. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter integers. Try again.")
        processes.append({
            "id": i,
            "arrival": a,
            "burst": b,
            "original_burst": b,
            "completion": 0,
            "turnaround": 0,
            "waiting": 0
        })
    return processes, n

def compute_preemptive_sjf(processes, n):
    time = 0
    completed = 0
    execution_order = []  # each entry is "P0", "P1", or "IDLE" for each time unit

    # run until all processes complete
    while completed < n:
        idx = -1
        min_burst = None
        for i, p in enumerate(processes):
            if p["arrival"] <= time and p["burst"] > 0:
                if min_burst is None or p["burst"] < min_burst:
                    min_burst = p["burst"]
                    idx = i

        if idx != -1:
            execution_order.append(f"P{processes[idx]['id']}")
            processes[idx]["burst"] -= 1
            time += 1
            if processes[idx]["burst"] == 0:
                processes[idx]["completion"] = time
                processes[idx]["turnaround"] = time - processes[idx]["arrival"]
                processes[idx]["waiting"] = processes[idx]["turnaround"] - processes[idx]["original_burst"]
                completed += 1
        else:
            execution_order.append("IDLE")
            time += 1

    return execution_order

def build_timeline_from_execution(execution_order):
    """
    Convert per-unit execution_order into parts and times like:
      parts = ["P0", "P0", "IDLE", "P1"]
      times = [0, 1, 2, 3, 5]  # start times and final time
    We'll compress consecutive identical labels into single parts entries
    with their start times. The final times list contains the start time of
    each part and the final end time (last completion).
    """
    if not execution_order:
        return [], [0]

    parts = []
    times = []
    current = execution_order[0]
    start = 0

    for t, label in enumerate(execution_order, start=1):
        if label != current:
            parts.append(current)
            times.append(start)
            current = label
            start = t - 1
    # append last segment
    parts.append(current)
    times.append(start)
    # final completion time is length of execution_order
    times.append(len(execution_order))
    return parts, times

def display(processes, execution_order):
    n = len(processes)
    print("\nExecution sequence (per time unit):")
    print(" ".join(execution_order))

    print("\n| PID | Arrival | Burst | Completion | Turnaround | Waiting |")
    print("---------------------------------------------------------------")
    total_completion = total_tat = total_wait = 0
    for p in processes:
        print(f"| P{p['id']:<3}|   {p['arrival']:<6}|  {p['original_burst']:<4}|"
              f"    {p['completion']:<6}|    {p['turnaround']:<6}|   {p['waiting']:<6}|")
        total_completion += p["completion"]
        total_tat += p["turnaround"]
        total_wait += p["waiting"]

    print(f"\nAverage Completion Time: {total_completion / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")
    print(f"Average Waiting Time   : {total_wait / n:.2f}")

    # Build and print the simple Gantt-like timeline (requested style)
    print("\nGANTT TIMELINE")
    parts, times = build_timeline_from_execution(execution_order)
    # Print parts separated by " | "
    print(" | ".join(parts))
    # Print times separated by two spaces (as in your example)
    print("  ".join(str(t) for t in times))

def main_menu():
    while True:
        print("\n===== Preemptive SJF Scheduler =====")
        print("1. Run scheduler")
        print("2. Exit")
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            processes, n = get_input()
            if not processes:
                continue
            execution_order = compute_preemptive_sjf(processes, n)
            display(processes, execution_order)
        elif choice == "2":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 or 2.")

if __name__ == "__main__":
    main_menu()