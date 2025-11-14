import random

def bully_election(processes, initiator, failed_processes, election_in_progress):
    # If initiator itself failed, it cannot start election, so just return None
    if initiator in failed_processes:
        return None

    if initiator in election_in_progress:
        # Already in election, avoid infinite recursion
        return None
    election_in_progress.add(initiator)

    print(f"\nProcess {initiator} initiates election.")
    
    higher_processes = [p for p in processes if p > initiator]
    replies = []
    
    # Initiator sends election messages to all higher processes
    for hp in higher_processes:
        if hp in failed_processes:
            print(f"Process {initiator} sends election message to Process {hp} -- no reply (Process {hp} failed)")
        else:
            print(f"Process {initiator} sends election message to Process {hp} -- OK")
            replies.append(hp)

    # If no higher process replies, initiator becomes coordinator
    if not replies:
        print(f"Process {initiator} becomes coordinator.")
        # Send coordinator message to all other alive processes
        for p in processes:
            if p != initiator and p not in failed_processes:
                print(f"Process {initiator} sends coordinator message to Process {p}")
        return initiator
    
    # Otherwise, higher processes initiate election recursively
    coordinators = []
    for rp in replies:
        c = bully_election(processes, rp, failed_processes, election_in_progress)
        if c is not None:
            coordinators.append(c)

    # The coordinator is the max among all returned coordinators
    return max(coordinators) if coordinators else None

def main():
    n = int(input("Enter the number of processes: "))
    processes = []
    for i in range(n):
        p = int(input(f"Enter process {i+1}: "))
        processes.append(p)
    
    processes = sorted(processes)
    current_leader = max(processes)
    print(f"Current Leader is Process {current_leader}")
    
    # Randomly fail one process (different from leader)
    failed_process = random.choice([p for p in processes if p != current_leader])
    failed_processes = [failed_process]
    print(f"(Debug) Process {failed_process} has failed.")
    
    initiator = int(input("Enter the initiator process for election: "))
    
    if initiator not in processes:
        print("Invalid initiator!")
        return
    
    # If initiator failed, find next alive process to start election
    if initiator in failed_processes:
        alive_processes = [p for p in processes if p not in failed_processes]
        higher_alive = [p for p in alive_processes if p > initiator]
        if higher_alive:
            new_initiator = min(higher_alive)
            print(f"Initiator Process {initiator} has failed. Process {new_initiator} becomes new initiator.")
            initiator = new_initiator
        else:
            # No higher process, lowest alive initiates
            initiator = min(alive_processes)
            print(f"Initiator Process {initiator} starts election (no higher alive process).")
    
    print("\nStarting Bully Election Algorithm:")
    
    coordinator = bully_election(processes, initiator, failed_processes, set())
    
    print(f"\nElection completed. New Coordinator is Process {coordinator}")

if __name__ == "__main__":
    main()