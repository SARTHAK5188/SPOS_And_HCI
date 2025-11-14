"""
Next Fit Memory Placement (menu driven, simple)

- Enter memory block sizes and process sizes as space-separated integers.
- Next Fit: for each process, search from the last allocated block (or start)
  and place the process in the first block that fits (wraps around).
- Shows allocation table and remaining fragment sizes.
"""

def get_input():
    try:
        blocks = list(map(int, input("Enter memory block sizes (space-separated): ").strip().split()))
        procs = list(map(int, input("Enter process sizes (space-separated): ").strip().split()))
        if not blocks or not procs:
            print("Blocks and processes must be non-empty.")
            return None, None
        if any(b <= 0 for b in blocks) or any(p <= 0 for p in procs):
            print("Sizes must be positive integers.")
            return None, None
        return blocks, procs
    except ValueError:
        print("Invalid input. Use integers separated by spaces.")
        return None, None

def next_fit(blocks, processes):
    memory = blocks[:]               # copy of block free sizes
    allocation = [-1] * len(processes)
    remaining_after_alloc = [None] * len(processes)

    start_idx = 0  # where to start searching for the next allocation

    for i, psize in enumerate(processes):
        found = False
        j = start_idx
        checked = 0
        while checked < len(memory):
            if memory[j] >= psize:
                allocation[i] = j
                memory[j] -= psize
                remaining_after_alloc[i] = memory[j]
                # next search will start from the block after the one we just used
                start_idx = (j + 1) % len(memory)
                found = True
                break
            j = (j + 1) % len(memory)
            checked += 1
        if not found:
            allocation[i] = -1
            remaining_after_alloc[i] = None
            # start_idx remains where it was

    return allocation, remaining_after_alloc, memory

def print_allocation(processes, allocation, remaining_after_alloc, final_memory, original_blocks):
    print("\nAllocation Results")
    print("Process | Size | Block Allocated | Block Size | Remaining Fragment")
    print("---------------------------------------------------------------")
    for i, p in enumerate(processes):
        blk = allocation[i]
        if blk != -1:
            print(f"P{i+1:<6} | {p:<4} | {blk+1:^15} | {original_blocks[blk]:^10} | {remaining_after_alloc[i]:^18}")
        else:
            print(f"P{i+1:<6} | {p:<4} | {'Not Allocated':^15} | {'-':^10} | {'-':^18}")
    print("\nFinal free sizes of blocks:", final_memory)
    print()

def main_menu():
    while True:
        print("\n=== Next Fit Memory Placement ===")
        print("1. Run Next Fit")
        print("2. Exit")
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            blocks, procs = get_input()
            if blocks is None:
                continue
            allocation, remaining_after_alloc, final_memory = next_fit(blocks, procs)
            print("\nInitial memory blocks:", blocks)
            print("Processes:", procs)
            print_allocation(procs, allocation, remaining_after_alloc, final_memory, blocks)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 or 2.")

if __name__ == "__main__":
    main_menu()