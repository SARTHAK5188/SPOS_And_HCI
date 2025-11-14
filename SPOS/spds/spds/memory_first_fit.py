
"""
First Fit Memory Placement (menu driven, structured like Worst Fit)

This program implements the First Fit placement:
- For each process, choose the first block that can hold it.
- Update that block's free size after allocation.
- Prints allocation and the remaining fragment of the block immediately after allocation.
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


def first_fit(blocks, processes):
    memory = blocks[:]               # copy of block free sizes
    allocation = [-1] * len(processes)
    remaining_after_alloc = [None] * len(processes)
    block_size_before = [None] * len(processes)

    for i, psize in enumerate(processes):
        for j, free in enumerate(memory):
            if free >= psize:
                block_size_before[i] = memory[j]
                memory[j] -= psize
                allocation[i] = j
                remaining_after_alloc[i] = memory[j]
                break
        if allocation[i] == -1:
            remaining_after_alloc[i] = None
            block_size_before[i] = None

    return allocation, remaining_after_alloc, memory, block_size_before


def print_allocation(processes, allocation, remaining_after_alloc, final_memory, block_size_before):
    print("\nAllocation Results")
    print("Process | Size | Block Allocated | Block Size | Remaining Fragment")
    print("---------------------------------------------------------------")
    for i, p in enumerate(processes):
        blk = allocation[i]
        if blk != -1:
            print(f"P{i+1:<6} | {p:<4} | {blk+1:^15} | {block_size_before[i]:^10} | {remaining_after_alloc[i]:^18}")
        else:
            print(f"P{i+1:<6} | {p:<4} | {'Not Allocated':^15} | {'-':^10} | {'-':^18}")
    print("\nFinal free sizes of blocks:", final_memory)
    print()


def main_menu():
    while True:
        print("\n=== First Fit Memory Placement ===")
        print("1. Run First Fit")
        print("2. Exit")
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "1":
            blocks, procs = get_input()
            if blocks is None:
                continue
            allocation, remaining_after_alloc, final_memory, block_size_before = first_fit(blocks, procs)
            print("\nInitial memory blocks:", blocks)
            print("Processes:", procs)
            print_allocation(procs, allocation, remaining_after_alloc, final_memory, block_size_before)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 or 2.")


if __name__ == "__main__":
    main_menu()


