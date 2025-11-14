import random

def ring_algo(processes, initiator, failed_processes):
    n = len(processes)
    
    # Check if initiator failed; if yes, find next alive process as initiator
    if initiator in failed_processes:
        failed_index = processes.index(initiator)
        print(f"Process {initiator} has failed as initiator.")
        for i in range(1, n+1):
            next_index = (failed_index + i) % n
            if processes[next_index] not in failed_processes:
                initiator = processes[next_index]
                print(f"Process {initiator} will take over as initiator.")
                break
    
    print("Election messages:")
    
    coordinator = initiator
    start_index = processes.index(initiator)
    
    current_index = start_index
    
    for _ in range(1, n):
        current = processes[current_index]
        
        # Find the next alive process to send message to
        next_index = (current_index + 1) % n
        next_process = processes[next_index]
        
        # If next_process failed, find the next alive after that failed one(s)
        if next_process in failed_processes:
            print(f"Process {current} sends election message to Process {next_process} -- Process {next_process} did not reply (failed)")
            # Find next alive process skipping failed ones
            skip_count = 1
            while True:
                candidate_index = (next_index + skip_count) % n
                candidate = processes[candidate_index]
                if candidate not in failed_processes:
                    # Now send message from current to candidate (skipping failed)
                    print(f"Process {current} sends election message to Process {candidate}")
                    next_index = candidate_index
                    next_process = candidate
                    break
                skip_count += 1
        else:
            print(f"Process {current} sends election message to Process {next_process}")
        
        # Update coordinator if next_process is higher
        if next_process > coordinator:
            coordinator = next_process
        
        current_index = next_index
    
    print(f"New Leader is Process {coordinator}")

# Main driver code
n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    p = int(input(f"Enter process {i+1}: "))
    processes.append(p)

current_leader = max(processes)
print(f"Current Leader is Process {current_leader}")

failed_process = random.choice(processes)
failed_processes = [failed_process]

initiator1 = int(input("Enter the first initiator: "))
initiator2 = int(input("Enter the second initiator: "))

if initiator1 not in processes or initiator2 not in processes:
    print("Invalid Input!")
else:
    print("\nElection by first initiator:")
    ring_algo(processes, initiator1, failed_processes)
    print("\nElection by second initiator:")
    ring_algo(processes, initiator2, failed_processes)