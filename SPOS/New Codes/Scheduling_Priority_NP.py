"""
Priority Scheduling (Non-Preemptive) — menu driven, simple Gantt-style timeline.

- Lower numeric priority value => higher priority (e.g. 1 is highest).
- If two ready processes have same priority, the one with earlier arrival (then lower id) is chosen.
- Gantt timeline printed in the requested style.
"""

def read_processes():
    try:
        n = int(input("Enter number of processes: ").strip())
        if n <= 0:
            print("Number of processes must be positive.")
            return None
    except ValueError:
        print("Please enter a valid integer.")
        return None

    procs = []
    for i in range(n):
        while True:
            try:
                a = int(input(f"Arrival time for P{i}: ").strip())
                b = int(input(f"Burst time for P{i}: ").strip())
                pr = int(input(f"Priority for P{i} (lower = higher): ").strip())
                if a < 0 or b <= 0:
                    print("Arrival must be >= 0 and Burst must be > 0. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter integers. Try again.")
        procs.append({
            "id": i,
            "arrival": a,
            "burst": b,
            "priority": pr,
            "completion": 0,
            "turnaround": 0,
            "waiting": 0,
            "response": -1,
            "done": False
        })
    return procs

def priority_non_preemptive(procs):
    # sort by arrival then id to make selection deterministic for ties
    procs.sort(key=lambda p: (p["arrival"], p["id"]))
    n = len(procs)
    time = 0
    completed = 0
    gantt_parts = []
    gantt_times = []

    while completed < n:
        # find the ready, not-done process with highest priority (lowest numeric)
        idx = -1
        best_pr = None
        for i, p in enumerate(procs):
            if not p["done"] and p["arrival"] <= time:
                if best_pr is None or p["priority"] < best_pr or (p["priority"] == best_pr and p["arrival"] < procs[idx]["arrival"]):
                    best_pr = p["priority"]
                    idx = i

        if idx != -1:
            p = procs[idx]
            # response time (first time it gets CPU)
            if p["response"] == -1:
                p["response"] = time - p["arrival"]
            # record Gantt: if idle happened earlier, it's already recorded; now record process start
            if not gantt_parts:
                gantt_parts.append(f"P{p['id']}")
                gantt_times.append(time)
            else:
                # if last part is same process (shouldn't happen in non-preemptive),
                # we still handle it; otherwise append new part start
                if gantt_parts[-1] != f"P{p['id']}":
                    gantt_parts.append(f"P{p['id']}")
                    gantt_times.append(time)
            # run the process to completion (non-preemptive)
            time += p["burst"]
            p["completion"] = time
            p["turnaround"] = p["completion"] - p["arrival"]
            p["waiting"] = p["turnaround"] - p["burst"]
            p["done"] = True
            completed += 1
        else:
            # CPU idle for one unit (record IDLE only if last part isn't IDLE)
            if not gantt_parts or gantt_parts[-1] != "IDLE":
                gantt_parts.append("IDLE")
                gantt_times.append(time)
            time += 1

    # append final completion time
    gantt_times.append(time)
    return procs, gantt_parts, gantt_times

def print_results(procs, gantt_parts, gantt_times):
    n = len(procs)
    print("\n| PID | Arrival | Burst | Priority | Completion | Turnaround | Waiting | Response |")
    print("-------------------------------------------------------------------------------")
    total_completion = total_tat = total_wait = 0
    for p in procs:
        print(f"| P{p['id']:<3}|   {p['arrival']:<6}|  {p['burst']:<4}|   {p['priority']:<6}|"
              f"    {p['completion']:<6}|    {p['turnaround']:<6}|   {p['waiting']:<6}|   {p['response']:<6}|")
        total_completion += p["completion"]
        total_tat += p["turnaround"]
        total_wait += p["waiting"]

    print(f"\nAverage Completion Time : {total_completion / n:.2f}")
    print(f"Average Turnaround Time : {total_tat / n:.2f}")
    print(f"Average Waiting Time    : {total_wait / n:.2f}")

    # Gantt timeline in requested simple style
    print("\nGANTT TIMELINE")
    print(" | ".join(gantt_parts))
    print("  ".join(str(t) for t in gantt_times))

def main_menu():
    while True:
        print("\n===== Priority Scheduling (Non-Preemptive) =====")
        print("1. Run Priority Scheduling")
        print("2. Exit")
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            procs = read_processes()
            if not procs:
                continue
            procs, parts, times = priority_non_preemptive(procs)
            print_results(procs, parts, times)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 or 2.")

if __name__ == "__main__":
    main_menu()