"""
Very simple FCFS (First Come First Serve) scheduler
Non-preemptive, based on arrival time. Menu driven for beginners.
"""

def run_fcfs():
    try:
        n = int(input("Enter number of processes: ").strip())
        if n <= 0:
            print("Number of processes must be positive.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return

    procs = []
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
                print("Please enter integers for times. Try again.")
        procs.append({"id": i, "arrival": a, "burst": b})

    # sort by arrival time (stable)
    procs.sort(key=lambda p: p["arrival"])

    time = 0
    order = []
    # compute metrics
    for p in procs:
        if time < p["arrival"]:
            order.append(f"IDLE({p['arrival'] - time})")
            time = p["arrival"]
        p_response = time - p["arrival"]
        order.append(f"P{p['id']}")
        time += p["burst"]
        p_completion = time
        p_turnaround = p_completion - p["arrival"]
        p_waiting = p_turnaround - p["burst"]
        # attach metrics to process dict for printing
        p.update({
            "completion": p_completion,
            "turnaround": p_turnaround,
            "waiting": p_waiting,
            "response": p_response
        })

    # print tables and averages
    print("\nINPUT TABLE")
    print(f"{'Proc':<6}{'Arrival':<8}{'Burst':<6}")
    for p in procs:
        print(f"P{p['id']:<5}{p['arrival']:<8}{p['burst']:<6}")

    print("\nEXECUTION ORDER")
    print(" -> ".join(order))

    print("\nRESULTS")
    print(f"{'Proc':<6}{'Comp':<6}{'TAT':<6}{'Wait':<6}{'Resp':<6}")
    total_comp = total_tat = total_wait = total_resp = 0
    for p in procs:
        print(f"P{p['id']:<5}{p['completion']:<6}{p['turnaround']:<6}{p['waiting']:<6}{p['response']:<6}")
        total_comp += p["completion"]
        total_tat += p["turnaround"]
        total_wait += p["waiting"]
        total_resp += p["response"]

    m = len(procs)
    print("\nAVERAGES")
    print(f"Average Completion Time : {total_comp / m}")
    print(f"Average Turnaround Time : {total_tat / m}")
    print(f"Average Waiting Time    : {total_wait / m}")
    print(f"Average Response Time   : {total_resp / m}")

    # simple Gantt-like timeline
    print("\nGANTT TIMELINE")
    times = []
    parts = []
    time = 0
    for p in procs:
        if time < p["arrival"]:
            parts.append("IDLE")
            times.append(time)
            time = p["arrival"]
        parts.append(f"P{p['id']}")
        times.append(time)
        time = p["completion"]
    times.append(time)
    print(" | ".join(parts))
    print("  ".join(str(t) for t in times))


def main_menu():
    while True:
        print("\n===== FCFS Scheduler =====")
        print("1. Run FCFS scheduling")
        print("2. Exit")
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            run_fcfs()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 or 2.")

if __name__ == "__main__":
    main_menu()